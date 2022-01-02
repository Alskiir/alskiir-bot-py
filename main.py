import discord
from discord.ext import commands


intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='-',intents=intents)

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')


bot.load_extension('cogs.rulesExtension')
bot.run('a')