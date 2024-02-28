import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
    print(15,"giriş yaptı")
    

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    if count_heh > 1000:
        await ctx.send("beni tekerleme yapan adam mı sandın")
    else:
        await ctx.send("he"* count_heh)

@bot.command()
async def deniz(ctx,a):
    await ctx.send("merhaba deniz" * int(a) )



bot.run("")
