import discord
import random
import json

try:
    with open('data/conselhos.json', 'r', encoding='utf-8') as f:
        conselhos = json.load(f)
except FileNotFoundError:
    print("[ERRO] Arquivo 'conselhos.json' não encontrado. O comando /conselho não terá conselhos para contar.")
    conselhos = ["steVe não encontrou seu diário..."]
except json.JSONDecodeError:
    print("[ERRO] O arquivo 'conselhos.json' contém um erro de formatação. Verifique as vírgulas e aspas.")
    conselhos = ["As páginas do diário do steVe parecem estar fora de ordem."]

async def setup(bot):
    @bot.tree.command(name="conselho", description="Peça ao steVe para te dar um conselho 🤗")
    async def conselho(interaction: discord.Interaction):
        if not conselhos:
            await interaction.response.send_message("looks like I'm out of advices today...")
            return
            
        conselho_escolhido = random.choice(conselhos)
        await interaction.response.send_message(conselho_escolhido)