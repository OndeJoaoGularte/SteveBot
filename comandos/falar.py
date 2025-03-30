import discord

async def setup(bot):
    @bot.tree.command(name="falar", description="Peça ao steVe para falar alguma coisa 🗣️")
    async def falar(interact: discord.Interaction, texto: str):
        await interact.response.send_message(texto)