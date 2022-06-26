#py -3 main.py        
from re import A, X
import discord
from numpy import NaN
import pandas as pd
import random


from datetime import datetime, date
from dateutil import relativedelta
from table2ascii import table2ascii as t2a, PresetStyle

#imported embeds
from Data.Embeds.profile import DanniEmbed, RiccardoEmbed
from Data.Embeds.misc import helpEmbed
from Data.Embeds.petEmbeds import petListEmbed

#imported variables
from Data.Arrays.ranniPics import ranniPics
from Data.Arrays.pokemonTypes import types
from Data.Arrays.petArrays import petEmojis, petNatures
from Functions.countdowns import addCountdown


#imported functions
from Functions.dates import MDYtoDMY, getCurrentDate
from Functions.length import dateDiff, length
from Functions.pets import adopt, getAllPets, getPet, getPetEmoji, getTotalPets, isValidPetType, printAllPets
from Functions.pokeType import notValidType
from Functions.pokeType import typeEffectiveness

client = discord.Client()

@client.event
async def on_ready():
    print("The Bot is Ready.")
    #print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    args = message.content.split(" ")

    if message.content == "r!help": #running
        await message.channel.send(embed=helpEmbed)
    
    #basic
    elif message.content == "r!hi": #running
        await message.channel.send("❤️Love you Danni❤️")
    elif message.content.startswith('r!hello'):
        await message.channel.send('Hello!')

    #profile
    elif message.content == "r!Riccardo": #running
        await message.channel.send(embed=RiccardoEmbed)    
    elif message.content == "r!Danni": #running
        await message.channel.send(embed=DanniEmbed)

    #relationship
    elif message.content == "r!anniversary": #running
        await message.channel.send("💍Ranni began on 1/10/2022💍")
    elif message.content == "r!length": #running
        await message.channel.send(length())
    elif message.content == "r!ranni": #running
        await message.channel.send(file=discord.File('Multimedia/pictures/ranniPics/' + random.choice(ranniPics)))

    #pokemon
    elif message.content.startswith('r!pokeType'): #running
        if len(args) != 2:
            await message.channel.send(notValidType())
        else:
            typeResponse = typeEffectiveness(args[1])
            if typeResponse[0] == 0:
                await message.channel.send(typeResponse[1])
            else:
                await message.channel.send(embed=typeResponse[1])



    elif message.content == "r!petsList": #running
        await message.channel.send(embed=petListEmbed)
    elif message.content.startswith("r!adopt"): #running
        if message.content == "r!adopt":
            await message.channel.send("Send message in the following format!\n\n r!adopt *Name* *Type*")
        else:
            if len(args) != 3:
                await message.channel.send("Send message in the following format!\n\n r!addPet *Name* *Type*")
            elif isValidPetType(args[2]) != True:
                await message.channel.send("Not a valid pet Type! Use r!petsList to see valid pet types!")
            else:
                await message.channel.send(adopt(args, message.author.name))      
    elif message.content == "r!allPets":
        await message.channel.send(f"```\n{printAllPets()}\n```")
   
    elif message.content == "r!countdowns":
        await message.channel.send("Countdowns list!")
    elif message.content.startswith("r!addCountdown"):
        await message.channel.send(addCountdown(message.content))

    elif message.content == "r!test":
        await message.channel.send(getCurrentDate())
    

client.run("OTc4NzMxMjI5NTcyNjQ0ODc0.Gm2gw7.18S9AIUMqeCh64EKafRQ_r59A2r4IO67rVp1BM")
