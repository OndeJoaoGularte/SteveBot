import discord

lembretes1 = {
    "01-05": {"nome": "Dia da Menina", "descricao": "Comemoração à existência de todas as meninas fodas"},
    "01-21": {"nome": "Dia do Dirigui", "descricao": "Comemorigui com noirigu ai meu narigui"},
    "01-30": {"nome": "Fim do Club Penguin", "descricao": "😣"},
    "02-11": {"nome": "Dia do Cellbit", "descricao": "rpg do cellbit"},
    "02-25": {"nome": "Dia do Sonegator Robinson", "descricao": "O primeiro Carnaval de Verão do Horário de Verão, onde o grande Chico Melancia deixou de ser um garoto para, enfim, se tornar um homem!"},
    "03-10": {"nome": "Dia do Maledeto", "descricao": "nós te amamos Maledeto  😍"},
    "04-04": {"nome": "Dia Oficial do Amor", "descricao": "Comemoração do primeiro casamento realizado na República Horário de Verão!"},
    "04-21": {"nome": "Dia da Independência", "descricao": "O salvador retornou e Horário de Verão pôde voltar às suas verdadeiras raízes"},
    "04-30": {"nome": "Dia do FC da Yoshi", "descricao": "Coroação do maior ídolo do Horário de Verão!"},
    "05-24": {"nome": "Dia do Ninjax", "descricao": "O que é ninjax?"},
    "06-08": {"nome": "Dia da Proclamação do Império", "descricao": "Criação do amado Horário de Verão"},
    "06-12": {"nome": "Dia dos Nomes", "descricao": "O dia em que o primeiro nome maluco foi dito no Horário de Verão"},
    "06-24": {"nome": "Dia do Festival do Arroto", "descricao": "Comemoração do suicídio de Ligeiro Engraçado"}
}

lembretes2 = {
    "07-02": {"nome": "cu", "descricao": "Primeiro registro existente sobre o grande Louça no cu"},
    "07-08": {"nome": "Dia do Iceberg", "descricao": "iceberg"},
    "07-11": {"nome": "Dia Feriado", "descricao": "Faltam 172 dias para acabar o ano"},
    "08-23": {"nome": "Dia do Amino", "descricao": "amino é foda"},
    "08-26": {"nome": "Dia da Grande Depressão", "descricao": "O fim do Se Você é um Fodinha e a demissão de Ligeiro Engraçado do cargo Guru do Sexo acabou ocasionando um vácuo de poder sexual no Horário de Verão. Esse vácuo de poder e a falta de sexo culminaram na Grande Depressão."},
    "09-04": {"nome": "Dia do Virgem", "descricao": "virgem"},
    "09-17": {"nome": "Dia de São Nunca", "descricao": "Coisas assustadoras acontecem nesse dia  😟"},
    "09-28": {"nome": "Dia do Sexo Louco", "descricao": "Obrigado Presidente Oráculo por nos mostrar a grandiosidade do sexo louco!"},
    "10-01": {"nome": "Dia da Masturbação", "descricao": '"Uns se matarão. Eu... eu irei me acabar na punheta" -Gotens, Lucas.'},
    "10-02": {"nome": "Dia da Mulher", "descricao": "Comemoração à existência do André, o representante das mulheres"},
    "10-28": {"nome": "Halloween de Verão", "descricao": "Halloween do Horário de Verão"},
    "11-06": {"nome": "Dia da Depressão", "descricao": "Lançamento da série Arcane"},
    "11-07": {"nome": "Dia do Blauber", "descricao": "Yoshi Blauber traidor arrombado"},
    "12-12": {"nome": "Dia da Eleição", "descricao": "Realização da eleição para o líder da Embaixada dos Memes e outros cargos de valor!"},
    "12-24": {"nome": "Feriado de Natal 0", "descricao": "aniversário de deus"},
    "12-26": {"nome": "Feriado de Natal 2", "descricao": "continuação do natal"}
}

class SemestreSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Primeira metade do ano (Jan-Jun)", value="1", emoji="🌱"),
            discord.SelectOption(label="Segunda metade do ano (Jul-Dez)", value="2", emoji="🍂"),
        ]

        super().__init__(placeholder="Escolha um semestre:", options=options)

    async def callback(self, interaction: discord.Interaction):
        view = DatasView(lembretes1 if self.values[0] == "1" else lembretes2)
        await interaction.response.send_message("📅 **Escolha uma data:**", view=view, ephemeral=True)

class DatasSelect(discord.ui.Select):
    def __init__(self, lembretes):
        options = [discord.SelectOption(label=data, description=info["nome"], value=data) for data, info in lembretes.items()]
        super().__init__(placeholder="Escolha uma data:", options=options[:25])

    async def callback(self, interaction: discord.Interaction):
        data = self.values[0]
        info = lembretes1.get(data) or lembretes2.get(data)
        embed = discord.Embed(title=f"📅 {info['nome']} ({data})", description=info["descricao"], color=discord.Color.blue())
        await interaction.response.send_message(embed=embed, ephemeral=True)

class SemestreView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(SemestreSelect())

class DatasView(discord.ui.View):
    def __init__(self, lembretes):
        super().__init__()
        self.add_item(DatasSelect(lembretes))

async def setup(bot):
    @bot.tree.command(name="datas", description="Consulte as datas comemorativas do Horário de Verão! 📅")
    async def datas(interaction: discord.Interaction):
        await interaction.response.send_message("📅 **Escolha um semestre:**", view=SemestreView(), ephemeral=True)
