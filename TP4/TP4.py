from json import load
import discord
from pydoc import describe
from datetime import datetime
from discord.ext import commands
import os
from discord import Client
import logging
import asyncio
logging.basicConfig(filename='journal.log', encoding='utf-8')
from dotenv import load_dotenv
load_dotenv()




class MyBot(Client):
    
    def __init__(self):
       

        intents = discord.Intents.default()
        intents.presences = True
        intents.members = True
        super().__init__(command_prefix="!", intents=intents)
    

    async def on_ready(self):
        print("Le bot est prêt !")



    async def on_message(self, message):
        if message.content.lower() == "!ping":
            await message.channel.send("Pong")
            time = str(datetime.now())
            f = open("example.log", "a")
            f.write(time + "La commande !ping a ete utilisee par @"+message.author.name+"! \n")
            f.close()
        if message.content == "!help":
            await message.channel.send("!ping pour reponse 'pong'")
    
    async def on_member_join(self, member):
        guild=member.guild
        if guild.system_channel is not None:
            to_send = 'BoNjOuR {0.mention} dans {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)
        
    

bot = MyBot()
bot.run(os.getenv("DISCORD_TOKEN"))



