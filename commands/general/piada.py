import discord
import random

async def setup(bot):
    piadas = [
        
        ]

    @bot.tree.command(name="piada", description="Peça ao steve para te contar uma piada 🤣")
    async def piada(interact: discord.Interaction):
        await interact.response.send_message(random.choice(piadas))


import discord
import random
import json
import asyncio

try:
    with open('data/piadas.json', 'r', encoding='utf-8') as f:
        piadas = json.load(f)
except FileNotFoundError:
    print("[ERROR] 'piadas.json' file not found.")
    piadas = [{"setup": "o steVe tá pensando numa piada", "punchline": "mas ele esqueceu...", "explanation": "acho que essa piada não foi boa, né?"}]
except json.JSONDecodeError:
    print("[ERROR] 'piadas.json' file is incorrectly formatted.")
    piadas = [{"setup": "o livro de piadas do steVe tá todo errado", "punchline": "ele não consegue ler nada!", "explanation": "acho que corrompeu o arquivo..."}]

async def setup(bot):
    @bot.tree.command(name="piada", description="Peça ao steVe para te contar uma piada 🤣")
    async def piada(interaction: discord.Interaction):
        piada_escolhida = random.choice(piadas)
        
        embed = discord.Embed(
            title="Here's a joke for you! 😁",
            description=f"**{piada_escolhida['setup']}**",
            color=discord.Color.from_rgb(127, 0, 255)
        )
        embed.set_footer(text="pensando...")
        
        await interaction.response.send_message(embed=embed)
        
        await asyncio.sleep(3)
        
        embed.description += f"\n\n...**{piada_escolhida['punchline']}**"
        embed.set_footer(text=f"{piada_escolhida['explanation']}")
        
        await interaction.edit_original_response(embed=embed)