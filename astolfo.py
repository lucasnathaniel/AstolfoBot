# -*- coding: utf-8 -*-

import discord
import asyncio
from discord.ext import commands

_TOKEN = open("Token.txt").readline().rstrip()

bot = commands.Bot(command_prefix='$')

def welcome(id):
	return """
	``` _______       .-''-.  ,---.    ,---.   ,---.  ,---..-./`) ,---.   .--. ______        ____
\\  ____  \\   .'_ _   \\ |    \\  /    |   |   /  |   |\\ .-.')|    \\  |  ||    _ `''.  .'  __ `.  
| |    \\ |  / ( ` )   '|  ,  \\/  ,  |   |  |   |  .'/ `-' \\|  ,  \\ |  || _ | ) _  \\/   '  \\  \\ 
| |____/ / . (_ o _)  ||  |\\_   /|  |   |  | _ |  |  `-'`"`|  |\\_ \\|  ||( ''_'  ) ||___|  /  | 
|   _ _ '. |  (_,_)___||  _( )_/ |  |   |  _( )_  |  .---. |  _( )_\\  || . (_) `. |   _.-`   | 
|  ( ' )  \\'  \\   .---.| (_ o _) |  |   \\ (_ o._) /  |   | | (_ o _)  ||(_    ._) '.'   _    | 
| (_{;}_) | \\  `-'    /|  (_,_)  |  |    \\ (_,_) /   |   | |  (_,_)\\  ||  (_.\\.' / |  _( )_  | 
|  (_,_)  /  \\       / |  |      |  |     \\     /    |   | |  |    |  ||       .'  \\ (_ o _) / 
/_______.'    `'-..-'  '--'      '--'      `---`     '---' '--'    '--''-----'`     '.(_,_).'
```
**Seja bem vinda ao TGalaxy Brasil, <@$$$>! Nosso objetivo é reunir o máximo da comunidade Trans|Cross brasileira e criar um gratificanete laço social oωo✿.**

Para acessar o restante do servidor, você deve publicar uma introdução antes de receber manualmente os devidos cargos de uma das <@&664408571538309120>.
Exemplo:

Nome: Como deseja ser chamada aqui (Requerido)
Idade: (Requerido)
Gênero: (Requerido)
Gosta/não gosta: (Opcional)
Estado ou país(caso não for daqui): (Requerido)
Mais alguma outra coisa: (Opcional)
	""".replace("$$$", id)

@bot.event
async def on_ready():
	print('We have logged in as {0.user.name}'.format(bot))

@bot.event
async def on_member_join(member):
	channel = bot.get_channel(664400035718496256)
	await channel.send(welcome(str(member.id)))

@bot.command(pass_context = True)
async def mute(ctx, member : discord.Member = None):
	if 664408571538309120 in [role.id for role in ctx.author.roles]:
		try:
			silenced_role = ctx.guild.get_role(664927129204686848)
			lady_role = ctx.guild.get_role(664407928618483732)
			days = ctx.message.content.split()[2]
			duration = int(days)*86400
			await member.add_roles(silenced_role)
			await member.remove_roles(lady_role)
			await ctx.send(f"<@!{member}> silenciada por {days} dia(s)")
			await asyncio.sleep(duration)
			await member.remove_roles(silenced_role)
			await member.add_roles(lady_role)
		except Exception as ex:
			print(ex)
			await ctx.send(f"<@!{ctx.message.author.id}>, comando invalido, querida :/. Use $mute @member <1-7>")
	else:
		await ctx.send(f"<@!{ctx.message.author}>, Voce nao tem permissao, querida :/")

@bot.command(pass_context = True)
async def unmute(ctx, member : discord.Member = None):
	if 664408571538309120 in [role.id for role in ctx.author.roles]:
		try:
			silenced_role = ctx.guild.get_role(664927129204686848)
			lady_role = ctx.guild.get_role(664407928618483732)
			await ctx.send(f"<@!{member}>, agora voce pode falar, baby C:")
			await member.remove_roles(silenced_role)
			await member.add_roles(lady_role)
		except Exception as ex:
			print(ex)
			await ctx.send(f"<@!{ctx.message.author.id}>, comando invalido, querida :/. Use $mute @member <1-7>")
	else:
		await ctx.send(f"<@!{ctx.message.author}>, Voce nao tem permissao, querida :/")

bot.run(_TOKEN)