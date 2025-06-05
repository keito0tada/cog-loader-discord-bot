import logging
import os
import sys

from dotenv import load_dotenv

from .run_bot import run_bot

if __name__ == "__main__":
    if os.path.isfile(".env"):
        load_dotenv()

    if os.getenv("ENVIRONMENT") == "development":
        logging.basicConfig(level=logging.DEBUG)
    elif os.getenv("ENVIRONMENT") == "production":
        logging.basicConfig(level=logging.INFO)
    else:
        logging.error("Invalid environment.")
        sys.exit(1)

    run_bot()
