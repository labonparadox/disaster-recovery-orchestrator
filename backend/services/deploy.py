from fastapi import APIRouter
from pydantic import BaseModel
import datetime
import logging
from database import fetch_data
from functions import docker_filler
from functions import terraform_trigger_aws
from helpers.set_logger import LoggerFactory
from helpers.config import settings


router = APIRouter()

logger = LoggerFactory.get_logger(
    name="deploy",
    log_file=settings.Log_file_deploy,
    level=logging.INFO
)

class Data(BaseModel):
    id: int

@router.post("/deploy")
async def deploy(data: Data):
    id = data.id

    try:
        info = fetch_data.Fetch.take_for_deploy(id)
        image = info[0]
        port = info[1]
        health_point = info[2]
        email = info[3]
        name = info[4]

        logger.info(f"Data fetched from DB: {info}")

    except Exception as e:
        logger.error(f"Fetching from DB failed: {e}")
        return {"message": f"Failed to fetch data: {str(e)}"}

    curr_time = datetime.datetime.now()
    key = f"{name}_key_{curr_time.strftime('%Y%m%d_%H%M%S')}"
    sg_name = f"{name}_sg_{curr_time.strftime('%Y%m%d_%H%M%S')}"
    server_name = f"{name}_sn_{curr_time.strftime('%Y%m%d_%H%M%S')}"

    try:
        userdata_path = await docker_filler.Docker_fill.file_saver(
            image=image,
            port=port,
            username=name
        )
        logger.info(f"userdata.sh created at: {userdata_path}")

    except Exception as e:
        logger.error(f"docker_filler failed: {e}")
        return {"message": f"Docker script creation failed: {str(e)}"}

    try:
        result = await terraform_trigger_aws.Trigger.aws_trigger(
            key=key,
            sg_name=sg_name,
            server_name=server_name
        )
        logger.info(f"Terraform deployment successful: {result}")
        return {
            "message": "Deployment successful",
            "key": key,
            "sg_name": sg_name,
            "server_name": server_name,
            "userdata": userdata_path
        }

    except Exception as e:
        logger.error(f"Terraform deployment failed: {e}")
        return {"message": f"Terraform deployment failed: {str(e)}"}