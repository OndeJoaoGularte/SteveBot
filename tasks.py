import discord
from discord.ext import tasks
from datetime import datetime, time

def setup(bot):
    chat=719744273989500951

    lembretes = {
        "01-05": "Feliz dia da Menina para todas as meninas!",
        "01-21": "Feliz dia do Dirigui para todos os diriguis!",
        "01-30": "Feliz dia do Club Penguin!",
        "02-11": "Feliz dia do Cellbit!",
        "02-25": "Feliz dia do Sonegator Robinson!",
        "03-10": "Feliz dia do Maledeto!",
        "04-04": "Feliz dia Oficial do Amor!",
        "04-21": "Feliz dia da Independência!",
        "04-30": "Feliz dia do FC da Yoshi!",
        "05-24": "Feliz dia do Ninjax!",
        "06-08": "Feliz dia da Proclamação do Império!",
        "06-12": "Feliz dia dos Nomes!",
        "06-24": "Feliz dia do Festival do Arroto!",
        "07-02": "Feliz cu!",
        "07-08": "Feliz dia do Iceberg!",
        "07-11": "Feliz dia Feriado!",
        "08-23": "Feliz dia do Amino!",
        "08-26": "Feliz dia da Grande Depressão!",
        "09-04": "Feliz dia do Virgem!",
        "09-17": "Feliz dia de São Nunca!",
        "09-28": "Feliz dia do Sexo Louco!",
        "10-01": "Feliz dia da Masturbação!",
        "10-02": "Feliz dia da Mulher!",
        "10-28": "Feliz Halloween de Verão!",
        "11-06": "Feliz dia da Depressão!",
        "11-07": "Feliz dia do Blauber!",
        "11-22": "Feliz dia da Sanfona!",
        "12-10": "Feliz dia do Harry Styles!",
        "12-12": "Feliz Eleição!",
        "12-24": "Feliz Feriado de Natal 0!",
        "12-26": "Feliz Feriado de Natal 2!"
    }

    @tasks.loop(hours=24)
    async def verificar_lembretes():
        hoje = datetime.now().strftime("%m-%d")
        canal = bot.get_channel(chat)

        if hoje in lembretes and canal:
            mensagem = f"@everyone 🔔 {lembretes[hoje]}"
            await canal.send(mensagem, allowed_mentions=discord.AllowedMentions(everyone=True))

    @tasks.loop(time=time(13, 00))
    async def enviar_mensagem():
        canal = bot.get_channel(chat)
        if canal:
            await canal.send("Tá na hora do Steve!")

    enviar_mensagem.start()
    verificar_lembretes.start()