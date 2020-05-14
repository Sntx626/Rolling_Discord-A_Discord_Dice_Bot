import discord
from discord.ext import commands
import random
import json
import re

with open("config.json") as f:
    command_prefix = json.load(f)["command prefix"]

import tools

def get_throws(dice): # returns the number of times the set is thrown
    try:
        pattern = re.compile(r'^(\d{0,})x')
        matches = pattern.finditer(dice)
        out = []
        for match in matches:
            out.append(int(match.group(1)))
        return out[0]
    except:
        return 1

def get_dice(dice): # returns a list of numbers of dice that are thrown
    try:
        pattern = re.compile(r'(\d{0,})d\d{1,}')
        matches = pattern.finditer(dice)
        out = []
        for match in matches:
            if match.group(1) == '':
                out.append(1)
            else:
                out.append(int(match.group(1)))
        return out
    except:
        raise ValueError(f'Error in get_dice({dice})')

def get_eyes(dice): # returns a list of the eyes of dice that are thrown
    try:
        pattern = re.compile(r'\d{0,}d(\d{1,})')
        matches = pattern.finditer(dice)
        out = []
        for match in matches:
            out.append(int(match.group(1)))
        return out
    except:
        raise ValueError(f'Error in get_eyes({dice})')

'''
    get_mod is ignored for now!
'''
def get_mod(dice): # returns a list of modifier for the dice that are thrown
    try:
        pattern = re.compile(r'\d{0,}d\d{1,}(.{0,})(\d{0,}d\d{1,})?')
        matches = pattern.finditer(dice)
        out = []
        for match in matches:
            out.append(match.group(1))
        return out
    except:
        raise ValueError(f'Error in get_mod({dice})')

def throw_dice(dice, eyes, mod): # returns a string as a result
    out = ''
    for d in range(len(dice)): # go through all individual dice
        data = []
        for i in range(dice[d]):
            rnd = random.randint(1, eyes[d])
            data.append(rnd)
        out += f'{data}/{eyes[d]}\t\t' #+ f' {mod[d]}'
    return out # return result string

class Games(commands.Cog):

    ##### initalization #####

    def __init__(self, client):
        self.client = client

    ##### commands #####

    @commands.command()
    async def roll(self, ctx, *, input="2x 1d20+ 13, 1d8+5 + 2d6"):
        tools.print_on_command_call(ctx.author, 'roll', f'{input}')

       	name = ""
        try:
            if ctx.author.nick is None:
                name = f'{ctx.author}'
                name = name[:(len(name)-5)]
            else:
                name = ctx.author.nick
        except:
            name = f'{ctx.author}'
            name = name[:(len(name)-5)]

        dice = input.split(',')

        dice_r = []
        for d in dice:
            d = d.strip()
            print("dice:", d)

            g_throws = get_throws(d) # number
            print(f"get_throws({d}):{g_throws}")
            g_dice = get_dice(d) # list
            print(f"get_dice({d}):{g_dice}")
            g_eyes = get_eyes(d) # list
            print(f"get_eyes({d}):{g_eyes}")
            g_mod = get_mod(d) # list
            print(f"get_mod({d}):{g_mod}")
            try:
                pass # check needed values
            except:
                embed = discord.Embed(
                    title = 'Error',
                    description = f"At least one of your Dice doesn't fit the Syntax, please refer to '{command_prefix}info'.",
                    colour = discord.Colour.red()
                )
                embed.set_author(name=f'{name}', icon_url=f'{ctx.author.avatar_url}')
                await ctx.send(embed=embed)
                tools.print_bot(f"Error: At least one of the Dice doesn't fit the Syntax", name, 'roll', input)
                return

            d_r = []
            for i in range(g_throws):
                d_r.append(throw_dice(g_dice, g_eyes, g_mod))
            dice_r.append(d_r)


        if len(dice_r) == 1:
            data = ''
            for d in dice_r[0]:
                data += d + '\n'
            embed = discord.Embed(
                title = '',
                description = f'{data}',
                colour = discord.Colour.blue()
            )
            embed.set_author(name=f'{name}', icon_url=f'{ctx.author.avatar_url}')

            await ctx.send(embed=embed)
            tools.print_bot(f"Dice thrown!", name, 'roll', input)
        else:
            embed = discord.Embed(
                description = 'Rolled:',
                colour = discord.Colour.blue()
            )
            embed.set_author(name=f'{name}', icon_url=f'{ctx.author.avatar_url}')

            for i in range(len(dice_r)):
                data = ''
                for d in range(len(dice_r[i])):
                    if d < len(dice_r[i])-1:
                        data += dice_r[i][d] + ',\n'
                    else:
                        data += dice_r[i][d]
                embed.add_field(name=f"Throw number {i+1}:", value=f"{data}", inline=False)

            await ctx.send(embed=embed)
            tools.print_bot(f'Dice thrown!', name, 'roll', input)

##### finalize and run #####

def setup(client):
    client.add_cog(Games(client))
