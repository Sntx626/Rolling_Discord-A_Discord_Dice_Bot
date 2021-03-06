import datetime
import json
import random

import discord
from discord.ext import commands

with open("config.json") as f:
    command_prefix = json.load(f)["bot_prefix"]

def print_on_command_call(ctx_author, command_name, input):
    #print(f"\n{ctx_author} '{command_prefix}{command_name} {input}':")
    pass

def print_bot(output, ctx_author, command_name, input):
    #print(output)
    pass

class Games(commands.Cog):

    ##### initalization #####

    def __init__(self, client):
        self.client = client

    ##### commands #####

    @commands.command()
    async def roll(self, ctx, d='d20', number='1', name=''):
        print_on_command_call(ctx.author, 'roll', f'{d} {number} {name}')

        if name == '':
            try:
                if ctx.author.nick is None:
                    name = f'{ctx.author}'
                    name = name[:(len(name)-5)]
                else:
                    name = ctx.author.nick
            except:
                name = f'{ctx.author}'
                name = name[:(len(name)-5)]

        if not number.isdigit():
            name = number
            number = 1
        number = int(number)

        if number < 1:
            embed = discord.Embed(
                title = 'Error',
                description = f"Please ensure you throw at least one dice!",
                colour = discord.Colour.red()
            )
            embed.set_author(name=f'{name}', icon_url=f'{ctx.author.avatar_url}')
            await ctx.send(embed=embed)
            print_bot(f"'roll d<number> <number of dice> <title name>' wasn't passed, instead '{d}' was inputted (all values are optional).", ctx.author, 'roll', f'{d} {number} {name}')
        elif number == 1:
            for i in range(number):
                if d.startswith('d') and d[1:].isdigit():
                    d = d[1:]
                    if int(d) > 0:
                        r = random.randint(1, int(d))
                        embed = discord.Embed(
                            title = '',
                            description = f'Rolled {r}/{int(d)}!',
                            colour = discord.Colour.blue()
                        )
                        embed.set_author(name=f'{name}', icon_url=f'{ctx.author.avatar_url}')
                        await ctx.send(embed=embed)
                        print_bot(f'Rolled {r}/{int(d)}!', ctx.author, 'roll', f'{d} {number} {name}')
                    else:
                        embed = discord.Embed(
                            title = 'Error',
                            description = f"Please ensure your dice has at least one side.",
                            colour = discord.Colour.red()
                        )
                        embed.set_author(name=f'{name}', icon_url=f'{ctx.author.avatar_url}')
                        await ctx.send(embed=embed)
                        print_bot(f"'roll d<number> <number of dice> <title name>' wasn't passed, instead '{d}' was inputted (all values are optional).", ctx.author, 'roll', f'{d} {number} {name}')
                elif d.isdigit():
                    if int(d) > 0:
                        r = random.randint(1, int(d))
                        embed = discord.Embed(
                            description = f'Rolled {r}/{int(d)}!',
                            colour = discord.Colour.blue()
                        )
                        embed.set_author(name=f'{name}', icon_url=f'{ctx.author.avatar_url}')
                        await ctx.send(embed=embed)
                        print_bot(f'Rolled {r}/{int(d)}!', ctx.author, 'roll', f'{d} {number} {name}')
                    else:
                        embed = discord.Embed(
                            title = 'Error',
                            description = f"Please ensure your dice has at least one side.",
                            colour = discord.Colour.red()
                        )
                        embed.set_author(name=f'{name}', icon_url=f'{ctx.author.avatar_url}')
                        await ctx.send(embed=embed)
                        print_bot(f"'roll d<number> <number of dice> <title name>' wasn't passed, instead '{d}' was inputted (all values are optional).", ctx.author, 'roll', f'{d} {number} {name}')
                else:
                    embed = discord.Embed(
                        title = 'Error',
                        description = f"Please use the following syntax: 'roll d<number> <name(optional)>'.",
                        colour = discord.Colour.red()
                    )
                    embed.set_author(name=f'{name}', icon_url=f'{ctx.author.avatar_url}')
                    await ctx.send(embed=embed)
                    print_bot(f"'roll d<number> <number of dice> <title name>' wasn't passed, instead '{d}' was inputted (all values are optional).", ctx.author, 'roll', f'{d} {number} {name}')
        elif number <= 25:
            if d.startswith('d') and d[1:].isdigit():
                d = d[1:]
                if int(d) > 0:
                    embed = discord.Embed(
                        description = f'Rolled:',
                        colour = discord.Colour.blue()
                    )
                    data = []
                    for i in range(number):
                        r = random.randint(1, int(d))
                        embed.add_field(name=f'Throw number {i+1}:', value=f'{r}/{int(d)}', inline=False)
                        data.append(r)
                    embed.set_author(name=f'{name}', icon_url=f'{ctx.author.avatar_url}')
                    await ctx.send(embed=embed)
                    print_bot(f'Rolled {data}\nout of {d} respectively.', ctx.author, 'roll', f'{d} {number} {name}')
                else:
                    embed = discord.Embed(
                        title = 'Error',
                        description = f"Please ensure your dice has at least one side.",
                        colour = discord.Colour.red()
                    )
                    embed.set_author(name=f'{name}', icon_url=f'{ctx.author.avatar_url}')
                    await ctx.send(embed=embed)
                    print_bot(f"'roll d<number> <number of dice> <title name>' wasn't passed, instead '{d}' was inputted (all values are optional).", ctx.author, 'roll', f'{d} {number} {name}')
            elif d.isdigit():
                if int(d) > 0:
                    r = random.randint(1, int(d))
                    embed = discord.Embed(
                        description = f'Rolled:',
                        colour = discord.Colour.blue()
                    )
                    data = []
                    for i in range(number):
                        r = random.randint(1, int(d))
                        embed.add_field(name=f'Throw number {i+1}:', value=f'{r}/{int(d)}', inline=False)
                        data.append(r)
                    embed.set_author(name=f'{name}', icon_url=f'{ctx.author.avatar_url}')
                    await ctx.send(embed=embed)
                    print_bot(f'Rolled {data}\nout of {d} respectively.', ctx.author, 'roll', f'{d} {number} {name}')
                else:
                    embed = discord.Embed(
                        title = 'Error',
                        description = f"Please ensure your dice has at least one side.",
                        colour = discord.Colour.red()
                    )
                    embed.set_author(name=f'{name}', icon_url=f'{ctx.author.avatar_url}')
                    await ctx.send(embed=embed)
                    print_bot(f"'roll d<number> <number of dice> <title name>' wasn't passed, instead '{d}' was inputted (all values are optional).", ctx.author, 'roll', f'{d} {number} {name}')
            else:
                embed = discord.Embed(
                    title = 'Error',
                    colour = discord.Colour.red()
                )
                embed.set_author(name=f'{name}', icon_url=f'{ctx.author.avatar_url}')
                await ctx.send(embed=embed)
                print_bot(f"'roll d<number> <number of dice> <title name>' wasn't passed, instead '{d}' was inputted (all values are optional).", ctx.author, 'roll', f'{d} {number} {name}')
        else:
            if d.startswith('d') and d[1:].isdigit():
                d = d[1:]
                if int(d) > 0:
                    embed = discord.Embed(
                        description = f'Rolled:',
                        colour = discord.Colour.blue()
                    )
                    data = []
                    for i in range(number):
                        r = random.randint(1, int(d))
                        data.append(r)
                    embed.add_field(name=f'results (raw)', value=f'{data}\nout of {d} respectively.', inline=False)
                    datac = data.copy()
                    data.sort()
                    embed.add_field(name=f'results (sorted)', value=f'{data}\nout of {d} respectively.', inline=False)
                    embed.set_author(name=f'{name}', icon_url=f'{ctx.author.avatar_url}')
                    await ctx.send(embed=embed)
                    print_bot(f'Rolled {datac}\nand\n{data}\nout of {d} respectively.', ctx.author, 'roll', f'{d} {number} {name}')
                else:
                    embed = discord.Embed(
                        title = 'Error',
                        description = f"Please ensure your dice has at least one side.",
                        colour = discord.Colour.red()
                    )
                    embed.set_author(name=f'{name}', icon_url=f'{ctx.author.avatar_url}')
                    await ctx.send(embed=embed)
                    print_bot(f"'roll d<number> <number of dice> <title name>' wasn't passed, instead '{d}' was inputted (all values are optional).", ctx.author, 'roll', f'{d} {number} {name}')
            elif d.isdigit():
                if int(d) > 0:
                    r = random.randint(1, int(d))
                    embed = discord.Embed(
                        description = f'Rolled:',
                        colour = discord.Colour.blue()
                    )
                    data = []
                    for i in range(number):
                        r = random.randint(1, int(d))
                        data.append(r)
                    embed.add_field(name=f'results (raw)', value=f'{data}\nout of {d} respectively.', inline=False)
                    datac = data.copy()
                    data.sort()
                    embed.add_field(name=f'results (sorted)', value=f'{data}\nout of {d} respectively.', inline=False)
                    embed.set_author(name=f'{name}', icon_url=f'{ctx.author.avatar_url}')
                    await ctx.send(embed=embed)
                    print_bot(f'Rolled {datac}\nand\n{data}\nout of {d} respectively.', ctx.author, 'roll', f'{d} {number} {name}')
                else:
                    embed = discord.Embed(
                        title = 'Error',
                        description = f"Please ensure your dice has at least one side.",
                        colour = discord.Colour.red()
                    )
                    embed.set_author(name=f'{name}', icon_url=f'{ctx.author.avatar_url}')
                    await ctx.send(embed=embed)
                    print_bot(f"'roll d<number> <number of dice> <title name>' wasn't passed, instead '{d}' was inputted (all values are optional).", ctx.author, 'roll', f'{d} {number} {name}')
            else:
                embed = discord.Embed(
                    title = 'Error',
                    colour = discord.Colour.red()
                )
                embed.set_author(name=f'{name}', icon_url=f'{ctx.author.avatar_url}')
                await ctx.send(embed=embed)
                print_bot(f"'roll d<number> <number of dice> <title name>' wasn't passed, instead '{d}' was inputted (all values are optional).", ctx.author, 'roll', f'{d} {number} {name}')

##### finalize and run #####

def setup(client):
    client.add_cog(Games(client))
