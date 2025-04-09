import discord
import asyncio
from discord import app_commands

async def setup(bot):
    @bot.tree.command(name="lembrete", description="Deixa que o steVe te lembra 📢")
    @app_commands.describe(
        minutos="Em quantos minutos você quer ser lembrado?",
        mensagem="O que você quer que o steVe te lembre?"
    )
    async def lembrete(interaction: discord.Interaction, minutos: int, mensagem: str):
        await interaction.response.send_message(
            f"⏳ Lembrete definido para **{minutos} minutos**: {mensagem}",
            ephemeral=True
        )

        await asyncio.sleep(minutos * 60)

        await interaction.followup.send(
            f"🔔 {interaction.user.mention} **Lembrete:** {mensagem}"
        )
