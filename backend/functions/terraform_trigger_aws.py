import subprocess
import logging
import os
from helpers.set_logger import LoggerFactory
from helpers.config import settings
import traceback

logger = LoggerFactory.get_logger(
    name="terraform",
    log_file=settings.Log_file_terraform,
    level=logging.INFO
)

class Trigger():
    @staticmethod
    async def aws_trigger(key=None, sg_name=None, server_name=None):
        try:
            working_dir = '/home/ubuntu/disaster-recovery-orchestrator/backend/scripts/terraform/aws/resources/server/'

            userdata_path = os.path.join(working_dir, 'userdata.sh')
            if not os.path.exists(userdata_path):
                logger.error(f"userdata.sh not found at {userdata_path}")
                return {"message": "userdata.sh not found. Please create it first."}

            logger.info(f" Found userdata.sh at {userdata_path}")

            os.chdir(working_dir)
            logger.info(f"Working directory: {os.getcwd()}")

            logger.info("Running terraform init...")
            result = subprocess.run(
                ['terraform', 'init'],
                capture_output=True,
                text=True,
                check=True
            )
            logger.info(" Terraform init successful")

            logger.info("Running terraform plan...")
            result = subprocess.run(
                ['terraform', 'plan'],
                capture_output=True,
                text=True,
                check=True
            )
            logger.info("Terraform plan successful")

            logger.info("Running terraform apply...")
            result = subprocess.run(
                ['terraform', 'apply', '-auto-approve'],
                capture_output=True,
                text=True,
                check=True
            )
            logger.info("Terraform apply successful")
            logger.info(f"Apply output: {result.stdout}")

            result = subprocess.run(
                ['terraform', 'output'],
                capture_output=True,
                text=True,
                check=True
            )

            return {
                "message": "Deployment successful",
                "output": result.stdout
            }

        except subprocess.CalledProcessError as e:
            logger.error(f"Terraform command failed with code {e.returncode}")
            logger.error(f"STDERR: {e.stderr}")
            logger.error(f"STDOUT: {e.stdout}")
            return {
                "message": f"Terraform failed with code {e.returncode}",
                "error": e.stderr,
                "returncode": e.returncode
            }
        except Exception as e:
            logger.error(f"Deployment failed: {e}")
            traceback.print_exc()
            return {"message": f"Deployment failed: {str(e)}"}