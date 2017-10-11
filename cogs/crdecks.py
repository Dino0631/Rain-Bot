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
from __main__ import send_cmd_help
import requests
import os
import time
import discord
from discord.ext import commands
import json
from bs4 import BeautifulSoup
import urllib
import urllib.request 
import asyncio
import aiohttp
from .utils.dataIO import dataIO
from cogs.utils import checks
import locale
class DeckError(Exception):
	def __init__(self, msg):
		self.msg = msg

aliases = {
    'archers': 'archers',
    'arch': 'archers',
    'arrows': 'arrows',
    'arrow': 'arrows',
    'arr': 'arrows',
    'baby-dragon': 'babydragon',
    'bbd': 'babydragon',
    'babyd': 'babydragon',
    'bd': 'babydragon',
    'babydragon': 'babydragon',
    'balloon': 'balloon',
    'loon': 'balloon',
    'bandit': 'bandit',
    'barbarian-hut': 'barbarianhut',
    'barb-hut': 'barbarianhut',
    'bh': 'barbarianhut',
    'barbarianhut': 'barbarianhut',
    'barbarians': 'barbarians',
    'barb': 'barbarians',
    'barbs': 'barbarians',
    'bats': 'bats',
    'bat': 'bats',
    'battle-ram': 'battleram',
    'br': 'battleram',
    'ram': 'battleram',
    'battleram': 'battleram',
    'bomb-tower': 'bombtower',
    'bt': 'bombtower',
    'bombtower': 'bombtower',
    'bomber': 'bomber',
    'bowler': 'bowler',
    'cannon': 'cannon',
    'cannon-cart': 'cannoncart',
    'cc': 'cannoncart',
    'cart': 'cannoncart',
    'cannoncart': 'cannoncart',
    'clone': 'clone',
    'dark-prince': 'darkprince',
    'dp': 'darkprince',
    'dank-prince': 'darkprince',
    'darkprince': 'darkprince',
    'dart-goblin': 'dartgoblin',
    'dg': 'dartgoblin',
    'dart-gob': 'dartgoblin',
    'dart-gobs': 'dartgoblin',
    'dartgoblin': 'dartgoblin',
    'electro-wizard': 'electrowizard',
    'ew': 'electrowizard',
    'ewiz': 'electrowizard',
    'ewizard': 'electrowizard',
    'electrowizard': 'electrowizard',
    'elite-barbarians': 'elitebarbarians',
    'eb': 'elitebarbarians',
    'ebarb': 'elitebarbarians',
    'ebarbs': 'elitebarbarians',
    'elitebarbarians': 'elitebarbarians',
    'elixir-collector': 'elixircollector',
    'ec': 'elixircollector',
    'pump': 'elixircollector',
    'collector': 'elixircollector',
    'elixircollector': 'elixircollector',
    'executioner': 'executioner',
    'ex': 'executioner',
    'exe': 'executioner',
    'exec': 'executioner',
    'fire-spirits': 'firespirits',
    'fs': 'firespirits',
    'firespirits': 'firespirits',
    'fireball': 'fireball',
    'fb': 'fireball',
    'flying-machine': 'flyingmachine',
    'fm': 'flyingmachine',
    'fly': 'flyingmachine',
    'machine': 'flyingmachine',
    'flyingmachine': 'flyingmachine',
    'freeze': 'freeze',
    'furnace': 'furnace',
    'giant-skeleton': 'giantskeleton',
    'gs': 'giantskeleton',
    'giantskeleton': 'giantskeleton',
    'giant': 'giant',
    'goblin-barrel': 'goblinbarrel',
    'gb': 'goblinbarrel',
    'gob-barrel': 'goblinbarrel',
    'barrel': 'goblinbarrel',
    'goblinbarrel': 'goblinbarrel',
    'goblin-gang': 'goblingang',
    'gg': 'goblingang',
    'gob-gang': 'goblingang',
    'gang': 'goblingang',
    'goblingang': 'goblingang',
    'goblin-hut': 'goblinhut',
    'gob-hut': 'goblinhut',
    'gh': 'goblinhut',
    'goblinhut': 'goblinhut',
    'goblins': 'goblins',
    'gobs': 'goblins',
    'gob': 'goblins',
    'stab-gobs': 'goblins',
    'stab-gob': 'goblins',
    'golem': 'golem',
    'graveyard': 'graveyard',
    'gy': 'graveyard',
    'skillyard': 'graveyard',
    'guards': 'guards',
    'heal': 'heal',
    'hog-rider': 'hogrider',
    'hog': 'hogrider',
    'hogrider': 'hogrider',
    'ice-golem': 'icegolem',
    'ig': 'icegolem',
    'icegolem': 'icegolem',
    'ice-spirit': 'icespirit',
    'is': 'icespirit',
    'icespirit': 'icespirit',
    'ice-wizard': 'icewizard',
    'iw': 'icewizard',
    'ice-wiz': 'icewizard',
    'iwiz': 'icewizard',
    'icewizard': 'icewizard',
    'inferno-dragon': 'infernodragon',
    'id': 'infernodragon',
    'infernodragon': 'infernodragon',
    'inferno-tower': 'infernotower',
    'inferno': 'infernotower',
    'it': 'infernotower',
    'infernotower': 'infernotower',
    'knight': 'knight',
    'lava-hound': 'lavahound',
    'lava': 'lavahound',
    'lh': 'lavahound',
    'hound': 'lavahound',
    'lavahound': 'lavahound',
    'lightning': 'lightning',
    'lumberjack': 'lumberjack',
    'lj': 'lumberjack',
    'mega-knight': 'megaknight',
    'mk': 'megaknight',
    'mknight': 'megaknight',
    'megaknight': 'megaknight',
    'mega-minion': 'megaminion',
    'mm': 'megaminion',
    'meta-minion': 'megaminion',
    'mega': 'megaminion',
    'megaminion': 'megaminion',
    'miner': 'miner',
    'mini-pekka': 'minipekka',
    'minip': 'minipekka',
    'mini-p': 'minipekka',
    'mp': 'minipekka',
    'minipekka': 'minipekka',
    'minion-horde': 'minionhorde',
    'mh': 'minionhorde',
    'horde': 'minionhorde',
    'minionhorde': 'minionhorde',
    'minions': 'minions',
    'mirror': 'mirror',
    'mortar': 'mortar',
    'musketeer': 'musketeer',
    '1m': 'musketeer',
    'musk': 'musketeer',
    'night-witch': 'nightwitch',
    'nwitch': 'nightwitch',
    'nw': 'nightwitch',
    'nightwitch': 'nightwitch',
    'pekka': 'pekka',
    'poison': 'poison',
    'prince': 'prince',
    'princess': 'princess',
    'rage': 'rage',
    'rocket': 'rocket',
    'royal-giant': 'royalgiant',
    'rg': 'royalgiant',
    'rgg': 'royalgiant',
    'royalgiant': 'royalgiant',
    'skeleton-army': 'skeletonarmy',
    'skarmy': 'skeletonarmy',
    'sa': 'skeletonarmy',
    'skeletonarmy': 'skeletonarmy',
    'skeleton-barrel': 'skeletonbarrel',
    'sbarrel': 'skeletonbarrel',
    'sb': 'skeletonbarrel',
    'skeletonbarrel': 'skeletonbarrel',
    'skeletons': 'skeletons',
    'skele': 'skeletons',
    'skeles': 'skeletons',
    'sparky': 'sparky',
    'spear-goblins': 'speargoblins',
    'spear-gobs': 'speargoblins',
    'spear-gob': 'speargoblins',
    'sgobs': 'speargoblins',
    'sgob': 'speargoblins',
    'speargoblins': 'speargoblins',
    'tesla': 'tesla',
    'the-log': 'thelog',
    'log': 'thelog',
    'thelog': 'thelog',
    'three-musketeers': 'threemusketeers',
    '3m': 'threemusketeers',
    '3musk': 'threemusketeers',
    '3musks': 'threemusketeers',
    'threemusketeers': 'threemusketeers',
    'tombstone': 'tombstone',
    'ts': 'tombstone',
    'tornado': 'tornado',
    'nado': 'tornado',
    'valkyrie': 'valkyrie',
    'valk': 'valkyrie',
    'witch': 'witch',
    'wizard': 'wizard',
    'wiz': 'wizard',
    'xbow': 'xbow',
    'x-bow': 'xbow',
    'zap': 'zap',
}
cards = [
	"archers",
	"arrows",
	"babydragon",
	"balloon",
	"bandit",
	"barbarianhut",
	"barbarians",
	"bats",
	"battleram",
	"bomber",
	"bombtower",
	"bowler",
	"cannon",
	"cannoncart",
	"clone",
	"darkprince",
	"dartgoblin",
	"electrowizard",
	"elitebarbarians",
	"elixircollector",
	"executioner",
	"fireball",
	"firespirits",
	"flyingmachine",
	"freeze",
	"furnace",
	"giant",
	"giantskeleton",
	"goblinbarrel",
	"goblingang",
	"goblinhut",
	"goblins",
	"golem",
	"graveyard",
	"guards",
	"heal",
	"hogrider",
	"icegolem",
	"icespirit",
	"icewizard",
	"infernodragon",
	"infernotower",
	"knight",
	"lavahound",
	"lightning",
	"lumberjack",
	"megaknight",
	"megaminion",
	"miner",
	"minionhorde",
	"minions",
	"minipekka",
	"mirror",
	"mortar",
	"musketeer",
	"nightwitch",
	"pekka",
	"poison",
	"prince",
	"princess",
	"rage",
	"rocket",
	"royalgiant",
	"skeletonarmy",
	"skeletonbarrel",
	"skeletons",
	"sparky",
	"speargoblins",
	"tesla",
	"thelog",
	"threemusketeers",
	"tombstone",
	"tornado",
	"valkyrie",
	"witch",
	"wizard",
	"xbow",
	"zap",
]
cardname2id = {
	"archers":'26000001',
	"arrows":'28000001',
	"babydragon":'26000015',
	"balloon":'26000006',
	"bandit":'26000046',
	"barbarianhut":'27000005',
	"barbarians":'26000008',
	"bats":'26000049',
	"battleram":'26000036',
	"bomber":'26000013',
	"bombtower":'27000004',
	"bowler":'26000034',
	"cannon":'27000000',
	"cannoncart":'26000054',
	"clone":'28000013',
	"darkprince":'26000027',
	"dartgoblin":'26000040',
	"electrowizard":'26000042',
	"elitebarbarians":'26000043',
	"elixircollector":'27000007',
	"executioner":'26000045',
	"fireball":'28000000',
	"firespirits":'26000031',
	"flyingmachine":'26000057',
	"freeze":'28000005',
	"furnace":'27000010',
	"giant":'26000003',
	"giantskeleton":'26000020',
	"goblinbarrel":'28000004',
	"goblingang":'26000041',
	"goblinhut":'27000001',
	"goblins":'26000002',
	"golem":'26000009',
	"graveyard":'28000010',
	"guards":'26000025',
	"heal":'28000016',
	"hogrider":'26000021',
	"icegolem":'26000038',
	"icespirit":'26000030',
	"icewizard":'26000023',
	"infernodragon":'27000003',
	"infernotower":'26000037',
	"knight":'26000000',
	"lavahound":'26000029',
	"lightning":'28000007',
	"lumberjack":'26000035',
	"megaknight":'26000055',
	"megaminion":'26000039',
	"miner":'26000032',
	"minionhorde":'26000022',
	"minions":'26000005',
	"minipekka":'26000018',
	"mirror":'28000006',
	"mortar":'27000002',
	"musketeer":'26000014',
	"nightwitch":'26000048',
	"pekka":'26000004',
	"poison":'28000009',
	"prince":'26000016',
	"princess":'26000026',
	"rage":'28000002',
	"rocket":'28000003',
	"royalgiant":'26000024',
	"skeletonarmy":'26000012',
	"skeletonbarrel":'',
	"skeletons":'26000010',
	"sparky":'26000033',
	"speargoblins":'26000019',
	"tesla":'27000006',
	"thelog":'28000011',
	"threemusketeers":'26000028',
	"tombstone":'27000009',
	"tornado":'28000012',
	"valkyrie":'26000011',
	"witch":'26000007',
	"wizard":'26000017',
	"xbow":'27000008',
	"zap":'28000008',
}
globalkey = 'global'
PATH = os.path.join('data', 'crdecks')
DECKS_JSON = os.path.join(PATH, 'decks.json')
MAXDECKS = 20
defaultdeckname = 'deck'
deckurl = 'https://link.clashroyale.com/deck/en?deck='
class CRDecks:
	"""docstring for CRDecks"""
	def __init__(self, bot):
		self.bot = bot
		self.saved_decks = self.get_decks()

	def get_decks(self):
		return dataIO.load_json(DECKS_JSON)

	def save_decks(self):
		dataIO.save_json(DECKS_JSON, self.saved_decks)


	@commands.group(pass_context=True)
	async def deck(self, ctx):
		if ctx.invoked_subcommand is None:
			await send_cmd_help(ctx)

	@checks.is_owner()
	@deck.command(pass_context=True)
	async def addglobal(self, ctx, *,cardsandname):
		user = globalkey
		try:
			cards, name = self.args2deckandname(cardsandname, user)
		except DeckError as e:
			await self.bot.say(e.msg)
			return

		if user not in self.saved_decks: #makes blank dict if you have nothing saved
			self.saved_decks[user] = {}
		if name in self.saved_decks[user]: #cant overwrite deck
			await self.bot.say("{} is already a name of one of your saved decks.".format(name))
			return
		self.saved_decks[user][name] = cards
		self.save_decks()
		await self.bot.say("Deck added to global decks.")

	@checks.is_owner()
	@deck.command(aliases=['rmglobal', 'delglobal'],pass_context=True)
	async def removeglobal(self, ctx, *,name):
		self.saved_decks = self.get_decks()
		user = globalkey
		if user not in self.saved_decks:
			await self.bot.say("No tags set for {}".format(user))
			return
		if name not in self.saved_decks[user]:
			await self.bot.say("No deck named \"{}\" for {}".format(name,user))
			return
		del self.saved_decks[name]
		self.save_decks()

	@deck.command(aliases=['rm', 'del'],pass_context=True)
	async def remove(self, ctx, *,name):
		try:
			self.remove_deck(name, ctx.message.author.id)
		except DeckError as e:
			await self.bot.say(e.msg)

	@deck.command(pass_context=True)
	async def add(self, ctx, *,cardsandname):
		user = ctx.message.author.id
		try:
			cards, name = self.args2deckandname(cardsandname, user)
		except DeckError as e:
			await self.bot.say(e.msg)
			return

		if user not in self.saved_decks: #makes blank dict if you have nothing saved
			self.saved_decks[user] = {}
		if name in self.saved_decks[user]: #cant overwrite deck
			await self.bot.say("{} is already a name of one of your saved decks.".format(name))
			return
		if len(self.saved_decks[user])>=MAXDECKS: #cant have >MAXDECKS decks
			await self.bot.say("You already have {} decks saved.".format(MAXDECKS))
			return
		self.saved_decks[user][name] = cards
		self.save_decks()
		await self.bot.say("Deck added to your decks.")

	@deck.command(name='get',pass_context=True)
	async def deck_get(self,ctx,*,cards):
		try:
			cards = self.args2deck(cards, ctx.message.author.id)
		except DeckError as e:
			await self.bot.say(e.msg)
		url = self.deck2url(cards)
		embed = discord.Embed(title=', '.join(cards), url=url)
		await self.bot.say(embed=embed)
		

	@deck.command(name='link',pass_context=True)
	async def deck_link(self,ctx,*,cards):
		user = ctx.message.author.id
		try:
			cards = self.args2deck(cards, ctx.message.author.id)
		except DeckError as e:
			await self.bot.say(e.msg)
		url = self.deck2url(cards)
		embed = discord.Embed(title=', '.join(cards), url=url)
		await self.bot.say(embed=embed)

	def deck2url(self, deck):
		cardids = list(map(lambda x: cardname2id[x], deck))
		url = deckurl + ';'.join(cardids)
		return(url)

	def args2deck(self, cards, user):
		self.saved_decks = self.get_decks()
		if globalkey in self.saved_decks:
			decks = {**self.saved_decks[user],**self.saved_decks[globalkey]}
		else:
			decks = self.saved_decks[user]

		if cards.lower().strip() in decks: #if name of saved deck
			cards = decks[cards]
		else:
			cards = cards.strip().lower().split()
		try:
			cards = list(map(lambda x:aliases[x], cards))
		except KeyError as e:
			raise DeckError("{} is not a recognized alias or card name".format(str(e)))
		return cards

	def args2deckandname(self, cardsandname, user):
		self.saved_decks = self.get_decks()
		cardsandname = cardsandname.split()
		if len(cardsandname)<8:
			raise DeckError("Must include at least 8 cards for a deck")
		elif len(cardsandname)<9:
			try:
				decknum = len(self.saved_decks[user])+1
			except KeyError:
				decknum = 1
			name = "{} {}".format(defaultdeckname,decknum)
		else:
			name = cardsandname[8:] #last args is name
		cards = cardsandname[:8] #first 8 are cards
		name = ' '.join(name).lower()
		if len(name)>32:
			raise DeckError("Name of deck must not be more than 32 chars (spaces included)")
		try:
			cards = list(map(lambda x:aliases[x], cards))
		except KeyError as e:
			raise DeckError("{} is not a recognized alias or card name".format(str(e)))
		return cards, name

	def remove_deck(self, deckname, user):
		self.saved_decks = self.get_decks()
		if user not in self.saved_decks:
			raise DeckError("No tags set for {}".format(user))
		if deckname not in self.saved_decks[user]:
			raise DeckError("No deck named \"{}\" for {}".format(deckname,user))
		del self.saved_decks[user][deckname]
		self.save_decks()

		
def check_folder():
	if not os.path.exists(PATH):
		os.makedirs(PATH)

def check_file():
	defaults = {}
	if not dataIO.is_valid_json(DECKS_JSON):
		dataIO.save_json(DECKS_JSON, defaults)

def setup(bot):
	check_folder()
	check_file()
	bot.add_cog(CRDecks(bot))