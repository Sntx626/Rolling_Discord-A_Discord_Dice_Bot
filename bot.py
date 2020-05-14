'''
My universal administration discord bot.
@author: \ᛊᚢᚾᛏᚨᚲᛊ#0829
@date: 22nd December 2019
'''

##### initalization #####

import discord
from discord.ext import commands, tasks

import json
with open("config.json") as f:
    config = json.load(f)
    client_secret = config["client secret"]
    command_prefix = config["command prefix"]
import datetime

config["results suffix"] = datetime.datetime.now().strftime("%f")

with open("config.json", 'w') as f:
    json.dump(config, f, indent=2)

with open("logs/base_results.json") as f:
    base_results = json.load(f)

with open("logs/results_"+ config["results suffix"] +".json", 'w') as f:
    json.dump(base_results, f, indent=2)

import tools

import os
from itertools import cycle

client = commands.Bot(command_prefix = command_prefix)
status = cycle([f"Listening to '{command_prefix}roll d20'",
                f"Listening to '{command_prefix}roll 6xd4'",
                f"Listening to '{command_prefix}roll d100'",
                f"Listening to '{command_prefix}roll 20x d12'",
                f"Listening to '{command_prefix}roll 4x 2d40'",
                f"Listening to '{command_prefix}roll d8'",
                f"Listening to '{command_prefix}roll d6'",
                f"Listening to '{command_prefix}roll 2d4'"])

##### events #####

@client.event
async def on_ready():
    change_status.start()
    print('\n\tBot is online.')

'''
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used.')
        print('Error: Invalid command used.')
'''

##### tasks #####

@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

##### commands #####

@client.command()
@commands.is_owner()
async def shutdown(ctx):
    tools.print_on_command_call(ctx.author, 'shutdown', '')
    await ctx.bot.logout()
    tools.print_bot(f"shutdown...")

# load cogs
@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    tools.print_on_command_call(ctx.author, 'load', extension)
    client.load_extension(f'cogs.{extension}')
    embed = discord.Embed(
        description = f'loaded: {extension}',
        colour = discord.Colour.blue()
    )
    await ctx.send(embed=embed)
    tools.print_bot(f"loaded: '{extension}'")


# unload cogs
@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    tools.print_on_command_call(ctx.author, 'unload', extension)
    client.unload_extension(f'cogs.{extension}')
    embed = discord.Embed(
        description = f'unloaded: {extension}',
        colour = discord.Colour.blue()
    )
    await ctx.send(embed=embed)
    tools.print_bot(f"unloaded: '{extension}'")

# reload cogs
@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, *, extension=''):
    tools.print_on_command_call(ctx.author, 'reload', extension)
    if extension == '':
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py') and not filename[:-3].endswith('.py'):
                client.unload_extension(f'cogs.{filename[:-3]}')
                client.load_extension(f'cogs.{filename[:-3]}')
        embed = discord.Embed(
            description = 'reloaded all',
            colour = discord.Colour.blue()
        )
        await ctx.send(embed=embed)
        tools.print_bot(f"reloaded: all", ctx.author, "reload", extension)
    else:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        embed = discord.Embed(
            description = f'reloaded: {extension}',
            colour = discord.Colour.blue()
        )
        await ctx.send(embed=embed)
        tools.print_bot(f"reloaded: '{extension}'")

##### finalize and run #####

for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and not filename[:-3].endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f"\n\tloaded: '{filename[:-3]}'")

client.run(config["client secret"])
