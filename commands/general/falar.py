import discord
from discord import app_commands

async def setup(bot):
    @bot.tree.command(name="falar", description="Peça ao steVe para repetir algo 🗣️")
    @app_commands.describe(texto="O que você quer que o steVe diga?")
    async def falar(interact: discord.Interaction, texto: str):
        await interact.response.send_message(texto)