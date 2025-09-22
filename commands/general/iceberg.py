import discord
import random
import json

try:
    with open('data/iceberg.json', 'r', encoding='utf-8') as f:
        iceberg_data = json.load(f)
except FileNotFoundError:
    print("[ERROR] 'iceberg.json' file not found.")
    iceberg_data = {"Erro 🧊": ["Não consegui encontrar os segredos do iceberg..."]}
except json.JSONDecodeError:
    print("[ERROR] 'iceberg.json' file is incorrectly formatted.")
    iceberg_data = {"Erro 🧊": ["O mapa do iceberg está ilegível!"]}

camada_imagens = {
    "Camada 1: Baby Thiagão": "https://media.discordapp.net/attachments/719744273989500951/1419718314820763798/image.png",
    "Camada 2: Charles Miner Mentioned": "https://media.discordapp.net/attachments/719744273989500951/1419718396668543149/image.png",
    "Camada 3: Horário de Verão Curtindo o Verão": "https://media.discordapp.net/attachments/719744273989500951/1419718484971098243/image.png",
    "Camada 4: Dudu com Pernas": "https://media.discordapp.net/attachments/719744273989500951/1419718576922693803/image.png",
    "Camada 5: Emoji Buceteiro": "https://media.discordapp.net/attachments/719744273989500951/1419718643641745462/image.png",
    "Camada 6: Alvin e os Esquilos": "https://media.discordapp.net/attachments/719744273989500951/1419718713036505162/image.png",
    "Camada 7: Anime de Verão": "https://media.discordapp.net/attachments/719744273989500951/1419718784712970381/image.png",
    "Camada 8: Louça no Cu": "https://media.discordapp.net/attachments/719744273989500951/1419718850240581742/image.png"
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

steve_comments = [
    "exploring this is like real archaeology!",
    "there are so many secrets buried here...",
    "who knows what else is hiding in the depths?",
    "this piece of history is fascinating!",
    "the deeper we go, the stranger it gets..."
]

async def setup(bot):
    @bot.tree.command(name="iceberg", description="Peça ao steVe para explorar o iceberg do Horário de Verão 🧊")
    async def iceberg(interaction: discord.Interaction):
        camada_sorteada = random.choice(list(iceberg_data.keys()))
        
        textos_da_camada = iceberg_data[camada_sorteada]
        
        texto_sorteado = random.choice(textos_da_camada) if textos_da_camada else "Este tópico é um mistério..."

        camada_key = camada_sorteada.split(':')[0]
        cor_embed = camada_cores.get(camada_key, discord.Color.default())
        imagem_embed = camada_imagens.get(camada_sorteada, None)

        embed = discord.Embed(
            title=camada_sorteada,
            description=f"### {texto_sorteado}",
            color=cor_embed
        )
        
        if imagem_embed:
            embed.set_image(url=imagem_embed)
            
        embed.set_footer(text=random.choice(steve_comments))
        
        await interaction.response.send_message(embed=embed)