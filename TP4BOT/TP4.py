import discord
from discord import Client


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
    
    async def on_member_join(self, member):
        guild=member.guild
        if guild.system_channel is not None:
            to_send = 'BoNjOuR {0.mention} dans {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)
        
    

bot = MyBot()
bot.run("OTU4Njg4MDcxOTQyMDQ1NzY2.YkQ91w.0Lm3t2yWfdvFrpt0FMMQ5C8jLJ4")



