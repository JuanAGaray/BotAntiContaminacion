import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def chiste(ctx, tipo='normal'):
    if tipo == 'normal':
        await ctx.send('Esto es un chiste')
    elif tipo == 'terror':
        await ctx.send('Esto es un chiste terror')
    elif tipo == 'animales':
        await ctx.send('Esto es un chiste animales')
    else:
        await ctx.send('Este tipo de chiste', tipo,'no existe')
        
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
        
@bot.command()
async def evento(ctx):
    img = open(r'imgs/event.jpeg', 'rb')
    img_discord = discord.File(img)
    await ctx.send(file=img_discord)
    
@bot.command()
async def img_aleatoria(ctx):
    lista_img = os.listdir('imgs')
    img = random.choice(lista_img)
    img_discord = discord.File(f'imgs/{img}')
    await ctx.send(file=img_discord)
    
@bot.command()
async def video(ctx):
    video_discord = discord.File('speed.mp4')
    await ctx.send(file=video_discord)
        
@bot.command()
async def audio(ctx):
    audio_discord = discord.File('audio.m4a')
    await ctx.send(file=audio_discord)

bot.run("token")
