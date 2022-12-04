from fastapi import FastAPI
import json
from dotenv import load_dotenv
import os

load_dotenv()  

API_KEY = os.getenv('API_KEY')
app = FastAPI()


# TODO: add docker container updater 
@app.get("/update/")
async def root(key: str, container: str = None):
    if key == API_KEY:
        with open("images.json",'r') as file:
            data = json.load(file)
            for container_itr in data:
                if container_itr['container'] == container:
                    return {"container": container}
                else:
                    return {"ERROR": "CONTAINER NOT FOUND"}
    else:
        return {"ERROR":"INVALID KEY"}

@app.get("/")
async def main():
    return {"it":"works!"}