from pathlib import Path
import logging
from helpers.config import settings
from helpers.set_logger import LoggerFactory

logger = LoggerFactory.get_logger(
    name="dockerfill",
    log_file=settings.Log_file_filler,
    level=logging.INFO
)


class Docker_fill():

    @staticmethod
    async def script_maker(image, port, username):
        try:
            container_name = f"{username.lower()}_im"
            internal_port = 80

            if "node" in image.lower() or "express" in image.lower():
                internal_port = 3000
            elif "python" in image.lower() or "flask" in image.lower() or "django" in image.lower():
                internal_port = 5000
            elif "httpd" in image.lower() or "apache" in image.lower():
                internal_port = 80
            elif "nginx" in image.lower():
                internal_port = 80

            userdata = f"""#!/bin/bash

LOG_FILE="/var/log/userdata.log"
exec > >(tee -a $LOG_FILE) 2>&1

echo "Time: $(date)"
echo "Image: {image}"
echo "Port: {port}"
echo "Container: {container_name}"

log() {{
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}}

log_error() {{
    echo "[$(date '+%Y-%m-%d %H:%M:%S')]  ERROR: $1"
}}

log_success() {{
    echo "[$(date '+%Y-%m-%d %H:%M:%S')]  $1"
}}

log "STEP 1: Preparing system..."

log "Waiting 10 seconds for system to stabilize..."
sleep 10

log "Updating package list..."
sudo apt-get update -y >> $LOG_FILE 2>&1

if ! command -v docker &> /dev/null; then
    log "Docker not found. Installing Docker..."
    sudo apt-get install -y docker.io >> $LOG_FILE 2>&1
    sudo systemctl start docker
    sudo systemctl enable docker
    log_success "Docker installed successfully"
else
    log "Docker already installed: $(docker --version)"
fi


log "STEP 2: Pulling Docker image {image}..."

if sudo docker pull {image} >> $LOG_FILE 2>&1; then
    log_success "Docker image {image} pulled successfully"
else
    log_error "Failed to pull Docker image {image}"
    log "Retrying with --no-cache..."
    sudo docker pull --no-cache {image} >> $LOG_FILE 2>&1
    if [ $? -eq 0 ]; then
        log_success "Docker image {image} pulled successfully (retry)"
    else
        log_error "Failed to pull Docker image {image} after retry"
        exit 1
    fi
fi

sudo docker images >> $LOG_FILE 2>&1

log "STEP 3: Running container {container_name}..."

if sudo docker ps -a | grep -q {container_name}; then
    log "Container {container_name} already exists. Removing..."
    sudo docker stop {container_name} >> $LOG_FILE 2>&1
    sudo docker rm {container_name} >> $LOG_FILE 2>&1
    log "Old container removed"
fi

log "Running: docker run -d -p {port}:{internal_port} --name {container_name} {image}"
if sudo docker run -d \\
    -p {port}:{internal_port} \\
    --name {container_name} \\
    --restart unless-stopped \\
    {image} >> $LOG_FILE 2>&1; then
    log_success "Container {container_name} started successfully"
else
    log_error "Failed to start container {container_name}"
    exit 1
fi


log "STEP 4: Verifying container is running..."

sleep 5

if sudo docker ps | grep -q {container_name}; then
    log_success "Container {container_name} is running!"

    log "Container details:"
    sudo docker ps --filter "name={container_name}" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" | tee -a $LOG_FILE

    log "Testing application on port {port}..."
    HTTP_CODE=$(curl -s -o /dev/null -w "%{{http_code}}" http://localhost:{port} 2>/dev/null)
    if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "301" ] || [ "$HTTP_CODE" = "302" ]; then
        log_success "Application is responding on port {port} (HTTP $HTTP_CODE)"
    else
        log "Application on port {port} is not responding yet (HTTP $HTTP_CODE)"
        log "Checking container logs..."
        sudo docker logs {container_name} --tail 20 >> $LOG_FILE 2>&1
    fi
else
    log_error "Container {container_name} failed to start!"
    log "Container logs:"
    sudo docker logs {container_name} >> $LOG_FILE 2>&1
    exit 1
fi


log "User Data Script Completed Successfully!"
log "Time: $(date)"
log "Container: {container_name}"
log "Port: {port}"
log "Internal Port: {internal_port}"
log "Image: {image}"

echo "STATUS: SUCCESS" >> $LOG_FILE
echo "CONTAINER_NAME: {container_name}" >> $LOG_FILE
echo "PORT: {port}" >> $LOG_FILE
echo "COMPLETED_AT: $(date)" >> $LOG_FILE

# Show running containers
sudo docker ps >> $LOG_FILE 2>&1

exit 0
"""
            logger.info(
                f"Script created for {username} with image {image} on port {port} (internal port {internal_port})")
            return userdata

        except Exception as e:
            logger.error(f"script_maker failed: {e}")
            return None

    @staticmethod
    async def file_saver(image, port, username):
        try:
            script = await Docker_fill.script_maker(
                image=image,
                port=port,
                username=username
            )

            if not script:
                raise Exception("Failed to generate script")

            terraform_dir = (
                    Path(__file__).parents[1]
                    / "scripts"
                    / "terraform"
                    / "aws"
                    / "resources"
                    / "server"
            )

            terraform_dir.mkdir(parents=True, exist_ok=True)

            userdata_file = terraform_dir / "userdata.sh"
            with open(userdata_file, "w") as f:
                f.write(script)

            userdata_file.chmod(0o755)

            logger.info(f"userdata.sh saved to: {userdata_file}")
            return str(userdata_file)

        except Exception as e:
            logger.error(f"file_saver failed: {e}")
            raise