# -*- coding: utf-8 -*-

# requeriments: pynacl youtube-dl

#embed
#https://cog-creators.github.io/discord-embed-sandbox/
import discord
import asyncio
import random
import re
import hashlib
from discord.ext import commands
from discord.ext.commands import has_permissions
from async_timeout import timeout

#Import files
from disaudio import *
from gifdb import *

# Silence useless bug reports messages
youtube_dl.utils.bug_reports_message = lambda: ''

bot = commands.Bot(command_prefix='$', case_insensitive=True)
bot.remove_command("help")
bot.add_cog(Music(bot))

def get_help():
	return """
	Prefixo = '$', ex.: $oi
	**__->Comandos básicos__**
	 **oi**    - Verifica se o bot está online
	 **roll**  - Rolagem aleatória
	 Ex.: *[$roll chances deu ganhar na mega-sena] [$roll 1337]*
	 **video** - Comando para iniciar a conferencia de video, caso você esteja num canal de voz
	 **help**  - Abre a ajuda
	**__->Comandos de ação__**
	 *Interação com outro usuário, basta usar o comando e marcar a outra pessoa, ex: $bite @K4L1*
	 Lista: `bite`, `cuddle`, `greet`, `highfive`, `hug`, `kiss`, `lewd`, `pat`, `poke`, `slap` e `lick`.
	**__->Comandos de música__**
	 **join**  - Conecta o bot ao voice que voce esta.
	 **play**  - Toca a música que for passada no parametro ou adiciona ela na fila.
	 Ex.: *[$play parado no bailao] [$play youtube.com/watch?v=fLtQI3r6Ni4]*
	 **pause** - Pausa a música que esta tocando no momento.
	 **stop**  - Para a música que esta tocando no momento.
	 **now**   - Mostra qual música esta tocando no momento.
	 **queue** - Mostra a lista de músicas que estao na fila.
	 **leave** - Desconecta o bot do voice em que voce esta.

	"""

def welcome(id):
	return """
**Seja bem vinda ao TGalaxy Brasil, <@$$$>! Nosso objetivo é reunir o máximo da comunidade Trans|Cross brasileira e criar um lindo laço social oωo✿.**

Para acessar o restante do servidor, você deve publicar uma introdução e isso lhe dará acesso automaticamente!
Exemplo:

Nome: Como deseja ser chamada aqui (Requerido)
Idade: (Requerido)
Gênero: (Requerido)
Hobbies: (Opcional)
Estado ou país(caso não for daqui): (Requerido)
Mais alguma outra coisa: (Opcional)

OBS: Por obséquio, leia <#664401311269257224>, é rapidinho C:
	""".replace("$$$", id)

@bot.event
async def on_ready():
	print("Discord Version:",discord.__version__)
	print('We have logged in as {0.user.name}'.format(bot))
	print(re.sub('<@!.*?>',"querida","oi <@!229759671039164416>", flags=re.DOTALL))
	await bot.change_presence(status=discord.Status.idle, activity=discord.Game("(✿◠‿◠) Nyaaaaa! (◕ᴗ◕✿)"))
	channel = bot.get_channel(671197064595767307) #geral
	voltei_message = await channel.send("Voltei C:")
	await asyncio.sleep(18)
	await voltei_message.delete()
	
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
		parameter = ctx.message.content.split()[1].lower()
		for role in ctx.guild.roles:
			name_role = role.name.lower()
			if parameter in name_role:
				if name_role == "nsfw" and ctx.guild.get_role(673947486804639765) in ctx.author.roles:
					await ctx.send(f"<@!{ctx.author.id}>, você não tem permissão pra isso, querida, volte quando você for mais velha :/")
					return
				if name_role in ["queen", "princess", "camponesa", "astolfo", "astolfo", "disboard.org", "plebeu", "@everyone", "menor"]:
					await ctx.send(f"<@!{ctx.author.id}>, você não tem permissão pra isso, querida :/")
					return
				if name_role == "trans":
					role = ctx.guild.get_role(665070487000580099)
				elif "trap" in parameter or "cross" in parameter:
					role = ctx.guild.get_role(665070596455137302)
				elif "lady" in parameter:
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
		parameter = ctx.message.content.split()[1].lower()
		for role in ctx.author.roles:
			if parameter in role.name.lower():
				if role.name.lower() in ["queen", "princess", "camponesa", "astolfo", "astolfo", "disboard.org", "plebeu", "lady", "lady silenciada"]:
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

#Iteraction events
@bot.command(pass_context = True)
async def cuddle(ctx, member : discord.Member = None):
	if member.id != ctx.author.id:
		gif = get_gif("cuddle")
		embed=discord.Embed(title="", description="").set_image(url=f"{gif}")
		await ctx.send(content=f"**{member.name}** você recebeu calíneos de **{ctx.author.name}**", embed=embed)
	else:
		await ctx.send(f"Você não pode fazer isso consigo mesma! :V")

@bot.command(pass_context = True)
async def kiss(ctx, member : discord.Member = None):
	if member.id != ctx.author.id:
		gif = get_gif("kiss")
		embed=discord.Embed(title="", description="").set_image(url=f"{gif}")
		await ctx.send(content=f"**{member.name}** você foi beijadíneo(a) por **{ctx.author.name}** (・ε・ ✿)", embed=embed)
	else:
		await ctx.send(f"Você não pode fazer isso consigo mesma! :V")

@bot.command(pass_context = True)
async def hug(ctx, member : discord.Member = None):
	if member.id != ctx.author.id:
		gif = get_gif("hug")
		embed=discord.Embed(title="", description="").set_image(url=f"{gif}")
		await ctx.send(content=f"**{member.name}** você foi ablatado(a) por **{ctx.author.name}** UwU", embed=embed)
	else:
		await ctx.send(f"Você não pode fazer isso consigo mesma! :V")

@bot.command(pass_context = True)
async def slap(ctx, member : discord.Member = None):
	if member.id != ctx.author.id:
		gif = get_gif("slap")
		embed=discord.Embed(title="", description="").set_image(url=f"{gif}")
		await ctx.send(content=f"**{member.name}** você foi agledido(a) por **{ctx.author.name}** >:)", embed=embed)
	else:
		await ctx.send(f"Você não pode fazer isso consigo mesma! :V")

@bot.command(pass_context = True)
async def bite(ctx, member : discord.Member = None):
	if member.id != ctx.author.id:
		gif = get_gif("bite")
		embed=discord.Embed(title="", description="").set_image(url=f"{gif}")
		await ctx.send(content=f"**{member.name}** você foi moidido(a) por **{ctx.author.name}** :3", embed=embed)
	else:
		await ctx.send(f"Você não pode fazer isso consigo mesma! :V")

@bot.command(pass_context = True)
async def poke(ctx, member : discord.Member = None):
	if member.id != ctx.author.id:
		gif = get_gif("poke")
		embed=discord.Embed(title="", description="").set_image(url=f"{gif}")
		await ctx.send(content=f"**{member.name}** você foi cuiticado(a) por **{ctx.author.name}** OwO", embed=embed)
	else:
		await ctx.send(f"Você não pode fazer isso consigo mesma! :V")

@bot.command(pass_context = True)
async def lick(ctx, member : discord.Member = None):
	if member.id != ctx.author.id:
		gif = get_gif("lick")
		embed=discord.Embed(title="", description="").set_image(url=f"{gif}")
		await ctx.send(content=f"**{member.name}** você foi lambidíneo(a) por **{ctx.author.name}** :p", embed=embed)
	else:
		await ctx.send(f"Você não pode fazer isso consigo mesma! :V")

@bot.command(pass_context = True)
async def pat(ctx, member : discord.Member = None):
	if member.id != ctx.author.id:
		gif = get_gif("pat")
		embed=discord.Embed(title="", description="").set_image(url=f"{gif}")
		await ctx.send(content=f"**{member.name}** você foi acaliciado(a) por **{ctx.author.name}** C:", embed=embed)
	else:
		await ctx.send(f"Você não pode fazer isso consigo mesma! :V")

@bot.command(pass_context = True)
async def lewd(ctx, member : discord.Member = None):
	if member.id != ctx.author.id:
		gif = get_gif("lewd")
		embed=discord.Embed(title="", description="").set_image(url=f"{gif}")
		await ctx.send(content=f"**{member.name}** você foi secadíneo(a) por **{ctx.author.name}** UwU", embed=embed)
	else:
		await ctx.send(f"Você não pode fazer isso consigo mesma! :V")

@bot.command(pass_context = True)
async def highfive(ctx, member : discord.Member = None):
	if member.id != ctx.author.id:
		gif = get_gif("highfive")
		embed=discord.Embed(title="", description="").set_image(url=f"{gif}")
		await ctx.send(content=f"**{member.name}** você foi comemolou com **{ctx.author.name}** :D", embed=embed)
	else:
		await ctx.send(f"Você não pode fazer isso consigo mesma! :V")

@bot.command(pass_context = True)
async def greet(ctx, member : discord.Member = None):
	if member.id != ctx.author.id:
		gif = get_gif("greet")
		embed=discord.Embed(title="", description="").set_image(url=f"{gif}")
		await ctx.send(content=f"**{member.name}** você foi saudadíneo(a) por **{ctx.author.name}** :D", embed=embed)
	else:
		await ctx.send(f"Você não pode fazer isso consigo mesma! :V")

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
	channels = ctx.guild.voice_channels
	for channel in channels:
		if ctx.message.author in channel.members:
			embed=discord.Embed(title="astolfo - Canal de Vídeo", description=f"Clique [aqui](https://discordapp.com/channels/{ctx.guild.id}/{channel.id}) para entrar no canal de vídeo de seu canal de voz.", color=int(hex(randint(0, 16777215)), 16))
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
@has_permissions(manage_guild=True)
async def clear(ctx):
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
		#await ctx.send(f"<@!{ctx.message.author.id}>, querida, algo de errado nao esta certo :/. Use $clear <1-100>")

#Help
@bot.command(pass_context = True)
async def help(ctx):
	helper = get_help()
	embed=discord.Embed(title="astolfo - Lista de comandos", description=helper)
	embed.set_thumbnail(url=bot.get_user(689596096225476656).avatar_url)
	await ctx.send(embed=embed)

@bot.command()
@commands.is_owner()
async def kill(ctx):
	await ctx.send("Adeus :C")
	await ctx.bot.logout()

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send(f'Comando Invalido, <@!{ctx.message.author.id}>! Please use $help para checkar os comandos! C:')
	elif isinstance(error, commands.CheckFailure):
		await ctx.send(f"<@!{ctx.author.id}>, você não tem permissão pra isso, querida, volte quando for mais velha :/")

def main():
	_TOKEN = open("Token.txt").readline().rstrip()
	bot.run(_TOKEN)

if __name__ == "__main__":
	main()