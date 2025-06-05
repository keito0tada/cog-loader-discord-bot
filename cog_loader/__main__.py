import os
from dotenv import load_dotenv
from .run_bot import run_bot

if __name__ == "__main__":
    if os.path.isfile(".env"):
        load_dotenv()
    run_bot()