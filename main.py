import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
import os
from keep_alive import keep_alive

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
    await tree.setup(bot)
    sincs = await bot.tree.sync()
    print(f"{len(sincs)} comandos sincronizados!")

@bot.event
async def on_member_join(membro: discord.Member):
    canal = bot.get_channel(719744273989500951)
    await canal.send(f"bem vinda(o) {membro.mention}!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    mensagem = message.content.lower()
    resposta = None

    if bot.user in message.mentions:
        respostas_mention = [
            "sou eu, steVe!", 
            f"sim {message.author.display_name}, sou eu!", 
            "como posso te ajudar?", 
            "steVe aqui, galera!", 
            "cheguei!", 
            f"oii {message.author.display_name}, sentiu minha falta? :3", 
            "precisa da ajuda do steVe?",
            "chamou? 0 .0",
            f"{message.author.display_name}, você summonou o steVe :v",
            "eu ouvi meu nomeee... >.<",
            f"oii {message.author.display_name}, tava dormindo ;-;... o que aconteceu?",
            f"quem me acordou? ah, é você, {message.author.display_name} :3",
            "sim? me chamou? :3",
            f"oii {message.author.display_name}, tô aqui :)",
            "steVe tá sempre pronto pra ajudar :D",
            "precisa de mim? hehe :3",
            "e aí? sou o steVe :)",
            f"oii {message.author.display_name}, como posso te ajudar?",
            "steVe aqui, o primeiro e único :3",
            f"precisa de ajuda, {message.author.display_name}? vou dar o meu melhor :)"
        ]
        resposta = random.choice(respostas_mention)

    elif "steve" in mensagem:
        respostas_steve = [
            f"oii {message.author.display_name}, esse é meu nome!", 
            "me chamam de El steVo nas ruas, sabia?", 
            "STEvE", 
            f"sou eu, {message.author.display_name}", 
            "você é meu amigo?", 
            "você é amigo de eu? :3", 
            "você sabe eu?",
            "alguém aqui disse steVe? :3",
            f"steVe... sou eu! e você é {message.author.display_name}!",
            "tá falando comigo?? steVe?? >.<",
            "eu amo ouvir meu nome :D",
            "fico feliz quando me chamam ;-;",
            f"{message.author.display_name}, tá falando sobre... mim? hehe >:3",
            "steVe pronto pro serviço! >:D",
            f"alguém disse steVe? esse sou eu :)",
            "esse é meu nome! :3",
            "tô famoso, né? hehe",
            f"oii {message.author.display_name}, você disse meu nome? :D",
            "as pessoas sempre falam de mim... :3",
            "eu não sou tímido, pode falar comigo quando quiser :)"
            ]
        resposta = random.choice(respostas_steve)

    elif mensagem.startswith("oi"):
        respostas_oi = [
            f"oii {message.author.display_name}!", 
            f"{message.author.display_name}!! oiii!", 
            "olá!!", 
            "e aí :3", 
            f"oii {message.author.display_name} :P", 
            f"olá {message.author.display_name}!",
            "oii :D",
            f"e aí {message.author.display_name} :)",
            "que oi fofo :3",
            f"olá olá {message.author.display_name}",
            "amo quando as pessoas me dão oi :)",
            "oi! quer ser meu amigo? :3",
            f"como você tá, {message.author.display_name}? :D",
            "oi oi oi oiiiii!!",
            f"meu deus é você, {message.author.display_name}!! >.<",
            "você disse oi? oiiiiii pra você :P",
            f"ei {message.author.display_name}, tudo certo?",
            "e aí aí e aí aí ei e aí! hehe fui malandro agora :3"
            ]
        resposta = random.choice(respostas_oi)

    if resposta:
        await message.channel.send(resposta)
keep_alive()
bot.run(token)