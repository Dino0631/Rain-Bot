"""
The MIT License (MIT)
Copyright (c) 2017 Dino
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
from .utils import checks
from .utils.dataIO import dataIO
from __main__ import send_cmd_help
from __main__ import send_cmd_help, settings
from bs4 import BeautifulSoup
from cogs.utils import checks
from cogs.utils.chat_formatting import escape_mass_mentions, box, pagify
from collections import deque, defaultdict
from datetime import datetime
from discord.ext import commands
from operator import itemgetter
import aiohttp
import asyncio
import discord
import inspect
import json
import locale
import logging
import os
import re
import requests
import time
import urllib
import urllib.request

class JapGobs:

	def __init__(self, bot):
		self.bot = bot
		def my_decorator(some_function):

			async def wrapper(*args, **kwargs):

				await some_function(*args, **kwargs)

				# print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')
				# print(type(args), kwargs)
				japgobchan = ['332647412969766912']
				message = args[0]
				if message.author.id != self.bot.user.id:
					if message.channel.id in japgobchan:
						await self.bot.send_message(message.channel, '👺')

			return wrapper
		# 	#loads some CRTags atttributes when bot is ready, otherwise it cant get servers/emojis
		self.bot.on_message = my_decorator(self.bot.on_message) #adds the above code to on_ready
		




def setup(bot):
	bot.add_cog(JapGobs(bot))