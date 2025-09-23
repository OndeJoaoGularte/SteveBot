import discord
import random
import json

try:
    with open('data/versiculos.json', 'r', encoding='utf-8') as f:
        versiculos = json.load(f)
except FileNotFoundError:
    print("[ERRO] Arquivo 'versiculos.json' não encontrado.")
    versiculos = [{"text": "steVe não encontrou sua Bíblia...", "reference": "Erro 404"}]
except json.JSONDecodeError:
    print("[ERRO] O arquivo 'versiculos.json' contém um erro de formatação. Verifique as vírgulas e aspas.")
    versiculos = [{"text": "As páginas da Bíblia do steVe parecem estar fora de ordem.", "reference": "Erro de Leitura"}]

async def setup(bot):
    @bot.tree.command(name="versiculo", description="Peça ao steVe para recitar uma passagem bíblica 🕊️")
    async def versiculo_command(interaction: discord.Interaction):
        versiculo_escolhido = random.choice(versiculos)
        
        embed = discord.Embed(
            title="A Palavra do Senhor! 📖",
            description=f"**―** *{versiculo_escolhido['text']}*",
            color=discord.Color.from_rgb(255, 255, 127)
        )
        embed.set_footer(text=versiculo_escolhido['reference'])
        
        await interaction.response.send_message(embed=embed)