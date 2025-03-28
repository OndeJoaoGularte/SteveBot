import discord
import random
import asyncio

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

    @bot.tree.command(name="help", description="Saiba todos os comandos do steVe 📖")
    async def help(interaction: discord.Interaction):
        embed = discord.Embed(
            title="Comandos do steVe:",
            description="Uma lista com todos os comandos disponíveis pelo steVe 🤓",
            color=discord.Color.brand_green()
        )
        
        embed.add_field(name="\u200B", value="\u200B", inline=False)
        embed.add_field(name="Comandos Gerais:", value="Comandos gerais para conhecer e virar amigo do steVe! 😁💘", inline=False)
        embed.add_field(name="/ping", value="Apresentação do steVe 👦🏽", inline=True)
        embed.add_field(name="/playlist", value="Conheça a Playlist favorita do steVe 🎶", inline=True)
        embed.add_field(name="/segredo", value="Peça para o steVe te contar um segredo 🤫", inline=True)
        embed.add_field(name="/falar", value="Peça ao steVe para falar alguma coisa 🗣️", inline=True)

        embed.add_field(name="\u200B", value="\u200B", inline=False)
        embed.add_field(name="Comandos Úteis:", value="Comandos úteis para realizar alguma tarefa junto do seu amigo steVe! 🤗💞", inline=False)
        embed.add_field(name="/lembrete", value="Chama o steVe que ele te avisa! 📣", inline=True)

        embed.add_field(name="\u200B", value="\u200B", inline=False)
        embed.add_field(name="Outras Funções:", value="Conheça as outras funções que seu amigo steVe realiza de forma autônoma e proativa! 🫡❣️", inline=False)
        embed.add_field(name="Relembrar datas comemorativas 🗓️", value="Deixa que o steVe te lembra! 📢", inline=True)

        embed.add_field(name="\u200B", value="\u200B", inline=False)
        embed.add_field(name="Tá na hora do steVe! 🕐", value="Mesmo sendo um cara meio desastrado, eu sempre dou o meu melhor todos os dias! Meus amigos contam comigo.", inline=True)

        embed.set_image(url="https://media.discordapp.net/attachments/719744273989500951/1355065207034216579/steve_ops.png?ex=67e79251&is=67e640d1&hm=b03fd9d5290c9d5db6b2d9a48fe2b5d3440fbbabb6bb1d243f2fb86a80cd8670&=&format=webp&quality=lossless&width=310&height=303")

        embed.set_footer(
            text="sorry for my bad portuguese i'm still learning you know ;-;",
            icon_url="https://media.discordapp.net/attachments/719744273989500951/1355065126687866890/stevefoda.png?ex=67e7923e&is=67e640be&hm=81fc3e09de1cdeffd6c2b78687f5788c558e90dc4ea3a3a22e5d08b13d9e67c2&=&format=webp&quality=lossless&width=453&height=431"
        )

        await interaction.response.send_message(embed=embed)
    

    segredos = ["heyy", "hiii!", "hello!!", "hey :3", "hi :P"]

    @bot.tree.command(name="segredo", description="Peça para o steVe te contar um segredo 🤫")
    async def segredo(interact: discord.Interaction):
        resposta = random.choice(segredos)
        await interact.response.send_message(resposta, ephemeral=True)