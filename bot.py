import discord
from discord.ext import commands

from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados com {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá {ctx.author.mention}!')

@bot.command()
async def pasw(ctx):
    senha = gen_pass(10)
    await ctx.send(f'Sua senha gerada é: {senha}')


bot.run('MTU1NzQ2MDQxMDc2Mjc5NzA2Ng.G9fo1H.VWrzoGliR_TFz7nmRo6NUFuGkqBTXBJYcuKZQ0')
