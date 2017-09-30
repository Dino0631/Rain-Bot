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
from operator import itemgetter

import inspect
cremojis = {}
cremojilist = []
refreshemoji = '🔄'
onetofour = ['one', 'two','three', 'four']
racfclans = {
	"ALPHA" : "2CCCP",
	"BRAVO" : "2U2GGQJ",
	"CHARLIE" : "2QUVVVP",
	"DELTA" : "Y8GYCGV",
	"ECHO" : "LGVV2CG",
	"ESPORTS" : "R8PPJQG",
	"FOXTROT" : "QUYCYV8",
	"GOLF" : "GUYGVJY",
	"HOTEL" : "UGQ28YU",
	"MINI" : "22LR8JJ2",
	"MINI2" : "2Q09VJC8"
}
racfclanslist = [
	"Alpha",
	"Bravo",
	"Charlie",
	"Delta",
	"Echo",
	"Foxtrot",
	"Golf",
	"Hotel",
	"Mini",
	"Mini2",
	"eSports"
]
BOTCMDER = ["Bot Commander"]
NUMITEMS = 9
statscr_url = "http://statsroyale.com/profile/"
crapiurl = 'http://api.cr-api.com'
crapi_url = 'http://cr-api.com'
statsurl = 'http://statsroyale.com'
PATH = os.path.join("data", "crtags")
SETTINGS_JSON = os.path.join(PATH, "settings.json")
BACKSETTINGS_JSON = os.path.join(PATH, "backsettings.json")
CLAN_JSON = os.path.join(PATH, "clan.json")
CREMOJIS_JSON = os.path.join(PATH, "cremojis.json")
SET_JSON = os.path.join(PATH, "set.json")
cremojis = dataIO.load_json(CREMOJIS_JSON)
validChars = ['0', '2', '8', '9', 'C', 'G', 'J', 'L', 'P', 'Q', 'R', 'U', 'V', 'Y']
tags = {}
headers = {
	'User-Agent': 'Bot(Rain), (https://github.com/Dino0631/discordbot/tree/master)',
	'From': 'htmldino@gmail.com'  
}
def api2emoji(cardname):
	return cardname.replace('_','')

async def async_refresh(url):
	async with aiohttp.get(url) as r:
		# response = await r.json()
		a = 1
		
class CRClan:

	def __init__(self):
		self.members = []                               #done
		self.sortedmembers = []                               #done
		self.tag = ''                             #done
		self._url = ''
		self.url = ''           #done
		self.tr_req = '0'                               #done
		self.clan_trophy = ''                           #done
		self.name = ''                                  #done
		self.donperweek = ''                            #done
		self.desc = ''                                  #done
		self.badge = ''                                 #done
		self.leader = {}                                #done
		self.sortedleader = {}
		self.size = 0                                   #done
		self.coleaders = []                             #done
		self.elders = []                                #done
		self.norole = []                                #done
		self.sortedcoleaders = []                               #done
		self.sortedelders = []                              #done
		self.sortednorole = []                              #done
		self.clan_badge = ''
		self.name = ''
		self.desc = ''
		self.desc2 = ''
		self.clan_trophy = ''
		self.tr_req = ''
		self.parsedtr_req = ''
		self.donperweek = ''
		self.badge = ''

	@classmethod
	async def create(self, tag):
		tag2id = dataIO.load_json(BACKSETTINGS_JSON)
		allemojis = dataIO.load_json(CREMOJIS_JSON)
		formatted = CRClan()
		self = CRClan()
		self.members = []                               #done
		self.sortedmembers = []                               #done
		formatted.members = []
		self.tag = tag                             #done
		formatted.tag = tag
		self._url = crapiurl + '/clan/' + tag           #done
		formatted._url = crapiurl + '/clan/' + tag
		self.url = crapi_url + '/clan/' + tag           #done
		formatted.url = crapi_url + '/clan/' + tag
		formatted.tag = "[{}]({})".format(formatted.tag,formatted.url)
		self.tr_req = '0'                               #done
		self.clan_trophy = ''                           #done
		self.name = ''                                  #done
		self.donperweek = ''                            #done
		self.desc = ''                                  #done
		self.badge = ''                                 #done
		self.leader = {}                                #done
		self.size = 0                                   #done
		self.coleaders = []                             #done
		self.sortedcoleaders = []                               #done
		formatted.coleaders = []
		self.elders = []                                #done
		self.sortedelders = []                               #done
		formatted.elders = []
		self.norole = []                                #done
		self.sortednorole = []                               #done
		formatted.norole = []
		self.parsedtr_req = ''
		formatted.parsedtr_req = ''
		# if clan_url != '':
		async with aiohttp.ClientSession() as session:
			async with session.get(self._url) as resp:
				# print(await resp.read())
				clandatadict = await resp.json()
		# print(clandatadict)
		# for x in clandatadict:
		#   try:
		#       print(x)
		#   except:
		#       print('some key')
		#   try:
		#       print(clandatadict[x])
		#   except:
		#       print('some value')
		# for member in clandatadict['members']:
		#   try:
		#       print(member)
		#   except:
		#       print('some member')
		# r = requests.get(self.clan_url, headers=headers)
		# html_doc = r.text
		formattedmembers = []
		members = []
		# print(clandatadict)
		# print(tag)
		# print("members in clandatadict?", 'members' in clandatadict)
		# for data in clandatadict:
		#   print('H{}H'.format(data))
		#   print(data == 'members')
		#   if data == 'members':
		#       members = clandatadict[data]
		#   # if type(clandatadict[data]) == type(1):
		#   #   clandatadict[data] = str(clandatadict[data])
		#   # print(data, ':', clandatadict[data])
		# print(len(members))
		i = 0
		for  m in clandatadict['members']:
			rank = str(m['currentRank'])
			name = str(m['name'])
			tag = str(m['tag']).upper()
			url = crapiurl +'/profile/'+ tag
			level = str(m['expLevel'])
			trophy = str(m['score'])
			donations = str(m['donations'])
			role = str(m['roleName'])
			if tag in tag2id:
				userid = tag2id[tag]
			else:
				userid = ''
			memberdict = {
				'name' : name.strip(),
				'rank' : rank.strip(),
				'tag' : tag.strip(),
				'userid': userid.strip(),
				'url' : url.strip(),
				'level' : level.strip(),
				'trophy' : trophy.strip(),
				'donations' : donations.strip(),
				'role' : role.strip()
			}
			memberdict['formatted'] = '`{}` {} [`{}`]({})'.format(memberdict['role'],memberdict['name'],memberdict['tag'],memberdict['url'].replace('api.', '', 1))
			if memberdict['userid'] != '':
				try:
					memberdict['formatted'] += ' <@'+memberdict['userid'] + '>'
				except:
					pass
				formattedmembers.append(memberdict['formatted'])
			if memberdict['role'] == 'Co-Leader':
				self.coleaders.append(memberdict)
				formatted.coleaders.append(memberdict['formatted'])
			if memberdict['role'] == 'Member':
				self.norole.append(memberdict)
				formatted.norole.append(memberdict['formatted'])
			if memberdict['role'] == 'Elder':
				self.elders.append(memberdict)
				formatted.elders.append(memberdict['formatted'])
			if memberdict['role'] == 'Leader':
				self.leader = memberdict
				formatted.leader = memberdict['formatted']
			self.size += 1
			self.members.append(memberdict)
			i+= 1

		formatted.members = formattedmembers
		sortedc = CRClan()
		n = 0
		for ele in ['coleaders', 'members', 'norole', 'elders']:
			# print('el testo')
			members = getattr(self, ele)
			templist = [members[0]]
			for m in members[1:]:
				# print('hi2')
				for i, mem in enumerate(templist):
					# print(i)
					# print('hi3')
					# print(m['name'], mem['name'])
					# time.sleep(1)
					if m['name'].upper()<mem['name'].upper():
						# print('hi4')
						templist.insert(i, m)
						break
					elif i == len(templist)-1:
						# print('hi5')
						templist.append(m)
						break
					if i>100:
						break
				# print(templist)
			# print('hi')
			# print(ele, templist)
			# time.sleep(10)
			setattr(self, 'sorted'+ele, templist)
		self.sortedleader = self.leader
		# print('formattedlmaoxd')
		for ele in ['coleaders', 'members', 'norole', 'elders']:
			ele = 'sorted' + ele
			# print(ele,getattr(self, ele))
		formatted.sortedleader  = formatted.leader
		for ele in ['coleaders', 'members', 'norole', 'elders']:
			ele = 'sorted' + ele
			mems = getattr(self, ele)
			templist = []
			for m in mems:
				templist.append(m['formatted'])

			setattr(formatted, ele, templist)
		# print('formattedlmaoxd2')
		for ele in ['coleaders', 'members', 'norole', 'elders']:
			ele = 'sorted' + ele
			# print(ele,getattr(formatted, ele))


		# for ele in ['coleaders', 'members', 'norole', 'elders']:
		#   currentmems = []
		#   # print(ele, getattr(self, ele))
		#   if len(getattr(self, ele))>0:
		#       sortalphamems = [getattr(self, ele)[0]]
		#       for m in getattr(self, ele)[1:]:
		#           n = -1
		#           for sm in sortalphamems:
		#               n += 1
		#               if sm['name'].upper()>m['name']:
		#                   sortalphamems.insert(n, m)
		#                   break
		#   else:
		#       sortalphamems = []

		#   setattr(sortedc, ele, sortalphamems)
		#   # print(ele, getattr(sortedc, ele))
		#   for m in getattr(sortedc, ele) :
		#       currentmems.append(m['formatted'])
		#   # print(ele, currentmems)
		#   setattr(formatted, ele, currentmems)
		# for ele in ['coleaders', 'members', 'norole', 'elders']:
		#   # print(ele,getattr(sortedc,ele))
		#   templist = []
		#   for m in getattr(sortedc, ele):
		#       templist.append(m['formatted'])
		#   setattr(formatted, ele, templist)
		# print('formattedlmaoxd')
		# for ele in ['coleaders', 'members', 'norole', 'elders']:
		#   print(ele, getattr(formatted,ele))



		self.clan_badge = crapiurl + clandatadict['badge_url']
		formatted.clan_badge = self.badge
		self.name = clandatadict['name']
		formatted.name = "Clan: {}".format(self.name)
		self.desc = clandatadict['description']
		formatted.desc = "Description: {}".format(self.desc)
		d = self.desc
		
		d2 = d

		i = 0
		index = 0
		count = d2.lower().count('discord.')
		while i<count:
			index = d2.lower().find('discord.', index+1)
			d4 = d2.replace(d2[index:index+len('discord.')], 'discord.')
			d3 = d4[index:]
			endlink = d3[d3.find('discord.'):].find(' ')
			if endlink == -1:
				endlink = len(d3)
			discordlink = d3[d3.find('discord.'):endlink+d3.find('discord.')]
			d2 = d2.replace(d2[index:index+len(discordlink)], " [{}](https://{})".format(d2[index:index+len(discordlink)], discordlink))

			i += 1
		sym = '#'
		numtagsind2 = 0
		tagsind2 = []
		index = 0
		i = 0
		while i<d2.count(sym):
			index = d2.find(sym, index+1)
			x = ''
			i2 = 1
			thing = ''
			while x != ' ':
				thing += x
				x = d2[index+i2]
				i2 += 1
			valid = True
			n = 0
			thing2 = ''
			for l in thing:
				if l not in validChars:
					if n>4 and not l.isalnum():
						valid = True
					else:
						valid = False
					break
				thing2 += l
				n+=1
			if valid and len(thing2)>4:
				numtagsind2 += 1
				tagsind2.append(thing2)
			i += 1
		for tag in tagsind2:
			tag = tag.replace(sym, '')
			d2 = d2.replace(sym+tag, '[{}]({})'.format(sym+tag, 'https://cr-api.com/clan/'+tag))
		self.desc2 =  d2
		formatted.desc2 = "Description: {}".format(self.desc2)
		self.clan_trophy = clandatadict['score']
		formatted.clan_trophy = "Trophies: {}".format(str(self.clan_trophy))
		self.tr_req = clandatadict['requiredScore']
		formatted.tr_req = "Trophy requirement: {}".format(str(self.tr_req))
		self.parsedtr_req = await parsereq(self.desc)
		if self.parsedtr_req == None:
			formatted.parsedtr_req = "{} Req: {}".format(allemojis['trophy'],self.tr_req)
		else:
			formatted.parsedtr_req = "{1} Req: {0}\nDescription {1} Req: {2}\n".format(self.tr_req, allemojis['trophy'], self.parsedtr_req)
		self.donperweek = clandatadict['donations']
		formatted.donperweek = "Donations this week: {}".format(str(self.donperweek))
		self.badge = crapi_url +'/static/img'+ clandatadict['badge_url']
		return [self, formatted, sortedc]

class XP:
	def __init__(self, denom, xp, level):
		self.current = xp
		self.denom = denom
		self.level = level
	
	@property
	def xpleft(self):
		return self.denom-self.current
	@property
	def formatted(self):
		return "Level {}, {}/{}{}".format(cremojis[str(self.level)+'xp'], self.current,self.denom, cremojis['levelsmall'])

class Arena:
	def __init__(self, imageurl,name):
		self.url = imageurl
		self.name = name
	@property
	def formatted(self):
		return "Arena: {}".format(self.name)
class Card:
	def __init__(self, name, rarity, level, count, denom):
		self.name = name
		self.rarity = rarity
		self.level = level
		self.count = count
		self.countreq = denom

	@property
	def cardsleft(self):
		return denom-count
	@property
	def formatted(self):
		return "{}{}".format(cremojis[api2emoji(self.name)], self.level)

def goldcalc(self, cardlvl):
	allgold = 0
	for rarity in cardlvl:
		for lvl in cardlvl[rarity]:
			allgold += totalupgrades[rarity][lvl]
			# totalgold[rarity] += totalupgrades[rarity][lvl]
	return allgold

class Deck:
	def __init__(self, carddicts):
		self.cards = []
		for card in carddicts:
			c = Card(card['name'], card['rarity'], card['level'], card['count'], card['requiredForUpgrade'])
			self.cards.append(c)

	@property
	def goldspent(self):
		cardlvl = {'c': [], 'r':[],'e':[],'l':[]}
		for c in self.cards:
			cardlvl[c['rarity'][0]].append(c['level'])
		return goldcalc(cardlvl)
	@property
	def formatted(self):
		formdeck = []
		for c in self.cards:
			formdeck.append(c.formatted)
		return ' '.join(formdeck)

class CRGames:
	def __init__(self,s):
		self.total =  s['total']
		self.tourney = s['tournamentGames']
		self.wins = s['wins']
		self.losses = s['losses']
		self.draws = s['draws']
		self.winstreak = s['currentWinStreak']
		if self.winstreak<0:
			self.winstreak = 0
	@property
	def formatted(self):
		return [
			"Total Games: {}{}".format(self.total, cremojis['battle']),
			"Tourney Games: {}{}".format(self.tourney, cremojis['tournament']),
			"Wins: {}{}".format(self.wins, cremojis['bluecrown']),
			"Losses: {}{}".format(self.losses, cremojis['redcrown']),
			"Draws: {}".format(self.draws),
			"Current Win Streak: {}".format(self.winstreak)

		]

class CRStats:
	def __init__(self, s):
		self.legendtr = s['legendaryTrophies']
		self.tcardswon = s['tournamentCardsWon']
		self.cardswon = s['challengeCardsWon']
		self.pb = s['maxTrophies']
		self.crown3 = s['threeCrownWins']
		self.favcard = s['favoriteCard']
		self.donations = s['totalDonations']
		self.maxwins = s['challengeMaxWins']

	@property
	def formatted(self):
		return [
			"Legend Trophies: {}{}".format(self.legendtr, cremojis['legendarytrophy']),
			"Tourney Cards Won: {}{}{}".format(self.tcardswon, cremojis['deck'], cremojis['tournament']),
			"Cards Won: {}{}".format(self.cardswon, cremojis['deck'], cremojis['tourngold']),
			"PB: {}{}".format(self.pb, cremojis['trophy']),
			"3 Crowns: {0}{1}{1}{1}".format(self.crown3, cremojis['bluecrown']),
			"Favorite Card: {}{}".format(self.favcard.replace('_',' ').title(), cremojis[api2emoji(self.favcard)]),
			"Total Donations: {}{}{}{}".format(self.donations, cremojis['common'], cremojis['rare'], cremojis['epic']),
			"Max Wins: {}{}".format(self.maxwins, cremojis['crownshield'])
		]

class CRChests:
	def __init__(self, s):
		self.pos = s['position']
		self.SMC = s['superMagicalPos']-self.pos
		self.legend = s['legendaryPos']-self.pos
		self.epic = s['epicPos']-self.pos

	@property
	def formatted(self):
		return [
			"Chests Opened: {}{}".format(self.pos,cremojis['shop']),
			', '.join(["{}{}".format(cremojis['supermagicalchest'],self.SMC),
			"{}{}".format(cremojis['legendarychest'],self.legend),
			"{}{}".format(cremojis['epicchest'],self.epic)])
		]

class CROffers:
	def __init__(self,s):
		self.legend = s['legendary']
		self.epic = s['epic']
		self.arena = s['arena']
		self.units = ' days'
	@property
	def legendf(self):
		return str(self.legend) + self.units
	@property
	def epicf(self):
		return str(self.epic) + self.units
	@property
	def arenaf(self):
		return str(self.arena) + self.units
	#f means Formatted (with days)
	@property
	def formatted(self):
		return [
			"Legendary Offer: {}{}".format(self.legendf, cremojis['legendarychest']),
			"Epic Offer: {}{}".format(self.epicf, cremojis['epicchest']),
			"Arena Offer: {}{}".format(self.arenaf, cremojis['legendaryarena'])
		]


class CRSeasons:
	def __init__(self,s):
		self.seasons = s
		
	@property
	def formatted(self):
		formseasons = []
		for  s in self.seasons:
			formseasons.append("{4}Season {0}: Ended at {1}{3}, PB {2}{3}".format(s['seasonNumber'],
				s['seasonEnding'],s['seasonHighest'],cremojis['trophy'],cremojis['rank']))
		return '\n'.join(list(reversed(formseasons)))

class CRPlayer:


	def __init__(self):
		self.url = ''
		self.origindict = ''
		self.tag = ''
		self.name =''
		self.trophies =''
		self.arena =  ''
		self.namechangeleft = ''
		self.globalrank = ''
		self.clan = ''
		self.xp = ''
		self.stats ='' 
		self.games = ''
		self.chestcycle =''
		self.deck = ''
		self.seasons =''
		self.offers = ''

	@classmethod
	async def create(self, tag):
		playerfulldict = {'norm':[], 'formatted':[ ]}
		self.url = crapiurl +'/profile/'+tag
		async with aiohttp.ClientSession() as session:
			async with session.get(self.url) as resp:
				# print(await resp.read())
				datadict = await resp.json()
		if 'error' in datadict:
			datadict = {"tag":"V82UVQV","name":"GhostlyDino","trophies":4709,"arena":{"imageURL":"/arena/league3.png","arena":"League 3","arenaID":14,"name":"Challenger III","trophyLimit":4600},"legendaryTrophies":614,"nameChanged":False,"globalRank":None,"clan":{"tag":"LGVV2CG","name":"Reddit Echo","role":"Co-Leader","badgeUrl":"/badge/A_Char_Rocket_02.png"},"experience":{"level":12,"xp":12549,"xpRequiredForLevelUp":80000,"xpToLevelUp":67451},"stats":{"legendaryTrophies":614,"tournamentCardsWon":895,"maxTrophies":5064,"threeCrownWins":849,"cardsFound":76,"favoriteCard":"mortar","totalDonations":36783,"challengeMaxWins":20,"challengeCardsWon":48674,"level":15},"games":{"total":5819,"tournamentGames":258,"wins":2496,"losses":1516,"draws":1807,"currentWinStreak":2},"chestCycle":{"position":1170,"superMagicalPos":1374,"legendaryPos":1196,"epicPos":1991},"shopOffers":{"legendary":23,"epic":2,"arena":6},"currentDeck":[{"name":"ice_spirit","rarity":"common","level":12,"count":1722,"requiredForUpgrade":5000,"leftToUpgrade":3278},{"name":"arrows","rarity":"common","level":11,"count":3866,"requiredForUpgrade":2000,"leftToUpgrade":-1866},{"name":"knight","rarity":"common","level":12,"count":3075,"requiredForUpgrade":5000,"leftToUpgrade":1925},{"name":"archers","rarity":"common","level":12,"count":1513,"requiredForUpgrade":5000,"leftToUpgrade":3487},{"name":"the_log","rarity":"legendary","level":2,"count":1,"requiredForUpgrade":4,"leftToUpgrade":3},{"name":"mortar","rarity":"common","level":12,"count":2853,"requiredForUpgrade":5000,"leftToUpgrade":2147},{"name":"rocket","rarity":"rare","level":9,"count":314,"requiredForUpgrade":800,"leftToUpgrade":486},{"name":"bats","rarity":"common","level":12,"count":1140,"requiredForUpgrade":5000,"leftToUpgrade":3860}],"previousSeasons":[{"seasonNumber":6,"seasonHighest":4949,"seasonEnding":4886,"seasonEndGlobalRank":None},{"seasonNumber":5,"seasonHighest":4652,"seasonEnding":4617,"seasonEndGlobalRank":None},{"seasonNumber":4,"seasonHighest":4911,"seasonEnding":4911,"seasonEndGlobalRank":None},{"seasonNumber":3,"seasonHighest":5064,"seasonEnding":4913,"seasonEndGlobalRank":None},{"seasonNumber":2,"seasonHighest":4899,"seasonEnding":4804,"seasonEndGlobalRank":None},{"seasonNumber":1,"seasonHighest":4808,"seasonEnding":4508,"seasonEndGlobalRank":None}]}
		# if 'error' in datadict:
		#   await StatsCRPlayer.create(tag)
		#   defaultdatadict = {"tag":"","name":"","trophies":'',"arena":
		#   {"imageURL":"","arena":"","arenaID":'',
		#   "name":"","trophyLimit":''},"legendaryTrophies":'',
		#   "nameChanged":'',"globalRank":'',"clan":
		#   {"tag":"",
		#   "name":"","role":"","badgeUrl":""},
		#   "experience":
		#   {"level":'',"xp":'',"xpRequiredForLevelUp":'',
		#   "xpToLevelUp":''},"stats":
		#   {"legendaryTrophies":'',"tournamentCardsWon":'',
		#   "maxTrophies":'',"threeCrownWins":'',"cardsFound":'',"favoriteCard":"mortar",
		#   "totalDonations":'',"challengeMaxWins":'',"challengeCardsWon":'',"level":''},
		#   "games":
		#   {"total":'',"tournamentGames":'',"wins":'',"losses":'',"draws":'',"currentWinStreak":9},"chestCycle":
		#   {"position":'',"superMagicalPos":'',"legendaryPos":'',"epicPos":''},"shopOffers":
		#   {"legendary":'',"epic":'',"arena":''},"currentDeck":[
		#   {"name":"","rarity":"","level":'',"count":'',"requiredForUpgrade":'',"leftToUpgrade":''},
		#   {"name":"","rarity":"","level":'',"count":'',"requiredForUpgrade":'',"leftToUpgrade":''},
		#   {"name":"","rarity":"","level":'',"count":'',"requiredForUpgrade":'',"leftToUpgrade":''},
		#   {"name":"","rarity":"","level":'',"count":'',"requiredForUpgrade":'',"leftToUpgrade":''},
		#   {"name":"","rarity":"","level":'',"count":'',"requiredForUpgrade":'',"leftToUpgrade":''},
		#   {"name":"","rarity":"","level":'',"count":'',"requiredForUpgrade":'',"leftToUpgrade":''},
		#   {"name":"","rarity":"","level":'',"count":'',"requiredForUpgrade":'',"leftToUpgrade":''},
		#   {"name":"","rarity":"","level":'',"count":'',"requiredForUpgrade":'',"leftToUpgrade":''}],"previousSeasons":[
		#   {"seasonNumber":'',"seasonHighest":'',"seasonEnding":'',"seasonEndGlobalRank":''},
		#   {"seasonNumber":'',"seasonHighest":'',"seasonEnding":'',"seasonEndGlobalRank":''},
		#   {"seasonNumber":'',"seasonHighest":'',"seasonEnding":'',"seasonEndGlobalRank":''},
		#   {"seasonNumber":'',"seasonHighest":'',"seasonEnding":'',"seasonEndGlobalRank":''},
		#   {"seasonNumber":'',"seasonHighest":'',"seasonEnding":'',"seasonEndGlobalRank":''},
		#   {"seasonNumber":'',"seasonHighest":'',"seasonEnding":'',"seasonEndGlobalRank":''}]}
		#   datadict = defaultdatadict
		#   # for data in datas:
		# print('PLAYER:')
		# print(datadict)
		# print('END PLAYER')
		formatted = CRPlayer()
		self.origindict = datadict
				
		self.tag = tag
		formatted.tag = '[{}]({})'.format(self.tag, self.url)
				
		self.name = datadict['name']
		formatted.name = datadict['name']
				
		self.trophies = datadict['trophies']
		formatted.trophies = "Trophies: {}{}".format(self.trophies, cremojis['trophy'])
				
		self.arena =  Arena(datadict['arena']['imageURL'], datadict['arena']['name'])
		formatted.arena = self.arena.formatted
				
		self.namechangeleft = not datadict['nameChanged']
		formatted.namechangeleft = "Can change name" if self.namechangeleft else "Can't Change Name"
				
		self.globalrank = datadict['globalRank']
		formatted.globalrank = "Global Rank: {}".format(self.globalrank) if self.globalrank != None  else ''
				
		self.clan = await CRClan.create(datadict['clan']['tag'])
		self.clan = self.clan[0]
		formatted.clan = "Clan: [{}]({})".format(self.clan.name, self.clan.url)
				
		self.xp = XP(datadict['experience']['xpRequiredForLevelUp'],datadict['experience']['xp'], datadict['experience']['level'])
		formatted.xp = self.xp.formatted

		self.stats = CRStats(datadict['stats'])
		formatted.stats = self.stats.formatted
		
		self.games = CRGames(datadict['games'])
		formatted.games = self.games.formatted
		
		self.chestcycle = CRChests(datadict['chestCycle'])
		formatted.chestcycle = self.chestcycle.formatted
		
		self.deck = Deck(datadict['currentDeck'])
		formatted.deck = self.deck.formatted
		
		self.seasons = CRSeasons(datadict['previousSeasons'])
		formatted.seasons = self.seasons.formatted

		self.offers = CROffers(datadict['shopOffers'])
		formatted.offers = self.offers.formatted
		return [self, formatted]

	@property
	def to_dict(self):
		return self.origindict



# class StatsCRPlayer:


#   def __init__(self):
#       self.a = 4

#   @classmethod
#   async def create(self, tag):
#       self.clan_badge = ''                 #done

#       self.name = ''                       #done
#       self.level = ''                      #done
#       self.clan = ''                       #done
#       self.prevseasontrophy = ''           #done
#       self.crown3 = ''                     #done
#       self.prevseasonpb = ''               #done
#       self.wins = ''                       #done
#       self.cardswon = ''                   #done
#       self.losses = ''                     #done
#       self.league = ''                     #done
#       self.prevseasonrank = ''             #done
#       self.donations = ''                  #done
#       self.trophy = ''                     #done
#       self.tcardswon = ''                  #done
#       self.pb = ''                         #done
#       self.chests = ''                     #done

#       asyncio.sleep(1)
#       user_url = 'http://statsroyale.com/profile/'+tag
#       await async_refresh(user_url+'/refresh')
#       r = requests.get(user_url, headers=headers)
#       html_doc = r.content
#       soup = BeautifulSoup(html_doc, "html.parser")
#       print(soup.prettify())
#       chests_queue = soup.find('div', {'class':'chests__queue'})
#       chests = chests_queue.get_text().split()
#       for index, item in enumerate(chests):
#           if item.startswith('+') and item.endswith(':'):
#               del chests[index]
#           elif item == 'Chest':
#               del chests[index]
#           if item == 'Super':
#               chests[index] = 'SMC'
#           elif item == 'Magic':
#               chests[index] = 'Magical'

#       for index, chest in enumerate(chests):
#           if str(chest) == 'Magic':
#               chests[index] = 'Magical'
#           elif str(chest) == 'Super':
#               chests[index] = 'SMC'
#       new_chests = []
#       x = 0
#       while x<len(chests):
#           new_chests.append(chests[x:x+2])
#           x += 2
#       chests = []


#       for index, chest in enumerate(new_chests):
#           chests.append(': '.join(chest))

#       self.chests = '\n'.join(chests)

#       soup = BeautifulSoup(html_doc, "html.parser")
#       profilehead = soup.find_all("div", "profileHeader profile__header")
#       statistics = soup.find_all("div", "statistics profile__statistics")
#       profilehead = profilehead[0]
#       statistics = statistics[0]
#       thing2 = statistics.get_text()
#       thing2 = thing2.replace('\n', ' ')
#       thing2 = thing2.split('   ')
#       for index, item in enumerate(thing2):
#           thing2[index] = item.strip()
#       statsdict = {}
#       for index, item in enumerate(thing2):
#           if item[:item.find(' ')].isdigit():
#               thing2[index] = item[item.find(' ')+1:]+ ': '+item[:item.find(' ')]
#               statsdict[item[item.find(' ')+1:].strip()] = item[:item.find(' ')] 
#           else:
#               statsdict[item.strip()] = ' '
#           thing2[index].strip()

#       pb = thing2[0]
#       trophy = thing2[1]
#       cardswon = thing2[2]
#       tcardswon = thing2[3]
#       donations = thing2[4]
#       prevseasonrank = thing2[5]
#       prevseasontrophy = thing2[6]
#       prevseasonpb = thing2[7]
#       wins = thing2[8]
#       losses = thing2[9]
#       crown3 = thing2[10]
#       league = thing2[11]
#       try:
#           clan_url = statsurl + str(profilehead.find('a').attrs['href'])
#       except AttributeError:
#           clan_url  = ''
#       playerLevel = profilehead.find('span', 'profileHeader__userLevel')
#       playerLevel = playerLevel.text
#       playerName = profilehead.find('div', 'ui__headerMedium profileHeader__name').text.strip()
#       playerName = playerName.replace(playerLevel, '').strip()
#       try:
#           playerClan = profilehead.find('a', 'ui__link ui__mediumText profileHeader__userClan').text.strip()
#       except AttributeError:
#           playerClan  = 'No Clan'
#       playerTag = tag
#       clan_badge = profilehead.find('img').attrs['src']
#       clan_badge = statsurl + clan_badge
#       self.clan_badge = clan_badge
#       player_data = []
#       player_data.append('[#{}]({})'.format(tag, user_url))
#       for x in statsdict:
#           if(statsdict[x].isdigit()):
#               statsdict[x] = '[' + statsdict[x] + '](http://)'
#       for x in statsdict:
#           if 'League' in x:
#               self.league = x
#           elif 'Highest trophies' in x:
#               self.pb = statsdict[x]
#           elif'Last known trophies' in x:
#               self.trophy = statsdict[x]
#           elif 'Challenge cards won' in x:
#               self.cardswon = statsdict[x]
#           elif 'Tourney cards won' in x:
#               self.tcardswon = statsdict[x]
#           elif 'Total donations' in x:
#               self.donations = statsdict[x]
#           elif 'Prev season rank' in x:
#               self.prevseasonrank = statsdict[x]
#           elif 'Prev season trophies' in x:
#               self.prevseasontrophy = statsdict[x]
#           elif 'Prev season highest' in x:
#               self.prevseasonpb = statsdict[x]
#           elif 'Wins' in x:
#               self.wins = statsdict[x]
#           elif 'Loses' in x:
#               self.losses = statsdict[x]
#           elif '3 crown wins' in x:
#               self.crown3 = statsdict[x]
#       self.name = playerName
#       self.level = playerLevel
#       self.clan = playerClan
#       self.clan_url = clan_url
#       return self

class InvalidRarity(Exception):
	pass
class ErrorKeyortag(Exception):
	def __init__(self, msg):
		self.msg = msg

numcards = {}
numcards['c'] = 20
numcards['r'] = 21
numcards['e'] = 22
numcards['l'] = 13
maxcards = {
	'c':13,
	'r':11,
	'e':8,
	'l':5
}
tourneycards = {
	'c':9,
	'r':7,
	'e':4,
	'l':1
}


upgrades = {}
upgrades['c'] = [
	5,
	20,
	50,
	150,
	400,
	1000,
	2000,
	4000,
	8000,
	20000,
	50000,
	100000
]
upgrades['r'] = upgrades['c'][2:]
upgrades['e'] = upgrades['r'][3:]
upgrades['e'][upgrades['e'].index(1000)] = 400
upgrades['l'] = upgrades['e'][3:]
upgrades['l'][upgrades['l'].index(8000)] = 5000
for rarity in upgrades:
	upgrades[rarity].insert(0, 0)


totalupgrades = {}
for rarity in upgrades:
	totalupgrades[rarity] = []
	for index, cost in enumerate(upgrades[rarity]):
		totalupgrades[rarity].append(sum(upgrades[rarity][:index+1]))

	async def parsereq( desc):
		trophynums = []
		n = 0
		for l in desc:
			try:
				if l.isdigit() or (l.lower()=='p' and desc[n+1].lower()=='b') or (l.lower()=='b' and desc[n-1].lower()=='p') or l.lower() == 'o':
					trophynums.append(l)
				elif trophynums[len(trophynums)-1] != " ":
					trophynums.append(' ')
			except IndexError:
				pass
			n+=1
		n = 0
		trnums = ''.join(trophynums)
		trnums = trnums.split(' ')
		while n<len(trnums):
			d = trnums[n]
			# print("trnums: {}".format(trnums))
			# print("{}, len: {}".format(d, len(d)))
			if len(d) == 4 or d.lower() =='pb':
				if d.isdigit():
					trnums[n] = "{:,}".format(int(d))
				n += 1
			else:
				trnums.remove(d)
		# print(trnums)
		# print(len(trnums))
		n = 0
		for d in trnums:
			trnums[n] = trnums[n].replace('O', '0').replace('o', '0')
			n += 1
		trophyreq = None
		if len(trnums)==0:
			trnums = None
		elif len(trnums) == 1:
			trnums = trnums[0]
		elif len(trnums)==2:
			n = 0
			while n<len(trnums):
				if trnums[n].isdigit():
					trnums[n] = "{:,}".format(int(d))
				n+=1
			trnums = ' '.join(trnums)
		parseddesc = trnums
		if parseddesc == None:
			trophyreq = None
		if type(parseddesc) == type('string'):
			trophyreq = parseddesc
		elif type(parseddesc) == type(list()):
			trreqs =''
			n = 0
			for d in parseddesc:
				trreqs +=d 
				# print("parseddesc len: {}\nn: {}\nnextone: {}".format(len(parseddesc) ,n, parseddesc[n+1].lower()))
				try:
					if n !=len(parseddesc)-1 and parseddesc[n+1].lower()!='pb':
						trreqs += ', '
					else:
						trreqs += ' '
				except IndexError:
					pass
				n+=1
			trophyreq = trreqs
		return trophyreq

class CRTags:

	def __init__(self, bot):
		self.cremojiobjs = {}
		self.settings = dataIO.load_json(SETTINGS_JSON)
		self.backsettings = dataIO.load_json(BACKSETTINGS_JSON)
		self.clansettings = dataIO.load_json(CLAN_JSON)
		self.bot = bot
		self.currentemojiobjs = []
		cremojis = self.allemojis = dataIO.load_json(CREMOJIS_JSON)
		self.emojiservers = []
		for e in cremojis:
			cremojilist.append(cremojis[e])
		self.word2num = {
			'one':1,
			'two':2,
			'three':3,
			'four':4
		}
		self.member2emojiobjs = {
			'elders' : '🇪',
			'coleaders' : '🇨',
			'members' : '🇲',
			'norole' : '🇳',
			'leader': '🇱'
		}
		self.number2emojis = {
			'one':'1⃣',
			'two':'2⃣',
			'three':'3⃣',
			'four':'4⃣'
		}

		self.reactionemojislist = [ #emojis for the first reaction part
			'search',
			'trophy',
			'cheerblue',
			'social',
			'deck',
			'locked'
		]
		self.utilreactionemojislist = [
			'nocancel',
			'refresh',
			'helpinfo',
		]
		self.reactionemojishelpinfolist = [ #emoji names auto adds reactionemojislist
			'elders',
			'norole',
			'coleaders',
			'leader',
			'members',
			'one',
			'two',
			'three',
			'four',
			'nocancel',
			'refresh',
			'helpinfo'
		]
		self.reactionemojishelpinfolist = self.reactionemojishelpinfolist + self.reactionemojislist
		self.reactionemojishelpinfo = { #emoji names from self.reactionemojishelpinfolist
			'search': 'Clan Tag',       # : descriptions for the emoji
			'trophy': 'Clan Trophies',
			'cheerblue': 'Description',
			'social': 'All Members UI',
			'deck':'Donations per week',
			'locked':'Trophy Requirement',
			'elders': 'Elders',
			'norole': 'People with no special role',
			'coleaders': 'Coleaders',
			'leader':'Leader',
			'members':'Members',
			'parsedtr_req': 'Trophy Requirement',
			'one':'Page 1',
			'two':'Page 2',
			'three':'Page 3',
			'four':'Page 4',
			'nocancel': 'Exit the UI',
			'refresh': 'Refresh the emoji options',
			'helpinfo': 'Shows This message'
		}
		self.reactionemojislist.extend(self.utilreactionemojislist)
		self.emojis2specembeds = { #emojiname : element of CRClan
			'search':'tag',
			'trophy':'clan_trophy',
			'cheerblue':'desc2',
			'social':'members',
			'elders': 'elders',
			'norole': 'norole',
			'coleaders': 'coleaders',
			'leader': 'leader',
			'deck':'donperweek',
			'locked':'parsedtr_req'
		}

		def my_decorator(some_function):

			async def wrapper(*args, **kwargs):

				await some_function(*args, **kwargs)
				for server in self.bot.servers:
					for emoji in server.emojis:
						# print(emoji.name)
						self.cremojiobjs[emoji.name] = emoji
				self.member2emojiobjs['nocancel'] =  self.cremojiobjs['nocancel']
				self.cremojiobjs = {**self.cremojiobjs, **self.member2emojiobjs, **self.number2emojis}
				self.emojiobjs2member = {}
				for e in self.member2emojiobjs:
					self.emojiobjs2member[self.member2emojiobjs[e]] = e
				self.reactionemojis = {}
				d = {}
				fulllist =self.reactionemojislist+self.utilreactionemojislist+list(self.member2emojiobjs)
				for e in fulllist:
					# print(self.reactionemojis[e])
					d[e] = self.cremojiobjs[e]
				self.reactionemojis = d
				helptitle = "When an emoji is pressed, the embed will change. If you want to remove part of a player profile, unclick the emoji, and click the refresh emoji. Here are what the emojis show:"
				helpemojis = []
				for e in self.reactionemojishelpinfolist:
					if e not in self.number2emojis:
						helpemojis.append("{}: {}".format(self.reactionemojis[e], self.reactionemojishelpinfo[e]))
				for e in onetofour:
					helpemojis.append("{}: {}".format(self.number2emojis[e], self.reactionemojishelpinfo[e]))
				self.helpembed = discord.Embed(title=helptitle,description='\n'.join(helpemojis),color=discord.Color(0x50d2fe))

			return wrapper
			#loads some CRTags atttributes when bot is ready, otherwise it cant get servers/emojis
		self.bot.on_ready = my_decorator(self.bot.on_ready) #adds the above code to on_ready
		# print('\n{}'.format(str(inspect.getsource(self.bot.on_ready))))


	@commands.group(pass_context=True)
	async def clan(self, ctx):
		"""get clan info
		"""
		# racfserver = self.bot.get_server('218534373169954816')
		# await self.bot.say(racfserver.get_member('222925389641547776').mention)
		# await self.bot.say(server.get_member('222925389641547776').mention)
		# print(dir(CRClan('QUYCYV8')))
		if ctx.invoked_subcommand is None:
			await send_cmd_help(ctx)

	def members2formatted(self, members2display):
		n = 0
		members_per_embed = 13
		member_data = [] # for displaying all members
		while n<int(len(members2display)/members_per_embed+1):
			member_data.append([])
			n += 1

		n = 0
		while n<int(len(members2display)/members_per_embed+1):
			try:
				membersection = members2display[(n)*members_per_embed:(n+1)*members_per_embed]
			except:
				membersection = members2display[(n)*members_per_embed:]
			# await self.bot.say(membersection)
			for member in membersection:
				memberstring = member['formatted']
				member_data[n].append(memberstring)
			n += 1
		return member_data


	async def keyortag2tag(self, keyortag, ctx):
		if keyortag == None:
			keyortag = ctx.message.author.id
		originalkey = keyortag
		keyortag = keyortag.upper()
		members = list(ctx.message.server.members)
		membernames = []
		memberswithdiscrim = []
		for member in members:
			membernames.append(member.name)
			memberswithdiscrim.append(member.name + '#' + str(member.discriminator))
		userid = None
		tag = ''
		valid = True
		for letter in keyortag:
			if letter not in validChars:
				valid = False
				break
		if keyortag in self.clansettings:
			tag = self.clansettings[keyortag]
		elif valid:
			tag = keyortag
		elif keyortag.startswith('<@'): #assume mention
			userid = keyortag[2:-1]
			userid = userid.replace('!', '')
		elif keyortag.isdigit(): #assume userid
			userid = keyortag
		elif originalkey in members or originalkey in membernames or originalkey in memberswithdiscrim: #if user in members
			for member in members:
				name = member.name
				if keyortag == member:
					userid = member.id
				elif keyortag == name:
					userid = member.id
					break
				elif keyortag == name + '#' + member.discriminator:
					userid = member.id
					break
		else:
			raise ErrorKeyortag('`{}` is not in the database, nor is an acceptable tag.'.format(keyortag))
		if userid != None:
			try:
				usertag = self.settings[userid]
			except KeyError:
				raise ErrorKeyortag("That person is not in the database")
			player = await CRPlayer.create(usertag)         
			tag = player[0].clan.tag
			print('in keyortag2tag')
			print(tag)
			# print(tag)
		return tag

	@checks.mod_or_permissions()
	@clan.command(name='set', pass_context=True)
	async def clansettag(self, ctx, tag, *, key):
		author = ctx.message.author
		server = ctx.message.server
		author = server.get_member(author.id)
		rolenames = []
		for role in author.roles:
			rolenames.append(author.name)
		isbotcmder=False
		for role in rolenames:
			if role in BOTCMDER:
				isbotcmder = True
				break
		if checks.is_owner_check(ctx) or isbotcmder:
			pass
		else:
			return
		key = key.upper()
		tag = tag.upper()
		tag.replace('O', '0')
		valid = True
		for letter in tag:
			if letter not in validChars:
				valid = False
		if valid: #self.is_valid(tag):
			self.clansettings[key] = str(tag)
			dataIO.save_json(CLAN_JSON, self.clansettings)
			await self.bot.say("Saved {} for {}".format(tag, key))
		else:
			await self.bot.say("Invalid tag {}, it must only have the following characters {}".format(author.mention), validChars)
			
	@clan.command(name='get',pass_context=True)
	async def get_clan(self, ctx, keyortag=None):
		user = ctx.message.author
		if keyortag == None:
			keyortag = user.id
		try:
			tag = await self.keyortag2tag(keyortag, ctx)
		except ErrorKeyortag as e:
			await self.bot.say(e.msg)
			return
		clanurl = crapiurl + '/clan/' + tag
		await ctx.invoke(self.claninfo, tag)
		await ctx.invoke(self.clanroster, tag)
		return
		# await self.async_refresh(clanurl+ '/refresh')
		clan = await CRClan.create(tag)
		clan_data = []
		member_data = [] # for displaying all members 
		clan_data.append(clan.desc2)
		clan_data.append(clan.leader['formatted'])
		clan_data.append("Clan Tag: [`{}`]({})".format(tag, clan.clanurl))
		clan_data.append("Clan Score: [{}](http://)".format(clan.clan_trophy))
		clan_data.append("Trophy Requirement: [{}](http://)".format(clan.tr_req))
		# clan_data.append("")
		# n = 0
		# while n<len(clan.members):
		#     await self.bot.say(clan.members[n])
		#     n += 1
		# return
		members2display = clan.members
		n = 0
		members_per_embed = 13
		member_data = [] # for displaying all members
		while n<int(len(members2display)/members_per_embed+1):
			member_data.append([])
			n += 1

		n = 0
		while n<int(len(members2display)/members_per_embed+1):
			try:
				membersection = members2display[(n)*members_per_embed:(n+1)*members_per_embed]
			except:
				membersection = members2display[(n)*members_per_embed:]
			# await self.bot.say(membersection)
			for member in membersection:
				memberstring = member['formatted']
				member_data[n].append(memberstring)
			n += 1


		em = []

		if len(clan_data)>0:
			em.append(discord.Embed(url=clan.clanurl, title="{}".format(clan.name), description='\n'.join(clan_data),color = discord.Color(0x50d2fe)))
		for data in member_data:
			if len(em) == 0:
				em.append(discord.Embed(url=clan.clanurl, title="{}".format(clan.name), description='\n'.join(data),color = discord.Color(0x50d2fe)))
			else:
				em.append(discord.Embed(description='\n'.join(data),color = discord.Color(0x50d2fe)))
		try:
			discordname = user.name if user.nick is None else user.nick
		except:
			discordname = user.name
		em[0].set_author(icon_url=user.avatar_url,name=discordname)
		em[0].set_thumbnail(url=clan.clan_badge)
		em[len(em)-1].set_footer(text='Data provided by {}'.format(crapiurl.replace('api.', '', 1)), icon_url='https://raw.githubusercontent.com/cr-api/cr-api-docs/master/docs/img/cr-api-logo-b.png')


		for e in em:
			await self.bot.say(embed=e)


	@clan.command(name='roster',aliases=[],pass_context=True)
	async def clanroster(self, ctx, keyortag=None):
		user = ctx.message.author
		if keyortag == None:
			keyortag = user.id
		try:
			tag = await self.keyortag2tag(keyortag, ctx)
		except ErrorKeyortag as e:
			await self.bot.say(e.msg)
			return
		clanurl = crapiurl + '/clan/' + tag
		# await self.async_refresh(clanurl+ '/refresh')
		clan = await CRClan.create(tag)
		clan = clan[0]
		clan_data = []
		member_data = [] # for displaying all members 
		# clan_data.append(clan.desc2)
		# clan_data.append(clan.leader['formatted'])
		# clan_data.append("Clan Tag: [`{}`]({})".format(tag, clan.clan_url))
		# clan_data.append("Clan Score: [{}](http://)".format(clan.clan_trophy))
		# clan_data.append("Trophy Requirement: [{}](http://)".format(clan.tr_req))
		# clan_data.append("")
		# n = 0
		# while n<len(clan.members):
		#     await self.bot.say(clan.members[n])
		#     n += 1
		# return
		membertype = None
		members2display = clan.members
		if members2display != clan.members:
			membertype = members2display[0]['role']
		member_data = self.members2formatted(members2display)
		for d in member_data:
			print(d)
		n = 0
		em = []
		if membertype != None:
			currentdesc = "**{}** `{}s`\n".format(len(members2display), membertype)
		else:
			currentdesc = ''
		if len(clan_data)>0:
			# emtitle = clan.name
			# if membertype != None:
				# emtitle += '\n{} {}s'.format(len(members2display), membertype)
			e = discord.Embed(url=clan.clanurl, title="{}".format(clan.name), description='{}{}'.format(currentdesc, '\n'.join(data)),color = discord.Color(0x50d2fe))
			em.append(e)
		for data in member_data:
			if len(em) == 0:
				# emtitle = clan.name
				# if membertype != None:
				#   emtitle += '\n{} {}s'.format(len(members2display), membertype)
				e = discord.Embed(url=clan.url, title="{}".format(clan.name), description='{}{}'.format(currentdesc, '\n'.join(data)),color = discord.Color(0x50d2fe))
				em.append(e)
				
			else:
				em.append(discord.Embed(description='\n'.join(data),color = discord.Color(0x50d2fe)))
		try:
			discordname = user.name if user.nick is None else user.nick
		except:
			discordname = user.name
		em[0].set_author(icon_url=user.avatar_url,name=discordname)
		# em[0].
		em[0].set_thumbnail(url=clan.badge)
		em[len(em)-1].set_footer(text='Data provided by {}'.format(crapi_url), icon_url='https://raw.githubusercontent.com/cr-api/cr-api-docs/master/docs/img/cr-api-logo-b.png')


		for e in em:
			await self.bot.say(embed=e)



	@clan.command(name='coleaders',aliases=['cos'],pass_context=True)
	async def clancoleaders(self, ctx, keyortag=None):
		user = ctx.message.author
		if keyortag == None:
			keyortag = user.id
		try:
			tag = await self.keyortag2tag(keyortag, ctx)
		except ErrorKeyortag as e:
			await self.bot.say(e.msg)
			return
		clanurl = crapiurl + '/clan/' + tag
		# await self.async_refresh(clanurl+ '/refresh')
		clan = await CRClan.create(tag)
		clan_data = []
		member_data = [] # for displaying all members 
		# clan_data.append(clan.desc2)
		# clan_data.append(clan.leader['formatted'])
		# clan_data.append("Clan Tag: [`{}`]({})".format(tag, clan.clan_url))
		# clan_data.append("Clan Score: [{}](http://)".format(clan.clan_trophy))
		# clan_data.append("Trophy Requirement: [{}](http://)".format(clan.tr_req))
		# clan_data.append("")
		# n = 0
		# while n<len(clan.members):
		#     await self.bot.say(clan.members[n])
		#     n += 1
		# return
		membertype = None
		members2display = clan.coleaders
		if members2display != clan.members:
			membertype = members2display[0]['role']
		n = 0
		members_per_embed = 13
		member_data = [] # for displaying all members
		while n<int(len(members2display)/members_per_embed+1):
			member_data.append([])
			n += 1

		n = 0
		while n<int(len(members2display)/members_per_embed+1):
			try:
				membersection = members2display[(n)*members_per_embed:(n+1)*members_per_embed]
			except:
				membersection = members2display[(n)*members_per_embed:]
			# await self.bot.say(membersection)
			for member in membersection:
				memberstring = member['formatted']
				member_data[n].append(memberstring)
			n += 1


		em = []
		if membertype != None:
			currentdesc = "**{}** `{}s`\n".format(len(members2display), membertype)
		else:
			currentdesc = ''
		if len(clan_data)>0:
			# emtitle = clan.name
			# if membertype != None:
				# emtitle += '\n{} {}s'.format(len(members2display), membertype)
			e = discord.Embed(url=clan.clanurl, title="{}".format(clan.name), description='{}{}'.format(currentdesc, '\n'.join(data)),color = discord.Color(0x50d2fe))
			em.append(e)
		for data in member_data:
			if len(em) == 0:
				# emtitle = clan.name
				# if membertype != None:
				#   emtitle += '\n{} {}s'.format(len(members2display), membertype)
				e = discord.Embed(url=clan.url, title="{}".format(clan.name), description='{}{}'.format(currentdesc, '\n'.join(data)),color = discord.Color(0x50d2fe))
				em.append(e)
				
			else:
				em.append(discord.Embed(description='\n'.join(data),color = discord.Color(0x50d2fe)))
		try:
			discordname = user.name if user.nick is None else user.nick
		except:
			discordname = user.name
		em[0].set_author(icon_url=user.avatar_url,name=discordname)
		# em[0].
		em[0].set_thumbnail(url=clan.badge)
		em[len(em)-1].set_footer(text='Data provided by {}'.format(crapi_url), icon_url='https://raw.githubusercontent.com/cr-api/cr-api-docs/master/docs/img/cr-api-logo-b.png')


		for e in em:
			await self.bot.say(embed=e)



	@clan.command(name='elders',aliases=['elder'],pass_context=True)
	async def clanelders(self, ctx, keyortag=None):
		user = ctx.message.author
		if keyortag == None:
			keyortag = user.id
		try:
			tag = await self.keyortag2tag(keyortag, ctx)
		except ErrorKeyortag as e:
			await self.bot.say(e.msg)
			return
		if tag == None:
			return
		clanurl = crapiurl + '/clan/' + tag
		# await self.async_refresh(clanurl+ '/refresh')
		clan = await CRClan.create(tag)
		clan_data = []
		member_data = [] # for displaying all members 
		# clan_data.append(clan.desc2)
		# clan_data.append(clan.leader['formatted'])
		# clan_data.append("Clan Tag: [`{}`]({})".format(tag, clan.clan_url))
		# clan_data.append("Clan Score: [{}](http://)".format(clan.clan_trophy))
		# clan_data.append("Trophy Requirement: [{}](http://)".format(clan.tr_req))
		# clan_data.append("")
		# n = 0
		# while n<len(clan.members):
		#     await self.bot.say(clan.members[n])
		#     n += 1
		# return
		membertype = None
		members2display = clan.elders
		if members2display != clan.members:
			membertype = members2display[0]['role']
		n = 0
		members_per_embed = 13
		member_data = [] # for displaying all members
		while n<int(len(members2display)/members_per_embed+1):
			member_data.append([])
			n += 1

		n = 0
		while n<int(len(members2display)/members_per_embed+1):
			try:
				membersection = members2display[(n)*members_per_embed:(n+1)*members_per_embed]
			except:
				membersection = members2display[(n)*members_per_embed:]
			# await self.bot.say(membersection)
			for member in membersection:
				memberstring = member['formatted']
				member_data[n].append(memberstring)
			n += 1


		em = []
		if membertype != None:
			currentdesc = "**{}** `{}s`\n".format(len(members2display), membertype)
		else:
			currentdesc = ''
		if len(clan_data)>0:
			# emtitle = clan.name
			# if membertype != None:
				# emtitle += '\n{} {}s'.format(len(members2display), membertype)
			e = discord.Embed(url=clan.clanurl, title="{}".format(clan.name), description='{}{}'.format(currentdesc, '\n'.join(data)),color = discord.Color(0x50d2fe))
			em.append(e)
		for data in member_data:
			if len(em) == 0:
				# emtitle = clan.name
				# if membertype != None:
				#   emtitle += '\n{} {}s'.format(len(members2display), membertype)
				e = discord.Embed(url=clan.url, title="{}".format(clan.name), description='{}{}'.format(currentdesc, '\n'.join(data)),color = discord.Color(0x50d2fe))
				em.append(e)
				
			else:
				em.append(discord.Embed(description='\n'.join(data),color = discord.Color(0x50d2fe)))
		try:
			discordname = user.name if user.nick is None else user.nick
		except:
			discordname = user.name
		em[0].set_author(icon_url=user.avatar_url,name=discordname)
		# em[0].
		em[0].set_thumbnail(url=clan.badge)
		em[len(em)-1].set_footer(text='Data provided by {}'.format(crapi_url), icon_url='https://raw.githubusercontent.com/cr-api/cr-api-docs/master/docs/img/cr-api-logo-b.png')


		for e in em:
			await self.bot.say(embed=e)




	@clan.command(name='norole',aliases=[],pass_context=True)
	async def clannorole(self, ctx, keyortag=None):
		user = ctx.message.author
		if keyortag == None:
			keyortag = user.id
		try:
			tag = await self.keyortag2tag(keyortag, ctx)
		except ErrorKeyortag as e:
			await self.bot.say(e.msg)
			return
		clanurl = crapiurl + '/clan/' + tag
		# await self.async_refresh(clanurl+ '/refresh')
		clan = await CRClan.create(tag)
		clan_data = []
		member_data = [] # for displaying all members 
		# clan_data.append(clan.desc2)
		# clan_data.append(clan.leader['formatted'])
		# clan_data.append("Clan Tag: [`{}`]({})".format(tag, clan.clan_url))
		# clan_data.append("Clan Score: [{}](http://)".format(clan.clan_trophy))
		# clan_data.append("Trophy Requirement: [{}](http://)".format(clan.tr_req))
		# clan_data.append("")
		# n = 0
		# while n<len(clan.members):
		#     await self.bot.say(clan.members[n])
		#     n += 1
		# return
		membertype = None
		members2display = clan.members
		if members2display != clan.members:
			membertype = members2display[0]['role']
		n = 0
		members_per_embed = 13
		member_data = [] # for displaying all members
		while n<int(len(members2display)/members_per_embed+1):
			member_data.append([])
			n += 1

		n = 0
		while n<int(len(members2display)/members_per_embed+1):
			try:
				membersection = members2display[(n)*members_per_embed:(n+1)*members_per_embed]
			except:
				membersection = members2display[(n)*members_per_embed:]
			# await self.bot.say(membersection)
			for member in membersection:
				memberstring = member['formatted']
				member_data[n].append(memberstring)
			n += 1


		em = []
		if membertype != None:
			currentdesc = "**{}** `{}s`\n".format(len(members2display), membertype)
		else:
			currentdesc = ''
		if len(clan_data)>0:
			# emtitle = clan.name
			# if membertype != None:
				# emtitle += '\n{} {}s'.format(len(members2display), membertype)
			e = discord.Embed(url=clan.clanurl, title="{}".format(clan.name), description='{}{}'.format(currentdesc, '\n'.join(data)),color = discord.Color(0x50d2fe))
			em.append(e)
		for data in member_data:
			if len(em) == 0:
				# emtitle = clan.name
				# if membertype != None:
				#   emtitle += '\n{} {}s'.format(len(members2display), membertype)
				e = discord.Embed(url=clan.url, title="{}".format(clan.name), description='{}{}'.format(currentdesc, '\n'.join(data)),color = discord.Color(0x50d2fe))
				em.append(e)
				
			else:
				em.append(discord.Embed(description='\n'.join(data),color = discord.Color(0x50d2fe)))
		try:
			discordname = user.name if user.nick is None else user.nick
		except:
			discordname = user.name
		em[0].set_author(icon_url=user.avatar_url,name=discordname)
		# em[0].
		em[0].set_thumbnail(url=clan.badge)
		em[len(em)-1].set_footer(text='Data provided by {}'.format(crapi_url), icon_url='https://raw.githubusercontent.com/cr-api/cr-api-docs/master/docs/img/cr-api-logo-b.png')


		for e in em:
			await self.bot.say(embed=e)


	@clan.command(name='info',pass_context=True)
	async def claninfo(self, ctx, keyortag=None):
		user = ctx.message.author
		if keyortag == None:
			keyortag = user.id
		elif keyortag.lower() == 'racf':
			for clan in racfclanslist:
				await ctx.invoke(self.claninfo, clan)
			return
		try:
			tag = await self.keyortag2tag(keyortag, ctx)
		except ErrorKeyortag as e:
			await self.bot.say(e.msg)
			return
		if tag == '':
			await self.bot.say("That user is not in a clan.")
			return
		clanurl = crapiurl + '/clan/' + tag
		# await self.async_refresh(clanurl+ '/refresh')
		clan = await CRClan.create(tag)
		clan_data = []
		member_data = [] # for displaying all members 
		clan_data.append(clan.desc2)
		clan_data.append(clan.leader['formatted'])
		clan_data.append("Clan Tag: [`{}`]({})".format(tag, clan.url))
		clan_data.append("Clan Score: [{}](http://)".format(clan.clan_trophy))
		clan_data.append("Trophy Requirement: [{}](http://)".format(clan.tr_req))


		em = []

		if len(clan_data)>0:
			em.append(discord.Embed(url=clan.url, title="{}".format(clan.name), description='\n'.join(clan_data),color = discord.Color(0x50d2fe)))
		for data in member_data:
			if len(em) == 0:
				em.append(discord.Embed(url=clan.url, title="{}".format(clan.name), description='\n'.join(data),color = discord.Color(0x50d2fe)))
			else:
				em.append(discord.Embed(description='\n'.join(data),color = discord.Color(0x50d2fe)))
		try:
			discordname = user.name if user.nick is None else user.nick
		except:
			discordname = user.name
		em[0].set_author(icon_url=user.avatar_url,name=discordname)
		em[0].set_thumbnail(url=clan.badge)
		em[len(em)-1].set_footer(text='Data provided by {}'.format(crapiurl.replace('api.', '', 1)), icon_url='https://raw.githubusercontent.com/cr-api/cr-api-docs/master/docs/img/cr-api-logo-b.png')

		for e in em:
			await self.bot.say(embed=e)



	def statsvalid(self, tag):
		for letter in tag:
			if letter not in validChars:
				return False
		return True

	async def async_refresh(self,url):
		async with aiohttp.get(url) as r:
			response = await r.json()
			return response

	async def refresh(self, tag):
		await self.async_refresh('http://statsroyale.com/profile/'+tags[user.id]+'/refresh')


	@commands.command(aliases=['tra'], pass_context=True)
	async def trapi(self,ctx,clan=None):
		uclan = None
		if clan != None:
			uclan = clan.upper()
		if clan == None:
			clan = racfclanslist
		elif uclan not in racfclans:
			await self.bot.say("the clan, *\u200b{}* is not in racf".format(clan))
			return
		if type(clan) == type(list()):
			await self.bot.send_typing(ctx.message.channel)
			em = discord.Embed(color=discord.Color(0xFF3844), title="RACF requirements:")
			for c in clan:
				for racfc in racfclanslist:
					if racfc.lower() == c.lower():
						goodcapsclan = racfc
						break
				try:
					tag = await self.keyortag2tag(c, ctx)
				except ErrorKeyortag as e:
					await self.bot.say(e.msg)
					return
				clan_data = await CRClan.create(tag)
				clan_data = clan_data[0]
				trophyreq = await parsereq(clan_data.desc)
				if trophyreq==None:
					trophyreq = clan_data.tr_req
				if goodcapsclan == 'eSports':
					trophyreq = self.allemojis['gitgud']
				em.add_field(name="{}:".format(goodcapsclan), value=trophyreq)

		else:
			try:
				tag = await self.keyortag2tag(clan, ctx)
			except ErrorKeyortag as e:
				await self.bot.say(e.msg)
				return
			# print("Tag: {}".format(tag))
			clan_data = await CRClan.create(tag)
			# clan_data.desc = "WE are reddit delta, we require a pb 4500 and our feeder is reddit echo"
			#uncomment the above line to test the pb detection
			trophyreq = await parsereq(clan_data.desc)
			if trophyreq==None:
				trophyreq = clan_data.tr_req
			for c in racfclanslist:
				if c.lower() == clan.lower():
					goodcapsclan = c
					break
			if goodcapsclan == 'eSports':
				trophyreq = self.allemojis['gitgud']
			em = discord.Embed(color=discord.Color(0xFF3844), title="{} trophy req:".format(goodcapsclan), description=trophyreq)

		await self.bot.say(embed=em)




	def savetag(self, userid, tag):
		try:
			if not userid.isdigit():
				print("must save userid, tag not backwards")
				return
		except:
			return
		self.settings[userid] = str(tag)
		for t in self.backsettings:
			if self.backsettings[t] == userid:
				self.backsettings.pop(t, None)
				break
		self.backsettings[str(tag)] = userid
		dataIO.save_json(SETTINGS_JSON, self.settings)
		dataIO.save_json(BACKSETTINGS_JSON, self.backsettings)

	def deltag(self, userid, tag):
		try:
			if not userid.isdigit():
				print("must del userid, tag not backwards")
				return
		except:
			return
		for t in self.backsettings:
			if self.backsettings[t] == userid:
				self.backsettings.pop(t, None)
				break
		self.settings.pop(userid, None)
		dataIO.save_json(SETTINGS_JSON, self.settings)
		dataIO.save_json(BACKSETTINGS_JSON, self.backsettings)


			
	async def keyortag2tag2(self,userortag,ctx):
		tags = dataIO.load_json(SETTINGS_JSON)
		tag = None
		userid = None
		valid=False
		user = None
		if userortag != None:
			valid = True
			for letter in userortag.upper():
				if letter not in validChars:
					valid = False
		if userortag == None: #assume author if none
			userid = ctx.message.author.id
		elif userortag.startswith('<@'): #assume mention
			userid = userortag[2:-1]
		elif userortag.isdigit(): #assume userid
			userid = userortag
		elif valid: #assume it is a tag
			tag = userortag.upper()
		else:   #assume member name
			for member in list(ctx.message.server.members):
				name = member.name
				if userortag == name:
					userid = member.id
				elif userortag == name + '#' + member.discriminator:
					userid = member.id
		if userid != None:
			user = await self.bot.get_user_info(userid)
				
		if tag == None:
			if userid in tags:
				tag = tags[userid]
			else:
				raise ErrorKeyortag("{} does not have a tag set.".format(user.display_name))
		return [tag, user]


	def react_check(self, reaction, user):
		if user is None or user.id != self.author.id:
			return False

		for emoji in self.currentemojiobjs:
			if reaction.emoji == emoji:
				return True
		return False

	async def reactembeds(self, ctx, messages, clan, clan_data, clan_datadict):

		self.author = ctx.message.author
		self.currentemojiobjs = []
		numbermsg = None
		message = messages[0]
		message2 = messages[1]
		# print(self.cremojiobjs)
		for e in self.reactionemojislist:
			self.currentemojiobjs.append(self.cremojiobjs[e])
		# for e in self.currentemojiobjs:
		#   await self.bot.say(e)
		# self.reactionemojislist = ['😄', reactionemojis[]]
		preaction = None
		for e in self.reactionemojislist: #successfully adds custom emojis
			await self.bot.add_reaction(message,self.reactionemojis[e])

		botreactionsmsg = await self.bot.get_message(message.channel, message.id)
		for r in botreactionsmsg.reactions:
			users = await self.bot.get_reaction_users(r)
			if ctx.message.author in users:
				preaction = (r, ctx.message.author)

		memberemojiobjs = []
		for e in self.member2emojiobjs:
			memberemojiobjs.append(self.member2emojiobjs[e])
		elementspossible = []
		for e in self.reactionemojislist:
			elementspossible.append(e)
		elements2display = []
		u = await self.bot.get_user_info(ctx.message.author.id)
		while True:
			if preaction == None:
				reaction = await self.bot.wait_for_reaction(emoji=self.currentemojiobjs,timeout=30,message=message,user=ctx.message.author)#, check=self.react_check)
			else:
				reaction = preaction
			preaction = None
			if reaction==None:
				await self.bot.edit_message(message,new_content=message.content+' Timed out, UI exited.')
				# await asyncio.sleep(30)
				# em = discord.Embed(title=clan.name,color=discord.Color.blue())
				# await self.bot.edit_message(message, embed = em)
				break
			reaction = list(reaction)
			currentuser = reaction[1]
			reaction = list(reaction)[0]
			remoji = reaction.emoji.name
			myreacts = []
			message = await self.bot.get_message(message.channel, message.id)
			emojiclicked = {}
			for r in botreactionsmsg.reactions:
				users = await self.bot.get_reaction_users(r)
				# print(type(r.emoji), r.emoji)
				try:
					emojiclicked[r.emoji.name] = ctx.message.author in users
				except AttributeError:
					emojiclicked[self.emojiobjs2member[r.emoji]] = ctx.message.author in users
			emojiclicked['refresh'] = False
			emojiclicked['helpinfo'] = False
			emojiclicked['nocancel'] = False
			if emojiclicked['social']:
				await self.bot.edit_message(message2, "Which role would you like to get? (sorted alphabetically)")

				preaction2 = None
				for e in self.member2emojiobjs: #successfully adds emojis
					if e != 'nocancel':
						await self.bot.add_reaction(message2,self.member2emojiobjs[e])
				await self.bot.add_reaction(message2,self.member2emojiobjs['nocancel'])

				message2 = await self.bot.get_message(message2.channel, message2.id)
				for r in message2.reactions:
					users = await self.bot.get_reaction_users(r)
					if ctx.message.author in users:
						preaction2 = (r, ctx.message.author)

				await asyncio.sleep(1)
				while True:
					if preaction2 == None:
						memberreaction = await self.bot.wait_for_reaction(emoji=memberemojiobjs,timeout=30,message=message2, user=ctx.message.author)#, check=
					else:
						memberreaction = preaction2
					preaction2 = None
					message2 = await self.bot.get_message(message2.channel, message2.id)
					if memberreaction==None:
						await self.bot.edit_message(message2,new_content=message2.content+' Timed out, UI exited.')
						await self.bot.edit_message(message,new_content=message.content+' Timed out, UI exited.')
						return
					memberuser = memberreaction[1]
					memberreaction = memberreaction[0]
					memberremoji = memberreaction.emoji
					currentemoji = memberreaction.emoji
					try:
						try:
							await self.bot.delete_message(numbermsg)
						except:
							pass
						if currentemoji.name == 'nocancel':
							await self.bot.edit_message(message2,new_content=message2.content+' {} button clicked, UI exited.'.format(memberremoji))
							await self.bot.edit_message(message,new_content=message.content+' {} button clicked, UI exited.'.format(memberremoji))
							return

					except AttributeError:
						pass
					try:
						await self.bot.delete_message(numbermsg)
					except:
						pass
					numbermsg = await self.bot.say('\u200b')
					memberremojiname = self.emojiobjs2member[memberremoji]
					try:
						members2display = getattr(clan, 'sorted'+memberremojiname)
					except AttributeError:
						pass
					if type(members2display) != type(list()):
						members2display = [members2display]
					member_data = self.members2formatted(members2display)
					em = []
					membertype = memberremojiname
					
					currentdesc = "**{}** *{}*\n".format(len(members2display), self.reactionemojishelpinfo[membertype])
					# if len(clan_data)>0:
					#   # emtitle = clan.name
					#   # if membertype != None:
					#       # emtitle += '\n{} {}s'.format(len(members2display), membertype)
					#   e = discord.Embed(url=clan.url, title="{}".format(clan.name), description='{}{}'.format(currentdesc, '\n'.join(data)),color = discord.Color(0x50d2fe))
					#   em.append(e)
					# names = []
					# for data in member_data:
					#   l = []
					#   for x in data:
					#       l.append(x[x.find('`',2)+1:x.find('[`')].strip())
					#   names.append(l)
					# for i, n in enumerate(names):
					#   names[i] = sorted(n, key=lambda s:s.lower())
					# # print('\n\n\n\nNAMES:\n')
					# allnames = []
					# for n in names:
					#   for x in n:
					#       allnames.append(x)
					# print(allnames)
					# # print('\n\n\n\nEND NAMES\n')
					# allnames = sorted(allnames, key=lambda s:s.lower())
					# alldata = []
					# for data in member_data:
					#   for x in data:
					#       alldata.append(x)
					# sorteddata = []
					# templist = []
					# for index, name in enumerate(allnames):
					#   print(name)
					#   for data in alldata:
					#       # print(data)
					#       x = data
					#       if name == x[x.find('`',2)+1:x.find('[`')].strip():
					#           # print('found')
					#           templist.append(data)
					#           break
					#   if len(templist)==13:
					#       sorteddata.append(templist)
					#       templist = []
					# if len(templist)>0:
					#   sorteddata.append(templist)
					# # print('\n\n\ndata\n')
					# for data in sorteddata:
					#   print(data)
					# print(len(sorteddata))
					# print('\n\n\ndata\n')

					n = 0
					for data in member_data:
							# emtitle = clan.name
							# if membertype != None:
							#   emtitle += '\n{} {}s'.format(len(members2display), membertype)
							sortedmembers = getattr(clan, 'sorted'+membertype)
							print('penismaker')
							if type(sortedmembers) != type(list()):
								sortedmembers = [sortedmembers]
							print(sortedmembers)
							membersbefore = 0
							for d in member_data[:n]:
								membersbefore += len(d)
							firstmemindata = membersbefore+1
							# print(clan.members[])
							e = discord.Embed(url=clan.url, title="{}".format(clan.name), description='{}{}'.format(currentdesc, '\n'.join(data)),color = discord.Color(0x50d2fe))
							# print(members2display[membersbefore]['name'],members2display[membersbefore+len(data)-1]['name'])
							e.set_footer(text='showing page {}/{}, {}-{}, {} to {}'.format(n+1, len(member_data), firstmemindata,firstmemindata+len(data)-1, sortedmembers[membersbefore]['name'] ,sortedmembers[membersbefore+len(data)-1]['name']))
							em.append(e)
							n += 1
					if len(em)>1:
						await self.bot.edit_message(numbermsg, new_content='Which page would you like to get?')
						for e in onetofour[:len(em)]:
							await self.bot.add_reaction(numbermsg, self.number2emojis[e])
						await self.bot.add_reaction(numbermsg, self.cremojiobjs['nocancel'])
						while True:
							numreaction = await self.bot.wait_for_reaction(emoji=list(self.number2emojis.values())+[self.cremojiobjs['nocancel']],timeout=30,message=numbermsg, user=ctx.message.author)
							if numreaction==None:
								await self.bot.edit_message(numbermsg,new_content=numbermsg.content+' Timed out, UI exited.')
								await self.bot.edit_message(message2,new_content=message2.content+' Timed out, UI exited.')
								await self.bot.edit_message(message,new_content=message.content+' Timed out, UI exited.')
								return

							numreaction = list(numreaction)
							
							numuser = numreaction[1]
							numreaction = numreaction[0]
							try:
								if  numreaction.emoji.name=='nocancel':
									await self.bot.delete_message(numbermsg)
									numbermsg = await self.bot.say('\u200b')
									break
							except AttributeError:
								pass
							await self.bot.remove_reaction(numbermsg, numreaction.emoji, numuser)
							for e in self.number2emojis:
								if self.number2emojis[e]==numreaction.emoji:
									numreaction = e
									break
							pagenum = self.word2num[numreaction]
							e = em[pagenum-1]
							await self.bot.edit_message(numbermsg,embed=e)
					else:
						try:
							await self.bot.edit_message(numbermsg,embed=em[0])
						except IndexError:
							await self.bot.edit_message(numbermsg,new_content=numbermsg.content+' No members of that type.')

			elements2display = []
			if remoji != 'nocancel' and remoji != 'social':
				for e in elementspossible:
					if emojiclicked[e]:
						elements2display.append(self.emojis2specembeds[e])
			if remoji=='nocancel':
				elements2display = []
			embed = self.data2embed(ctx.message.author, clan, clan_data, clan_datadict, elements2display)
			if remoji=='nocancel':
				await self.bot.edit_message(message, new_content=message.content+ " {} clicked, UI exited.".format(reaction.emoji), embed=embed)
				break

			if reaction.emoji.name == 'helpinfo':
				await self.bot.edit_message(message, embed=self.helpembed)
			elif reaction.emoji.name != 'social':
				await self.bot.edit_message(message,embed=embed)#specembeds[self.emojis2specembeds[emoji]])

	async def reactembedsmembers(self, ctx, messages, clan, clan_data, clan_datadict):

		self.author = ctx.message.author
		self.currentemojiobjs = []
		numbermsg = None
		message2 = messages[0]
		numbermsg = messages[1]
		# print(self.cremojiobjs)
		# for e in self.reactionemojislist:
		#   self.currentemojiobjs.append(self.cremojiobjs[e])
		# for e in self.currentemojiobjs:
		#   await self.bot.say(e)
		# self.reactionemojislist = ['😄', reactionemojis[]]
		# preaction = None
		# for e in self.reactionemojislist: #successfully adds custom emojis
		#   await self.bot.add_reaction(message,self.reactionemojis[e])
		#   if preaction == None:
		#       botreactionsmsg = await self.bot.get_message(message.channel, message.id)
		#       for r in botreactionsmsg.reactions:
		#           users = await self.bot.get_reaction_users(r)
		#           if ctx.message.author in users:
		#               preaction = (r, ctx.message.author)

		memberemojiobjs = []
		for e in self.member2emojiobjs:
			memberemojiobjs.append(self.member2emojiobjs[e])
		# elementspossible = []
		# for e in self.reactionemojislist:
		#   elementspossible.append(e)
		# elements2display = []
		# u = await self.bot.get_user_info(ctx.message.author.id)
		await self.bot.edit_message(message2, "Which role would you like to get? (sorted alphabetically)")

		preaction2 = None
		n = 0
		for e in self.member2emojiobjs: #successfully adds emojis
			if e != 'nocancel':
				await self.bot.add_reaction(message2,self.member2emojiobjs[e])
				if preaction2 == None and n%3 == 0:
					message2 = await self.bot.get_message(message2.channel, message2.id)
					for r in message2.reactions:
						users = await self.bot.get_reaction_users(r)
						if ctx.message.author in users:
							preaction2 = (r, ctx.message.author)
		await self.bot.add_reaction(message2,self.member2emojiobjs['nocancel'])

		await asyncio.sleep(.5)
		while True:
			if preaction2 == None:
				memberreaction = await self.bot.wait_for_reaction(emoji=memberemojiobjs,timeout=30,message=message2, user=ctx.message.author)#, check=
			else:
				memberreaction = preaction2
			preaction2 = None
			message2 = await self.bot.get_message(message2.channel, message2.id)
			if memberreaction==None:
				await self.bot.edit_message(message2,new_content=message2.content+' Timed out, UI exited.')
				return
			memberuser = memberreaction[1]
			memberreaction = memberreaction[0]
			memberremoji = memberreaction.emoji
			currentemoji = memberreaction.emoji
			try:
				if currentemoji.name == 'nocancel':
					await self.bot.edit_message(message2,new_content=message2.content+' {} button clicked, UI exited.'.format(memberremoji))
				try:
					await self.bot.delete_message(numbermsg)
				except:
					pass
				if currentemoji.name == 'nocancel':
					return

			except AttributeError:
				pass
			try:
				await self.bot.delete_message(numbermsg)
			except:
				pass
			numbermsg = await self.bot.say('\u200b')
			memberremojiname = self.emojiobjs2member[memberremoji]
			try:
				members2display = getattr(clan, 'sorted'+memberremojiname)
			except:
				pass
			if type(members2display) != type(list()):
				members2display = [members2display]
			member_data = self.members2formatted(members2display)
			em = []
			membertype = memberremojiname
			currentdesc = "**{}** *{}*\n".format(len(members2display), self.reactionemojishelpinfo[membertype])
			# if len(clan_data)>0:
			#   # emtitle = clan.name
			#   # if membertype != None:
			#       # emtitle += '\n{} {}s'.format(len(members2display), membertype)
			#   e = discord.Embed(url=clan.url, title="{}".format(clan.name), description='{}{}'.format(currentdesc, '\n'.join(data)),color = discord.Color(0x50d2fe))
			#   em.append(e)
			# names = []
			# for data in member_data:
			#   l = []
			#   for x in data:
			#       l.append(x[x.find('`',2)+1:x.find('[`')].strip())
			#   names.append(l)
			# for i, n in enumerate(names):
			#   names[i] = sorted(n, key=lambda s:s.lower())
			# # print('\n\n\n\nNAMES:\n')
			# allnames = []
			# for n in names:
			#   for x in n:
			#       allnames.append(x)
			# # print(allnames)
			# # print('\n\n\n\nEND NAMES\n')
			# allnames = sorted(allnames, key=lambda s:s.lower())
			# alldata = []
			# for data in member_data:
			#   for x in data:
			#       alldata.append(x)
			# sorteddata = []
			# templist = []
			# for index, name in enumerate(allnames):
			#   # print(name)
			#   for data in alldata:
			#       # print(data)
			#       x = data
			#       if name == x[x.find('`',2)+1:x.find('[`')].strip():
			#           # print('found')
			#           templist.append(data)
			#           break
			#   if len(templist)==13:
			#       sorteddata.append(templist)
			#       templist = []
			# if len(templist)>0:
			#   sorteddata.append(templist)
			# print('\n\n\ndata\n')
			# for data in sorteddata:
			#   print(data)
			# print(len(sorteddata))
			# print('\n\n\ndata\n')

			n = 0
			for data in member_data:
					# emtitle = clan.name
					# if membertype != None:
					#   emtitle += '\n{} {}s'.format(len(members2display), membertype)
					sortedmembers = getattr(clan, 'sorted'+membertype)
					# print('penismaker')
					if type(sortedmembers) != type(list()):
						sortedmembers = [sortedmembers]
					print(sortedmembers)
					membersbefore = 0
					for d in member_data[:n]:
						membersbefore += len(d)
					firstmemindata = membersbefore+1
					# print(clan.members[])
					e = discord.Embed(url=clan.url, title="{}".format(clan.name), description='{}{}'.format(currentdesc, '\n'.join(data)),color = discord.Color(0x50d2fe))
					# print(members2display[membersbefore]['name'],members2display[membersbefore+len(data)-1]['name'])
					e.set_footer(text='showing page {}/{}, {}-{}, {} to {}'.format(n+1, len(member_data), firstmemindata,firstmemindata+len(data)-1, sortedmembers[membersbefore]['name'] ,sortedmembers[membersbefore+len(data)-1]['name']))
					em.append(e)
					n += 1
			if len(em)>1:
				await self.bot.edit_message(numbermsg, new_content='Which page would you like to get?')
				for e in onetofour[:len(em)]:
					await self.bot.add_reaction(numbermsg, self.number2emojis[e])
				await self.bot.add_reaction(numbermsg, self.cremojiobjs['nocancel'])
				while True:
					numreaction = await self.bot.wait_for_reaction(emoji=list(self.number2emojis.values())+[self.cremojiobjs['nocancel']],timeout=30,message=numbermsg, user=ctx.message.author)
					if numreaction==None:
						await self.bot.edit_message(numbermsg,new_content=numbermsg.content+' Timed out, UI exited.')
						await self.bot.edit_message(message2,new_content=message2.content+' Timed out, UI exited.')
						return

					numreaction = list(numreaction)
					
					numuser = numreaction[1]
					numreaction = numreaction[0]
					try:
						if  numreaction.emoji.name=='nocancel':
							await self.bot.delete_message(numbermsg)
							numbermsg = await self.bot.say('\u200b')
							break
					except AttributeError:
						pass
					await self.bot.remove_reaction(numbermsg, numreaction.emoji, numuser)
					for e in self.number2emojis:
						if self.number2emojis[e]==numreaction.emoji:
							numreaction = e
							break
					pagenum = self.word2num[numreaction]
					e = em[pagenum-1]
					await self.bot.edit_message(numbermsg,embed=e)
			else:
				await self.bot.edit_message(numbermsg,embed=em[0])


	def elements2data(self, elements2display, fclan):
		clan_data = []
		clan_datadict = {}
		for ele in elements2display:
			# print(ele)
			thing = getattr(fclan,ele)
			# print(type(thing)==type([]))
			# print(thing)
			# print('\n')
			# print('i am {}'.format(type(thing)))
			if type(thing) == type(list()):
				clan_datadict[ele]=getattr(fclan, ele)
				clan_data.append(getattr(fclan, ele))

			else:
				thing = str(thing)
				clan_datadict[ele] = getattr(fclan, ele)
				clan_data.append(getattr(fclan, ele))
		return [clan_datadict, clan_data]

	def data2embed(self, user, clan, clan_data, clan_datadict, elements2display):
		try:
			discordname = user.name if user.nick is None else user.nick
		except:
			discordname = user.name
		# specembeds = {}
		em = discord.Embed(title=clan.name,url=clan.url, color = discord.Color(0x50d2fe))
		em.set_thumbnail(url=clan.badge)
		em.set_author(icon_url=user.avatar_url,name=discordname)
		em.set_footer(text='Data provided by CR-API', icon_url='https://i.imgur.com/Grj2j6D.png')
		n = 0
		ele2title = {}
		for e in self.emojis2specembeds:
			bean = self.emojis2specembeds[e]
			if type(bean) == type(list()):
				for b in bean:
					ele2title[b] = self.reactionemojishelpinfo[b]
			else:
				ele2title[bean] = self.reactionemojishelpinfo[e]

		for ele in elements2display:
			chars = 0
			# print(type(self.clan_datadict[ele]), self.clan_datadict[ele])
			cele = ele
			tempe = discord.Embed(title=clan.name,url=clan.url, color = discord.Color(0x50d2fe))
			tempe.set_thumbnail(url=clan.badge)
			tempe.set_author(icon_url=user.avatar_url,name=discordname)
			tempe.set_footer(text='Data provided by CR-API', icon_url='https://i.imgur.com/Grj2j6D.png')
			inline = not( cele == 'seasons' or cele == 'games')
			if type(ele) == type(list()):
				for e in ele:
					if type(clan_datadict[e]) == type(list()):
						for d in clan_datadict[e]:
							chars += len(d)
						# if chars >256:
						#   if cele == 'stats':
						#       tempe.add_field(name = cele.title(), value = '\n'.join(self.clan_datadict[ele][:int(len(self.clan_datadict[ele])/2)]), inline=False)
						#   else:
						#       em.add_field(name = cele.title(), value = '\n'.join(self.clan_datadict[ele][:int(len(self.clan_datadict[ele])/2)]), inline=inline)
						#   em.add_field(name = '\u200b', value = '\n'.join(self.clan_datadict[ele][int(len(self.clan_datadict[ele])/2):]),inline=inline)
						#   if cele == 'stats':
						#       tempe.add_field(name = cele.title(), value = '\n'.join(self.clan_datadict[ele][:int(len(self.clan_datadict[ele])/2)]), inline=False)
						#   else:
						#       tempe.add_field(name = cele.title(), value = '\n'.join(self.clan_datadict[ele][:int(len(self.clan_datadict[ele])/2)]), inline=inline)
						#   tempe.add_field(name = '\u200b', value = '\n'.join(self.clan_datadict[ele][int(len(self.clan_datadict[ele])/2):]),inline=inline)
						if False:
							pass
						else:
							# print(ele2title[e])
							# print(clan_datadict[e])
							em.add_field(name = ele2title[cele], value = '\n'.join(clan_datadict[e]),inline=inline)
							tempe.add_field(name = ele2title[cele], value = '\n'.join(clan_datadict[e]),inline=inline)
					elif type(clan_datadict[e]) == type('str'):
						chars += len(clan_datadict[e])
						em.add_field(name = ele2title[e], value = clan_datadict[e])
						tempe.add_field(name = ele2title[e], value = clan_datadict[e])
					# specembeds[cele] = tempe
					n+=1

			elif type(clan_datadict[ele]) == type(list()):
				for d in clan_datadict[ele]:
					chars += len(d)
				# if chars >256:
				#   if cele == 'stats':
				#       tempe.add_field(name = cele.title(), value = '\n'.join(self.clan_datadict[ele][:int(len(self.clan_datadict[ele])/2)]), inline=False)
				#   else:
				#       em.add_field(name = cele.title(), value = '\n'.join(self.clan_datadict[ele][:int(len(self.clan_datadict[ele])/2)]), inline=inline)
				#   em.add_field(name = '\u200b', value = '\n'.join(self.clan_datadict[ele][int(len(self.clan_datadict[ele])/2):]),inline=inline)
				#   if cele == 'stats':
				#       tempe.add_field(name = cele.title(), value = '\n'.join(self.clan_datadict[ele][:int(len(self.clan_datadict[ele])/2)]), inline=False)
				#   else:
				#       tempe.add_field(name = cele.title(), value = '\n'.join(self.clan_datadict[ele][:int(len(self.clan_datadict[ele])/2)]), inline=inline)
				#   tempe.add_field(name = '\u200b', value = '\n'.join(self.clan_datadict[ele][int(len(self.clan_datadict[ele])/2):]),inline=inline)
				if False:
					pass
				else:
					# print(ele2title[ele])
					# print(clan_datadict[ele])
					em.add_field(name = ele2title[cele], value = '\n'.join(clan_datadict[ele]),inline=inline)
					tempe.add_field(name = ele2title[cele], value = '\n'.join(clan_datadict[ele]),inline=inline)
			elif type(clan_datadict[ele]) == type('str'):
				chars += len(clan_datadict[ele])
				em.add_field(name = ele2title[ele], value = clan_datadict[ele])
				tempe.add_field(name = ele2title[ele], value = clan_datadict[ele])
			# specembeds[cele] = tempe
			n+=1

		return em

	@commands.command(pass_context=True)
	async def reactiontest(self,ctx):
		print(self.penis)
		await self.bot.add_reaction(ctx.message, '😄')
		await asyncio.sleep(.5)
		reaction = await self.bot.wait_for_reaction(emoji='😄',timeout=30,message=ctx.message,user=ctx.message.author)
		reaction = list(reaction)
		user = reaction[1]
		reaction = reaction[0]
		await self.bot.say(reaction.emoji+ user.name)
		
	@clan.command(name='emoji', aliases=['e', 'em'],  pass_context=True)
	async def _emoji(self, ctx, userortag=None):
		"""Get user trophies. If not given a user, get author's data"""
		#fix user, player, player_data, player_data, player_datadict
		print
		try:
			tag = await self.keyortag2tag(userortag, ctx)
		except ErrorKeyortag as e:
			await self.bot.say(e.msg)
			return
		user = ctx.message.author
		# print('in _emoji')
		# print(tag)
		clan = await CRClan.create(tag)
		fclan = clan[1]
		clan = clan[0]
		elements = []
		elements2display  = [
			'tag',
			'desc2',
			'clan_trophy',
			# 'members',
			# 'coleaders',
			# 'leader',
			# 'norole',
			# 'elders',
			'donperweek',
			'parsedtr_req'

		]
		done = [
			'desc', 'create', '_url', 'url', 'name', 'member_count', 'donperweek', 'parsedtr_req'
		]
		for e in dir(clan):
			if '__' not in e and e not in elements2display and e not in done:
				print(e, getattr(clan, e))
		# return
		print(fclan.tag)
		things = self.elements2data(elements2display, fclan)
		clan_datadict = things[0]
		print(clan_datadict)
		clan_data = things[1]
		# print('{}\n{}'.format(fclan.stats, type(fclan.stats)))
		specembeds = {}
		em = self.data2embed(user, clan, clan_data, clan_datadict, elements2display)
		await self.bot.say(embed=em)
		# for key in specembeds:
		#   await self.bot.say(embed=specembeds[key])
		message = await self.bot.say("React to this for clan stats! click {} for help.".format(self.reactionemojis['helpinfo']))
		message2 = await self.bot.say('\u200b')
		await self.reactembeds(ctx, [message, message2], clan, clan_data, clan_datadict)
		# em.set_author(icon_url=user.avatar_url,name=discordname)
		# em.set_thumbnail(url=clan.clan.badge)
		# em.set_footer(text='Data provided by CR-API', icon_url='https://i.imgur.com/Grj2j6D.png')
		# await self.bot.say(embed=em)

	@clan.command(name='members', aliases=['m'],  pass_context=True)
	async def _members(self, ctx, *, args=None):
		"""get clan members of user, tag, etc, otherwise get author clan members.
		syntax:
		you can do l or lead or leader, c or co or coleaders,
		e or eld or elders, n or no or norole, a or all
		| means or, which means you can put username or usermention or etc in that spot
		clan members "username"|usermention|userid|clantag -l -c -e -n -a
		If using single characters, you may combine in one -letters rather than -l -e -t ...
		if -a is in the list, it will only display for that option(all members)
		"""
		userortag = None
		if args == None:
			await send_cmd_help(ctx)
			return
		code2element = {
			'l':'leader',
			'lead':'leader',
			'leader':'leader',
			'c':'coleaders',
			'co':'coleaders',
			'coleaders':'coleaders',
			'e':'elders',
			'eld':'elders',
			'elders':'elders',
			'n':'norole',
			'no':'norole',
			'norole':'norole',
			'a':'members',
			'all':'members'
		}
		elements2display = []
		elements = []
		possUserortag = []
		print('args:')
		for x  in args.strip().split():
			print(x, type(x))
			if x.startswith('-'):
				elements.append(x[1:])
			else:
				print('hi')
				possUserortag.append(x)
		print(elements,'\n', possUserortag)
		errors = []
		for uort in possUserortag:
			try:
				tag = await self.keyortag2tag(uort, ctx)
			except ErrorKeyortag as e:
				errors.append(e.msg)
				possUserortag.remove(uort)

		list2print = ['\n',', '.join(elements), ', '.join(possUserortag), ', '.join(errors)]
		print('\n'.join(list2print))
		if len(errors) == len(possUserortag) and len(possUserortag)>0:
			await self.bot.say('\n'.join(errors))
			return

		errors2 = []
		valid = True
		uniquechars = []
		things = ''.join(elements)
		for e in things:
			for l in e:
				if l not in uniquechars:
					uniquechars.append(l)
		
		for e in uniquechars:
			if e not in ['l','c','e','n','a'] and len(elements)==1:
				valid = False
				break
		for e in elements:
			try:
				if code2element[e] not in elements2display:
					if code2element[e] == 'members':
						elements2display = [code2element[e]]
						break
					elements2display.append(code2element[e])
			except KeyError:
				if valid:
					print('hi i exist')
					elements = list(uniquechars)
					if 'a' in elements:
						elements = ['a']
					elements2display = []
					for e in elements:
						elements2display.append(code2element[e])
				else:
					errors2.append("{} is not a stated member code.")
		print(elements)
		if len(errors2) >0:
			await self.bot.say("{}{}{}".format('\n'.join(errors2), '\n', "The acceptable codes are: {}".format(', '.join(code2element.keys()))))
		if len(possUserortag)>1: 
			await self.bot.say("Using first thing for tag creation.")
		elif len(possUserortag) == 0:
			possUserortag.append(ctx.message.author.id)
		tag = await self.keyortag2tag(possUserortag[0], ctx)
		print('\n')
		print(tag)
		print('\n', '\n'.join(list2print))

		user = ctx.message.author
		# print('in _emoji')
		# print(tag)
		clan = await CRClan.create(tag)
		fclan = clan[1]
		clan = clan[0]
		elements = []
		# return
		# print(fclan.tag)
		# things = self.elements2data(elements2display, fclan)
		# clan_datadict = things[0]
		# print(clan_datadict)
		# clan_data = things[1]
		# print('{}\n{}'.format(fclan.stats, type(fclan.stats)))
		# specembeds = {}
		# em = self.data2embed(user, clan, clan_data, clan_datadict, elements2display)
		members2display = []
		descmemtype = []
		try:
			for membertype in elements2display:
				descmemtype.append(membertype)
				thing = getattr(clan, 'sorted'+membertype)
				if type(thing)!=type(list()):
					thing = [thing]
				print(thing)
				members2display.extend(thing)
		except:
			pass
		if type(members2display) != type(list()):
			members2display = [members2display]
		member_data = self.members2formatted(members2display)
		em = []
		print(descmemtype)
		descmemtype = list(map(lambda x: self.reactionemojishelpinfo[x], descmemtype))
		print(descmemtype)
		currentdesc = "**{}** *{}*\n".format(len(members2display), ', '.join(descmemtype))
		n = 0
		for data in member_data:
				# emtitle = clan.name
				# if membertype != None:
				#   emtitle += '\n{} {}s'.format(len(members2display), membertype)
				sortedmembers = getattr(clan, 'sorted'+membertype)
				# print('penismaker')
				if type(sortedmembers) != type(list()):
					sortedmembers = [sortedmembers]
				# print(sortedmembers)
				membersbefore = 0
				for d in member_data[:n]:
					membersbefore += len(d)
				firstmemindata = membersbefore+1
				# print(clan.members[])
				if n == 0:
					description = '{}{}'.format(currentdesc, '\n'.join(data))
				else:
					description ='{}'.format('\n'.join(data))
				e = discord.Embed(url=clan.url, title="{}".format(clan.name), description=description,color = discord.Color(0x50d2fe))
				# print(members2display[membersbefore]['name'],members2display[membersbefore+len(data)-1]['name'])
				if n+1==len(member_data):
					e.set_footer(text='Data provided by CR-API', icon_url='https://i.imgur.com/Grj2j6D.png')
					# e.set_footer(text='Info Provided by CR-API'.format(n+1, len(member_data), firstmemindata,firstmemindata+len(data)-1, sortedmembers[membersbefore]['name'] ,sortedmembers[membersbefore+len(data)-1]['name']))
				em.append(e)
				n += 1
		for e in em:
			await self.bot.say(embed=e)


		
	@clan.command(name='membersemoji', aliases=['memojis'],  pass_context=True)
	async def _membersemoji(self, ctx, userortag=None):
		"""Get user trophies. If not given a user, get author's data"""
		#fix user, player, player_data, player_data, player_datadict
		try:
			tag = await self.keyortag2tag(userortag, ctx)
		except ErrorKeyortag as e:
			await self.bot.say(e.msg)
			return
		if tag == None:
			return
		user = ctx.message.author
		print('in _emoji')
		print(tag)
		clan = await CRClan.create(tag)
		fclan = clan[1]
		clan = clan[0]
		elements = []
		elements2display  = [
			'tag',
			'desc2',
			'clan_trophy',
			'members',
			'coleaders',
			'leader',
			'norole',
			'elders'
		]
		print(fclan.tag)
		things = self.elements2data(elements2display, fclan)
		clan_datadict = things[0]
		print(clan_datadict)
		clan_data = things[1]
		# print('{}\n{}'.format(fclan.stats, type(fclan.stats)))
		specembeds = {}
		em = self.data2embed(user, clan, clan_data, clan_datadict, elements2display)
		# for key in specembeds:
		#   await self.bot.say(embed=specembeds[key])
		message = await self.bot.say("Which role would you like to get (sorted alphabetically)".format(self.reactionemojis['helpinfo']))
		message2 = await self.bot.say('\u200b')
		await self.reactembedsmembers(ctx, [message, message2], clan, clan_data, clan_datadict)
		# em.set_author(icon_url=user.avatar_url,name=discordname)
		# em.set_thumbnail(url=clan.clan.badge)
		# em.set_footer(text='Data provided by CR-API', icon_url='https://i.imgur.com/Grj2j6D.png')
		# await self.bot.say(embed=em)



	

def check_folder():
	if not os.path.exists(PATH):
		os.makedirs(PATH)

def check_file():
	defaults = {}
	if not dataIO.is_valid_json(SETTINGS_JSON):
		dataIO.save_json(SETTINGS_JSON, defaults)
	if not dataIO.is_valid_json(CLAN_JSON):
		dataIO.save_json(CLAN_JSON, defaults)
	if not dataIO.is_valid_json(BACKSETTINGS_JSON):
		dataIO.save_json(BACKSETTINGS_JSON, defaults)
	if not dataIO.is_valid_json(CREMOJIS_JSON):
		dataIO.save_json(CREMOJIS_JSON, defaults)

def setup(bot):
	check_folder()
	check_file()
	bot.add_cog(CRTags(bot))