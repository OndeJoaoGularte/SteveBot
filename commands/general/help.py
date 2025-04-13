import discord

class HelpSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Comandos Gerais", description="Veja os comandos gerais do steVe"),
            discord.SelectOption(label="Comandos Úteis", description="Veja comandos para te ajudar no dia a dia"),
            discord.SelectOption(label="Outras Funções", description="Veja funções automáticas do steVe")
        ]
        super().__init__(placeholder="Selecione uma categoria...", options=options, custom_id="help_select")

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(color=discord.Color.orange())
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/719744273989500951/1355065126687866890/stevefoda.png")

        if self.values[0] == "Comandos Gerais":
            embed.title = "Comandos Gerais"
            embed.description = "Comandos gerais para conhecer e virar amigo do steVe! 😁💘"
            embed.add_field(name="\u200B", value="\u200B", inline=False)
            embed.add_field(name="/ping", value="Apresentação do steVe  👦🏽", inline=True)
            embed.add_field(name="/playlist", value="Conheça a Playlist favorita do steVe 🎶", inline=True)
            embed.add_field(name="", value="", inline=False)
            embed.add_field(name="/segredo", value="Peça ao steVe para te contar um segredo 🤫", inline=True)
            embed.add_field(name="/falar", value="Peça ao steVe para repetir algo 🗣️", inline=True)
            embed.add_field(name="", value="", inline=False)
            embed.add_field(name="/piada", value="Peça ao steve para te contar uma piada 🤣", inline=True)
            embed.add_field(name="/conselho", value="Peça ao steVe para te dar um conselho 🤗", inline=True)
            embed.add_field(name="", value="", inline=False)
            embed.add_field(name="/guru", value="Peça ao steve para recitar um ensinamento do guru 🪷", inline=True)
            embed.add_field(name="/gritar", value="Peça ao steVe para gritar 😱", inline=True)
            embed.add_field(name="", value="", inline=False)
            embed.add_field(name="/oraculo", value="Peça ao steve para ver sua sorte 🍀", inline=True)
            embed.add_field(name="/versiculo", value="Peça ao steVe recitar uma passagem bíblica 🕊️", inline=True)
            embed.add_field(name="", value="", inline=False)
            embed.add_field(name="/acontecimento", value="Peça ao steve para te relembrar de algum acontecimento do Horário de Verão 🤔", inline=True)
            embed.add_field(name="/iceberg", value="Peça ao steVe para explorar o iceberg do Horário de Verão 🧊", inline=True)
            embed.add_field(name="", value="", inline=False)
            embed.add_field(name="/fato", value="Peça ao steVe para te contar um fato histórico 🧐", inline=True)
            embed.add_field(name="/amor", value="Peça ao steVe para calcular o quanto ele te ama 💓", inline=True)

        elif self.values[0] == "Comandos Úteis":
            embed.title = "Comandos Úteis"
            embed.description = "Comandos úteis para realizar alguma tarefa junto do seu amigo steVe! 🤗💞"
            embed.add_field(name="/lembrete", value="Deixa que o steVe te lembra 📢", inline=True)
            embed.add_field(name="/datas", value="Consulte as datas comemorativas do Horário de Verão 🗓️", inline=True)
            embed.add_field(name="", value="", inline=False)
            embed.add_field(name="/nome", value="Peça ao steVe para gerar um nome maluco 🤪", inline=True)
            embed.add_field(name="/bater", value="Peça a permissão do steve para bater em alguém 👊🏽", inline=True)
            embed.add_field(name="", value="", inline=False)
            embed.add_field(name="/beijar", value="Peça a permissão do steve para beijar alguém 💋", inline=True)
            embed.add_field(name="/casar", value="Peça a permissão do steve para casar com alguém 💍", inline=True)
            embed.add_field(name="", value="", inline=False)
            embed.add_field(name="/shipp", value="Peça ao steve para medir a química de um casal 🥰", inline=True)
            embed.add_field(name="/duelo", value="Peça ao steve para calcular quem ganharia em um duelo ⚔️", inline=True)

        elif self.values[0] == "Outras Funções":
            embed.title = "Outras Funções"
            embed.description = "Conheça as outras funções que seu amigo steVe realiza de forma autônoma e proativa! 🫡❣️"
            embed.add_field(name="\u200B", value="\u200B", inline=False)
            embed.add_field(name="Relembrar datas", value="O steVe está sempre preparado para avisar de qualquer feriado do Horário de Verão 🎉", inline=True)
            embed.add_field(name="", value="", inline=False)
            embed.add_field(name="Conceder cargos automáticos", value="O steVe está sempre garantindo que todos os novos integrantes do Horário de Verão tenham seus cargos 😉", inline=True)
            embed.add_field(name="", value="", inline=False)
            embed.add_field(name="Lembretes do Youtube", value="O steVe está sempre atento às novidades do canal Horário de Verão 🎮", inline=True)
        
        embed.add_field(name="\u200B", value="", inline=False)
        embed.add_field(name="Tá na hora do steVe! 🕐", value="Mesmo sendo um cara meio desastrado, eu sempre dou o meu melhor todos os dias! Meus amigos contam comigo.", inline=True)
        embed.set_image(url="https://media.discordapp.net/attachments/719744273989500951/1355065207034216579/steve_ops.png?ex=67e79251&is=67e640d1&hm=b03fd9d5290c9d5db6b2d9a48fe2b5d3440fbbabb6bb1d243f2fb86a80cd8670&=&format=webp&quality=lossless&width=310&height=303")
        embed.set_footer(
            text="sorry for my bad portuguese i'm still learning you know ;-;",
            icon_url="https://media.discordapp.net/attachments/719744273989500951/1355065126687866890/stevefoda.png"
        )

        await interaction.response.edit_message(embed=embed, view=self.view)

class HelpView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(HelpSelect())

async def setup(bot):
    @bot.tree.command(name="help", description="Saiba todos os comandos do steVe 📖")
    async def help(interaction: discord.Interaction):
        embed = discord.Embed(
            title="Ajuda do steVe",
            description="Escolha uma categoria abaixo para exibir uma lista com os comandos disponíveis 🤖",
            color=discord.Color.orange()
        )
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/719744273989500951/1355065126687866890/stevefoda.png")
        await interaction.response.send_message(embed=embed, view=HelpView(), ephemeral=True)