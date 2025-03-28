import discord
import random
import asyncio

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
    "11-22": {"nome": "Dia da Sanfona", "descricao": "Ana rainha o resto girafinha"},
    "12-10": {"nome": "Dia do Harry Styles", "descricao": "Dia que a rainha Ana viu o show do Harry Styles"},
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

        super().__init__(
            placeholder="Escolha um semestre:",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        semestre = self.values[0]
        view = DatasView(lembretes1 if semestre == "1" else lembretes2)
        await interaction.response.send_message("📅 **Escolha uma data:**", view=view, ephemeral=True)

class DatasSelect(discord.ui.Select):
    def __init__(self, lembretes: dict):
        options = [
            discord.SelectOption(label=data, description=info["nome"], value=data)
            for data, info in lembretes.items()
        ]

        super().__init__(
            placeholder="Escolha uma data:",
            min_values=1,
            max_values=1,
            options=options[:25],
        )

    async def callback(self, interaction: discord.Interaction):
        data_escolhida = self.values[0]
        info = lembretes1.get(data_escolhida) or lembretes2.get(data_escolhida)

        embed = discord.Embed(
            title=f"📅 {info['nome']} ({data_escolhida})",
            description=info["descricao"],
            color=discord.Color.blue()
        )

        await interaction.response.send_message(embed=embed, ephemeral=True)

class SemestreView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(SemestreSelect())


class DatasView(discord.ui.View):
    def __init__(self, lembretes: dict):
        super().__init__()
        self.add_item(DatasSelect(lembretes))

async def setup(bot: discord.Client):
    @bot.tree.command(name="ping", description="Apresentação do steVe 👦🏽")
    async def ping(interact: discord.Interaction):
        await interact.response.send_message(f"Hello {interact.user.display_name}, my name is steVe! I love Horário de Verão :D")

    @bot.tree.command(name="playlist", description="Conheça a Playlist favorita do steVe 🎶")
    async def playlist(interact: discord.Interaction):
        await interact.response.send_message("This is my favourite playlist :3 \n https://open.spotify.com/playlist/6SvFeIyMAnLq7m5zc10f2g?si=f443a7f7ef504acf")

    @bot.tree.command(name="falar", description="Peça ao steVe para falar alguma coisa 🗣️")
    async def falar(interact: discord.Interaction, texto: str):
        await interact.response.send_message(texto)

    @bot.tree.command(name="lembrete", description="Deixa que o steVe te lembra! 📢")
    async def lembrete(interaction: discord.Interaction, minutos: int, mensagem: str):
        await interaction.response.send_message(f"⏳ Lembrete definido para **{minutos} minutos**: {mensagem}", ephemeral=True)

        await asyncio.sleep(minutos * 60)

        await interaction.followup.send(f"🔔 {interaction.user.mention} **Lembrete:** {mensagem}")

    segredos = ["heyy", "hiii!", "hello!!", "hey :3", "hi :P"]

    @bot.tree.command(name="segredo", description="Peça para o steVe te contar um segredo 🤫")
    async def segredo(interact: discord.Interaction):
        resposta = random.choice(segredos)
        await interact.response.send_message(resposta, ephemeral=True)

    @bot.tree.command(name="help", description="Saiba todos os comandos do steVe 📖")
    async def help(interaction: discord.Interaction):
        embed = discord.Embed(
            title="Comandos do steVe:",
            description="Uma lista com todas as funções do steVe 🤖",
            color=discord.Color.brand_green()
        )
        
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/719744273989500951/1355065126687866890/stevefoda.png?ex=67e7923e&is=67e640be&hm=81fc3e09de1cdeffd6c2b78687f5788c558e90dc4ea3a3a22e5d08b13d9e67c2&=&format=webp&quality=lossless&width=453&height=431")

        embed.add_field(name="\u200B", value="\u200B", inline=False)
        embed.add_field(name="Comandos Gerais:", value="Comandos gerais para conhecer e virar amigo do steVe! 😁💘", inline=False)
        embed.add_field(name="/ping", value="Apresentação do steVe  👦🏽", inline=True)
        embed.add_field(name="/playlist", value="Conheça a Playlist favorita do steVe 🎶", inline=True)
        embed.add_field(name="/segredo", value="Peça para o steVe te contar um segredo 🤫", inline=True)
        embed.add_field(name="/falar", value="Peça ao steVe para falar algo 🗣️", inline=True)

        embed.add_field(name="\u200B", value="\u200B", inline=False)
        embed.add_field(name="Comandos Úteis:", value="Comandos úteis para realizar alguma tarefa junto do seu amigo steVe! 🤗💞", inline=False)
        embed.add_field(name="/lembrete", value="Deixa que o steVe te lembra! 📢", inline=True)
        embed.add_field(name="/datas", value="Consulte as datas comemorativas do Horário de Verão! 🗓️", inline=True)

        embed.add_field(name="\u200B", value="\u200B", inline=False)
        embed.add_field(name="Outras Funções:", value="Conheça as outras funções que seu amigo steVe realiza de forma autônoma e proativa! 🫡❣️", inline=False)
        embed.add_field(name="Relembrar datas!", value="O steVe sempre vai nos lembrar dos feriados do Horário de Verão!  🎉", inline=True)

        embed.add_field(name="\u200B", value="\u200B", inline=False)
        embed.add_field(name="Tá na hora do steVe! 🕐", value="Mesmo sendo um cara meio desastrado, eu sempre dou o meu melhor todos os dias! Meus amigos contam comigo.", inline=True)

        embed.set_image(url="https://media.discordapp.net/attachments/719744273989500951/1355065207034216579/steve_ops.png?ex=67e79251&is=67e640d1&hm=b03fd9d5290c9d5db6b2d9a48fe2b5d3440fbbabb6bb1d243f2fb86a80cd8670&=&format=webp&quality=lossless&width=310&height=303")

        embed.set_footer(
            text="sorry for my bad portuguese i'm still learning you know ;-;",
            icon_url="https://media.discordapp.net/attachments/719744273989500951/1355065126687866890/stevefoda.png?ex=67e7923e&is=67e640be&hm=81fc3e09de1cdeffd6c2b78687f5788c558e90dc4ea3a3a22e5d08b13d9e67c2&=&format=webp&quality=lossless&width=453&height=431"
        )

        await interaction.response.send_message(embed=embed)

    @bot.tree.command(name="datas", description="Consulte as datas comemorativas do Horário de Verão! 📅")
    async def datas(interaction: discord.Interaction):
        await interaction.response.send_message(
            "📅 **Escolha um semestre:**",
            view=SemestreView(),
            ephemeral=True
        )