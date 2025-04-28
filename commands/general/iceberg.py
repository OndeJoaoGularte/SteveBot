import discord
import random

async def setup(bot):
    iceberg = [
        
        ]

    @bot.tree.command(name="iceberg", description="Peça ao steVe para explorar o iceberg do Horário de Verão 🧊")
    async def iceberg(interact: discord.Interaction):
        await interact.response.send_message(random.choice(iceberg))
