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
	from PIL import Image, ImageDraw,ImageFont
	from __main__ import send_cmd_help, settings
	from bs4 import BeautifulSoup
	from cogs.utils import attempt6
	from cogs.utils import checks
	from cogs.utils.dataIO import dataIO
	from discord.ext import commands
	from discord.ext.commands import bot
	from math import *
	from urllib.parse import quote_plus
	import PIL
	import aiohttp
	import asyncio
	import datetime
	import discord
	import imageio
	import inspect
	import json
	import locale
	import moviepy.editor as mpy
	import os
	import random
	import requests
	import string
	import sys
	import time
	class NotMathCode(Exception):
		def __init__(self, word):
			self.msg = "{} is not in the math functions. If you think it should be added, dm <@{}>".format(word, settings.owner)
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
	FONTPATH = ''
	if sys.platform == 'win32':
		FONTPATH = os.path.join('C:\\', 'Windows', 'Fonts')
	# class UserNotConnected(Exception):
	# 	def __init__(self):
	# 		self.msg = "User is not in a voice channel of this server."
	# class ChannelNotPrivate(Exception):
	# 	def __init__(self):
	# 		self.msg = "This command only works in dm or group."
	mathchars = {
		'^':'**',
		't':'t'		#indep variable
	}
	mathcodes = {
		'abs':'abs',
		'sin':'sin',
		'cos':'cos',
		'tan':'tan',
		'pi':'pi',
		'e':'e',
		'sqrt':'sqrt',
		'sinh':'sinh',
		'cosh':'cosh',
		'tanh':'tanh',
		'floor':'floor',
		'ceiling':'ceil',
		'log':'log10',
		'ln':'log',
		'arcsin':'asin',
		'arccos':'acos',
		'arctan':'atan',
		'arcsinh':'asinh',
		'arccosh':'acosh',
		'arctanh':'atanh',

	}
	mathcodes = {**mathcodes, **mathchars}
	def convert2math(exp):
		words = []
		current_letters = ''
		for x in exp:
			# print(x)
			if x.isalpha():
				# print(' ', x)
				current_letters += x
			else:
				# print('woah', x)
				if current_letters != '':
					# print('penis')
					words.append(current_letters)
				current_letters = ''
		if current_letters != '':
			words.append(current_letters)
		for word in words:
			if word not in mathcodes:
				raise NotMathCode(word)
		for word in words:
			exp = exp.replace(word,mathcodes[word])
		return exp, words

	def inttuple(colors): #takes a tuple/list and converts all members to int and returns a tuple
		intcolors = []
		for c in colors:
			intcolors.append(int(c))
		return tuple(intcolors)

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
			self.smallestimagedim = self.imagewidth if self.imagewidth<self.imageheight else self.imageheight

		def center2coords(self,center,size): #graph is x=[-1,1], y=[-1,1]
			# print(self.imagewidth, self.imageheight)
			center = (center[0]*self.smallestimagedim/2,center[1]*self.smallestimagedim/2)
			center = (center[0]+self.imagewidth/2,-center[1]+self.imageheight/2) #pretend center of image is (0,0)
			xy1 = (center[0]-size[0]/2,center[1]-size[1]/2)
			xy2 = (xy1[0]+size[0],xy1[1]+size[1])
			return [xy1, xy2]

		@checks.is_owner()
		@commands.command(pass_context=True)
		async def makegif(self,ctx, *, args:str=''):
			self.set_draw(True)
			string2var = {
				'color=':'shapecolor',
				'bg=':'bgcolor',
				'shape=':'shape',
				'fps=':'fps',
				'interval=':'interval',
				'imagesize=':'imagesize',
				'shapesize=':'shapesize',
				'eq=':'equation',
				'path=':'path',
				'text=':'text',
			}
			options = {
				'shape':'rectangle',
				'fps':30,
				'equation':'(t,0)',
				'interval':'[0,2*pi,pi/64]',
				'imagesize':'(200,200)',
				'shapesize':'(40,40)',
				'shapecolor':'(0,192,255)',
				'bgcolor':'(255,255,255)',
				'path':'0',
				'text':None,
			}
			args = args.split(' ')
			opts = []
			n = 0
			for arg in args:
				hasopt = False
				for s in string2var:
					if arg.startswith(s):
						hasopt = True
				print(arg, hasopt)
				if hasopt:
					opts.append(arg)
				else:
					opts[len(opts)-1] += " {}".format(arg)

				n += 1
			print(opts)
			args = opts
			# args = args.split(' ')
			while '' in args:
				args.remove('')
			n = 0
			for x in args:
				for s in string2var:
					if x.startswith(s):
						options[string2var[s]] = x.replace(s,'')
				n += 1

			print(options)
			try:
				options['equation'], words = convert2math(options['equation'])
			except NotMathCode as e:
				await self.bot.say(e.msg)
			print(options['equation'])
			# return
			# print(options['shape'])
			bgcolor = options['bgcolor']
			shapesize = options['shapesize']
			shape = options['shape']
			shapecolor = options['shapecolor']
			fps = int(options['fps'])
			imagesize = options['imagesize']
			imagesize = imagesize.replace('(','').replace(')','').split(',') 
			self.imagewidth = int(imagesize[0])
			self.imageheight = int(imagesize[1])
			self.smallestimagedim = self.imagewidth if self.imagewidth<self.imageheight else self.imageheight
			interval = options['interval']
			equation = options['equation']
			path = int(options['path'])
			text = options['text']
			try:
				shapesize, words = convert2math(shapesize)
			except NotMathCode as e:
				await self.bot.say(e.msg)
			try:
				bgcolor, words = convert2math(bgcolor)
			except NotMathCode as e:
				await self.bot.say(e.msg)
			try:
				shapecolor, words = convert2math(shapecolor)
			except NotMathCode as e:
				await self.bot.say(e.msg)
			try:
				interval, words = convert2math(interval)
			except NotMathCode as e:
				await self.bot.say(e.msg)
			if 't' in words:
				await self.bot.say('`t` must not be in the interval equation')
			interval = interval.replace('[','').replace(']','')
			interval = interval.split(',')
			realinterval = [0,0,1]
			for n in list(range(0,3)):
				print(interval[n],type(interval[n]))
				realinterval[n] = eval(interval[n])
				print(realinterval[n],type(realinterval[n]))
			interval = realinterval
			shapewidth = options['shapesize'][0]
			shapeheight = options['shapesize'][1]
			# if dataIO.load_json(SETTINGS_JSON)['drawing']:
			# 	await self.bot.say("May only make one gif at a time.")
			# 	return
			# c = (100,100)
			# s = (200,200)
			# print(c,s)
			# xy1, xy2 = self.center2coords(c,s)
			# print(xy1, xy2)
			ALLIMAGES = []
			#delete all pngs in the data dir
			try:
				filelist = [ f for f in os.listdir(PICPATH) if f.endswith(".png") ]
				for f in filelist:
					os.remove(os.path.join(PICPATH,f))
					# print('removing', os.path.join(PICPATH,f))
			except Exception as e:
				print(e)
			for f in os.listdir(FONTPATH):
				print(f)
			fontname = 'Supercell-magic-webfont'
			fontext = '.ttf'
			currentfont = os.path.join(FONTPATH, 'arial' + fontext)
			font = ImageFont.truetype(currentfont)
			numframes = 0
			t = interval[0]
			while t < interval[1]:
				IMAGE = os.path.join(PICPATH, 'image{0:04d}.png'.format(numframes))
				ALLIMAGES.append(IMAGE)
				# IMAGE = 'data/image.png'
				img = Image.new('RGB', (self.imagewidth, self.imageheight))
				draw = ImageDraw.Draw(img, mode='RGB')
				#background
				print('shape',shape)
				draw.rectangle([(0,0),(self.imagewidth,self.imageheight)],fill=inttuple(eval(bgcolor))) 
				if path:
					current_t=t
					t = interval[0]
					while t < interval[1]:
						eq = options['equation']
						# n = 0
						# for l in eq:
						# 	try:
						# 		if l == 'a' and not eq[n-1].isalpha() and not eq[n+1].isalpha():
						# 			eq = eq[:n]+'a' + eq[n+1:]
						# 	except IndexError:
						# 		pass
						# 	n += 1
						# print(eq)
						center = eval(eq)
						size = (1,1)
						draw.rectangle(self.center2coords(center,size), fill = inttuple(eval(shapecolor)))

						t += interval[2]
					t = current_t
				#shape
				# print(self.center2coords((t,shapeheight/2),(shapewidth,shapeheight)))
				#equation
				# print(type(t))
				# print(options['equation'])
				center = eval(options['equation'])
				# print(t)
				# print(center)
				# center = (0,0)
				size = eval(shapesize)
				print(self.center2coords(center,size))
				if text is None:
					getattr(draw, shape)(self.center2coords(center,size), fill = inttuple(eval(shapecolor)))
				else:
					center = self.center2coords(center,(0,0))[0]
					draw.text(center, text, font=font, fill = inttuple(eval(shapecolor)), align='center')
				img.save(IMAGE, "png")
				numframes += 1
				t += interval[2]

			gif_name = shape + 's'
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