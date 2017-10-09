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
	import shutil
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
	IMGPATH = os.path.join(PATH, 'imgs')
	FONTPATH = ''
	if sys.platform == 'win32':
		FONTPATH = os.path.join('C:\\', 'Windows', 'Fonts')
	else:
		FONTPATH = PATH
	# class UserNotConnected(Exception):
	# 	def __init__(self):
	# 		self.msg = "User is not in a voice channel of this server."
	# class ChannelNotPrivate(Exception):
	# 	def __init__(self):
	# 		self.msg = "This command only works in dm or group."
	mathchars = {
		'^':'**',
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
	def convert2math(exp, variables=['t']):
		bad = ['shutil', 'os', 'sys']
		for i in bad:
			if i in exp:
				raise NotMathCode("Don't try to be malicious, it not nice... {}".format(i))
		for v in variables:
			if len(v) == 1 and v not in mathcodes:
				mathcodes[v] = v
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

		def coords2math(self, xy, imagesize):
			xy = (xy[0]-imagesize[0]/2,xy[1]-imagesize[1]/2)
			xy = (xy[0]/(imagesize[0]/2), -xy[1]/(imagesize[1]/2))
			return xy

		@checks.is_owner()
		@commands.command(pass_context=True)
		async def makegradient(self,ctx, *, args:str=''):
			string2var = {
				'c=':'color',
				'c1=':'color1',
				'size=':'imagesize',
			}
			options = {
				'imagesize':'(200,200)',
				'color':'(0,0,0)',
				'color1':'(0,192,255)',
			}
			args = args.split(' ')
			opts = []
			n = 0
			for arg in args:
				hasopt = False
				for s in string2var:
					if arg.startswith(s):
						hasopt = True
				# print(arg, hasopt)
				if hasopt:
					opts.append(arg)
				elif len(opts)>0:
					opts[len(opts)-1] += " {}".format(arg)

				n += 1
			# print(opts)
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

			# print(options)
			# return
			# print(options['shape'])
			color = options['color']
			color1 = options['color1']
			imagesize = options['imagesize']
			imagesize = imagesize.replace('(','').replace(')','').split(',')
			try:
				color, words = convert2math(color, [])
				color = eval(color)
			except NotMathCode as e:
				await self.bot.say(e.msg)
				return
			try:
				color1, words = convert2math(color1, [])
				color1 = eval(color1)
			except NotMathCode as e:
				await self.bot.say(e.msg)
				return

			try:
				imagesize, words = convert2math(imagesize, [])
				imagesize = inttuple(imagesize)
			except NotMathCode as e:
				await self.bot.say(e.msg)
				return
			lastimg = None
			try:
				filelist = [ f for f in os.listdir(IMGPATH) ]
			except Exception as e:
				print(e)
			if len(filelist) >0:
				lastimg = filelist[len(filelist)-1]
			# print(filelist)
			if lastimg is not None:
				currentfolder = 'image{0:03d}'.format(int(lastimg.replace('image',''))+1)
			else:
				currentfolder = 'image000'
			# print(currentfolder)
			currentfolder = os.path.join(IMGPATH, currentfolder)
			# print(currentfolder)
			os.mkdir(currentfolder)
			# print(imagesize)
			# print(color)
			deltacolors = []
			colors = [color, color1]
			n = 0
			for c in colors[0]:
				deltacolors.append((colors[1][n]-colors[0][n])/imagesize[0])
				n += 1
			IMAGE = os.path.join(currentfolder, 'image.png')
			maxx = int(imagesize[0]/2)
			maxy = int(imagesize[1]/2)
			img = Image.new('RGB', (imagesize[0], imagesize[1]))
			for xpos in range(-maxx,maxx):
				for ypos in range(-maxy,maxy):
					draw = ImageDraw.Draw(img, mode='RGB')
					# draw.rectangle([(xpos,ypos),(xpos,ypos)], fill=inttuple(eval(color)))
					coords = self.coords2math((xpos,ypos),(imagesize[0],imagesize[1]))
					coords2 = (xpos/imagesize[0]*255, ypos/imagesize[1]*255)
					x = coords2[0]
					y = coords2[1]
					
					gradient = ((xpos+maxx))
					currentcolors = []
					n = 0
					for c in colors[0]:
						# print(c,gradient,deltacolors[n])
						# print(c+gradient*deltacolors[n])
						currentcolors.append( sqrt(255*(c+gradient*deltacolors[n])) )
						n += 1
					# currentcolors = (sqrt(255*(colors[0][1]+gradient*r)), sqrt(255*(sg+gradient*g)), sqrt(255*(sb+gradient*b)))
					# fill(currentcolors[0], currentcolors[1],currentcolors[2])
					rect = [(xpos+maxx,ypos+maxy),(xpos+maxx,ypos+maxy)]
					draw.rectangle(rect, fill=inttuple(inttuple(currentcolors)))
					# print(coords, coords2)
				# print(inttuple(currentcolors))
			# except Exception as e:
			# 	print(e, dir(e))
			img.save(IMAGE, "png")

			with open(IMAGE, 'rb') as f:
				await self.bot.send_file(ctx.message.channel, f)
			shutil.rmtree(currentfolder)

		@checks.is_owner()
		@commands.command(pass_context=True)
		async def makeimg(self,ctx, *, args:str=''):
			string2var = {
				'color=':'color',
				'size=':'imagesize',
			}
			options = {
				'imagesize':'(200,200)',
				'color':'(0,192,255)',
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
				elif len(opts)>0:
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
			# return
			# print(options['shape'])
			color = options['color']
			imagesize = options['imagesize']
			imagesize = imagesize.replace('(','').replace(')','').split(',')
			try:
				color, words = convert2math(color, ['x','y'])
			except NotMathCode as e:
				await self.bot.say(e.msg)
				return
			try:
				imagesize, words = convert2math(imagesize, [])
				imagesize = inttuple(imagesize)
			except NotMathCode as e:
				await self.bot.say(e.msg)
				return
			lastimg = None
			try:
				filelist = [ f for f in os.listdir(IMGPATH) ]
			except Exception as e:
				print(e)
			if len(filelist) >0:
				lastimg = filelist[len(filelist)-1]
			print(filelist)
			if lastimg is not None:
				currentfolder = 'image{0:03d}'.format(int(lastimg.replace('image',''))+1)
			else:
				currentfolder = 'image000'
			print(currentfolder)
			currentfolder = os.path.join(IMGPATH, currentfolder)
			print(currentfolder)
			os.mkdir(currentfolder)
			print(imagesize)
			print(color)
			# try:
			IMAGE = os.path.join(currentfolder, 'image.png')
			img = Image.new('RGB', (imagesize[0], imagesize[1]))
			for xpos in range(imagesize[0]):
				for ypos in range(imagesize[1]):
					draw = ImageDraw.Draw(img, mode='RGB')
					# draw.rectangle([(xpos,ypos),(xpos,ypos)], fill=inttuple(eval(color)))
					coords = self.coords2math((xpos,ypos),(imagesize[0],imagesize[1]))

					coords2 = (xpos/imagesize[0]*255, ypos/imagesize[1]*255)
					x = coords[0]*255
					y = coords[1]*255
					rect = [(xpos,ypos),(xpos,ypos)]
					draw.rectangle(rect, fill=inttuple(eval(color)))
					# print(coords, coords2)
			# print('penis', self.coords2math((200,200),(200,200)))
			# except Exception as e:
			# 	print(e, dir(e))
			img.save(IMAGE, "png")

			with open(IMAGE, 'rb') as f:
				await self.bot.send_file(ctx.message.channel, f)
			shutil.rmtree(currentfolder)

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
				elif len(opts)>0:
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
				return
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
				return
			try:
				bgcolor, words = convert2math(bgcolor)
			except NotMathCode as e:
				await self.bot.say(e.msg)
				return
			try:
				shapecolor, words = convert2math(shapecolor)
			except NotMathCode as e:
				await self.bot.say(e.msg)
				return
			try:
				interval, words = convert2math(interval)
			except NotMathCode as e:
				await self.bot.say(e.msg)
				return
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
		if not os.path.exists(IMGPATH):
			os.makedirs(IMGPATH)

	def check_file():
		defaults = {'drawing' : False}
		if not dataIO.is_valid_json(SETTINGS_JSON):
			dataIO.save_json(SETTINGS_JSON, defaults)

	def setup(bot):
		check_folder()
		check_file()
		r = MakeGif(bot)
		bot.add_cog(r)