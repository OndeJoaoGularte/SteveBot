import discord
import random
import json

try:
    with open('data/gritos.json', 'r', encoding='utf-8') as f:
        gritos = json.load(f)
except FileNotFoundError:
    print("[ERRO] Arquivo 'gritos.json' não encontrado.")
    gritos = ["AHHH, TÔ SEM VOZ!"]
except json.JSONDecodeError:
    print("[ERRO] O arquivo 'gritos.json' contém um erro de formatação. Verifique as vírgulas e aspas.")
    gritos = ["MINHA GARGANTA TÁ DOENDO!"]

async def setup(bot):
    @bot.tree.command(name="gritar", description="Peça ao steVe para gritar 😱")
    async def gritar(interaction: discord.Interaction):
        if not gritos:
            await interaction.response.send_message("parece que minha garganta tá ruim hoje...")
            return
            
        grito_escolhido = random.choice(gritos)
        await interaction.response.send_message(grito_escolhido)