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
import itertools
import discord
from discord.ext import commands
from discord.ext.commands import Context
import cogs
from cogs.utils.chat_formatting import pagify
from cogs.utils import checks
from random import choice
import aiohttp
from __main__ import send_cmd_help
import os
from cogs.utils.dataIO import dataIO

PATH = os.path.join('data', 'welcome')
WELCOMEJSON = os.path.join(PATH, 'settings.json')
NOBPATH = os.path.join('data', 'nob')
NOBJSON = os.path.join(NOBPATH, 'setting.json')
class Welcome:
	"""Display pecifc info.

	Note:  specific plugin for Red
	"""

	def __init__(self, bot):
		"""Constructor."""
		self.bot = bot
		self.settings = dataIO.load_json(WELCOMEJSON)
		self.nobdict = dataIO.load_json(NOBJSON)

	@checks.mod_or_permissions()
	@commands.group(aliases=['wel'],pass_context=True)
	async def welcome(self, ctx):

		if ctx.invoked_subcommand is None:
			await send_cmd_help(ctx)

			
	@welcome.command(aliases=['chan'], pass_context=True)
	async def setchan(self, ctx, channel:discord.Channel=None, *, welmsg:str=r'"Welcome to "+server.name+", "+member.name+"!"'):
		server = ctx.message.server
		if channel == None:
			channel = ctx.message.channel
		try:
			test  = self.settings[server.id]
		except KeyError:
			self.settings[server.id] = {}
		self.settings[server.id]['channel'] = channel.id
		self.settings[server.id]['message'] = welmsg
		dataIO.save_json(WELCOMEJSON, self.settings)
		await self.bot.say('Set welcome channel to: {}'.format
		
		
	@welcome.command(aliases=['msg'], pass_context=True)
	async def setmessage(self, ctx, *, message):
		'''write `server` to imply the server name and
		 `member` to imply the member being welcomed'''
		server = ctx.message.server
		channel = ctx.message.channel
		print(self.settings)
		message = '\"' + message + '\"'
		message = message.replace('`server`', r'"+server.name+"').replace('`member`', r'"+member.name+"')
		self.settings[server.id]['message'] = message
		dataIO.save_json(WELCOMEJSON, self.settings)
		await self.bot.say('Set welcome msg to: ```{}```'.format(message))


	@welcome.command(aliases=['del'], pass_context=True)
	async def delserv(self, ctx):
		server = ctx.message.server
		self.settings.pop(server.id, None)
		dataIO.save_json(WELCOMEJSON, self.settings)
		await self.bot.say('Deleted welcome channel settings for this server')

	@checks.is_owner()
	@welcome.command(pass_context=True)
	async def sendjson(self, ctx):
		heroku = False
		if 'DYNO_RAM' in os.environ:
			heroku = True
		if heroku:
			await self.bot.send_file(destination=ctx.message.channel, fp=r"/app/data/welcome/settings.json", filename="welcome.json")
		else:
			await self.bot.send_file(destination=ctx.message.channel, fp=r"data\welcome\settings.json", filename="welcome.json")

		
		

def check_folder():
	if not os.path.exists(PATH):
		os.makedirs(PATH)

def check_file():
	defaults = {}
	if not dataIO.is_valid_json(WELCOMEJSON):
		dataIO.save_json(WELCOMEJSON, defaults)

def setup(bot):
	check_folder()
	check_file()
	r = Welcome(bot)
	bot.add_cog(r)
