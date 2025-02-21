import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Define bot intents
intents = discord.Intents.default()
intents.message_content = True  # Required for message commands

# Initialize bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print(f'Connected to {len(bot.guilds)} servers')

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

# Dynamic Module Loader
@bot.command()
async def load(ctx, extension):
    try:
        bot.load_extension(f'modules.{extension}')
        await ctx.send(f'Loaded {extension} successfully.')
    except Exception as e:
        await ctx.send(f'Error loading {extension}: {e}')

@bot.command()
async def unload(ctx, extension):
    try:
        bot.unload_extension(f'modules.{extension}')
        await ctx.send(f'Unloaded {extension} successfully.')
    except Exception as e:
        await ctx.send(f'Error unloading {extension}: {e}')

@bot.command()
async def reload(ctx, extension):
    try:
        bot.reload_extension(f'modules.{extension}')
        await ctx.send(f'Reloaded {extension} successfully.')
    except Exception as e:
        await ctx.send(f'Error reloading {extension}: {e}')

# Load all cogs on startup
def load_modules():
    for filename in os.listdir('./modules'):
        if filename.endswith('.py'):
            bot.load_extension(f'modules.{filename[:-3]}')

load_modules()

# Run bot
bot.run(TOKEN)
