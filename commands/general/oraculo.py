import discord
import random

async def setup(bot):
    oraculo = [
        
        ]

    @bot.tree.command(name="oraculo", description="Peça ao steve para ver sua sorte 🍀")
    async def oraculo(interact: discord.Interaction):
        await interact.response.send_message(random.choice(oraculo))
