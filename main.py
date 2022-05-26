#py -3 main.py        
import discord
import pandas as pd


from Data.Embeds.profile import DanniEmbed, RiccardoEmbed
from Data.Embeds.misc import helpEmbed


client = discord.Client()

@client.event
async def on_ready():
    print("The Bot is Ready.")
    #print('We have logged in as {0.user}'.format(client))
 
# Give the location of the file

 
df = pd.read_excel('Pets.xlsx')
print(df)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "r!help":
        await message.channel.send(embed=helpEmbed)
    elif message.content == "r!Riccardo":
        await message.channel.send(embed=RiccardoEmbed)    
    elif message.content == "r!Danni":
        await message.channel.send(embed=DanniEmbed)
    elif message.content.startswith('r!hello'):
        await message.channel.send('Hello!')
    elif message.content == "r!hi":
        await message.channel.send('Goodbye!')
    elif message.content == "r!pets":
        await message.channel.send("Name: " + "*" + df.iloc[0]['Name'] + "*" + "\nType: " + df.iloc[0]['Type'] + "\nNature: " + df.iloc[0]['Nature'])

    


client.run("OTc4NzMxMjI5NTcyNjQ0ODc0.Gm2gw7.18S9AIUMqeCh64EKafRQ_r59A2r4IO67rVp1BM")
