def notValidType():
    return "Please type the command followed by a Pokemon type!\n\n*Example: r!pokeType dark*\n\nOptions:\n\n⚪Normal⚪\n🔥Fire🔥\n💧Water💧\n🌿Grass🌿\n⚡Electric⚡\n❄️Ice❄️\n🥊Fighting🥊\n☠️Poison☠️\n🌋Ground🌋\n💨Flying💨\n🪨Rock🪨\n🔮Psychic🔮\n👻Ghost👻\n🪲Bug🪲\n🕶️Dark🕶️\n⚙️Steel⚙️\n🐉Dragon🐉\n🌸Fairy🌸"

def getLength (list):
    x = 0
    for i in list:
        x = x+1
    return(x)