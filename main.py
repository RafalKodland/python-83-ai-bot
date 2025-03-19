import discord
from discord.ext import commands

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
            await attachment.save(f"./files/{attachment.filename}")
            await ctx.send("Plik zapisany")
    else:
        await ctx.send("Ta komenda oczekuje załączenia do niech co najmniej jednego obrazka!")


bot.run("TOKEN")