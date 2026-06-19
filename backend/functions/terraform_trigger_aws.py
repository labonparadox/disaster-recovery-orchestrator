import logging
import datetime
import subprocess
from python_terraform import Terraform, TerraformCommandError
from backend.helpers.set_logger import LoggerFactory
from backend.helpers.config import settings
from pathlib import Path
import sys
import os

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

        ssh_key = os.path.expanduser("~/.ssh/id_rsa.pub")
        if not os.path.exists(ssh_key):
            logger.info("SSH key not found, generating one...")
            try:
                subprocess.run([
                    'ssh-keygen', '-t', 'rsa', '-b', '2048',
                    '-f', os.path.expanduser("~/.ssh/id_rsa"),
                    '-N', ''
                ], check=True, capture_output=True)
                logger.info(" SSH key created successfully")
            except subprocess.CalledProcessError as e:
                logger.error(f"Failed to create SSH key: {e}")
                raise

        if not os.path.exists(working_dir):
            logger.error(f" Terraform directory does not exist: {working_dir}")
            raise FileNotFoundError(f"Directory not found: {working_dir}")

        key_tf = os.path.join(working_dir, 'key.tf')
        if not os.path.exists(key_tf):
            logger.error(f" key.tf not found in: {working_dir}")
            raise FileNotFoundError(f"key.tf not found in {working_dir}")

        if not os.path.exists(ssh_key):
            logger.error(f"SSH public key not found at: {ssh_key}")
            raise FileNotFoundError(f"SSH key not found at {ssh_key}")

        state_file = os.path.join(working_dir, 'terraform.tfstate')
        if os.path.exists(state_file) and os.path.getsize(state_file) == 0:
            os.remove(state_file)
            logger.info("Removed empty state file")

        tf = Terraform(working_dir=working_dir)

        try:
            return_code, stdout, stderr = tf.init()

            if return_code != 0:
                logger.error(f"Init failed with code {return_code}")
                raise RuntimeError(f"Terraform init failed with code {return_code}")

            logger.info(f"The init completed successfully at {curr_time}")

        except TerraformCommandError as e:
            logger.error(f"The init failed due to TerraformCommandError at {curr_time}: {e}")
            raise
        except Exception as e:
            logger.error(f"The init failed due to {e} at {curr_time}")
            raise

        try:
            return_code, stdout, stderr = tf.apply(auto_approve=True)

            if return_code != 0:
                logger.error(f"Apply failed with code {return_code}")
                raise RuntimeError(f"Terraform apply failed with code {return_code}")

            logger.info(f"The apply completed successfully at {curr_time}")

        except TerraformCommandError as e:
            logger.error(f"The apply failed due to TerraformCommandError at {curr_time}: {e}")
            raise
        except Exception as e:
            logger.error(f"The apply failed due to {e} at {curr_time}")
            raise

        return return_code, stdout, stderr


if __name__ == "__main__":
    import asyncio

    asyncio.run(Trigger.aws_trigger())