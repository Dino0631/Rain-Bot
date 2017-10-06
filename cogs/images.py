# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2017 Dino#0631 (discord)

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
import os
heroku = False
if 'DYNO_RAM' in os.environ:
	heroku = True
if not heroku:
	import discord
	from discord.ext.commands import bot
	from discord.ext import commands
	import datetime
	import time
	import random
	import asyncio
	import json
	import requests
	from bs4 import BeautifulSoup
	# from __main__ import send_cmd_help
	import string
	import aiohttp
	from urllib.parse import quote_plus
	import locale
	import inspect
	import moviepy.editor as mp
	from bs4 import BeautifulSoup
	import asyncio
	import aiohttp
	from cogs.utils.dataIO import dataIO
	from cogs.utils import checks
	import locale
	import imageio
	from __main__ import settings
	import subprocess
	from gtts import gTTS
	# from ffmpy import subprocess
	# try:
	#     imageio.plugins.ffmpeg.download()
	# except Exception as e:
	#     print(e)
	#     print(dir(e))
	# input()
	PATH = os.path.join('data', 'images')
	AUDIOPATH = os.path.join(PATH, 'png')
	VIDEOPATH = os.path.join(PATH, 'mp4')
	SETTINGS_JSON = os.path.join(PATH, 'settings.json')
	class UserNotConnected(Exception):
		def __init__(self):
			self.msg = "User is not in a voice channel of this server."
	class ChannelNotPrivate(Exception):
		def __init__(self):
			self.msg = "This command only works in dm or group."

	class Images:
		"""Display RACF specifc info.

		Note: RACF specific plugin for Red
		"""

		def __init__(self, bot):
			"""Constructor."""
			self.bot = bot
			self.extP = '.png'
			self.extV = '.mp4'
			# self.is_playing = False
			# self.settings = dataIO.load_json(SETTINGS_JSON)
			# self.settings['playing'] = self.is_playing
			# dataIO.save_json(SETTINGS_JSON, self.settings)

		async def on_ready(self):
			imageio.plugins.ffmpeg.download()


		# @checks.is_owner()
		# @commands.command(pass_context=True)
		# async def mp4s2mp3(self,ctx, option=None):
		# 	for mp4 in os.listdir(VIDEOPATH):
		# 		mp3 = mp4.replace('.mp4','.mp3')
		# 		if option == 'overwrite':
		# 			condition = True
		# 		else:
		# 			condition = mp3 not in os.listdir(AUDIOPATH)
		# 		if condition:
		# 			clip = mp.VideoFileClip(os.path.join(VIDEOPATH, mp4))
		# 			clip.audio.write_audiofile(os.path.join(AUDIOPATH, mp3))

		# async def get_voice_client(self, ctx):
		# 	servclient = None
		# 	for client in list(self.bot.voice_clients):
		# 		# print(client.server)
		# 		# print(ctx.message.content)
		# 		if client.server == ctx.message.server:
		# 			servclient = client
		# 			break
		# 	return servclient

		# async def disconnect(self, ctx):
		# 	client = await self.get_voice_client(ctx)
		# 	if client is not None:
		# 		await client.disconnect()

		# async def connect_with_user(self, ctx, user=None):
		# 	if user == None:
		# 		user = ctx.message.author
		# 	channel = user.voice_channel
		# 	if channel is None:
		# 		raise UserNotConnected()
		# 	else:
		# 		if self.bot.is_voice_connected(ctx.message.server):
		# 			voiceclient = await self.get_voice_client(ctx)
		# 			if voiceclient.channel != user.voice_channel or not self.bot.user.bot:
		# 				await voiceclient.move_to(user.voice_channel)
		# 		else:
		# 			voiceclient = await self.bot.join_voice_channel(channel)
		# 	return voiceclient

		# async def connect_with_userdm(self, ctx, user=None):
		# 	if user == None:
		# 		user = ctx.message.author
		# 	if not ctx.message.channel.is_private:
		# 		raise ChannelNotPrivate()
		# 	else:
		# 		if self.bot.is_voice_connected(ctx.message.server):
		# 			voiceclient = await self.get_voice_client(ctx)
		# 			if voiceclient.channel != user.voice_channel:
		# 				await voiceclient.move_to(user.channel)
		# 		else:
		# 			voiceclient = await self.bot.join_voice_channel(channel)
		# 	return voiceclient

		# async def playmp3(self, client, filename):
		# 	player = client.create_ffmpeg_player(filename)
		# 	player.start()
		# 	print(dir(player))

		# @checks.mod_or_permissions()
		# @commands.group(name='crsfx',pass_context=True)
		# async def crsfx(self, ctx):
		# 	"""play sound effects
		# 	"""
		# 	if ctx.invoked_subcommand is None:
		# 		await send_cmd_help(ctx)

		# @crsfx.command(pass_context=True)
		# async def test(self, ctx):
		# 	print('hi')
		# 	await self.bot.say(self.bot.is_voice_connected(ctx.message.server))
		# 	for v in self.bot.voice_clients:
		# 		await self.bot.say(v)

		# @crsfx.command(pass_context=True)
		# async def sfxdc(self, ctx):
		# 	servclient = await self.get_voice_client(ctx)
		# 	if servclient is not None:
		# 		await servclient.disconnect()
		# @crsfx.command(pass_context=True)
		# async def list(self,ctx):
		# 	mp3list = []
		# 	for x in os.listdir(AUDIOPATH):
		# 		if '.mp3' in x:
		# 			mp3list.append('`{}`'.format(x))
		# 	await self.bot.say(', '.join(mp3list))

		# @commands.command(pass_context=True, no_pm=True)
		# async def crclip(self, ctx, filename=None, times=1,user:discord.User=None):
		# 	'''
		# 	syntax:
		# 	filename must be a filename in my folder or filenames in my folder, separated by a /
		# 	times must be a number or it will just do it once
		# 	user must be a mention, id, username and it will find the voice channel in the server
		# 	where the user is, and play it to them. specifying user only works for mods.

		# 	'''
		# 	# print('checking')
		# 	# print(await ctx.invoke(self.perm_to_join_to_user))
		# 	server = ctx.message.server
		# 	mod_role = settings.get_server_mod(server)
		# 	admin_role = settings.get_server_admin(server)
		# 	mod_or_admin = False
		# 	roles = list(map(lambda x: x.name, ctx.message.author.roles))
		# 	mod_or_admin = admin_role in roles or mod_role in roles or checks.is_owner_check(ctx)
		# 	if user == None or not mod_or_admin:
		# 		user = ctx.message.author
		# 	filenames = []
		# 	if filename == None:
		# 		await self.bot.say("You must specify a filename to play")
		# 		return
		# 	if '/' in filename:
		# 		filenames = filename.split('/')
		# 	else:
		# 		filenames = [filename]
		# 	for name in filenames:
		# 		if name + self.exten not in os.listdir(AUDIOPATH) and name + self.exten not in os.listdir(TTSPATH):
		# 			await self.bot.say("The file, `{}` is not saved in the audio folder.".format(name+self.exten))
		# 			return
		# 	try:
		# 		client = await self.connect_with_user(ctx,user)
		# 	except UserNotConnected as e:
		# 		await self.bot.say(e.msg)
		# 		return
		# 	filenames = list(map(lambda filename:os.path.join(AUDIOPATH if filename +self.exten in os.listdir(AUDIOPATH) else TTSPATH, filename + self.exten), filenames))
		# 	try:
		# 		times = int(times)
		# 	except:
		# 		times = 1
		# 	if times>5:
		# 		times=5
		# 	elif times<1:
		# 		times=1
		# 	self.is_playing = dataIO.load_json(SETTINGS_JSON)['playing']
		# 	if self.is_playing:
		# 		await self.bot.say("You may not play anything if it is already playing something.")
		# 		return

		# 	self.set_play(True)
		# 	dataIO.save_json(SETTINGS_JSON, self.settings)
		# 	n = 0
		# 	if times==1:
		# 		for name in filenames:
		# 			if n>0:
		# 				while player.is_playing():
		# 					await asyncio.sleep(.2)
		# 			player = client.create_ffmpeg_player(name)
		# 			player.start()
		# 			n += 1
		# 	else:
				
		# 		for x in range(times):
		# 			for name in filenames:
		# 				if n>0:
		# 					while player.is_playing():
		# 						await asyncio.sleep(.2)
		# 				player = client.create_ffmpeg_player(name)
		# 				player.start()
		# 				n += 1

		# 	while player.is_playing():
		# 		await asyncio.sleep(.2)
		# 	self.set_play(False)
		# 	print(self.is_playing)
		
		@commands.command(pass_context=True)
		async def tts(self, ctx, *, args):
			user = ctx.message.author
			try:
				client = await self.connect_with_user(ctx,user)
			except UserNotConnected as e:
				await self.bot.say(e.msg)
				return
			if len(args)>20:
				filename = args[:20]
			else:
				filename = args
			filename = filename + self.exten
			filename = os.path.join(TTSPATH, filename)
			tts = gTTS(text=args, lang="en")
			tts.save(filename)
			self.set_play(False)
			player = client.create_ffmpeg_player(filename)
			player.start()
			self.set_play(True)



def check_folder():
	if not os.path.exists(PATH):
		os.makedirs(PATH)
	if not os.path.exists(IMAGEPATH):
		os.makedirs(AUDIOPATH)
	if not os.path.exists(VIDEOPATH):
		os.makedirs(VIDEOPATH)
def check_file():
	defaults = {}
	if not dataIO.is_valid_json(SETTINGS_JSON):
		dataIO.save_json(SETTINGS_JSON, defaults)

def setup(bot):
	check_folder()
	check_file()
	r = Images(bot)
	bot.add_cog(r)