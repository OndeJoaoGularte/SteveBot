import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
import os

import tree as tree
import tasks as tasks

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

    mensagem = message.content.lower()
    resposta = None

    if bot.user in message.mentions:
        respostas_mention = ["it's me, steVe!", "yes, it's me", "how can i help you?", "steVe here, guys", "i'm here!", "missed me? :3", "do you need steVe's help?"]
        resposta = random.choice(respostas_mention)

    elif "steve" in mensagem:
        respostas_steve = ["heyy, that's my name!", "they call me steVen steVers in the streets, you know?", "STEvE", "that's me, pal", "are you my friend?", "are you a friend of mine? :3", "do you know me i?"]
        resposta = random.choice(respostas_steve)

    elif mensagem.startswith("oi"):
        respostas_oi = ["heyy", "hiii!", "hello!!", "hey :3", "hi :P", "peace!"]
        resposta = random.choice(respostas_oi)

    if resposta:
        await message.channel.send(resposta)

bot.run(token)