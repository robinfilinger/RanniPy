import discord

typeEmbed=discord.Embed(description="Try using some of these commands!", color=0x000000)
typeEmbed.set_author(name="😋Welcome to Ranni!😋")
typeEmbed.set_thumbnail(url="https://raw.githubusercontent.com/robinfilinger/Ranni/main/BOT/Profile%20Pics/candid.JPG")
typeEmbed.add_field(name="Basic", value="`hi` `hello`", inline=False)
typeEmbed.add_field(name="Profile", value="`Riccardo` `Danni` `profileColor`", inline=False)
typeEmbed.add_field(name="Relationship", value="`length` `anniversary` `ranni`", inline=False)
typeEmbed.add_field(name="Pokemon", value="`pokeType`", inline=False)

#.setColor('#000000')
#                .setTitle(pokemonType)
#                .setThumbnail(pokeType[7])
#                .addFields(
#                    { name: 'Attacking', value: "**Super Effective Against: **" + pokeType[1] + "\n**Not Very Effective Against: **" + pokeType[2] + "\n**Does Not Affect: **" + pokeType[3]},
#                    { name: 'Defending', value: "**Vulnerable To: **" + pokeType[4] + "\n**Resistant To: **" + pokeType[5] + "\n**Immune To: **" + pokeType[6] },
#                )