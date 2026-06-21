from fastapi import APIRouter
from pydantic import BaseModel
import datetime
from database import fetch_data
from functions import docker_filler
from functions import terraform_trigger_aws

router = APIRouter()

class Data(BaseModel):

    id: int


@router.post("/deploy")
def deploy(data: Data):

    id = data.id

    info = fetch_data.Fetch.take_for_deploy(id)

    image = info[0]
    port = info[1]
    health_point = info[2]
    email = info[3]
    name = info[4]

    curr_time = datetime.datetime.now()

    key = f"{name}_key_{curr_time}"
    sg_name = f"{name}_sg_{curr_time}"
    server_name = f"{name}_sn_{curr_time}"

    docker_filler.Docker_fill.script_maker(image,port,name)

    terraform_trigger_aws.Trigger.aws_trigger(key,sg_name,server_name)








