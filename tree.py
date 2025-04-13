import discord

async def setup(bot: discord.Client):
    await bot.load_extension("commands.general.segredo")
    await bot.load_extension("commands.general.ping")
    await bot.load_extension("commands.general.playlist")
    await bot.load_extension("commands.general.falar")
    await bot.load_extension("commands.general.help")
    await bot.load_extension("commands.general.conselho")
    await bot.load_extension("commands.general.acontecimento")
    await bot.load_extension("commands.general.fato")
    await bot.load_extension("commands.general.gritar")
    await bot.load_extension("commands.general.guru")
    await bot.load_extension("commands.general.iceberg")
    await bot.load_extension("commands.general.oraculo")
    await bot.load_extension("commands.general.piada")
    await bot.load_extension("commands.general.versiculo")
    await bot.load_extension("commands.general.amor")
    
    await bot.load_extension("commands.utility.datas")
    await bot.load_extension("commands.utility.lembrete")