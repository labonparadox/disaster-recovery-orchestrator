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

            userdata = f"""#!/bin/bash
        
        sleep 10
        
        sudo docker pull {image}
        
        sudo docker run -d \
        -p {port}:{port} \
        --name {username}_im \
        {image}
        """

            return userdata

        except Exception as e:

            logger.info(f" the script filling failed {e}")

    @staticmethod

    async def file_saver(image,port,username):

        try:


            script = Docker_fill.script_maker(
                image=image,
                port=port,
                username=username
            )

            terraform_dir = (
                    Path(__file__).parents[2]
                    / "scripts"
                    / "terraform"
                    / "aws"
                    / "resources"
                    / "server"
            )

            userdata_file = terraform_dir / "userdata.sh"



            with open(userdata_file, "w") as f:
                f.write(script)

            return str(userdata_file)

        except Exception as e:

            logger.info(f"function file saver failed {e}")
