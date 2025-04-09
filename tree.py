import discord

async def setup(bot: discord.Client):
    await bot.load_extension("commands.general.segredo")
    await bot.load_extension("commands.general.ping")
    await bot.load_extension("commands.general.playlist")
    await bot.load_extension("commands.general.falar")
    await bot.load_extension("commands.general.help")
    
    await bot.load_extension("commands.utility.datas")
    await bot.load_extension("commands.utility.lembrete")