import discord
from discord.ext import commands

def setup(bot: commands.Bot):
    @bot.command()
    async def oi(ctx: commands.Context):
        nome = ctx.author.display_name
        await ctx.send(f"oi {nome}, eu sou o steve só que agora em python!")

    @bot.command()
    async def enviar_embed(ctx: commands.Context):
        minha_embed = discord.Embed(title="teste", description="teste")
        
        url_imagem = "https://media.discordapp.net/attachments/719744273989500951/1354945197657559150/steve.png?format=webp&quality=lossless&width=453&height=431"
        
        minha_embed.set_image(url=url_imagem)
        minha_embed.set_thumbnail(url=url_imagem)
        minha_embed.set_footer(text="teste")
        minha_embed.set_author(name="Steve", icon_url=url_imagem)

        await ctx.send(embed=minha_embed)
        await ctx.message.delete()