import discord

async def setup(bot: discord.Client):
    await bot.load_extension("comandos.segredo")
    await bot.load_extension("comandos.ping")
    await bot.load_extension("comandos.playlist")
    await bot.load_extension("comandos.falar")
    await bot.load_extension("comandos.lembrete")
    await bot.load_extension("comandos.help")
    await bot.load_extension("comandos.datas")