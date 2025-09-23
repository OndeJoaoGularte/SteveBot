import discord
import random
import json

try:
    with open('data/fatos.json', 'r', encoding='utf-8') as f:
        fatos = json.load(f)
except FileNotFoundError:
    print("[ERRO] Arquivo 'fatos.json' não encontrado.")
    fatos = [{"titulo": "Um fato sobre este comando...", "texto": "Ele não funciona se o arquivo 'fatos.json' não for encontrado."}]
except json.JSONDecodeError:
    print("[ERRO] O arquivo 'fatos.json' contém um erro de formatação. Verifique as vírgulas e aspas.")
    fatos = [{"titulo": "Um fato sobre JSON...", "texto": "É preciso ter muito cuidado com vírgulas e aspas para não quebrar o arquivo."}]

comentarios = [
    "história é legal, né? :3",
    "eu amo ler sobre isso ;-;",
    "isso não é fascinante? 🧐",
    "ás vezes a realidade é mais doida do que a ficção!",
    "podia falar disso o dia inteiro, te juro ;-;",
    "espero que você tenha achado tão interessante quanto eu! :D"
]

async def setup(bot):
    @bot.tree.command(name="fato", description="Peça ao steVe para te contar um fato histórico 🧐")
    async def fato(interaction: discord.Interaction):
        fato_escolhido = random.choice(fatos)
        
        embed = discord.Embed(
            title=f"Fatos Históricos do steVe! 📜",
            description=f"### {fato_escolhido['title']}\n{fato_escolhido['text']}",
            color=discord.Color.from_rgb(255, 127, 0)
        )
        
        embed.set_footer(text=random.choice(comentarios))
        
        await interaction.response.send_message(embed=embed)