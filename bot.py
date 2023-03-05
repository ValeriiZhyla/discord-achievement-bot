import os

DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))

from discord.ext import commands
import discord

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())


@bot.event
async def on_ready():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hi there!")


@bot.command()
async def mirror(context, message):
    await context.send(f"Hi there! Mirroring {message}")


bot.run(DISCORD_BOT_TOKEN)
