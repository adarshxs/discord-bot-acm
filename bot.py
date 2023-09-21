import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?',
                   description=description,
                   intents=intents)

rules_message = '''
Welcome to the server🎉 Please read the rules below:

• You have to register on the gravitas'23 website. No external registrations will be accepted.
• Make sure to "Check-In" to the Hybrid Cryptic Hunt through the official website. You will also have to check-in for everyone you have paid for.
• You will not be able to use the app without checking in.
• You will require a working internet connection throughout the hunt.
• For some of the questions, you will also need access to a laptop.
• To make a team on the app, one person must select the "Create a Team" button and share the code given with the rest of the group.
'''

q_format = '''
FORMAT OF THE QUESTIONS:

There are two types of questions:
• Text Based🖹 - You have to enter the text to solve the question.
• QR Based🖼️- You must go to the location and solve the QR code that is hidden there
'''
q_points = '''
POINTS PER QUESTION
1. Easy - 100 points
2. Medium - 250 points
3. Hard - 500 points

Hints💡 will also be available. The cost of using a hint is: 
50% of the points for an easy question😮
20% of the points for a medium or hard question🤔
'''


@bot.event
async def on_ready():
  print(f'Logged in as {bot.user} (ID: {bot.user.id})')
  print('------')


@bot.command()
async def rules(ctx):
  await ctx.send(rules_message)


@bot.command()
async def type(ctx):
  await ctx.send(q_format)


@bot.command()
async def points(ctx):
  await ctx.send(q_points)


@bot.command()
async def add(ctx, left: int, right: int):
  """Adds two numbers together."""
  await ctx.send(left + right)


@bot.group()
async def cool(ctx):
  """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
  if ctx.invoked_subcommand is None:
    await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
  """Is the bot cool?"""
  await ctx.send('Yes, the bot is cool.')


bot.run(
    '')
