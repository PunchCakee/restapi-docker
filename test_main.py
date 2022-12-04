import httpx
from fastapi.testclient import TestClient
from main import app
from dotenv import load_dotenv
import os

load_dotenv()  


client = TestClient(app)

def test_api_key():
    API_KEY = os.getenv('API_KEY')
    r = client.get(f"http://127.0.0.1:8000/update/?key={API_KEY}").json()
    assert r == {'ERROR': 'CONTAINER NOT FOUND'}

def test_api_hello():
    r = client.get("http://127.0.0.1:8000/").json()
    assert r == {"it":"works!"}