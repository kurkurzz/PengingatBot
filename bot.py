import discord
from discord.utils import get
import datetime as dt
import os

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        channel =  get(guild.text_channels,name='acah-study📚')
        if channel is not None:
            date_now = dt.datetime.now()
            date_end = dt.datetime(year=2021,month=1,day=24)
            days_left = (date_end - date_now).days
            display_text = f'Hamba hanya nak mengingatkan bahawa sem ni tinggal **{days_left} hari** lagi.'
            if days_left <= 10:
                display_text += ' Rasa nak terkencing tunggu.'
            elif days_left == 0:
                display_text = 'Hamba hanya nak mengingatkan bahawa sem ni dah habis. Enjoy anak muda.'
                
            message = await channel.send(display_text)

            guild_emojis = [discord.utils.get(guild.emojis, name='ultraman'), discord.utils.get(guild.emojis, name='thonking') ,discord.utils.get(guild.emojis, name='mukastim')] 
            emojis = ['🥳','😪','🦾','🖕']
            end_emojis = ['🥳','😪','🦾','🖕','👋','🤩','🤔','🤯','🥴','😵','🥶','🥵','😱','😰','😠','😡','🤬']
            for guild_emoji in guild_emojis:
                emojis.append(guild_emoji)

            if days_left==0:
                for emoji in end_emojis:
                    await message.add_reaction(emoji)
            else:
                for emoji in emojis:
                    await message.add_reaction(emoji)
    await client.close()

client.run(os.environ['TOKEN'])

