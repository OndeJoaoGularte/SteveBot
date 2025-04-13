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
            "it's me, steVe!", 
            f"yes {message.author.display_name}, it's me", 
            "how can i help you?", 
            "steVe here, guys", 
            "i'm here!", 
            f"hey {message.author.display_name}, missed me? :3", 
            "do you need steVe's help?",
            "you called me? 0 .0",
            f"{message.author.display_name}, you summoned the steVe :v",
            "i heard my name... >.<",
            f"hi {message.author.display_name}, i was napping... what happened?",
            f"who woke me up? oh, it was you, {message.author.display_name} :3",
            "yes? you called me? :3",
            f"hey {message.author.display_name}, i'm here :)",
            "steVe is always ready to help :D",
            "you need me? hehe :3",
            "what's up? i'm steVe :)",
            f"hi {message.author.display_name}, how can i help you?",
            "here i am, the one and only steVe :3",
            f"you need help, {message.author.display_name}? i can try my best :)"
        ]
        resposta = random.choice(respostas_mention)

    elif "steve" in mensagem:
        respostas_steve = [
            f"heyy {message.author.display_name}, that's my name!", 
            "they call me steVen steVers in the streets, you know?", 
            "STEvE", 
            f"that's me, {message.author.display_name}", 
            "are you my friend?", 
            "are you a friend of mine? :3", 
            "do you know me i?",
            "did someone say steVe? :3",
            f"steVe... that’s me! and you’re {message.author.display_name}!",
            "you mean me?? steVe?? >.<",
            "i like hearing my name :D",
            f"{message.author.display_name}, are you talking about... me? hehe >:3",
            "steVe reporting for duty! >:D",
            f"did someone say steVe? that's me :)",
            "that's my name! :3",
            "i'm famous, huh? hehe",
            f"hi {message.author.display_name}, you said my name? :D",
            "people always talk about me... :3",
            "i'm not shy, you can talk to me more :)",
            "yes yes, steVe reporting for duty :)"
            ]
        resposta = random.choice(respostas_steve)

    elif mensagem.startswith("oi"):
        respostas_oi = [
            f"heyy {message.author.display_name}!", 
            f"{message.author.display_name}!! hiii!", 
            "hello!!", 
            "hey :3", 
            f"hi {message.author.display_name} :P", 
            f"hello {message.author.display_name}!",
            "hii :D",
            f"hey there {message.author.display_name} :)",
            "what a nice hello :3",
            f"hello hello {message.author.display_name}",
            "i love when people say hi to me :)",
            "hi! wanna be friends? :3",
            f"what’s up, {message.author.display_name}? :D",
            "hi hi hi hiiiii!!",
            f"omg it's {message.author.display_name}!! >.<",
            "you said oi? i say oiiiiii :P",
            f"yo {message.author.display_name}, everything okay?",
            "heyy hey hey heyyy!"
            ]
        resposta = random.choice(respostas_oi)

    if resposta:
        await message.channel.send(resposta)

bot.run(token)