import discord

petListEmbed=discord.Embed(description="These are the types of pets you may select!", color=0x00ffff)
petListEmbed.set_author(name="Pets List!")
petListEmbed.set_thumbnail(url="https://raw.githubusercontent.com/robinfilinger/Ranni/main/BOT/Profile%20Pics/candid.JPG")
petListEmbed.add_field(name="Cat🐱", value="Meow!", inline=True)
petListEmbed.add_field(name="Dog🐶", value="Bark!", inline=True)
petListEmbed.add_field(name="Bird🐤", value="Chirp!", inline=True)
petListEmbed.add_field(name="Dino🦖", value="Roar!", inline=True)
petListEmbed.add_field(name="Bee🐝", value="Buzz!", inline=True)
petListEmbed.add_field(name="Mouse🐭", value="Squeak!", inline=True)
petListEmbed.add_field(name="Horse🐴", value="Neigh!", inline=True)
petListEmbed.add_field(name="Snake🐍", value="  Hiss!", inline=True)
petListEmbed.add_field(name="Duck🦆", value="Quack!", inline=True)
petListEmbed.add_field(name="Pig🐷", value="Oink!", inline=True)
petListEmbed.add_field(name="Cow🐮", value="Moo!", inline=True)
petListEmbed.add_field(name="Sheep🐑", value="Baaaa!", inline=True)