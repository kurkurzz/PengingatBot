import discord
from discord.utils import get
from credentials import TOKEN
import datetime as dt
import os

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        channel =  get(guild.text_channels,name='acah-study📚')
        if channel is not None:
            date_now = dt.datetime.now()
            date_end = dt.datetime(year=2021,month=1,day=23)
            days_left = (date_end - date_now).days
            display_text = f'Hamba hanya nak mengingatkan bahawa sem ni tinggal {days_left} hari lagi.'
            if days_left <= 10:
                display_text += ' Rasa nak terkencing tunggu.'
            elif days_left <= 0:
                display_text += ' Aikk? habis dah'
                
            message = await channel.send(display_text)
            guild_emoji = discord.utils.get(guild.emojis, name='ultraman')   
            emojis = ['🥳','😪','🦾','🖕']
            if guild_emoji:
                emojis.append(guild_emoji)
            for emoji in emojis:
                await message.add_reaction(emoji)
            await client.close()

client.run(os.environ['TOKEN'])