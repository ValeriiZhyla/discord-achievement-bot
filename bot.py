from datetime import datetime

from discord import ForumChannel
from discord.ext.commands import Context

from discord.ext import commands, tasks
import discord
from config import config
from dataclasses import dataclass

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.command()
async def mirror(context, message):
    await context.send(f"Hi there! Mirroring {message}")


@dataclass
class KnowledgeBaseThreadMetadata:
    thread_id: int
    owner_id: int
    created_at: datetime
    thread_name: str
    owner_name: str


@bot.command()
async def refresh_knowledge_base(ctx: Context):
    forum: ForumChannel = await bot.fetch_channel(config.KNOWLEDGE_BASE_FORUM_CHANNEL_ID)
    fetched_threads: list[KnowledgeBaseThreadMetadata] = []
    for thread in forum.threads:
        thread_metadata = KnowledgeBaseThreadMetadata(thread_id=thread.id, owner_id=thread.owner.id, created_at=thread.created_at, thread_name=thread.name,
                                                      owner_name=thread.owner.name)
        fetched_threads.append(thread_metadata)
    await ctx.send("Information about knowledge base was fetched")
    await ctx.send("Comparing fetched threads with database content")


# TODO Play with SQLAalchemy https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/


bot.run(config.DISCORD_BOT_TOKEN)
