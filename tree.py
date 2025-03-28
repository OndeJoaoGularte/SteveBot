import discord
import random

async def setup(bot: discord.Client):
    @bot.tree.command(name="ping", description="Apresentação do Steve 👦🏽")
    async def ping(interact: discord.Interaction):
        await interact.response.send_message(f"Hello {interact.user.display_name}, my name is Steve! I love Horário de Verão :D")

    @bot.tree.command(name="playlist", description="Conheça a Playlist favorita do Steve 🎶")
    async def playlist(interact: discord.Interaction):
        await interact.response.send_message("This is my favourite playlist :3 \n https://open.spotify.com/playlist/6SvFeIyMAnLq7m5zc10f2g?si=f443a7f7ef504acf")

    @bot.tree.command(name="falar", description="Peça ao Steve para falar alguma coisa 🗣️")
    async def falar(interact: discord.Interaction, texto: str):
        await interact.response.send_message(texto)

    segredos = ["heyy", "hiii!", "hello!!", "hey :3", "hi :P"]

    @bot.tree.command(name="segredo", description="Peça para o Steve te contar um segredo 🤫")
    async def segredo(interact: discord.Interaction):
        resposta = random.choice(segredos)
        await interact.response.send_message(resposta, ephemeral=True)