import discord
from discord.ui import View, Button

PLAYLIST_URL = "https://open.spotify.com/playlist/6SvFeIyMAnLq7m5zc10f2g?si=f443a7f7ef504acf"

async def setup(bot):
    @bot.tree.command(name="playlist", description="Conheça a Playlist favorita do steVe 🎶")
    async def playlist(interaction: discord.Interaction):
        embed = discord.Embed(
            title="Playlist do steVe! 🎸",
            description=(
                "Essa é a minha playlist favorita :3"
            ),
            color=discord.Color.from_rgb(0, 255, 127)
        )
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/719744273989500951/1418392301750980732/image.png")

        view = View()
        view.add_item(Button(label="Ouvir no Spotify", style=discord.ButtonStyle.link, url=PLAYLIST_URL, emoji="🎧"))

        await interaction.response.send_message(embed=embed, view=view)