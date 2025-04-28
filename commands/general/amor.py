import discord
import random

async def setup(bot):
    piadas = [
        
        ]

    @bot.tree.command(name="piada", description="Peça ao steVe para te contar o quanto ele te ama 💓")
    async def piada(interact: discord.Interaction):
        await interact.response.send_message(random.choice(piadas))
