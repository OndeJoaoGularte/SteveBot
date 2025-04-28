import discord
import random

async def setup(bot):
    versículos = [
        
        ]

    @bot.tree.command(name="versículo", description="Peça ao steVe recitar uma passagem bíblica 🕊️")
    async def versículo(interact: discord.Interaction):
        await interact.response.send_message(random.choice(versículos))
