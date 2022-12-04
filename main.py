from fastapi import FastAPI
import json
import constants

app = FastAPI()

# TODO: add docker container updater 

@app.get("/update/")
async def root(key: str, container: str):
    if key == constants.API_KEY:
        with open("images.json",'r') as file:
            data = json.load(file)
            for container_itr in data:
                print(container_itr)
                if container_itr['container'] == container:
                    return {"container": container}
                else:
                    return {"ERROR": "CONTAINER NOT FOUND"}
    else:
        return {"ERROR":"INVALID KEY"}

@app.get("/")
async def main():
    return {"it":"works!"}

