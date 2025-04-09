import discord

async def setup(bot):
    @bot.tree.command(name="playlist", description="Conheça a Playlist favorita do steVe 🎶")
    async def playlist(interact: discord.Interaction):
        await interact.response.send_message("This is my favourite playlist :3 \n https://open.spotify.com/playlist/6SvFeIyMAnLq7m5zc10f2g?si=f443a7f7ef504acf")