import discord
import os
from discord.ext import commands
import requests
import random
import asyncio
import youtube_dl

# bot_logic in original

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

kask = ["kask","kaskım","Kaskımı","kaskını","kaskini","kaskin"]

def sifre_olusturucu(sifre_uzunlugu):
    ogeler = "+-/*!&$#?=@<>"
    sifre = ""

    for i in range(sifre_uzunlugu):
        sifre += random.choice(ogeler)

    return sifre

def cumle():

    cumlesec = random.randint(1,5)

    if cumlesec == 1:
        return "KASKIMI GERİ VER"
    
    elif cumlesec == 2:
        return "BİSİKLET KASKI O NE KADAR DEĞERLİ BİLİYOR MUSUN?"
    
    elif cumlesec == 3:
        return "KASKIMI GERİ VERİR MİSİN?"
    
    elif cumlesec == 4:
        return "KIRMA!"
    
    elif cumlesec == 5:
        return "KASKIMI ZORLA ALIYORSUNUZ ŞUAN"



def emoji_olusturucu():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)


def yazi_tura():
    para = random.randint(0, 5)
    if para == 0:
        return "YAZI"
    else:
        return "TURA"


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command('mem')
async def mem(ctx):
    randomMem = random.choice(os.listdir('img'))
    with open(f"img/{randomMem}" , "rb") as f:
        pic = discord.File(f)

    await ctx.send(file=pic)    


def getDogImg():
    url = 'https://random.dog/woof.json'
    response = requests.get(url)
    data = response.json()
    return data['url']

@bot.command('dog')
async def dog(ctx):
    dogImg = getDogImg()
    await ctx.send(dogImg)

@bot.listen()
async def on_message(message):
    randomMem = random.choice(os.listdir('img'))
    with open(f"img/{randomMem}" , "rb") as f:
        pic = discord.File(f)

    if message.author != bot.user:
        content = message.content.lower()  
        for kelime in kask:
            if kelime in content:
                response = cumle()
                await message.channel.send(response)
                await message.send(file=pic)
                break


              


    
            

            


        



@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')



@bot.command()
async def sans(ctx):
    await ctx.send("kaybeden biber yer 🌶️ "+yazi_tura())



voice_clients = {}

yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options = {'options': '-vn'}

@bot.event
async def on_message(msg):
    if msg.content.startswith("play"):
        try:
            url = msg.content.split()[1]

            voice_client = await msg.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client

            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None,lambda: ytdl.extract_info(url ,download = False))

            song = data['url']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options , executable="C:\\ffmpeg\\ffmpeg.exe")

            voice_client.play(player)


        except Exception as err:
            print(err)

        if msg.content.startswith("?pause"):
            try:
                voice_clients[msg.guild.id].pause()
            except Exception as err:
                print(err)

        if msg.content.startswith("?resume"):
            try:
                voice_clients[msg.guild.id].resume()
            except Exception as err:
                print(err)

        if msg.content.startswith("?stop"):
            try:
                voice_clients[msg.guild.id].stop()
                await voice_clients[msg.guild.id].disconnect()
            except Exception as err:
                print(err)



    







    

bot.run("MTE1MzM3NjE1MDI5MTIxODQ4Mw.GH_8zg.ueOcL8I9sbuNRmzhPIhDMZhrPFwck8qdCzR6p0")