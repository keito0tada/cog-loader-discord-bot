import logging

from flask import Flask
from waitress import serve

app = Flask(__name__)


@app.route("/")
def health_check() -> tuple[str, int]:
    logging.info("Health check called.")
    return "OK", 200


def run_health_check() -> None:
    serve(app, host="0.0.0.0", port=8000)
