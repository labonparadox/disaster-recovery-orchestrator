import logging
import datetime
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
    log_file= settings.Log_file_terraform,
    level=logging.INFO
)


class Trigger():

    @staticmethod
    async def aws_trigger():

        curr_time = datetime.time()
        tf = Terraform(working_dir='/home/ubuntu/disaster-recovery-orchestrator/backend/scripts/terraform/aws/resources/server/')

        try:

            return_code , stdout, stderr = tf.init()

            logger.info(f"The init is being done at {curr_time}")

        except TerraformCommandError:

            logger.error(f"The init being failed due to TerraformCommandError at {curr_time}")

            raise

        except Exception as e:

            logger.info(f"The init being failed due to {e} at {curr_time}")

            raise

        try:

            return_code, stdout, stderr = tf.apply(skip_plan=True)

            logger.info(f"The apply is being done at {curr_time}")

        except TerraformCommandError:

            logger.error(f"The apply being failed due to TerraformCommandError at {curr_time}")

            raise

        except Exception as e:

            logger.info(f"The apply being failed due to {e} at {curr_time}")

            raise

        return return_code, stdout, stderr


if __name__ == "__main__":
    import asyncio
    asyncio.run(Trigger.aws_trigger())
