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
	from __main__ import send_cmd_help
	import string
	import aiohttp
	from urllib.parse import quote_plus
	import locale
	import inspect
	import imageio
	try:
		import moviepy.editor as mp
	except:
		imageio.plugins.ffmpeg.download()
		import moviepy.editor as mp
	from bs4 import BeautifulSoup
	import asyncio
	import aiohttp
	from cogs.utils.dataIO import dataIO
	from cogs.utils import checks
	import locale
	import moviepy.editor as mpy
	import sys
	import os
	import PIL
	from PIL import Image, ImageDraw
	# from ffmpy import subprocess
	# try:
	#     imageio.plugins.ffmpeg.download()
	# except Exception as e:
	#     print(e)
	#     print(dir(e))
	# input()
	PATH = os.path.join('data', 'makegif')
	PICPATH = os.path.join(PATH, 'png')
	GIFPATH = os.path.join(PATH, 'gif')
	# class UserNotConnected(Exception):
	# 	def __init__(self):
	# 		self.msg = "User is not in a voice channel of this server."
	class ChannelNotPrivate(Exception):
		def __init__(self):
			self.msg = "This command only works in dm or group."

	class MakeGif:
		"""Display RACF specifc info.

		Note: RACF specific plugin for Red
		"""

		def __init__(self, bot):
			"""Constructor."""
			self.bot = bot


		@checks.is_owner()
		@commands.command(pass_context=True)
		async def showgif(self,ctx, option=None):
			imagewidth = 500
			imageheight = 100
			ALLIMAGES = []
			shapewidth = 100
			#delete all pngs in the data dir
			try:
				filelist = [ f for f in os.listdir("data") if f.endswith(".png") ]
				for f in filelist:
					os.remove(os.path.join(PICPATH,f))
			except Exception as e:
				print(e)
			for n in range(-shapewidth,imagewidth, 10):
				IMAGE = os.path.join(PICPATH, 'image{0:04d}.png'.format(n+shapewidth))
				ALLIMAGES.append(IMAGE)
				# IMAGE = 'data/image.png'
				try:
					img = Image.open(IMAGE)
				except FileNotFoundError:
					img = Image.new('RGB', (imagewidth, imageheight))
				draw = ImageDraw.Draw(img, mode='RGB')
				#background
				draw.rectangle([(0,0),(imagewidth,imageheight)],fill=(255,255,255)) 
				#shape
				draw.ellipse([(n,0),(n+shapewidth,imageheight)], fill = (0,192,255))
				img.save(IMAGE, "png")

			gif_name = 'ellipses'
			fps = 30
			file_list = []
			for f in os.listdir(PICPATH):
				file_list.append(os.path.join(PICPATH,f))
			# list.sort(file_list, key=lambda x: int(x.split('_')[1].split('.png')[0])) # Sort the images by #, this may need to be tweaked for your use case
			clip = mpy.ImageSequenceClip(file_list, fps=fps)
			gifname = os.path.join(GIFPATH, '{}.gif'.format(gif_name))
			clip.write_gif(gifname, fps=fps)
			with open(gifname, 'rb') as f:
				await self.bot.send_file(ctx.message.channel, f)

	def check_folder():
		if not os.path.exists(PATH):
			os.makedirs(PATH)
		if not os.path.exists(GIFPATH):
			os.makedirs(GIFPATH)
		if not os.path.exists(PICPATH):
			os.makedirs(PICPATH)

	def check_file():
		pass

	def setup(bot):
		check_folder()
		check_file()
		r = MakeGif(bot)
		bot.add_cog(r)