import discord
from Data.Arrays.pokemonTypes import types

def notValidType():
    return "Please type the command followed by a Pokemon type!\n\n*Example: r!pokeType dark*\n\nOptions:\n\n⚪Normal⚪\n🔥Fire🔥\n💧Water💧\n🌿Grass🌿\n⚡Electric⚡\n❄️Ice❄️\n🥊Fighting🥊\n☠️Poison☠️\n🌋Ground🌋\n💨Flying💨\n🪨Rock🪨\n🔮Psychic🔮\n👻Ghost👻\n🪲Bug🪲\n🕶️Dark🕶️\n⚙️Steel⚙️\n🐉Dragon🐉\n🌸Fairy🌸"

def typeEffectiveness(type):
    typeRow = None
    for x in range(len(types)):
       if type.lower() == types[x][0]:
           typeRow = x
    if typeRow == None:
        return [0, notValidType()]
    
    pokeType = types[typeRow]

    typeEmbed=discord.Embed(title = pokeType[0].capitalize(), color=0x000000)
    typeEmbed.set_thumbnail(url=pokeType[7])
    typeEmbed.add_field(name= 'Attacking', value= "**Super Effective Against: **" + pokeType[1] + "\n**Not Very Effective Against: **" + pokeType[2] + "\n**Does Not Affect: **" + pokeType[3], inline=False)
    typeEmbed.add_field(name= 'Defending', value= "**Vulnerable To: **" + pokeType[4] + "\n**Resistant To: **" + pokeType[5] + "\n**Immune To: **" + pokeType[6], inline=False)
    return [1, typeEmbed]

def pokedexInfo(pokemon):
    return pokemon