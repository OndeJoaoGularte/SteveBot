import discord
import random

async def setup(bot):
    piadas = [
        
        ]

    @bot.tree.command(name="piada", description="Peça para o steVe te dar um piada 🤗")
    async def piada(interact: discord.Interaction):
        await interact.response.send_message(random.choice(piadas))
