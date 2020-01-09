# -*- coding: utf-8 -*-

import discord

_TOKEN = open("Token.txt").readline().rstrip()

client = discord.Client()

def welcome(id):
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

@client.event
async def on_ready():
	print('We have logged in as {0.user.name}'.format(client))

@client.event
async def on_member_join(member):
	channel = client.get_channel(664400035718496256)
	await channel.send(welcome(str(member.id)))

client.run(_TOKEN)