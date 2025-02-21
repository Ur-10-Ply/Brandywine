# bot/config/settings.py
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve token from .env
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
