import discord
import random

async def setup(bot):
    gritar = [
        
        ]

    @bot.tree.command(name="gritar", description="Peça ao steVe para gritar 😱")
    async def gritar(interact: discord.Interaction):
        await interact.response.send_message(random.choice(gritar))
