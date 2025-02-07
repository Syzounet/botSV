import discord
from dotenv import load_dotenv
import os
from discord.ext import commands
import qrcode

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# 📜 Envoi du premier indice
@bot.command()
async def indice(ctx):
    await ctx.send("Bienvenue dans la chasse au trésor ! Voici ton premier indice :")
    await ctx.send("« Un jour où l'été approche, nos vies se sont entremêlées. ».")
    await ctx.send("Scanne ce QR code pour la suite :")

    # Générer un QR code avec un lien vers le site
    qr = qrcode.make("https://ton-site.com/indice1.html")
    qr.save("indice1.png")

    await ctx.send(file=discord.File("indice1.png"))

# 🎥 Vidéo comme indice
@bot.command()
async def video(ctx):
    await ctx.send("Regarde cette vidéo, elle contient un message secret :")
    await ctx.send("https://youtu.be/XXXXX")

# 🔌 Mini-jeu électronique
@bot.command()
async def minijeu(ctx):
    await ctx.send("Défi spécial : Connecte le circuit correctement pour allumer la LED 💡")
    await ctx.send("Joue ici : https://ton-site.com/jeu.html")


# 🎁 Fin de la chasse au trésor
@bot.command()
async def fin(ctx):
    await ctx.send("Mon amour ta réussi bravo 🎉")
    await ctx.send("Tu dois savoir, que quoi qu'il arrive, je serais toujours la pour toi parce qu'on forme une putain d'équipe. Nous deux contre le monde, parce que toi, c'est moi et moi c'est toi. Parce que toi et moi c'est vrai c'est absolument authentique tellement que ça brûle dans mon coeur, mon amour. j'aime cette histoire qu'on est entrain d'écrire et je te fais la promesse que je ne laisserais pas ce monde briser ta douceur ")
bot.run(TOKEN)
