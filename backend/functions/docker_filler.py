from pathlib import Path

class Docker_fill():

    @staticmethod
    async def script_maker(image, port, username):

        userdata = f"""#!/bin/bash
    
    sleep 10
    
    sudo docker pull {image}
    
    sudo docker run -d \
    -p {port}:{port} \
    --name {username}_im \
    {image}
    """

        return userdata

    @staticmethod

    async def file_saver(image,port,username):


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
