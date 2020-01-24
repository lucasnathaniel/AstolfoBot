# -*- coding: utf-8 -*-

import discord
import asyncio
import random
import re
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
**Seja bem vinda ao TGalaxy Brasil, <@$$$>! Nosso objetivo é reunir o máximo da comunidade Trans|Cross brasileira e criar um lindo laço social oωo✿.**

Para acessar o restante do servidor, você deve publicar uma introdução e isso lhe dará acesso automaticamente!
Exemplo:

Nome: Como deseja ser chamada aqui (Requerido)
Idade: (Requerido)
Gênero: (Requerido)
Gosta/não gosta: (Opcional)
Estado ou país(caso não for daqui): (Requerido)
Mais alguma outra coisa: (Opcional)

OBS: Por obséquio, leia <#664401311269257224>, é rapidinho C:
	""".replace("$$$", id)

@bot.event
async def on_ready():
	print('We have logged in as {0.user.name}'.format(bot))

@bot.event
async def on_member_join(member):
	channel = bot.get_channel(664400035718496256)
	await channel.send(welcome(str(member.id)))

@bot.event
async def on_message(message):
	#Roleplay
	if "astolfo" in message.content.lower() and message.author.id != 664718856509718528:
		message = random.choice(await message.channel.history(limit=1000).flatten())
		await message.channel.send(re.sub('<@!.*?>',"querida",message.content, flags=re.DOTALL))
	#Disboard message
	if message.channel.id == 669719596919554067 and message.author.id == 302050872383242240 and "Bump done" in message.content:
		disboard_channel = bot.get_channel(669719596919554067)
		duration = 7200
		await disboard_channel.send("Vou lembrar dentro de 2 horas (Disboard) C:")
		await asyncio.sleep(duration)
		await disboard_channel.send("<@&664408571538309120>, querida, please digite `!d bump` (Disboard) C:")
	#Get Lady role
	if message.channel.id == 664400035718496256 and len(message.author.roles) == 1 and len(message.content) > 20:
		lady_role = message.guild.get_role(664407928618483732)
		await message.author.add_roles(lady_role)
	await bot.process_commands(message)

@bot.command(pass_context = True)
async def sou(ctx):
	if ctx.channel.id == 665081142734749711:
		print(f"Adicionando role para {ctx.author}")
		for role in ctx.guild.roles:
			name_role = role.name.lower()
			if name_role == ctx.message.content.split()[1].lower():
				if name_role in ["queen", "princess", "astolfo", "disboard.org", "lady", "lady silenciada", "@everyone"]:
					await ctx.send(f"<@!{ctx.author.id}>, você não tem permissão pra isso, querida :/")
					return
				if name_role == "trans":
					role = ctx.guild.get_role(665070487000580099)
				if name_role == "trap/cross":
					role = ctx.guild.get_role(665070596455137302)
				await ctx.author.add_roles(role)
				await ctx.send(f"Tag {role.name} adicionada para <@!{ctx.author.id}>!")
				return
		await ctx.send(f"<@!{ctx.author.id}>, a tag {ctx.message.content.split()[1]} nao foi encontrada, querida :/")

@bot.command(pass_context = True)
async def oi(ctx):
	await ctx.send(f"Oi <@!{ctx.author.id}>!")

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