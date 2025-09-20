import discord
from discord.ui import View, Select
import random
import json

try:
    with open('data/oraculo.json', 'r', encoding='utf-8') as f:
        oraculo_data = json.load(f)
except FileNotFoundError:
    print("[ERROR] 'oraculo.json' file not found.")
    oraculo_data = {}

SIGNOS_INFO = {
    "aries": {"nome": "Áries", "emoji": "♈"}, "touro": {"nome": "Touro", "emoji": "♉"},
    "gemeos": {"nome": "Gêmeos", "emoji": "♊"}, "cancer": {"nome": "Câncer", "emoji": "♋"},
    "leao": {"nome": "Leão", "emoji": "♌"}, "virgem": {"nome": "Virgem", "emoji": "♍"},
    "libra": {"nome": "Libra", "emoji": "♎"}, "escorpiao": {"nome": "Escorpião", "emoji": "♏"},
    "sagitario": {"nome": "Sagitário", "emoji": "♐"}, "capricornio": {"nome": "Capricórnio", "emoji": "♑"},
    "aquario": {"nome": "Aquário", "emoji": "♒"}, "peixes": {"nome": "Peixes", "emoji": "♓"}
}

class SignoSelect(Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label=info["nome"], 
                value=signo,
                emoji=info["emoji"]
            ) for signo, info in SIGNOS_INFO.items()
        ]
        super().__init__(placeholder="Qual é o seu signo?", options=options)

    async def callback(self, interaction: discord.Interaction):
        signo_selecionado = self.values[0]
        
        previsoes = oraculo_data.get(signo_selecionado, [])
        
        if not previsoes:
            await interaction.response.edit_message(content="Ops, parece que as estrelas estão silenciosas sobre este signo hoje...", embed=None, view=None)
            return
            
        previsao_escolhida = random.choice(previsoes)
        info_signo = SIGNOS_INFO[signo_selecionado]
        
        embed = discord.Embed(
            title=f"🍀 steVe's Oracle for {info_signo['nome']} {info_signo['emoji']}",
            description=f"ok, me concentrei aqui e as estrelas me disseram o seguinte para você:\n\n> *{previsao_escolhida}*",
            color=discord.Color.from_rgb(0, 127, 255)
        )
        embed.set_footer(text="lembre-se: é só uma previsão e talvez esteja errada, você não precisa seguir a risca, tá? ;-;")
        
        # Edita a mensagem original para mostrar o resultado, removendo o menu
        await interaction.response.edit_message(content=None, embed=embed, view=None)

# View que contém o menu
class OraculoView(View):
    def __init__(self):
        super().__init__()
        self.add_item(SignoSelect())

async def setup(bot):
    @bot.tree.command(name="oraculo", description="Peça ao steVe para ler sua sorte nos astros 🍀")
    async def oraculo(interaction: discord.Interaction):
        embed = discord.Embed(
            title="🔮 steVe's Astral Oracle 🔮",
            description="eu também entendo um pouco de estrelas, sabia? :3 Selecione seu signo no menu abaixo para eu poder ler o que o futuro te reserva!",
            color=discord.Color.from_rgb(127, 127, 255)
        )
        await interaction.response.send_message(embed=embed, view=OraculoView())
