import discord
import random
import json

try:
    with open('data/iceberg.json', 'r', encoding='utf-8') as f:
        iceberg_data = json.load(f)
except FileNotFoundError:
    print("[ERRO] Arquivo 'iceberg.json' não encontrado.")
    iceberg_data = {
        "Erro 🧊": {
            "topics": ["Não consegui encontrar os segredos do iceberg..."],
            "image_url": "", "comments": ["Verifique se o arquivo existe."]
        }
    }
except json.JSONDecodeError:
    print("[ERRO] O arquivo 'iceberg.json' contém um erro de formatação. Verifique as vírgulas e aspas.")
    iceberg_data = {
        "Erro 🧊": {
            "topics": ["O mapa do iceberg está ilegível!"],
            "image_url": "", "comments": ["Verifique a sintaxe do JSON."]
        }
    }

camada_cores = {
    "Camada 1": discord.Color.from_rgb(127, 255, 255),
    "Camada 2": discord.Color.from_rgb(65, 255, 255),
    "Camada 3": discord.Color.from_rgb(65, 127, 255), 
    "Camada 4": discord.Color.from_rgb(0, 127, 255), 
    "Camada 5": discord.Color.from_rgb(0, 0, 255),
    "Camada 6": discord.Color.from_rgb(0, 0, 139),
    "Camada 7": discord.Color.from_rgb(0, 0, 112),
    "Camada 8": discord.Color.from_rgb(0, 0, 0)
}

async def setup(bot):
    @bot.tree.command(name="iceberg", description="Peça ao steVe para explorar o iceberg do Horário de Verão 🧊")
    async def iceberg(interaction: discord.Interaction):
        camada_nome = random.choice(list(iceberg_data.keys()))
        
        camada_dados = iceberg_data[camada_nome]
        
        lista_topicos = camada_dados.get("topics", [])
        imagem_url = camada_dados.get("image_url")
        lista_comentarios = camada_dados.get("comments", ["..."])

        texto_sorteado = random.choice(lista_topicos) if lista_topicos else "Este tópico é um mistério..."
        comentario_sorteado = random.choice(lista_comentarios)

        camada_key = camada_nome.split(':')[0]
        cor_embed = camada_cores.get(camada_key, discord.Color.default())

        embed = discord.Embed(
            title=camada_nome,
            description=f"### {texto_sorteado}",
            color=cor_embed
        )
        
        embed.set_thumbnail(url=imagem_url)
        embed.set_footer(text=comentario_sorteado)
        
        await interaction.response.send_message(embed=embed)