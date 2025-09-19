import discord

async def setup(bot):
    @bot.tree.command(name="ping", description="Apresentação do steVe 👦🏽")
    async def ping(interaction: discord.Interaction):
        latency_ms = round(bot.latency * 1000)

        if latency_ms <= 100:
            color = discord.Color.green()
        elif latency_ms <= 200:
            color = discord.Color.yellow()
        else:
            color = discord.Color.red()

        embed = discord.Embed(
            title="Hey, I'm steVe! 🍁",
            description=f"hello **{interaction.user.display_name}**, my name is steVe! I love Horário de Verão :3",
            color=color
        )
        embed.set_footer(text=f"my response time is {latency_ms}ms.")

        await interaction.response.send_message(embed=embed)