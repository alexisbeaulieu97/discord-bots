# dice-bot.py
import os
import random
import re

from dotenv import load_dotenv
from discord.ext import commands

# load environment
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# regex
THROW_REGEX = r'^!\d{1,2}d\d{1,3}$'

# instantiate bot
bot = commands.Bot(command_prefix='!')

def dice(n_throws: int, n_sides: int):
    rolls = [str(random.choice(range(1, n_sides + 1))) for _ in range(n_throws)]
    return rolls

def validate_throw(msg):
    regex = re.compile(THROW_REGEX)
    return regex.match(msg.content)

# events
@bot.event
async def on_message(message):
    out = ''
    if message.content[0] == '!' and message.author != bot.user and not validate_throw(message):
        out = "```Use me to throw between 1 and 99 dice having between 1 and 999 faces!\n"\
            "This can be done by typing 'number of throws'd'number of faces'\n"\
            "For example: 5d10```"
    else:
        params = message.content.strip('!').split('d')
        dice_throw = dice(int(params[0]), int(params[1]))
        out = ', '.join(dice_throw)
    
    await message.channel.send(out)

if __name__ == "__main__":
    bot.run(TOKEN)
