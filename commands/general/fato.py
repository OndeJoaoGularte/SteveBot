import discord
import random
import json

try:
    with open('data/fatos.json', 'r', encoding='utf-8') as f:
        fatos = json.load(f)
except FileNotFoundError:
    print("[ERROR] 'fatos.json' file not found.")
    fatos = [{"titulo": "Um fato sobre este comando...", "texto": "Ele não funciona se o arquivo 'fatos.json' não for encontrado."}]
except json.JSONDecodeError:
    print("[ERROR] 'fatos.json' file is incorrectly formatted.")
    fatos = [{"titulo": "Um fato sobre JSON...", "texto": "É preciso ter muito cuidado com vírgulas e aspas para não quebrar o arquivo."}]

comentarios = [
    "history is so cool, isn't it? :3",
    "I love reading about this stuff!",
    "isn't that fascinating? 🧐",
    "sometimes reality is crazier than fiction!",
    "I could talk about this all day!",
    "I hope you found that as interesting as I did! :D"
]

async def setup(bot):
    @bot.tree.command(name="fato", description="Peça ao steVe para te contar um fato histórico 🧐")
    async def fato(interaction: discord.Interaction):
        fato_escolhido = random.choice(fatos)
        
        embed = discord.Embed(
            title=f"steVe's Historical Facts! 📜",
            description=f"### {fato_escolhido['title']}\n{fato_escolhido['text']}",
            color=discord.Color.from_rgb(255, 127, 0)
        )
        
        embed.set_footer(text=random.choice(comentarios))
        
        await interaction.response.send_message(embed=embed)