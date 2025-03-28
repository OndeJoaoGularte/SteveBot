import discord
from discord.ext import tasks
from datetime import time

def setup(bot):
    @tasks.loop(time=time(1, 4))
    async def enviar_mensagem():
            canal = bot.get_channel(719744273989500951)
            if canal:
                await canal.send("Tá na hora do Steve!")

    enviar_mensagem.start()