import discord

DanniEmbed=discord.Embed(description="Codename: Mallorkus", color=0xffffff)
DanniEmbed.set_author(name="🤠Danni!🤠")
DanniEmbed.set_thumbnail(url="https://raw.githubusercontent.com/robinfilinger/Ranni/main/BOT/Profile%20Pics/Danni2.jpg")
DanniEmbed.add_field(name="Name", value="Danniela Ariana Salinas Estrada", inline=False)
DanniEmbed.add_field(name="Birthday", value="July 27, 2000", inline=False)
DanniEmbed.add_field(name="Hometown", value="Sandwich, IL", inline=False)
DanniEmbed.add_field(name="Relationship w/", value="Dorkus", inline=False)
DanniEmbed.add_field(name="Status", value="All Yours", inline=False)

'''
export const DanniEmbed = new MessageEmbed()
              .setColor(getDProfColor())
              .setThumbnail('https://raw.githubusercontent.com/robinfilinger/Ranni/main/BOT/Profile%20Pics/Danni2.jpg')
                .setAuthor({ name: '🤠Danni!🤠'})
                .setDescription('Codename: Mallorkus')
                .addFields(
                    { name: 'Name:', value: 'Danniela Ariana Salinas Estrada' },
                    //{ name: '\u200B', value: '\u200B' },
                    { name: 'Birthday', value: 'July 27, 2000' },
                    { name: 'Hometown', value: 'Sandwich, IL' },
                    { name: 'Relationship w/', value: 'Dorkus' },
                    { name: "Status", value: "All Yours", },
                )
export const RiccardoEmbed = new MessageEmbed()
                .setColor(getRProfColor())
                .setThumbnail('https://raw.githubusercontent.com/robinfilinger/Ranni/main/BOT/Profile%20Pics/Riccardo.jpg')
                  .setAuthor({ name: '😋Riccardo!😋'})
                  .setDescription('Codename: Dorkus')
                  .addFields(
                      { name: 'Name:', value: 'Richard Joseph Filingeri' },
                      //{ name: '\u200B', value: '\u200B' },
                      { name: 'Birthday', value: 'August 25, 2000' },
                      { name: 'Hometown', value: 'Rye Brook, NY' },
                      { name: 'Relationship w/', value: 'Mallorkus' },
                      { name: "Status", value: "Mine", },
                  )
'''