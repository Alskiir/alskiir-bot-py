from discord.ext import commands
from keep_alive import keep_alive
import discord
import os
import asyncio

token = os.environ["TOKEN"]

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='-', intents=intents)


@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')


async def main():
    async with bot:
        await bot.load_extension('cogs.rulesExtension')
        await bot.start(token)

keep_alive()
asyncio.run(main())

# bot.load_extension('cogs.rulesExtension')
# bot.run(token)
