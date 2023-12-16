import discord
from table2ascii import table2ascii as t2a, PresetStyle

#help
helpEmbed=discord.Embed(description="Try using some of these commands!", color=0x00ffff)
helpEmbed.set_author(name="😋Welcome to Ranni!😋")
helpEmbed.set_thumbnail(url="https://raw.githubusercontent.com/robinfilinger/RanniPy/main/Multimedia/pictures/ranniPics/candid.JPG")
helpEmbed.add_field(name="Basic", value="`hi` `hello`", inline=False)
helpEmbed.add_field(name="Profile", value="`Riccardo` `Danni` `profileColor`", inline=False)
helpEmbed.add_field(name="Relationship", value="`length` `anniversary` `ranni` `miAmor`", inline=False)
helpEmbed.add_field(name="Pokemon", value="`pokeType`", inline=False)
helpEmbed.add_field(name="Pets", value="`adopt` `petsList` `allPets` editName editFood edit myPets", inline=False)
helpEmbed.add_field(name="Countdowns", value="`addCountdown` `countdowns` ", inline=False)
helpEmbed.add_field(name="Holidays", value="`holidays` `today` ", inline=False)

