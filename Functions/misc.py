import discord
from table2ascii import table2ascii as t2a, PresetStyle

#header=["ID", "Name", "Type", "Birthday", "Age", "Nature", "Owner", "FavFood"],
def toTable(inHeader, inBody):
    output = t2a(
    header= inHeader,
    body= inBody
    )
    return output

#[name, value, inline]
def toEmbed():
    tableEmbed=discord.Embed(description="Testing this feature", color=0x00ffff)
    tableEmbed.set_author(name="List of Pets")
    pets = [['0', 'Draco', 'Dino🦖','05/30/2022','0 y, 6 m, and 23 d', 'Hasty', 'Riccardo'], 
            ['1', 'Tobee', 'Bee🐝','01/10/2022', '0 y, 11 m, and 13 d', 'Hardy', 'Danni'],
            ['1', 'Tobee', 'Bee🐝','01/10/2022', '0 y, 11 m, and 13 d', 'Hardy', 'Danni']]

    for pet in pets:
        tableEmbed.add_field(name=pet[1],value=pet[2] + '\n' + pet[3] + '\n' + pet[4] + '\t\n' + pet[5] + '\n' + pet[6],inline=True)
    return tableEmbed

   