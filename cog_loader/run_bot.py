import logging
import os
import sys
import time
from typing import Final

import discord
import psycopg2
from discord.ext import commands

DISCORD_BOT_TOKEN: Final[str | None] = os.getenv("DISCORD_BOT_TOKEN")
DATABASE_URL: Final[str | None] = os.getenv("DATABASE_URL")
ENVIRONMENT: Final[str | None] = os.getenv("ENVIRONMENT")


def wait_for_db_connection(
    interval: int = 10, timeout: int = 60
) -> psycopg2.extensions.connection:
    start_time = time.time()
    while True:
        try:
            conn = psycopg2.connect(DATABASE_URL)
            return conn
        except psycopg2.OperationalError as e:
            if time.time() - start_time > timeout:
                raise e
            time.sleep(interval)


class Bot(commands.Bot):
    def __init__(self, command_prefix: str, intents: discord.Intents):
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.database_connector = wait_for_db_connection()


def check_environment() -> None:
    if ENVIRONMENT is None or ENVIRONMENT not in ["development", "production"]:
        logging.error(f"Invalid environment: {ENVIRONMENT}. ")
        sys.exit(1)

    if DISCORD_BOT_TOKEN is None:
        logging.error("Environment variable DISCORD_BOT_TOKEN is not set.")
        sys.exit(1)

    if DATABASE_URL is None:
        logging.error("Environment variables DATABASE_URL is not set.")
        sys.exit(1)


async def load_extensions(bot: commands.Bot) -> None:
    await bot.load_extension("misc_cog.cog")


def run_bot() -> None:
    check_environment()

    bot = Bot(command_prefix="/", intents=discord.Intents.all())

    @bot.event
    async def on_ready() -> None:
        logging.info("On Ready")
        await bot.load_extension("cog_loader.pingpong")
        await load_extensions(bot)
        await bot.tree.sync()

    bot.run(DISCORD_BOT_TOKEN)  # type: ignore
