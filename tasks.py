import discord
from discord.ext import tasks
from datetime import datetime, time

def setup(bot):
    chat=719744273989500951

    lembretes = {
        "01-05": "Feliz dia da Menina para todas as meninas fodas! :3",
        "01-21": "Feligui dirigui do diarigu! :3",
        "01-30": "Tô chorando cadê meu Club Penguin? ;-;",
        "02-11": "Feliz dia do Cellbit pra todos e principalmente pro nosso detetive favorito! :3",
        "02-25": "Feliz dia do Sonegator Robinson para todos os foliões! :3",
        "03-10": "Feliz dia do Maledeto! Como um dia um grande homem disse: 'Tudo isso aqui é do MA LE DE TO' :3",
        "04-04": "Feliz dia Oficial do Amor! Eu amo o amor e amo principalmente o direito das pessoas amarem quem elas quiserem :3",
        "04-21": "Feliz dia da Independência! Eu te amo ~~Ligeiro Engraçado~~ Alex Diferente :3",
        "04-30": "Feliz dia do FC da Yoshi para todas as Yoshis :3",
        "05-24": "O que é NINJAX?",
        "06-08": "Feliz dia da Proclamação do Império! Eu te amo Horário de Verão e faria tudo por você :3",
        "06-12": "Feliz dia dos Nomes! Eu amo os nomes malucos, é a minha parte preferida do Horário de Verão, eles me fazem muito feliz :3",
        "06-24": "Feliz dia do Festival do Arroto... Sei lá que dia idiota...",
        "07-02": "LOUÇA NO CU",
        "07-08": "Saudades do Iceberg do Verão...",
        "07-11": "Faltam 174 dias pro fim do ano!",
        "08-23": "Feliz dia do Amino para todos os aminers!",
        "08-26": "Feliz dia da Grande Depressão! Não sei se feliz é a palavra certa na real... Sinto falta do Guru...",
        "09-04": "Feliz dia do Virgem para todos os virgens!",
        "09-17": "Feliz dia de São Nunca! O dia mais assustador do ano :O",
        "09-28": "Feliz dia do Sexo Louco! Não entendo muito bem esse dia mas eba!",
        "10-01": "Feliz dia da Masturbação! Eu... Sei lá... Feliz dia..!",
        "10-02": "Feliz dia da Mulher para o Mr Mulher! :3",
        "10-28": "Feliz Halloween de Verão! Ai que medo",
        "11-06": "Feliz dia do fim da Depressão! Eu odeio a depressão e o fato dela magoar meus amigos ;-;",
        "11-07": "Feliz dia do Blauber! Eu particularmente não acho que o Diego seja um traidor gente",
        "11-22": "Feliz dia da Sanfona! Aninha rainha e o resto girafinha! 💔",
        "12-10": "Feliz dia do Harry Styles! Ele é muito importante para a comunidade LGBT como um todo, eu amo representatividade! 💝",
        "12-12": "**censurado**",
        "12-24": "Feliz Feriado de Natal 0! Feliz aniversário Alex!",
        "12-26": "Feliz Feriado de Natal 2 para todos os natalinos! O Natal é tão bom que devia ser o ano todo :3"
    }

    @tasks.loop(hours=24)
    async def verificar_lembretes():
        hoje = datetime.now().strftime("%m-%d")
        canal = bot.get_channel(chat)

        if hoje in lembretes and canal:
            mensagem = f"@everyone 🔔 {lembretes[hoje]}"
            await canal.send(mensagem, allowed_mentions=discord.AllowedMentions(everyone=True))

    @tasks.loop(time=time(9, 00))
    async def enviar_mensagem():
        canal = bot.get_channel(chat)
        if canal:
            await canal.send("Tá na hora do Steve!")

    enviar_mensagem.start()
    verificar_lembretes.start()