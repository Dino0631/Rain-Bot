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
import discord
from discord.ext.commands import bot
from discord.ext import commands
import datetime
import time
import random
import asyncio
import json
import requests
import os
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
# try:
#     imageio.plugins.ffmpeg.download()
# except Exception as e:
#     print(e)
#     print(dir(e))
# input()
heroku = False
if 'DYNO_RAM' in os.environ:
	heroku = True
if heroku:
	from ctypes.util import find_library
	opuslib = find_library('opus')
	print(opuslib)
	print(type(opuslib))
	print(dir(opuslib))
	discord.opus.load_opus(find_library('opus'))
PATH = os.path.join('data', 'crsfx')
AUDIOPATH = os.path.join(PATH, 'mp3')
VIDEOPATH = os.path.join(PATH, 'mp4')
class UserNotConnected(Exception):
	def __init__(self):
		self.msg = "User is not in a voice channel of this server."

class CRSFX:
	"""Display RACF specifc info.

	Note: RACF specific plugin for Red
	"""

	def __init__(self, bot):
		"""Constructor."""
		self.bot = bot

	# async def on_ready(self):

	@checks.is_owner()
	@commands.command(pass_context=True)
	async def mp4s2mp3(self,ctx, option=None):
		for mp4 in os.listdir(VIDEOPATH):
			mp3 = mp4.replace('.mp4','.mp3')
			if option == 'overwrite':
				condition = True
			else:
				condition = mp3 not in os.listdir(AUDIOPATH)
			if condition:
				clip = mp.VideoFileClip(os.path.join(VIDEOPATH, mp4))
				clip.audio.write_audiofile(os.path.join(AUDIOPATH, mp3))

	async def get_voice_client(self, ctx):
		servclient = None
		for client in list(self.bot.voice_clients):
			if client.server == ctx.message.server:
				servclient = client
				break
		return servclient

	async def disconnect(self, ctx):
		client = await self.get_voice_client(ctx)
		if client is not None:
			await client.disconnect()

	async def connect_with_user(self, ctx, user=None):
		if user == None:
			user = ctx.message.author
		channel = user.voice_channel
		if channel is None:
			raise UserNotConnected()
		else:
			if self.bot.is_voice_connected(ctx.message.server):
				voiceclient = await self.get_voice_client(ctx)
				if voiceclient.channel != user.voice_channel:
					await voiceclient.move_to(user.channel)
			else:
				voiceclient = await self.bot.join_voice_channel(channel)
		return voiceclient

	async def playmp3(self, client, filename):
		player = client.create_ffmpeg_player(filename)
		player.start()
		print(dir(player))

	@checks.mod_or_permissions()
	@commands.group(name='crsfx',pass_context=True)
	async def crsfx(self, ctx):
		"""play sound effects
		"""
		if ctx.invoked_subcommand is None:
			await send_cmd_help(ctx)

	@crsfx.command(pass_context=True)
	async def test(self, ctx):
		print('hi')
		await self.bot.say(self.bot.is_voice_connected(ctx.message.server))
		for v in self.bot.voice_clients:
			await self.bot.say(v)

	@crsfx.command(pass_context=True)
	async def sfxdc(self, ctx):
		servclient = await self.get_voice_client(ctx)
		if servclient is not None:
			await servclient.disconnect()

	
	@commands.command(pass_context=True)
	async def crclip(self, ctx, filename=None, user:discord.User=None):
		if user == None:
			user = ctx.message.author
		exten = '.mp3'
		if filename == None:
			await self.bot.say("You must specify a filename to play")
			return
		elif filename + exten not in os.listdir(AUDIOPATH):
			await self.bot.say("That file is not saved in the audio folder.")
			return
		try:
			client = await self.connect_with_user(ctx,user)
		except UserNotConnected as e:
			await self.bot.say(e.msg)
			return
		
		filename = os.path.join(AUDIOPATH, filename + exten)
		player = client.create_ffmpeg_player(filename)
		player.start()
		# await asyncio.sleep(2)
		# await self.disconnect(ctx)
		

def setup(bot):
	r = CRSFX(bot)
	bot.add_cog(r)