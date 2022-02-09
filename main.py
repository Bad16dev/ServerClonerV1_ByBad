import os
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

from dotenv import load_dotenv

load_dotenv()

token = os.getenv("token")
prefix = input("\033[0;96m[~\033[0;96m] \033[0;96mEnter Prefix : ")
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
async def cp(ctx): 
    wow = await client.create_guild(f'Cloned : {ctx.guild.name}')
    await asyncio.sleep(4)
    for g in client.guilds:
        if f'Cloned : {ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(chann.name, overwrites=chann.overwrites, topic=chann.topic, slowmode_delay=chann.slowmode_delay, nsfw=chann.nsfw, position=chann.position)
            print(ctx.guild.roles)
    for role in ctx.guild.roles[::-1]:
        if role.name != "@everyone":
            try:
                await wow.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
                print(f"Created New Role : {role.name}")
            except:
                break

@client.command()
async def nuke_s(ctx):
    for guild in client.guilds:
        try:
            await guild.leave()
            print(f'Left From [{guild.name}]')
        except:
            print(f'Cant Leave [{guild.name}]')
  
    for guild in client.guilds:
        try:
            await guild.delete()
            print(f'[{guild.name}] Have Been Deleted')
        except:
            print(f'Cant Delete [{guild.name}]')

client.run(token, bot=False)
