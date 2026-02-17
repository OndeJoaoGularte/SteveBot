import discord
import json
from discord.ext import tasks
from datetime import datetime, time

# Dica: Mover esse ID para o .env como CHANNEL_ID é ainda melhor!
ID_CANAL = 719744273989500951

# Carrega os lembretes do JSON
try:
    with open('data/lembretes.json', 'r', encoding='utf-8') as f:
        lembretes_data = json.load(f)
except Exception as e:
    print(f"❌ Erro ao carregar lembretes: {e}")
    lembretes_data = {}

def setup(bot):
    # Loop que roda em horários específicos (9 da manhã e 9:01 da manhã)
    # Assim garantimos que ele cheque os lembretes no momento certo
    @tasks.loop(time=[time(9, 0), time(9, 1)])
    async def rotina_diaria():
        hoje = datetime.now().strftime("%d-%m")
        chat = bot.get_channel(ID_CANAL)
        
        if not chat:
            return

        # Se for exatamente 9:00, manda o bom dia
        agora = datetime.now().time()
        if agora.hour == 9 and agora.minute == 0:
            await chat.send("Tá na hora do steVe! Bom dia galera! ☀️")

        # Se houver lembrete para hoje, manda também
        if hoje in lembretes_data:
            msg = f"🔔 **Lembrete Especial do Dia:**\n{lembretes_data[hoje]}"
            await chat.send(msg, allowed_mentions=discord.AllowedMentions(everyone=True))

    rotina_diaria.start()