import discord
from discord.ext import commands
import json
import random

with open('setting.json','r',encoding='utf8')as jfile:
    jdata=json.load(jfile)


intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(int(jdata[Welcome_channel]))
    await channel.send(f'{member}是醜男還偷偷進來')

@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(int(jdata[Leave_channel]))
    await channel.send(f'{member} 滾啦')

@bot.command()
async def ping(ctx):#ctx自動偵測說話那個人資料
    await ctx.send(f'{round(bot.latency*1000)}(ms)')#latency延遲

@bot.command()
async def fuck(ctx):#ctx自動偵測說話那個人資料
    await ctx.send('幹不要亂罵啦')

@bot.command()
async def 笑話1(ctx):#ctx自動偵測說話那個人資料
    await ctx.send('先進船的人會先說什麼 ？想知道答案打\n!笑話1解答')

@bot.command()
async def 笑話1解答(ctx):#ctx自動偵測說話那個人資料
    await ctx.send('會說online\n因為仙境傳說online')

@bot.command()
async def 笑話2(ctx):#ctx自動偵測說話那個人資料
    await ctx.send('客人吃完東西服務生問：那我收囉？\n 客人：好然後客人就開始跳舞了')

@bot.command()
async def 東大小羅(ctx):
    await ctx.send('來自天外奇蹟的主角')

@bot.command()
async def 小羅照片(ctx):
    random_pic=random.choice(jdata['pic'])
    pic1=discord.File(random_pic)
    await ctx.send(file=pic1)

@bot.command()
async def 網路上爺爺照片(ctx):
    random_pic2=random.choice(jdata['url_pic'])
    pic2=discord.File(random_pic2)
    await ctx.send(file=pic2)

@bot.command()
async def 學餐(ctx):
    random_dinner=random.choice(jdata['dinner'])
    dinner=discord.File(random_dinner)
    await ctx.send(file=dinner)

@bot.command()
async def 清單(ctx):
    await ctx.send('ping\nfuck\n笑話1\n笑話2\n東大小羅\n小羅照片\n網路上爺爺照片\n學餐\n')

@bot.command()
async def 賽狗(ctx):
    await ctx.send('拉機賽狗')

bot.run(jdata['TOKEN'])#字典去找token

