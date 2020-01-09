# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get

_TOKEN = open("Token.txt").readline().rstrip()

bot = commands.Bot(command_prefix='$')

def welcome():
	return """
	``` _______       .-''-.  ,---.    ,---.   ,---.  ,---..-./`) ,---.   .--. ______        ____
\\  ____  \\   .'_ _   \\ |    \\  /    |   |   /  |   |\\ .-.')|    \\  |  ||    _ `''.  .'  __ `.  
| |    \\ |  / ( ` )   '|  ,  \\/  ,  |   |  |   |  .'/ `-' \\|  ,  \\ |  || _ | ) _  \\/   '  \\  \\ 
| |____/ / . (_ o _)  ||  |\\_   /|  |   |  | _ |  |  `-'`"`|  |\\_ \\|  ||( ''_'  ) ||___|  /  | 
|   _ _ '. |  (_,_)___||  _( )_/ |  |   |  _( )_  |  .---. |  _( )_\\  || . (_) `. |   _.-`   | 
|  ( ' )  \'  \\   .---.| (_ o _) |  |   \\ (_ o._) /  |   | | (_ o _)  ||(_    ._) '.'   _    | 
| (_{;}_) | \\  `-'    /|  (_,_)  |  |    \\ (_,_) /   |   | |  (_,_)\\  ||  (_.\\.' / |  _( )_  | 
|  (_,_)  /  \\       / |  |      |  |     \\     /    |   | |  |    |  ||       .'  \\ (_ o _) / 
/_______.'    `'-..-'  '--'      '--'      `---`     '---' '--'    '--''-----'`     '.(_,_).'
```
**Sejam bem vindas ao TGalaxy Brasil!, cujo objetivo é reunir o máximo da comunidade Trans|Cross brasileira e criar um gratificanete laço social oωo✿.**

Para acessar o restante do servidor, você deve publicar uma introdução antes de receber manualmente os devidos cargos de uma das @Princess.
Exemplo:

Nome: Como deseja ser chamada aqui (Requerido)
Idade: (Requerido)
Gênero: (Requerido)
Gosta/não gosta: (Opcional)
Estado ou país(caso não for daqui): (Requerido)
Mais alguma outra coisa: (Opcional)
	"""

@bot.event
async def on_ready():
	print('We have logged in as {0.user.name}'.format(bot))

@bot.event
async def on_member_join(member):
	target_channel = bot.get_channel("664400035718496256")
	await client.send_message(target_channel, welcome())

@bot.command(pass_context=True)
async def give_random_user(ctx):
	msg = await ctx.send(get_random_user())
	emoji = '\U0001F498'
	await msg.add_reaction(emoji)


bot.run(_TOKEN)