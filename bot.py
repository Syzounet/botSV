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
async def W(ctx):
    await ctx.send("Bienvenue dans la chasse au trésor chaque 'jeu' te donneras une lettre avec lesquelles tu devras envoyer '!lettre' pour continuer a jouer ! Voici ton premier indice :")
    await ctx.send("« Un jour où l'été approche, nos vies se sont entremêlées. ».")
    await ctx.send("Scanne ce QR code pour la suite :")

    # Générer un QR code avec un lien vers le site
    qr = qrcode.make("http://5.196.26.73/site/")
    qr.save("indice1.png")

    await ctx.send(file=discord.File("indice1.png"))

# 🔌 Mini-jeu électronique
@bot.command()
async def Y(ctx):
    await ctx.send("Défi spécial : Connecte le circuit correctement pour allumer la LED 💡")
    await ctx.send("Joue ici : http://5.196.26.73/site/mini-jeu/index.html")

@bot.command()
async def M(ctx):
    await ctx.send("Tu as trouvé la lettre M")
    await ctx.send("Voici maintenant une dernière énigme pour toi :")
    message = (
        "🔍 **Énigme :**\n\n"
        "**\"Un lieu de passage où les cœurs se croisent,**\n"
        "**Entre départs pressés et attentes parfois lasses.**\n"
        "**On y trouve des rêves entre deux bouchées,**\n"
        "**Un emblème doré sous des arches dressées.**\n"
        "**C’est là qu’un 'oui' a scellé le destin,**\n"
        "**Dans un coin familier, à l’abri du train.\"**\n\n"
    )
    await ctx.send(message)

@bot.command()
async def macdo(ctx):
    await ctx.send("Bravo trop forte la meilleur même")
    await ctx.send("Tu as trouvé la lettre V")

# 🎁 Fin de la chasse au trésor
@bot.command()
async def V(ctx):
    await ctx.send("Mon baybay ta réussi bravo 🎉")
    await ctx.send("Tu dois savoir, que quoi qu'il arrive, je serais toujours la pour toi parce qu'on forme une putain d'équipe. Nous deux contre le monde, parce que toi, c'est moi et moi c'est toi. Parce que toi et moi c'est vrai c'est absolument authentique tellement que ça brûle dans mon coeur, mon amour. j'aime cette histoire qu'on est entrain d'écrire et je te fais la promesse que je ne laisserais pas ce monde briser ta douceur ")
    await ctx.send("*Joyeuse Saint-Valentin mon baybay ❤️")
bot.run(TOKEN)
