# load .env
from dotenv import load_dotenv
load_dotenv()

# set environment variables
import os
BOT_SCREEN_NAME = os.getenv('BOT_SCREEN_NAME')
ACCESS_TOKEN_KEY = os.getenv('ACCESS_TOKEN_KEY')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
