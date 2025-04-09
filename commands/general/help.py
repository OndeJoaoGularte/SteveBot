import discord

async def setup(bot):
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
        embed.add_field(name="/lembrete", value="Deixa que o steVe te lembra 📢", inline=True)
        embed.add_field(name="/datas", value="Consulte as datas comemorativas do Horário de Verão 🗓️", inline=True)

        embed.add_field(name="\u200B", value="\u200B", inline=False)
        embed.add_field(name="Outras Funções:", value="Conheça as outras funções que seu amigo steVe realiza de forma autônoma e proativa! 🫡❣️", inline=False)
        embed.add_field(name="Relembrar datas", value="O steVe sempre vai nos lembrar dos feriados do Horário de Verão  🎉", inline=True)

        embed.add_field(name="\u200B", value="\u200B", inline=False)
        embed.add_field(name="Tá na hora do steVe! 🕐", value="Mesmo sendo um cara meio desastrado, eu sempre dou o meu melhor todos os dias! Meus amigos contam comigo.", inline=True)

        embed.set_image(url="https://media.discordapp.net/attachments/719744273989500951/1355065207034216579/steve_ops.png?ex=67e79251&is=67e640d1&hm=b03fd9d5290c9d5db6b2d9a48fe2b5d3440fbbabb6bb1d243f2fb86a80cd8670&=&format=webp&quality=lossless&width=310&height=303")

        embed.set_footer(
            text="sorry for my bad portuguese i'm still learning you know ;-;",
            icon_url="https://media.discordapp.net/attachments/719744273989500951/1355065126687866890/stevefoda.png?ex=67e7923e&is=67e640be&hm=81fc3e09de1cdeffd6c2b78687f5788c558e90dc4ea3a3a22e5d08b13d9e67c2&=&format=webp&quality=lossless&width=453&height=431"
        )

        await interaction.response.send_message(embed=embed)