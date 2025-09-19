import discord
import random
import json

try:
    with open('data/gritos.json', 'r', encoding='utf-8') as f:
        gritos = json.load(f)
except FileNotFoundError:
    print("[ERROR] 'gritos.json' file not found.")
    gritos = ["AHHH, TÔ SEM VOZ!"]
except json.JSONDecodeError:
    print("[ERROR] 'gritos.json' file is incorrectly formatted.")
    gritos = ["MINHA GARGANTA TÁ DOENDO!"]

async def setup(bot):
    @bot.tree.command(name="gritar", description="Peça ao steVe para gritar 😱")
    async def gritar(interaction: discord.Interaction):
        if not gritos:
            await interaction.response.send_message("looks like I'm voiceless today...")
            return
            
        grito_escolhido = random.choice(gritos)
        await interaction.response.send_message(grito_escolhido)