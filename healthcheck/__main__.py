import logging
import os
import sys

from .healthcheck import run_health_check

if __name__ == "__main__":
    if os.getenv("ENVIRONMENT") == "development":
        logging.basicConfig(level=logging.DEBUG)
    elif os.getenv("ENVIRONMENT") == "production":
        logging.basicConfig(level=logging.INFO)
    else:
        logging.error("Invalid environment.")
        sys.exit(1)

    run_health_check()
