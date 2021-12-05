import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes, youtube_dl, typing, re
import urllib.parse, urllib.request, re, json, requests,aiohttp, asyncio, functools, logging
from discord.ext import commands
from discord.utils import get
from urllib.parse import urlencode
from colorama import Fore

token  = ''
BOT_PREFIX = '!'
stream_url = 'https://twitch.tv/lativ'
start_time = datetime.datetime.utcnow()
bot = commands.Bot(command_prefix=BOT_PREFIX)
bitly_key = ''

async def is_admin(ctx):
     return ctx.author.id ==            #Your Admin ID like: 704798303744819220, 715669280078823454
    
async def is_owner(ctx):
    return ctx.author.id ==             #Your Admin ID like: 704798303744819220

@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name + "\n")

@bot.command()
async def about(cfx):
        embed = discord.Embed(title="About the bot", description="Its a little Selfbot", color=0x00ffff)
        embed.add_field(name="Created with:", value="discord.py", inline=False)
        embed.add_field(name="Created by:", value="BombenProdukt#1337", inline=False)
        await cfx.channel.send(embed=embed)

@bot.command(pass_context=True, aliases=['j', 'joi'])
@commands.check(is_admin)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")

    await ctx.send(f"Successfully joined {channel}")


@bot.command(pass_context=True, aliases=['l', 'lea'])
@commands.check(is_admin)
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left {channel}")
        await ctx.send(f"Successfully leaved {channel}")
    else:
        print("Bot was told to leave voice channel, but was not in one")
        await ctx.send("Don't think I am in a voice channel")


@bot.command(pass_context=True, aliases=['p', 'pla'])
@commands.check(is_admin)
async def play(ctx, *, url: str):

    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Music playing")
        return

    await ctx.send("Loading...")

    voice = get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'default_search': 'auto',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.50

    nname = name.rsplit("-", 2)
    #await ctx.send(f"Playing: {nname[0]}")
    print("playing\n")
    
@bot.command(pass_context=True, aliases=['tc'])
@commands.check(is_owner)
async def create_tc(ctx, message):
    guild = ctx.message.guild
    await guild.create_text_channel(message)
    print("Successfully textchannel created!")

@bot.command(pass_context=True, aliases=['vc'])
@commands.check(is_owner)
async def create_vc(ctx, message):
    guild = ctx.message.guild
    await guild.create_voice_channel(message)
    print("Successfully voicechannel created!")
    
@bot.command(pass_context=True)
@commands.check(is_owner)
async def stream(ctx, *, message):
    stream = discord.Streaming(
        name=message,
        url=stream_url, 
    )
    await bot.change_presence(activity=stream)
    print("Activity successfully set to stream")
    
@bot.command(pass_context=True)
@commands.check(is_owner)
async def game(ctx, *, message):
    game = discord.Game(
        name=message
    )
    await bot.change_presence(activity=game)
    print("Activity successfully set to playing")
    
@bot.command(pass_context=True)
@commands.check(is_owner)
async def listening(ctx, *, message):
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=message, 
        ))
    print("Activity successfully set to listening")
       
@bot.command(pass_context=True)
@commands.check(is_owner)
async def watching(ctx, *, message):
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name=message
        ))
    print("Activity successfully set to watching")
    
@bot.command()
@commands.check(is_owner)
async def status(ctx):
    await ctx.send('Alles läuft gut und ich bin einsatzbereit!')

@bot.command()
@commands.check(is_owner)
async def lesbian(ctx):
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
@commands.check(is_owner)
async def cum(ctx):
    r = requests.get("https://nekos.life/api/v2/img/cum")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em) 
    
@bot.command()
@commands.check(is_owner)
async def anal(ctx):
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em) 
    
@bot.command()
@commands.check(is_owner)
async def boobs(ctx):
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em) 

@bot.command()
@commands.check(is_owner)
async def wallpaper(ctx):
    r = requests.get("https://nekos.life/api/v2/img/wallpaper")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   
    
@bot.command()
@commands.check(is_admin)
async def uptime(ctx):
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send(f'`'+uptime+'`') 
    
@bot.command()
@commands.check(is_owner)
async def spam(ctx, amount: int, *, message):   
    for _i in range(amount):
        await ctx.send(message)

@bot.command(aliases=['shorteen'])
@commands.check(is_admin)
async def bitly(ctx, *, link):
    if bitly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Bitly API key has not been set"+Fore.RESET)
    else:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api-ssl.bitly.com/v3/shorten?longUrl={link}&domain=bit.ly&format=json&access_token={bitly_key}') as req:
                    r = await req.read()
                    r = json.loads(r) 
            new = r['data']['url']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            await ctx.send(embed=em)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)
    
@bot.command(name='view', aliases=['view-bot', 'viewbot'])
@commands.check(is_admin)
async def _ebay_view(ctx, url, views: int):
    start_time = datetime.datetime.now()
    def EbayViewer(url, views):
        headers = {
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }        
        for _i in range(views):
            requests.get(url, headers=headers)
    EbayViewer(url, views)
    elapsed_time = datetime.datetime.now() - start_time
    em = discord.Embed(title='ViewBot')
    em.add_field(name='Views sent', value=views, inline=False)
    em.add_field(name='Elapsed time', value=elapsed_time, inline=False)
    await ctx.send(embed=em)
    
@bot.command(aliases=['pfp', 'avatar'])
@commands.check(is_admin)
async def av(ctx, *, user: discord.Member=None):
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format = format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file = discord.File(file, f"Avatar.{format}"))
        
@bot.command(aliases=['ri', 'role'])
@commands.check(is_admin)
async def roleinfo(ctx, *, role: discord.Role): # b'\xfc'
    await ctx.message.delete()
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == "#000000":
        colour = "default"
        color = ("#%06x" % random.randint(0, 0xFFFFFF))
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}"
    f"\nRole ID: {role.id}")
    em.add_field(name="Users", value=users)
    em.add_field(name="Mentionable", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Position", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name="Colour", value=colour)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)
    
@bot.command(aliases=['changehypesquad'])
@commands.check(is_owner)
async def hypesquad(ctx, house): # b'\xfc'
    await ctx.message.delete()
    request = requests.Session()
    headers = {
      'Authorization': token,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }    
    if house == "bravery":
      payload = {'house_id': 1}
    elif house == "brilliance":
      payload = {'house_id': 2}
    elif house == "balance":
      payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        
@bot.command()
@commands.check(is_owner)
async def dm(ctx, user : discord.Member, *, message):
    user = bot.get_user(user.id)
    if ctx.author.id == bot.user.id:
        return
    else:
        try:
            await user.send(message) 
        except:
            pass
            
@bot.command()
@commands.check(is_admin)
async def purge(ctx, amount: int):
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == bot.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass
            
@bot.command()
@commands.check(is_owner)
async def purgeall(ctx, amount: int):
    async for message in ctx.message.channel.history(limit=amount):
        try:
           await message.delete()
        except:
            pass

@bot.command()
@commands.check(is_owner)
async def server(cfx):
    print('Servers connected to:')
    for server in bot.servers:
        print(server.name)

@bot.command()
@commands.check(is_admin)
async def ascii(ctx, *, text):
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")

@bot.command(aliases=['bitcoin'])
@commands.check(is_admin)
async def btc(ctx):
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)
    
@bot.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
@commands.check(is_admin)
async def _first_message(ctx, channel: discord.TextChannel = None): 
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=embed)

@bot.command(aliases=['js'])
@commands.check(is_owner)
async def joinserver(ctx, invite_url):
    code = re.findall(r"(?:https?://)?discord(?:(?:app)?\.com/invite|\.gg)(/?[a-zA-Z0-9]+/?)", invite_url)
    if not code:
        return await ctx.send("Invalid invite url")
    headers = { 'authorization': token }
    code = code[0].strip('/')
    join = requests.post('https://discord.com/api/v6/invites/%s' % (code), headers = headers)
    if not join.status_code == 200:
        return await ctx.send("Could not join server")
    else:
        return await ctx.send("Succesfully joined server!")

@bot.command(aliases=['ls'])
@commands.check(is_owner)
async def leaveserver(ctx, guild: typing.Union[int, str]=None):
    if guild is None: # Leave guild the command was used in
        await ctx.guild.leave()
    elif isinstance(guild, int):
        guild = bot.get_guild(guild)
        await guild.leave()
    elif isinstance(guild, str):
        guild = discord.utils.find(lambda g: g.name.lower() == guild.lower(), bot.guilds)
        if guild is None:
            return await ctx.send("No guild found by that name")
        await guild.leave()
    return await ctx.author.send(f"Successfully left guild **{ctx.guild.name}**")


bot.run(token, bot=False)
