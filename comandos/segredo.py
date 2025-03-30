import discord
import random

async def setup(bot):
    segredos = ["heyy", "hiii!", "hello!!", "hey :3", "hi :P"]

    @bot.tree.command(name="segredo", description="Peça para o steVe te contar um segredo 🤫")
    async def segredo(interact: discord.Interaction):
        await interact.response.send_message(random.choice(segredos), ephemeral=True)
