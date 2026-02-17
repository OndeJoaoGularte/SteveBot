import discord
import random
import json
import os
from discord.ext import commands
from dotenv import load_dotenv
from keep_alive import keep_alive

# Importações dos seus módulos
import tree
import tasks

# Configurações iniciais
load_dotenv()
token = os.getenv("token")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned, intents=intents)

# Carregar as frases do JSON
try:
    with open('data/chat.json', 'r', encoding='utf-8') as f:
        chat_data = json.load(f)
except FileNotFoundError:
    print("❌ Erro: Arquivo data/chat.json não encontrado!")
    chat_data = {"mentions": [], "steve_keyword": [], "greetings": []}

@bot.event
async def on_ready():
    await carregar_comandos()
    tasks.setup(bot)
    print(f"✅ steVe está online como {bot.user}")

async def carregar_comandos():
    await tree.setup(bot)
    try:
        sincs = await bot.tree.sync()
        print(f"✨ {len(sincs)} comandos sincronizados!")
    except Exception as e:
        print(f"❌ Erro ao sincronizar comandos: {e}")

@bot.event
async def on_member_join(membro: discord.Member):
    # Canal de boas-vindas
    canal = bot.get_channel(719744273989500951)
    if canal:
        await canal.send(f"Bem vinda(o) {membro.mention}! O steVe estava te esperando! :3")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg_lower = message.content.lower()
    user_name = message.author.display_name
    response = None

    # Lógica de resposta baseada no JSON
    if bot.user in message.mentions:
        response = random.choice(chat_data["mentions"])
    elif "steve" in msg_lower:
        response = random.choice(chat_data["steve_keyword"])
    elif msg_lower.startswith("oi"):
        response = random.choice(chat_data["greetings"])

    if response:
        # Troca o {user} pelo nome real da pessoa
        await message.channel.send(response.replace("{user}", user_name))

    # Necessário para que o bot ainda processe comandos prefixados
    await bot.process_commands(message)

# Inicia o servidor de keep_alive e o bot
keep_alive()
bot.run(token)