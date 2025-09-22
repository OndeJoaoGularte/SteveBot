import discord
import random
import json

try:
    with open('data/ensinamentos.json', 'r', encoding='utf-8') as f:
        ensinamentos = json.load(f)
except FileNotFoundError:
    print("[ERRO] Arquivo 'ensinamentos.json' não encontrado. O comando /ensinamento não terá ensinamentos para contar.")
    ensinamentos = ["steVe não encontrou seu diário..."]
except json.JSONDecodeError:
    print("[ERRO] O arquivo 'ensinamentos.json' contém um erro de formatação. Verifique as vírgulas e aspas.")
    ensinamentos = ["As páginas do diário do steVe parecem estar fora de ordem."]

async def setup(bot):
    @bot.tree.command(name="ensinamento", description="Peça ao steVe para recitar um ensinamento do guru 🪷")
    async def ensinamento(interaction: discord.Interaction):
        if not ensinamentos:
            await interaction.response.send_message("looks like I'm out of teachings today...")
            return
            
        ensinamento_escolhido = random.choice(ensinamentos)
        await interaction.response.send_message(ensinamento_escolhido)