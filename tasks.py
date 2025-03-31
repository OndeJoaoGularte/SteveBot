import discord
from discord.ext import tasks
from datetime import datetime, time

canal = 719744273989500951

lembretes = {
        "05-01": "Feliz dia da Menina para todas as meninas fodas! :3",
        "21-01": "Feligui dirigui do diarigu! :3",
        "30-01": "Tô chorando cadê meu Club Penguin? ;-;",
        "11-02": "Feliz dia do Cellbit pra todos e principalmente pro nosso detetive favorito! :3",
        "25-02": "Feliz dia do Sonegator Robinson para todos os foliões! :3",
        "10-03": "Feliz dia do Maledeto! Como um dia um grande homem disse: 'Tudo isso aqui é do MA LE DE TO' :3",
        "04-04": "Feliz dia Oficial do Amor! Eu amo o amor e amo principalmente o direito das pessoas amarem quem elas quiserem :3",
        "21-04": "Feliz dia da Independência! Eu te amo ~~Ligeiro Engraçado~~ Alex Diferente :3",
        "30-04": "Feliz dia do FC da Yoshi para todas as Yoshis :3",
        "24-05": "O que é NINJAX?",
        "08-06": "Feliz dia da Proclamação do Império! Eu te amo Horário de Verão e faria tudo por você :3",
        "12-06": "Feliz dia dos Nomes! Eu amo os nomes malucos, é a minha parte preferida do Horário de Verão, eles me fazem muito feliz :3",
        "24-06": "Feliz dia do Festival do Arroto... Sei lá que dia idiota...",
        "02-07": "LOUÇA NO CU",
        "08-07": "Saudades do Iceberg do Verão...",
        "11-07": "Faltam 174 dias pro fim do ano!",
        "23-08": "Feliz dia do Amino para todos os aminers!",
        "26-08": "Feliz dia da Grande Depressão! Não sei se feliz é a palavra certa na real... Sinto falta do Guru...",
        "04-09": "Feliz dia do Virgem para todos os virgens!",
        "17-09": "Feliz dia de São Nunca! O dia mais assustador do ano :O",
        "28-09": "Feliz dia do Sexo Louco! Não entendo muito bem esse dia mas eba!",
        "01-10": "Feliz dia da Masturbação! Eu... Sei lá... Feliz dia..!",
        "02-10": "Feliz dia da Mulher para o Mr Mulher! :3",
        "28-10": "Feliz Halloween de Verão! Ai que medo",
        "06-11": "Feliz dia do fim da Depressão! Eu odeio a depressão e o fato dela magoar meus amigos ;-;",
        "07-11": "Feliz dia do Blauber! Eu particularmente não acho que o Diego seja um traidor gente",
        "22-11": "Feliz dia da Sanfona! Aninha rainha e o resto girafinha! 💔",
        "10-12": "Feliz dia do Harry Styles! Ele é muito importante para a comunidade LGBT como um todo, eu amo representatividade! 💝",
        "12-12": "**censurado**",
        "24-12": "Feliz Feriado de Natal 0! Feliz aniversário Alex!",
        "26-12": "Feliz Feriado de Natal 2 para todos os natalinos! O Natal é tão bom que devia ser o ano todo :3"
    }

def setup(bot):
    @tasks.loop(hours=24)
    async def verificar_lembretes():
        hoje = datetime.now().strftime("%d-%m")
        chat = bot.get_channel(canal)

        if hoje in lembretes and chat:
            mensagem = f"🔔  \n {lembretes[hoje]}"
            await chat.send(mensagem, allowed_mentions=discord.AllowedMentions(everyone=True))

    @tasks.loop(time=time(9, 00))
    async def enviar_mensagem():
        chat = bot.get_channel(canal)
        if chat:
            await chat.send("Tá na hora do Steve!")

    enviar_mensagem.start()
    verificar_lembretes.start()