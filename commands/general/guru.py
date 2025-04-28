import discord
import random

async def setup(bot):
    ensinamentos = [
        
        ]

    @bot.tree.command(name="guru", description="Peça ao steve para recitar um ensinamento do guru 🪷")
    async def guru(interact: discord.Interaction):
        await interact.response.send_message(random.choice(ensinamentos))
