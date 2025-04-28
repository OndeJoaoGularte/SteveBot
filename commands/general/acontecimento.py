import discord
import random

async def setup(bot):
    acontecimentos = [
        
        ]

    @bot.tree.command(name="acontecimento", description="Peça ao steve para te relembrar de algum acontecimento do Horário de Verão 🤔")
    async def acontecimento(interact: discord.Interaction):
        await interact.response.send_message(random.choice(acontecimentos))
