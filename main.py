import discord
import logging
import os
from dotenv import load_dotenv
import random

# ENV #
load_dotenv()
token = str(os.getenv('TOKEN'))
# ENV - END #

# Logging #
logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='bot-latest.log', encoding='utf-8', mode="w")
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
# Logging - End #
# Discord Bot #
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    
@bot.slash_command(name="hello", description="Say Hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hello!")
    
@bot.command()
async def gtn(ctx, min=1, max=10):
    """A Slash Command to play a Guess-the-Number game."""

    await ctx.respond('Guess a number between 1 and 10.')
    guess = await bot.wait_for('message', check=lambda message: message.author == ctx.author)

    answer = int(random.randint(min, max))

    if int(guess.content) == answer:
        await ctx.send('Correct! :white_check_mark:')
    else:
        await ctx.send(f'Wrong Answer :x: The right answer was: {answer}')
        
@bot.command()
async def help(ctx):
    
    embed = discord.Embed(
        title="Help",
        description="A collection of all commands and help for commands(WIP)",
        color=discord.Colour.purple(),
    )
    embed.add_field(name="/help", value="The help commands gives you a collection of all commands of the bot and in the future usage of commands(**WIP**)")
    embed.add_field(name="/gtn", value="Its a guess the number game(**WIP**)")
    embed.add_field(name="/hello", value="This just says hello to the bot...")
    
    embed.set_footer(text="VertrauensGamerᵀᴹ", icon_url="https://cdn.discordapp.com/avatars/466537555798654987/3d3a360eb92b3fccd9e4e7ddea831703.webp?size=128")
    embed.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/1267489664105844871/031582b6db6edc0d014d85e23ee5b22c.webp?size=96")
    
    await ctx.respond(embed=embed)
    await ctx.respond(discord.ui.button(label="Creator of the Bot", style=discord.ButtonStyle.url, url="https://github.com/VertrauensGamer"))
    
@bot.command()
async def ping(ctx):
    await ctx.respond(f"Bot's ping is {bot.latency}")
    
bot.run(token)
# Discord Bot - End #