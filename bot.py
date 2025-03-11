import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is online! Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await message.reply(f'Hello, {message.author.name}! You said: \"{message.content}\"')
    await bot.process_commands(message)

bot.run('MTM0ODk1ODM4NTExODExNzk0MQ.GqzvzQ.KpVVcD8ZYY9EZ7ieklBdt0ZruDc4Q4zQueTkEE')
