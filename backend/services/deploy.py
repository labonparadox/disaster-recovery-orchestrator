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

        logger.info(f"the data db fetched is {info}")

    except Exception as e:

        logger.info(f"Fetching from failed {e}")



    curr_time = datetime.datetime.now()

    key = f"{name}_key_{curr_time}"
    sg_name = f"{name}_sg_{curr_time}"
    server_name = f"{name}_sn_{curr_time}"

    try:

        await docker_filler.Docker_fill.script_maker(image,port,name)

    except Exception as e:
        logger.info(f"docker filler failed {e}")

    try:
        await terraform_trigger_aws.Trigger.aws_trigger(key,sg_name,server_name)

    except Exception as e:

        logger.info(f"terraform trigger failed {e}")









