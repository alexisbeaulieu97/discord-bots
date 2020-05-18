# dice-bot.py
import os
import random

from dotenv import load_dotenv
from discord.ext import commands

# load environment
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# instantiate bot
bot = commands.Bot(command_prefix='!')

# commands
@bot.command(name="d4", help="Throw a d4")
async def d4(ctx):
    await dice(ctx, 1, 4)

@bot.command(name="d8", help="Throw a d8")
async def d8(ctx):
    await dice(ctx, 1, 8)

@bot.command(name="d10", help="Throw a d10")
async def d10(ctx):
    await dice(ctx, 1, 10)

@bot.command(name="d20", help="Throw a d20")
async def d20(ctx):
    await dice(ctx, 1, 20)

@bot.command(name="throw", help="Make {n_throws} of a {n_sides} dice. | EX : !throw 5 10")
async def dice(ctx, n_throws: int, n_sides: int):
    response = [str(random.choice(range(1, n_sides + 1))) for _ in range(n_throws)]
    await ctx.send(', '.join(response))

bot.run(TOKEN)
