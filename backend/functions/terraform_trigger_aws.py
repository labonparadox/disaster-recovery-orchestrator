import subprocess
import logging
import datetime
from helpers.set_logger import LoggerFactory
from helpers.config import settings
import os
import sys
import asyncio
import traceback
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

logger = LoggerFactory.get_logger(
    name="terraform",
    log_file=settings.Log_file_terraform,
    level=logging.INFO
)

class Trigger():
    @staticmethod
    async def aws_trigger():
        curr_time = datetime.datetime.now()

        working_dir = '/home/ubuntu/disaster-recovery-orchestrator/backend/scripts/terraform/aws/resources/server/'

        # Check SSH key
        ssh_key = os.path.expanduser("~/.ssh/id_rsa.pub")
        if not os.path.exists(ssh_key):
            subprocess.run([
                'ssh-keygen', '-t', 'rsa', '-b', '2048',
                '-f', os.path.expanduser("~/.ssh/id_rsa"),
                '-N', ''
            ], check=True)

        os.chdir(working_dir)

        try:
            result = subprocess.run(
                ['terraform', 'init'],
                capture_output=True,
                text=True,
                check=True
            )

        except subprocess.CalledProcessError as e:

            raise

        try:
            result = subprocess.run(
                ['terraform', 'plan'],
                capture_output=True,
                text=True,
                check=True
            )

        except subprocess.CalledProcessError as e:
            logger.info(e)

        # Step 3: Terraform Apply with AUTO APPROVAL

        try:
            result = subprocess.run(
                ['terraform', 'apply', '-auto-approve'],
                capture_output=True,
                text=True,
                check=True,
                input='yes\n'
            )



        except subprocess.CalledProcessError as e:

            raise RuntimeError(f"Terraform apply failed with code {e.returncode}")

        try:
            result = subprocess.run(
                ['terraform', 'output'],
                capture_output=True,
                text=True,
                check=True
            )

        except Exception as e:
            logger.info(e)


if __name__ == "__main__":
    import asyncio
    try:
        asyncio.run(Trigger.aws_trigger())
    except KeyboardInterrupt:
        logger.info("issue happens")
    except Exception as e:

        traceback.print_exc()