import discord
import random

async def setup(bot):
    conselhos = [
        "a traição só vem daqueles que você confia.",
        "nunca deixe ninguém dizer o que você deve fazer.",
        "todo forte, também é fraco. todo campeão também já enfrentou várias derrotas. todo choro, também já durou uma noite. mas o importante é que a alegria vem ao amanhecer.",
        "se te chamarem de lixo, lembre-se. todo lixo pode ser reciclado.",
        "o problema não é o poder, mas sim, quem o detém.",
        "levanta a cabeça, princesa. Se não, a coroa cai.",
        "quem é meu campeão? quem? isso mesmo, você!",
        "se um dia você acordar se sentindo mal, levanta, toma um copo d'água, come uma torrada... isso sempre me alegra.",
        "um dia eu acordei triste, aí eu fui, sei lá, comer uma maçã.",
        "deu errado? tenta a mesma coisa de novo, mas dessa vez melhor.",
        "se você não pode convencê-los, confunda-os.",
        "não tem problema falar sem pensar, pelo menos alguém vai rir.",
        "problema ignorado é problema resolvido.",
        "uma boa dica é sempre dormir de calça jeans e tênis, aí não precisa se arrumar na hora de acordar.",
        "se o despertador não te acordar, houve um motivo.",
        "nunca olhe diretamente para uma tulipa.",
        "se você vir um pombo hoje... já sabe o que significa.",
        "dormir é bom, acordar é uma dádiva.",
        "lembre-se que há milhões de anticorpos que morreriam por você.",
        "se tudo der errado, saiba que seu amigo steVe sempre estará aqui por você.",
        "uma vida irrefletida não vale a pena ser vivida.",
        "erga-se ou será erguido."
        ]

    @bot.tree.command(name="conselho", description="Peça ao steVe para te dar um conselho 🤗")
    async def conselho(interact: discord.Interaction):
        await interact.response.send_message(random.choice(conselhos))
