import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_EMAIL = os.getenv('TWITTER_EMAIL')
TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')
PROXYMESH_HOST = os.getenv('PROXYMESH_HOST')
PROXYMESH_PORT = os.getenv('PROXYMESH_PORT')
MONGO_URI = os.getenv('MONGO_URI')