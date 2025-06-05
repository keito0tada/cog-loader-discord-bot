import logging

import discord
from discord import app_commands
from discord.ext import commands


class PingPong(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping")
    async def ping(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("pong")


async def setup(bot: discord.ext.commands.Bot) -> None:
    await bot.add_cog(PingPong(bot=bot))
    logging.info("PingPong cog loaded successfully.")
