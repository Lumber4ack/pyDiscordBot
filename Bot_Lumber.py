import time
import discord
from random import *
from discord.ext import commands
from discord.ext.commands import Bot
from random import *
import asyncio

Bot = commands.Bot(command_prefix='!')
Bot.remove_command("help")

@Bot.event
async def on_ready():
    await Bot.change_presence(status = discord.Status.online, activity = discord.Game( "Валик в бутылко ленде" ))
@Bot.command()
async def und(ctx, amount = 1):
    await ctx.channel.purge(limit = amount)
    author = ctx.message.author
    a = f"{author.mention} I love minecraft"
    b = f"{author.mention} Gicci gang"
    c = f"{author.mention} Yuu II"
    d = f"{author.mention} GGGGGRa"
    e = f"{author.mention} Fucking Shit"
    f = f"{author.mention} Lalalal"
    g = f"{author.mention} Kanada"
    i = f"{author.mention} Я в своем познании настолько преисполнился что я как будто бы уже сто триллионов миллиардов лет проживаю на триллионах и триллионах таких же планет как эта Земля"
    list = [a, b, c, d, e, f, g, i]
    random = int(randint(0,7))
    await ctx.send(list[random])
@Bot.command(pass_context=True)
async def fsb(ctx, amount = 1):
    await ctx.channel.purge(limit = amount)
    emb = discord.Embed(title = "Fotoshop Battle", colour = discord.Color.blue())
    a1 = "https://picua.org/images/2020/02/10/a616b731649279261b067548790f90c2.jpg"
    a2 = "https://picua.org/images/2020/02/10/cfc235d79fbc44873c0c8abf8fc6685f.jpg"
    a3 = "https://picua.org/images/2020/02/10/3b1a59bc88757fc678904f06a08c2c8c.jpg"
    a4 = "https://picua.org/images/2020/02/10/fd1f900dd97debf547f01abfd6f72da3.jpg"
    a5 = "https://picua.org/images/2020/02/10/f7ab535fee1412e627f76039e8705abd.jpg"
    a6 = "https://picua.org/images/2020/02/10/475ae6ff9276b61160c845930e737e86.jpg"
    a7 = "https://picua.org/images/2020/02/10/01124ee7d28d16ad9c5f4a4260aeee57.jpg"
    a8 = "https://picua.org/images/2020/02/10/9f1266cbeb2b4c013dd92aec421873a1.jpg"
    a9 = "https://picua.org/images/2020/02/10/689a10d0c2d94f40ba1ac458444ced81.jpg"
    b1 = "https://picua.org/images/2020/02/10/e61ba250c325b245913896e6e9795316.jpg"
    b2 = "https://picua.org/images/2020/02/10/648faf367b1797a694a57cf172f47011.jpg"
    b3 = "https://picua.org/images/2020/02/10/693c0746f93b9b58c8d983f1ba905f90.png"
    b4 = "https://picua.org/images/2020/02/10/48b2f2e76784ec6808db7407da77b236.png"
    b5 = "https://picua.org/images/2020/02/10/e04d122cfc24986b279e44c4cd9644ca.jpg"
    b6 = "https://picua.org/images/2020/02/10/d3e61e43d0956c5306cede3d6138d775.jpg"
    b7 = "https://picua.org/images/2020/02/10/3b5c9c432e7ad5b5b4465cfde55b31de.jpg"
    b8 = "https://picua.org/images/2020/02/10/44d1637d39c8118ceccd62bdb0a6691b.jpg"
    b9 = "https://picua.org/images/2020/02/10/641536fc09fd69b9f8aacd1f667a0ab7.png"
    c1 = "https://picua.org/images/2020/02/10/aedc8b6e221fcd80b35c2e38c3ee1f2f.jpg"
    c2 = "https://picua.org/images/2020/02/10/bbe2d4911f6286e125e3cda2415657df.jpg"
    c3 = "https://picua.org/images/2020/02/10/332fd69ec7ae36ca3848528381a421a5.png"
    c4 = "https://picua.org/images/2020/02/10/5dde83e2b1af38c567b4f461007bf1b5.jpg"
    c5 = "https://picua.org/images/2020/02/10/c93109bbef9ba465b8116238b3ab4e80.jpg"
    foto_list=[a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5]
    random = int(randint(0,22))
    test_r = foto_list[random]
    emb.set_author(name = Bot.user.name, icon_url = Bot.user.avatar_url)
    emb.set_image(url = test_r)
    await ctx.send(embed = emb)
@Bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def dell(ctx, amount):
    numb = int(amount)+1
    await ctx.channel.purge(limit = numb)
@Bot.command(pass_context = True)
async def help(ctx, amount=1):
    await ctx.channel.purge(limit = amount)
    emb = discord.Embed(title="Команды бота Максима")
    emb.add_field(name="{}und".format('!'),value="Просто команда котороя выводит текс в рандоме")
    emb.add_field(name="{}fsb".format('!'),value="Команда для фотошоп батла, выводит картинки")
    emb.add_field(name="{}dell".format('!'),value="Команда для админов, удаляет количесто выбраных сообщений \n Пример : !dell 2 \n Удаляет 2 сообщения" )
    await ctx.send(embed = emb)
    
    
Bot.run('Njc0Njg2MDA2NTY1NTM1Nzc0.XjsMkg.NygMggHjlzY4rC_Egq--qbPS8EI')
