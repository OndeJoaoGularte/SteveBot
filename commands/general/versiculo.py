import discord
import random
import json

try:
    with open('data/versiculos.json', 'r', encoding='utf-8') as f:
        versiculos = json.load(f)
except FileNotFoundError:
    print("[ERRO] Arquivo 'versiculos.json' não encontrado. O comando /versiculo não funcionará.")
    versiculos = [{"texto": "steVe não encontrou sua Bíblia...", "referencia": "Erro 404"}]
except json.JSONDecodeError:
    print("[ERRO] O arquivo 'versiculos.json' contém um erro de formatação.")
    versiculos = [{"texto": "As páginas da Bíblia do steVe parecem estar fora de ordem.", "referencia": "Erro de Leitura"}]

async def setup(bot):
    @bot.tree.command(name="versiculo", description="Peça ao steVe para recitar uma passagem bíblica 🕊️")
    async def versiculo_command(interaction: discord.Interaction):
        versiculo_escolhido = random.choice(versiculos)
        
        embed = discord.Embed(
            title="Praise the Lord! 📖",
            description=f"**―** *{versiculo_escolhido['texto']}*",
            color=discord.Color.from_rgb(255, 255, 127)
        )
        embed.set_footer(text=versiculo_escolhido['referencia'])
        
        await interaction.response.send_message(embed=embed)