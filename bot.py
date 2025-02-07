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

bot.run(TOKEN)
