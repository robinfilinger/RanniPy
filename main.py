#py -3 main.py        
from re import X
from tokenize import Special
import discord
import pandas as pd
import random


from datetime import datetime, date
from dateutil import relativedelta

#imported variables
from Data.Embeds.profile import DanniEmbed, RiccardoEmbed
from Data.Embeds.misc import helpEmbed
from Data.Arrays.ranniPics import ranniPics
from Data.Arrays.pokemonTypes import types

#imported functions
from Functions.length import length

client = discord.Client()

@client.event
async def on_ready():
    print("The Bot is Ready.")
    #print('We have logged in as {0.user}'.format(client))


 
df = pd.read_excel('Pets.xlsx')
#print(df)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "r!help":
        await message.channel.send(embed=helpEmbed)
    
    elif message.content == "r!hi":
        await message.channel.send("❤️Love you Danni❤️")

    elif message.content == "r!Riccardo":
        await message.channel.send(embed=RiccardoEmbed)    
    elif message.content == "r!Danni":
        await message.channel.send(embed=DanniEmbed)

    elif message.content == "r!anniversary":
        await message.channel.send("💍Ranni began on 1/10/2022💍")
    elif message.content == "r!length":
        await message.channel.send(length())
    elif message.content == "r!ranni":
        await message.channel.send(file=discord.File('Multimedia/pictures/ranniPics/' + random.choice(ranniPics)))

    elif message.content.startswith('r!pokeType'):
        args = message.content.split(' ')
        if len(args) == 1:
            await message.channel.send('Goodbye!')
        else:
            await message.channel.send(args[1])
    

    elif message.content.startswith('r!hello'):
        await message.channel.send('Hello!')

    elif message.content == "r!pets":
        await message.channel.send("Name: " + "*" + df.iloc[0]['Name'] + "*" + "\nType: " + df.iloc[0]['Type'] + "\nNature: " + df.iloc[0]['Nature'])

    elif message.content == "r!test":
        await message.channel.send(len())

    


client.run("OTc4NzMxMjI5NTcyNjQ0ODc0.Gm2gw7.18S9AIUMqeCh64EKafRQ_r59A2r4IO67rVp1BM")
