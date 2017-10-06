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
	import math
	from cogs.utils import attempt6
	# from ffmpy import subprocess
	# try:
	#     imageio.plugins.ffmpeg.download()
	# except Exception as e:
	#     print(e)
	#     print(dir(e))
	# input()
	PATH = os.path.join('data', 'makegif')
	SETTINGS_JSON = os.path.join(PATH, 'settings.json')
	PICPATH = os.path.join(PATH, 'png')
	GIFPATH = os.path.join(PATH, 'gif')
	# class UserNotConnected(Exception):
	# 	def __init__(self):
	# 		self.msg = "User is not in a voice channel of this server."
	# class ChannelNotPrivate(Exception):
	# 	def __init__(self):
	# 		self.msg = "This command only works in dm or group."
	def checkmath(exp):
		letters = []
		current_letters = ''
		for x in exp:
			print(x)
			if x.isalpha():
				print(' ', x)
				current_letters += x
			else:
				print('woah', x)
				if current_letters != '':
					print('penis')
					letters.append(current_letters)
				current_letters = ''
		if current_letters != '':
			letters.append(current_letters)
		return letters


	class MakeGif:
		"""Display RACF specifc info.

		Note: RACF specific plugin for Red
		"""

		def set_draw(self, boolean):
			self.is_drawing = boolean
			self.settings = dataIO.load_json(SETTINGS_JSON)
			self.settings['drawing'] = self.is_drawing
			dataIO.save_json(SETTINGS_JSON, self.settings)

		def __init__(self, bot):
			"""Constructor."""
			self.bot = bot
			self.is_drawing = False
			self.settings = dataIO.load_json(SETTINGS_JSON)
			self.imagewidth = 200
			self.imageheight = 200

		def center2coords(self,center,size): #graph is x=[-1,1], y=[-1,1]
			center = (center[0]*self.imagewidth/2,center[1]*self.imageheight/2)
			center = (center[0]+self.imagewidth/2,-center[1]+self.imageheight/2) #pretend center of image is (0,0)
			xy1 = (center[0]-size[0]/2,center[1]-size[1]/2)
			xy2 = (xy1[0]+size[0],xy1[1]+size[1])
			return [xy1, xy2]

		@checks.is_owner()
		@commands.command(pass_context=True)
		async def makegif(self,ctx, *, args:str=''):
			things = checkmath('sin(t)**2')
			print(things)
			return
			args = args.split(' ')
			while '' in args:
				args.remove('')
			string2var = {
				'shape=':'shape',
				'fps=':'fps',
				'interval=':'interval',
				'imagesize=':'imagesize',
				'shapesize=':'shapesize',
			}
			options = {
				'shape':'rectangle',
				'fps':30,
				'interval':[0,2*math.pi,math.pi/64],
				'imagesize':[200,200],
				'shapesize':[40,40],
			}
			for x in args:
				for s in string2var:
					if x.startswith(s):
						options[string2var[s]] = x.replace(s,'')

			print(options)
			return

			shape = options['shape']
			fps = int(options['fps'])
			interval = options['interval']
			shapewidth = options['shapesize'][0]
			shapeheight = options['shapesize'][1]
			if self.is_drawing:
				await self.bot.say("May only make one gif at a time.")
				return
			self.set_draw(True)
			# c = (100,100)
			# s = (200,200)
			# print(c,s)
			# xy1, xy2 = self.center2coords(c,s)
			# print(xy1, xy2)
			ALLIMAGES = []
			#delete all pngs in the data dir
			try:
				filelist = [ f for f in os.listdir("data") if f.endswith(".png") ]
				for f in filelist:
					os.remove(os.path.join(PICPATH,f))
			except Exception as e:
				print(e)
			numframes = 0
			t = interval[0]
			while t < interval[1]:
				IMAGE = os.path.join(PICPATH, 'image{0:04d}.png'.format(numframes))
				ALLIMAGES.append(IMAGE)
				# IMAGE = 'data/image.png'
				img = Image.new('RGB', (self.imagewidth, self.imageheight))
				draw = ImageDraw.Draw(img, mode='RGB')
				#background
				getattr(draw, shape)([(0,0),(self.imagewidth,self.imageheight)],fill=(255,255,255)) 
				#shape
				# print(self.center2coords((t,shapeheight/2),(shapewidth,shapeheight)))
				#equation
				center = (t,0)
				# center = (0,0)
				size = (shapewidth,shapeheight)
				print(self.center2coords(center,size))
				draw.ellipse(self.center2coords(center,size), fill = (0,192,255))
				img.save(IMAGE, "png")
				numframes += 1
				t += interval[2]

			gif_name = 'ellipses'
			file_list = []
			for f in os.listdir(PICPATH):
				file_list.append(os.path.join(PICPATH,f))
			# list.sort(file_list, key=lambda x: int(x.split('_')[1].split('.png')[0])) # Sort the images by #, this may need to be tweaked for your use case
			clip = mpy.ImageSequenceClip(file_list, fps=fps)
			gifname = os.path.join(GIFPATH, '{}.gif'.format(gif_name))
			clip.write_gif(gifname, fps=fps)
			with open(gifname, 'rb') as f:
				await self.bot.send_file(ctx.message.channel, f)
			self.set_draw(False)

	def check_folder():
		if not os.path.exists(PATH):
			os.makedirs(PATH)
		if not os.path.exists(GIFPATH):
			os.makedirs(GIFPATH)
		if not os.path.exists(PICPATH):
			os.makedirs(PICPATH)

	def check_file():
		defaults = {'drawing' : False}
		if not dataIO.is_valid_json(SETTINGS_JSON):
			dataIO.save_json(SETTINGS_JSON, defaults)

	def setup(bot):
		check_folder()
		check_file()
		r = MakeGif(bot)
		bot.add_cog(r)