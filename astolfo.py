# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get

_TOKEN = open("Token.txt").readline().rstrip()

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
	print('We have logged in as {0.user.name}'.format(bot))

@bot.command(pass_context=True)
async def give_random_user(ctx):
	msg = await ctx.send(get_random_user())
	emoji = '\U0001F498'
	await msg.add_reaction(emoji)


bot.run(_TOKEN)