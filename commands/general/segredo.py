import discord
import random
import json

try:
    with open('data/segredos.json', 'r', encoding='utf-8') as f:
        segredos = json.load(f)
except FileNotFoundError:
    print("[ERRO] Arquivo 'segredos.json' não encontrado. O comando /segredo não terá segredos para contar.")
    segredos = ["steVe não encontrou seu diário..."]
except json.JSONDecodeError:
    print("[ERRO] O arquivo 'segredos.json' contém um erro de formatação. Verifique as vírgulas e aspas.")
    segredos = ["As páginas do diário do steVe parecem estar fora de ordem."]

async def setup(bot):
    @bot.tree.command(name="segredo", description="Peça ao steVe para te contar um segredo 🤫")
    async def segredo_command(interaction: discord.Interaction):
        if not segredos:
            await interaction.response.send_message("looks like I'm out of secrets today...", ephemeral=True)
            return
            
        segredo_escolhido = random.choice(segredos)
        await interaction.response.send_message(segredo_escolhido, ephemeral=True)