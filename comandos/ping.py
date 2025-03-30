import discord

async def setup(bot):
    @bot.tree.command(name="ping", description="Apresentação do steVe 👦🏽")
    async def ping(interact: discord.Interaction):
        await interact.response.send_message(f"Hello {interact.user.display_name}, my name is steVe! I love Horário de Verão :D")


