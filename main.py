#py -3 main.py        
from cmath import nan
from re import X
from tokenize import Special
import discord
from numpy import NaN
import pandas as pd
import random


from datetime import datetime, date
from dateutil import relativedelta

#imported embeds
from Data.Embeds.profile import DanniEmbed, RiccardoEmbed
from Data.Embeds.misc import helpEmbed

#imported variables
from Data.Arrays.ranniPics import ranniPics
from Data.Arrays.pokemonTypes import types

#imported functions
from Functions.length import length
from Functions.pokeType import notValidType
from Functions.pokeType import typeEffectiveness

client = discord.Client()

@client.event
async def on_ready():
    print("The Bot is Ready.")
    #print('We have logged in as {0.user}'.format(client))


 
df = pd.read_excel('Pets.xlsx')
print(df)
print(df.iloc[1]['Name'])
#if pd.isna(df.iloc[1]['Name']):
#    print("true")
#else:
#    print("false")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "r!help": #running
        await message.channel.send(embed=helpEmbed)
    
    elif message.content == "r!hi": #running
        await message.channel.send("❤️Love you Danni❤️")

    elif message.content == "r!Riccardo": #running
        await message.channel.send(embed=RiccardoEmbed)    
    elif message.content == "r!Danni": #running
        await message.channel.send(embed=DanniEmbed)

    elif message.content == "r!anniversary": #running
        await message.channel.send("💍Ranni began on 1/10/2022💍")
    elif message.content == "r!length": #running
        await message.channel.send(length())
    elif message.content == "r!ranni": #running
        await message.channel.send(file=discord.File('Multimedia/pictures/ranniPics/' + random.choice(ranniPics)))

    elif message.content.startswith('r!pokeType'): #running
        args = message.content.split(' ')
        if len(args) != 2:
            await message.channel.send(notValidType())
        else:
            typeResponse = typeEffectiveness(args[1])
            if typeResponse[0] == 0:
                await message.channel.send(typeResponse[1])
            else:
                await message.channel.send(embed=typeResponse[1])


    elif message.content.startswith('r!hello'):
        await message.channel.send('Hello!')

    elif message.content == "r!pets":
        await message.channel.send("Name: " + "*" + df.iloc[0]['Name'] + "*" + "\nType: " + df.iloc[0]['Type'] + "\nNature: " + df.iloc[0]['Nature'])

    elif message.content == "r!test":
        
        await message.channel.send(len())

    


client.run("OTc4NzMxMjI5NTcyNjQ0ODc0.Gm2gw7.18S9AIUMqeCh64EKafRQ_r59A2r4IO67rVp1BM")
