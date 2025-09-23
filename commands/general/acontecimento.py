import discord
import random
import json

try:
    with open('data/acontecimentos.json', 'r', encoding='utf-8') as f:
        acontecimentos = json.load(f)
except FileNotFoundError:
    print("[ERRO] Arquivo 'acontecimentos.json' não encontrado.")
    acontecimentos = ["steVe não encontrou seu diário..."]
except json.JSONDecodeError:
    print("[ERRO] O arquivo 'acontecimentos.json' contém um erro de formatação. Verifique as vírgulas e aspas.")
    acontecimentos = ["As páginas do diário do steVe parecem estar fora de ordem."]

async def setup(bot):
    @bot.tree.command(name="acontecimento", description="Peça ao steVe para te relembrar de algum acontecimento do Horário de Verão 🤔")
    async def acontecimento(interaction: discord.Interaction):
        if not acontecimentos:
            await interaction.response.send_message("parece que tô sem acontecimentos para contar hoje...")
            return
            
        acontecimento_escolhido = random.choice(acontecimentos)
        await interaction.response.send_message(acontecimento_escolhido)