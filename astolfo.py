# -*- coding: utf-8 -*-

import discord
import asyncio
import random
import re
import hashlib
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
	print(re.sub('<@!.*?>',"querida","oi <@!229759671039164416>", flags=re.DOTALL))

@bot.event
async def on_member_join(member):
	channel = bot.get_channel(664400035718496256)
	await channel.send(welcome(str(member.id)))

@bot.event
async def on_member_ban(guild, member):
	log_channel = bot.get_channel(670307380176879660)
	await log_channel.send(f"{member} banido C:")

@bot.event
async def on_member_unban(guild, member):
	log_channel = bot.get_channel(670307380176879660)
	await log_channel.send(f"{member} desbanido C:")

@bot.event
async def on_message(message):
	#Roleplay
	if "astolfo" in message.content.lower() and message.author.id != 664718856509718528:
		selected_message = random.choice(await message.channel.history(limit=1100).flatten())
		print(selected_message.content)
		await message.channel.send(re.sub('<@.*?>',"querida",selected_message.content, flags=re.DOTALL).replace("@everyone", ""))
	#Disboard message
	if message.channel.id == 669719596919554067 and message.author.id == 302050872383242240:
		if "Bump done" in message.embeds[0].description:
			duration = 7200
			await message.channel.send("Vou lembrar dentro de 2 horas (Disboard) C:")
			await asyncio.sleep(duration)
			await message.channel.send("<@&664408571538309120>, querida, please digite `!d bump` (Disboard) C:")
		elif "Please wait another" in message.embeds[0].description:
			await message.channel.send("Espere mais um tempinho, jovem! (Disboard) :C")
	#Get Lady role
	if message.channel.id == 664400035718496256 and len(message.author.roles) == 1 and len(message.content) > 20:
		lady_role = message.guild.get_role(664407928618483732)
		await message.author.add_roles(lady_role)
	await bot.process_commands(message)
#Atribuicao de roles
@bot.command(pass_context = True)
async def sou(ctx):
	if ctx.channel.id == 665081142734749711:
		print(f"Adicionando role para {ctx.author}")
		for role in ctx.guild.roles:
			name_role = role.name.lower()
			if name_role == ctx.message.content.split()[1].lower():
				if name_role == "nsfw" and ctx.guild.get_role(673947486804639765) in ctx.author.roles:
					await ctx.send(f"<@!{ctx.author.id}>, você não tem permissão pra isso, querida, volte quando você for mais velha :/")
					return
				if name_role in ["queen", "princess", "astolfo", "disboard.org", "plebeu", "lady silenciada", "@everyone", "menor"]:
					await ctx.send(f"<@!{ctx.author.id}>, você não tem permissão pra isso, querida :/")
					return
				if name_role == "trans":
					role = ctx.guild.get_role(665070487000580099)
				elif name_role == "trap/cross":
					role = ctx.guild.get_role(665070596455137302)
				elif name_role == "lady":
					plebeu_role = ctx.guild.get_role(664407928618483732)
					await ctx.author.remove_roles(plebeu_role)
					role = ctx.guild.get_role(671230841812156446)
				if role in ctx.author.roles:
					await ctx.send(f"<@!{ctx.author.id}>!, você já tem a tag `{role.name}`, por favor não canse minha beleza! :C")
					return
				else:
					await ctx.author.add_roles(role)
					await ctx.send(f"Tag `{role.name}` adicionada para <@!{ctx.author.id}>!")
					return
		await ctx.send(f"<@!{ctx.author.id}>, a tag `{ctx.message.content.split()[1]}` nao foi encontrada, querida :/")
#Desatribuicao de roles
@bot.command(pass_context = True)
async def naosou(ctx):
	if ctx.channel.id == 665081142734749711:
		print(f"Adicionando role para {ctx.author}")
		for role in ctx.author.roles:
			if role.name.lower() == ctx.message.content.split()[1].lower():
				if role.name.lower() in ["queen", "princess", "astolfo", "disboard.org", "plebeu", "lady", "lady silenciada"]:
					await ctx.send(f"<@!{ctx.author.id}>!, você não pode remover a tag `{role.name}`, por favor não canse minha beleza! :C")
				else:
					await ctx.author.remove_roles(role)
					await ctx.send(f"Tag `{role.name}` removida de <@!{ctx.author.id}>!")
					return
		await ctx.send(f"<@!{ctx.author.id}>, a tag `{ctx.message.content.split()[1]}` nao foi encontrada, querida :/")
#Checka se o bot ta on
@bot.command(pass_context = True)
async def oi(ctx):
	await ctx.send(f"Oi <@!{ctx.author.id}>!")
#Roll percentual
@bot.command(pass_context = True)
async def roll(ctx):
	conteudo = ctx.message.content
	if len(conteudo.split()) > 1:
		if conteudo.split()[1].isdigit():
			await ctx.send(f"{random.randint(0, min(int(conteudo.split()[1]), 2147483647))}")
			return
	await ctx.send(f"{int(hashlib.md5(conteudo.encode('utf-8')).hexdigest()[0:2], 16)%101}%")

@bot.command(pass_context = True)
async def video(ctx):
	channels = (c.name for c in ctx.message.server.channels if c.type==ChannelType.voice)
	for channel in channels:
		if ctx.author in channel.members:
			embed=discord.Embed(title="Astolfo - Canal de Vídeo", description=f"Clique [aqui](https://discordapp.com/channels/{ctx.guild.id}/{ctx.member.channel.id}) para entrar no canal de vídeo de seu canal de voz.")
			await ctx.send(embed=embed)
			return
	await ctx.send(f"<@!{ctx.author.id}> Você não está em um canal de voz, querida")
#Muta o individuo
#@bot.command(pass_context = True)
#async def mute(ctx, member : discord.Member = None):
#	if 664408571538309120 in [role.id for role in ctx.author.roles]:
#		try:
#			silenced_role = ctx.guild.get_role(664927129204686848)
#			lady_role = ctx.guild.get_role(664407928618483732)
#			days = ctx.message.content.split()[2]
#			duration = int(days)*86400
#			await member.add_roles(silenced_role)
#			await member.remove_roles(lady_role)
#			await ctx.send(f"<@!{member}> silenciada por {days} dia(s)")
#			await asyncio.sleep(duration)
#			await member.remove_roles(silenced_role)
#			await member.add_roles(lady_role)
#		except Exception as ex:
#			print(ex)
#			await ctx.send(f"<@!{ctx.message.author.id}>, comando invalido, querida :/. Use $mute @member <1-7>")
#	else:
#		await ctx.send(f"<@!{ctx.message.author}>, Voce nao tem permissao, querida :/")
#Desmuta o individuo
#@bot.command(pass_context = True)
#async def unmute(ctx, member : discord.Member = None):
#	if 664408571538309120 in [role.id for role in ctx.author.roles]:
#		try:
#			silenced_role = ctx.guild.get_role(664927129204686848)
#			lady_role = ctx.guild.get_role(664407928618483732)
#			await ctx.send(f"<@!{member}>, agora voce pode falar, baby C:")
#			await member.remove_roles(silenced_role)
#			await member.add_roles(lady_role)
#		except Exception as ex:
#			print(ex)
#			await ctx.send(f"<@!{ctx.message.author.id}>, comando invalido, querida :/. Use $mute @member <1-7>")
#	else:
#		await ctx.send(f"<@!{ctx.message.author}>, Voce nao tem permissao, querida :/")
#Limpa as msg
@bot.command(pass_context = True)
async def clear(ctx):
	if 664408571538309120 in [role.id for role in ctx.author.roles]:
		try:
			number = int(ctx.message.content.split()[1])
			if number >=1 and number <=100:
				log_channel = bot.get_channel(670307380176879660)
				await log_channel.send(f"<@!{ctx.message.author.id}> deletou {number} mensagens no canal <#{ctx.channel.id}>")
				for current_message in await ctx.channel.history(limit=number).flatten():
					await current_message.delete()
			else:
				await ctx.send(f"<@!{ctx.message.author.id}>, querida, algo de errado nao esta certo :/. Use $clear <1-50>")
		except Exception as ex:
			print(ex)
			await ctx.send(f"<@!{ctx.message.author.id}>, querida, algo de errado nao esta certo :/. Use $clear <1-100>")
	else:
		await ctx.send(f"<@!{ctx.message.author}>, Voce nao tem permissao, querida :/")

bot.run(_TOKEN)