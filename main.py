import discord
from discord.ext import commands
from model import detect_class
from os import remove

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć! Jestem botem, {bot.user}!')

@bot.command()
async def receive(ctx):
    if len(ctx.message.attachments) > 0:
        for attachment in ctx.message.attachments:
            names = {
                "Pigeon": "Gołębia",
                "Sparrow": "Wróbla"
            }

            file_path = f"./files/{attachment.filename}"
            await attachment.save(file_path)
            await ctx.send("Przetwarzanie pliku, proszę czekać...")

            result = detect_class(file_path)

            if result[1] > 0.8:
                await ctx.send(f"Udało się rozpoznać {names[result[0]]}")
            else:
                await ctx.send("Niestety nie udało się rozpoznać co to jest za ptak")
            
            remove(file_path)
    else:
        await ctx.send("Ta komenda oczekuje załączenia do niech co najmniej jednego obrazka!")


bot.run("")