import discord
import random

async def setup(bot):
    fatos = [
        
        ]

    @bot.tree.command(name="fato", description="Peça ao steVe para te contar um fato histórico 🧐")
    async def fato(interact: discord.Interaction):
        await interact.response.send_message(random.choice(fatos))
