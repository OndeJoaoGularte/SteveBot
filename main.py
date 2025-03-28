from dotenv import load_dotenv
import os

import discord
import random
from discord.ext import commands

import tree
# import comandos
import tasks

load_dotenv()
token = os.getenv("token")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned, intents=intents)

@bot.event
async def on_ready():
    await carregar_comandos()
    tasks.setup(bot)
    print("tá funcionando")

async def carregar_comandos():
    #comandos.setup(bot)
    await tree.setup(bot)
    sincs = await bot.tree.sync()
    print(f"{len(sincs)} comandos sincronizados!")

@bot.event
async def on_member_join(membro: discord.Member):
    canal = bot.get_channel(719744273989500951)
    await canal.send(f"bem vinda(o) {membro.mention}!")

@bot.event
async def on_reaction_add(reacao: discord.Reaction, membro: discord.Member):
    await reacao.message.reply(f"isso {membro.display_name}, reage com {reacao.emoji} mesmo, assim você vai longe 👍🏾")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user in message.mentions:
        await message.channel.send("Chamou?")

    mensagem = message.content.lower()

    if mensagem.startswith("oi"):
        respostas_oi = ["heyy", "hiii!", "hello!!", "hey :3", "hi :P"]
        resposta = random.choice(respostas_oi)
        await message.channel.send(resposta)

    if "steve" in mensagem:
            respostas_steve = ["heyy", "hiii!", "hello!!", "hey :3", "hi :P"]
            resposta = random.choice(respostas_steve)
            await message.channel.send(resposta)

bot.run(token)