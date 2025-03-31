import discord
import random

async def setup(bot):
    segredos = [
        "I have alektorophobia, I ended up developing it after something horrible happened to me in a chicken coop", 
        "my dream is to study history at a top university like MIT, Oxford, or Harvard :3", 
        "for me, there's nothing more important than my friends. They are the family I chose!",
        "my passion for history actually started with philosophy. When I discovered that there was a possibility Socrates might not have even existed, I became fascinated by ancient history, especially the history and culture of Athens!", 
        "I spent almost two months on an exchange program at João's house (Ligeiro Engraçado lol), learning a bit of portuguese and, most importantly, math, physics, and chemistry. He taught me many important things, and I'm very grateful for that! The most important thing I learned from him was how a friendship can be pure and beautiful 💝",
        "my father's name is Mohan Kumar! I got my last name from him :3",
        "my mother's name is Aisha Kumar! It was her idea to immigrate to Canada even before I was born. She is very Christian, just like me :3",
        "my uncle died by manhole. One time, he bent down to look at it, and a snake bit him on the head... I miss Uncle Veeram a lot...",
        "my favorite band is Skillet! I love how they manage to create songs that indirectly reference religion—so those who know the Word of the Lord interpret it one way, and those who don’t interpret it another!",
        "I used to swim when I was younger. I remember that at the age of 8, I won my first championship! Nowadays, I don't swim as often, but I'm still a great swimmer, okay?",
        "I was really nervous when I was heading to Belgium, especially because I went straight from Brazil here without having time to visit my parents in Canada. But being here has been great for me! No offense to João, but Marco is way better at physics than he is, and he’s teaching me everything!",
        "It's been almost a year since I last saw my parents, I miss them a lot. They’ve always supported me in everything, including my exchange program... One day, I want to be able to repay them for everything they did for me",
        "I have a soft spot for chocolate cake—it's my absolute favorite dessert!",
        "when I was a kid, I dreamed of being an astronaut. I wanted to explore space more than anything!",
        "I secretly love watching \"Rap de Anime\" when I’m feeling stressed—it helps me relax and forget about everything for a while. Ordeeeem e Caaaos 🎶 ",
        "I once tried to learn how to play the guitar, but I gave up after a few lessons. I have sensitive fingers you know...",
        "sometimes, I sit by the window and watch the rain for hours. There's something so peaceful about it, I don't know what...",
        "if I could live anywhere in the world, I think I’d love to live in Japan. They would call me \"steVe-san\" hehe dattebayo!"
        ]

    @bot.tree.command(name="segredo", description="Peça para o steVe te contar um segredo 🤫")
    async def segredo(interact: discord.Interaction):
        await interact.response.send_message(random.choice(segredos), ephemeral=True)
