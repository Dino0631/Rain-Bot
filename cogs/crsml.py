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
cremojis = {}
cremojilist = []
cremojiobjs = {}
refreshemoji = '🔄'
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
	"eSports",
	"Foxtrot",
	"Golf",
	"Hotel",
	"Mini",
	"Mini2"
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
		self.member_count = 0                           #done
		self.members = []                               #done
		self.clan_tag = ''                             #done
		self._url = ''
		self.url = '' 			#done
		self.tr_req = '0'                               #done
		self.clan_trophy = ''                           #done
		self.name = ''                                  #done
		self.donperweek = ''							#done
		self.desc = ''									#done
		self.badge = ''									#done
		self.leader = {}								#done
		self.size = 0									#done
		self.coleaders = []								#done
		self.elders = []								#done
		self.norole = []								#done
		self.clan_badge = ''
		self.name = ''
		self.desc = ''
		self.desc2 = ''
		self.clan_trophy = ''
		self.tr_req = ''
		self.donperweek = ''
		self.badge = ''

	@classmethod
	async def create(self, tag):
		tag2id = dataIO.load_json(BACKSETTINGS_JSON)
		formatted = CRClan()
		self.member_count = 0                           #done
		self.members = []                               #done
		formatted.members = ['All Members']
		self.clan_tag = tag                             #done
		formatted.clan_tag = tag
		self._url = crapiurl + '/clan/' + tag       	#done
		formatted._url = crapiurl + '/clan/' + tag
		self.url = crapi_url + '/clan/' + tag 			#done
		formatted.url = crapi_url + '/clan/' + tag
		self.tr_req = '0'                               #done
		self.clan_trophy = ''                           #done
		self.name = ''                                  #done
		self.donperweek = ''							#done
		self.desc = ''									#done
		self.badge = ''									#done
		self.leader = {}								#done
		self.size = 0									#done
		self.coleaders = []								#done
		formatted.coleaders = ['Coleaders:']
		self.elders = []								#done
		formatted.elders = ['Elders:']
		self.norole = []								#done
		formatted.norole = ["No Role:"]
		# if clan_url != '':
		async with aiohttp.ClientSession() as session:
			async with session.get(self._url) as resp:
				# print(await resp.read())
				clandatadict = await resp.json()
		# print(clandatadict)
		# for x in clandatadict:
		# 	try:
		# 		print(x)
		# 	except:
		# 		print('some key')
		# 	try:
		# 		print(clandatadict[x])
		# 	except:
		# 		print('some value')
		# for member in clandatadict['members']:
		# 	try:
		# 		print(member)
		# 	except:
		# 		print('some member')
		# r = requests.get(self.clan_url, headers=headers)
		# html_doc = r.text
		formattedmembers = []
		members = []
		print(clandatadict)
		print("members in clandatadict?", 'members' in clandatadict)
		for data in clandatadict:
			print('H{}H'.format(data))
			print(data == 'members')
			if data == 'members':
				members = clandatadict[data]
			# if type(clandatadict[data]) == type(1):
			# 	clandatadict[data] = str(clandatadict[data])
			# print(data, ':', clandatadict[data])
		print(len(members))
		i = 0
		for  m in members:
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
			memberdict['formatted'] = '`'+ memberdict['role']+'` ' + memberdict['name']+' [`#'+memberdict['tag']+'`]('+memberdict['url'].replace('api.', '', 1)+')'
			if memberdict['userid'] != '':
				try:
					memberdict['formatted'] += ' <@'+memberdict['userid'] + '>'
				except:
					pass
				formattedmembers.append(memberdict['formatted'])
			if memberdict['role'] == 'Co-Leader':
				self.coleaders.append(memberdict)
			formatted.coleaders.extend(memberdict)
			if memberdict['role'] == 'Member':
				self.norole.append(memberdict)
			formatted.norole.extend(memberdict)
			if memberdict['role'] == 'Elder':
				self.elders.append(memberdict)
			formatted.elders.extend(memberdict)
			if memberdict['role'] == 'Leader':
				self.leader = memberdict
				formatted.leader = memberdict
			self.size += 1
			self.members.append(memberdict)
			i+= 1

		formatted.members = formattedmembers
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
		self.donperweek = clandatadict['donations']
		formatted.donperweek = "Donations this week: {}".format(str(self.donperweek))
		self.badge = crapi_url +'/static/img'+ clandatadict['badge_url']
		return [self, formatted]

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
				datadict = await resp.json()
		if 'error' in datadict:
			datadict = {"tag":"V82UVQV","name":"GhostlyDino","trophies":4709,"arena":{"imageURL":"/arena/league3.png","arena":"League 3","arenaID":14,"name":"Challenger III","trophyLimit":4600},"legendaryTrophies":614,"nameChanged":False,"globalRank":null,"clan":{"tag":"LGVV2CG","name":"Reddit Echo","role":"Co-Leader","badgeUrl":"/badge/A_Char_Rocket_02.png"},"experience":{"level":12,"xp":12549,"xpRequiredForLevelUp":80000,"xpToLevelUp":67451},"stats":{"legendaryTrophies":614,"tournamentCardsWon":895,"maxTrophies":5064,"threeCrownWins":849,"cardsFound":76,"favoriteCard":"mortar","totalDonations":36783,"challengeMaxWins":20,"challengeCardsWon":48674,"level":15},"games":{"total":5819,"tournamentGames":258,"wins":2496,"losses":1516,"draws":1807,"currentWinStreak":2},"chestCycle":{"position":1170,"superMagicalPos":1374,"legendaryPos":1196,"epicPos":1991},"shopOffers":{"legendary":23,"epic":2,"arena":6},"currentDeck":[{"name":"ice_spirit","rarity":"common","level":12,"count":1722,"requiredForUpgrade":5000,"leftToUpgrade":3278},{"name":"arrows","rarity":"common","level":11,"count":3866,"requiredForUpgrade":2000,"leftToUpgrade":-1866},{"name":"knight","rarity":"common","level":12,"count":3075,"requiredForUpgrade":5000,"leftToUpgrade":1925},{"name":"archers","rarity":"common","level":12,"count":1513,"requiredForUpgrade":5000,"leftToUpgrade":3487},{"name":"the_log","rarity":"legendary","level":2,"count":1,"requiredForUpgrade":4,"leftToUpgrade":3},{"name":"mortar","rarity":"common","level":12,"count":2853,"requiredForUpgrade":5000,"leftToUpgrade":2147},{"name":"rocket","rarity":"rare","level":9,"count":314,"requiredForUpgrade":800,"leftToUpgrade":486},{"name":"bats","rarity":"common","level":12,"count":1140,"requiredForUpgrade":5000,"leftToUpgrade":3860}],"previousSeasons":[{"seasonNumber":6,"seasonHighest":4949,"seasonEnding":4886,"seasonEndGlobalRank":null},{"seasonNumber":5,"seasonHighest":4652,"seasonEnding":4617,"seasonEndGlobalRank":null},{"seasonNumber":4,"seasonHighest":4911,"seasonEnding":4911,"seasonEndGlobalRank":null},{"seasonNumber":3,"seasonHighest":5064,"seasonEnding":4913,"seasonEndGlobalRank":null},{"seasonNumber":2,"seasonHighest":4899,"seasonEnding":4804,"seasonEndGlobalRank":null},{"seasonNumber":1,"seasonHighest":4808,"seasonEnding":4508,"seasonEndGlobalRank":null}]}
		# if 'error' in datadict:
		# 	await StatsCRPlayer.create(tag)
		# 	defaultdatadict = {"tag":"","name":"","trophies":'',"arena":
		# 	{"imageURL":"","arena":"","arenaID":'',
		# 	"name":"","trophyLimit":''},"legendaryTrophies":'',
		# 	"nameChanged":'',"globalRank":'',"clan":
		# 	{"tag":"",
		# 	"name":"","role":"","badgeUrl":""},
		# 	"experience":
		# 	{"level":'',"xp":'',"xpRequiredForLevelUp":'',
		# 	"xpToLevelUp":''},"stats":
		# 	{"legendaryTrophies":'',"tournamentCardsWon":'',
		# 	"maxTrophies":'',"threeCrownWins":'',"cardsFound":'',"favoriteCard":"mortar",
		# 	"totalDonations":'',"challengeMaxWins":'',"challengeCardsWon":'',"level":''},
		# 	"games":
		# 	{"total":'',"tournamentGames":'',"wins":'',"losses":'',"draws":'',"currentWinStreak":9},"chestCycle":
		# 	{"position":'',"superMagicalPos":'',"legendaryPos":'',"epicPos":''},"shopOffers":
		# 	{"legendary":'',"epic":'',"arena":''},"currentDeck":[
		# 	{"name":"","rarity":"","level":'',"count":'',"requiredForUpgrade":'',"leftToUpgrade":''},
		# 	{"name":"","rarity":"","level":'',"count":'',"requiredForUpgrade":'',"leftToUpgrade":''},
		# 	{"name":"","rarity":"","level":'',"count":'',"requiredForUpgrade":'',"leftToUpgrade":''},
		# 	{"name":"","rarity":"","level":'',"count":'',"requiredForUpgrade":'',"leftToUpgrade":''},
		# 	{"name":"","rarity":"","level":'',"count":'',"requiredForUpgrade":'',"leftToUpgrade":''},
		# 	{"name":"","rarity":"","level":'',"count":'',"requiredForUpgrade":'',"leftToUpgrade":''},
		# 	{"name":"","rarity":"","level":'',"count":'',"requiredForUpgrade":'',"leftToUpgrade":''},
		# 	{"name":"","rarity":"","level":'',"count":'',"requiredForUpgrade":'',"leftToUpgrade":''}],"previousSeasons":[
		# 	{"seasonNumber":'',"seasonHighest":'',"seasonEnding":'',"seasonEndGlobalRank":''},
		# 	{"seasonNumber":'',"seasonHighest":'',"seasonEnding":'',"seasonEndGlobalRank":''},
		# 	{"seasonNumber":'',"seasonHighest":'',"seasonEnding":'',"seasonEndGlobalRank":''},
		# 	{"seasonNumber":'',"seasonHighest":'',"seasonEnding":'',"seasonEndGlobalRank":''},
		# 	{"seasonNumber":'',"seasonHighest":'',"seasonEnding":'',"seasonEndGlobalRank":''},
		# 	{"seasonNumber":'',"seasonHighest":'',"seasonEnding":'',"seasonEndGlobalRank":''}]}
		# 	datadict = defaultdatadict
		# 	# for data in datas:
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



class StatsCRPlayer:


	def __init__(self):
		self.a = 4

	@classmethod
	async def create(self, tag):
		self.clan_badge = ''                 #done

		self.name = ''                       #done
		self.level = ''                      #done
		self.clan = ''                       #done
		self.prevseasontrophy = ''           #done
		self.crown3 = ''                     #done
		self.prevseasonpb = ''               #done
		self.wins = ''                       #done
		self.cardswon = ''                   #done
		self.losses = ''                     #done
		self.league = ''                     #done
		self.prevseasonrank = ''             #done
		self.donations = ''                  #done
		self.trophy = ''                     #done
		self.tcardswon = ''                  #done
		self.pb = ''                         #done
		self.chests = ''                     #done

		asyncio.sleep(1)
		user_url = 'http://statsroyale.com/profile/'+tag
		await async_refresh(user_url+'/refresh')
		r = requests.get(user_url, headers=headers)
		html_doc = r.content
		soup = BeautifulSoup(html_doc, "html.parser")
		print(soup.prettify())
		chests_queue = soup.find('div', {'class':'chests__queue'})
		chests = chests_queue.get_text().split()
		for index, item in enumerate(chests):
			if item.startswith('+') and item.endswith(':'):
				del chests[index]
			elif item == 'Chest':
				del chests[index]
			if item == 'Super':
				chests[index] = 'SMC'
			elif item == 'Magic':
				chests[index] = 'Magical'

		for index, chest in enumerate(chests):
			if str(chest) == 'Magic':
				chests[index] = 'Magical'
			elif str(chest) == 'Super':
				chests[index] = 'SMC'
		new_chests = []
		x = 0
		while x<len(chests):
			new_chests.append(chests[x:x+2])
			x += 2
		chests = []


		for index, chest in enumerate(new_chests):
			chests.append(': '.join(chest))

		self.chests = '\n'.join(chests)

		soup = BeautifulSoup(html_doc, "html.parser")
		profilehead = soup.find_all("div", "profileHeader profile__header")
		statistics = soup.find_all("div", "statistics profile__statistics")
		profilehead = profilehead[0]
		statistics = statistics[0]
		thing2 = statistics.get_text()
		thing2 = thing2.replace('\n', ' ')
		thing2 = thing2.split('   ')
		for index, item in enumerate(thing2):
			thing2[index] = item.strip()
		statsdict = {}
		for index, item in enumerate(thing2):
			if item[:item.find(' ')].isdigit():
				thing2[index] = item[item.find(' ')+1:]+ ': '+item[:item.find(' ')]
				statsdict[item[item.find(' ')+1:].strip()] = item[:item.find(' ')] 
			else:
				statsdict[item.strip()] = ' '
			thing2[index].strip()

		pb = thing2[0]
		trophy = thing2[1]
		cardswon = thing2[2]
		tcardswon = thing2[3]
		donations = thing2[4]
		prevseasonrank = thing2[5]
		prevseasontrophy = thing2[6]
		prevseasonpb = thing2[7]
		wins = thing2[8]
		losses = thing2[9]
		crown3 = thing2[10]
		league = thing2[11]
		try:
			clan_url = statsurl + str(profilehead.find('a').attrs['href'])
		except AttributeError:
			clan_url  = ''
		playerLevel = profilehead.find('span', 'profileHeader__userLevel')
		playerLevel = playerLevel.text
		playerName = profilehead.find('div', 'ui__headerMedium profileHeader__name').text.strip()
		playerName = playerName.replace(playerLevel, '').strip()
		try:
			playerClan = profilehead.find('a', 'ui__link ui__mediumText profileHeader__userClan').text.strip()
		except AttributeError:
			playerClan  = 'No Clan'
		playerTag = tag
		clan_badge = profilehead.find('img').attrs['src']
		clan_badge = statsurl + clan_badge
		self.clan_badge = clan_badge
		player_data = []
		player_data.append('[#{}]({})'.format(tag, user_url))
		for x in statsdict:
			if(statsdict[x].isdigit()):
				statsdict[x] = '[' + statsdict[x] + '](http://)'
		for x in statsdict:
			if 'League' in x:
				self.league = x
			elif 'Highest trophies' in x:
				self.pb = statsdict[x]
			elif'Last known trophies' in x:
				self.trophy = statsdict[x]
			elif 'Challenge cards won' in x:
				self.cardswon = statsdict[x]
			elif 'Tourney cards won' in x:
				self.tcardswon = statsdict[x]
			elif 'Total donations' in x:
				self.donations = statsdict[x]
			elif 'Prev season rank' in x:
				self.prevseasonrank = statsdict[x]
			elif 'Prev season trophies' in x:
				self.prevseasontrophy = statsdict[x]
			elif 'Prev season highest' in x:
				self.prevseasonpb = statsdict[x]
			elif 'Wins' in x:
				self.wins = statsdict[x]
			elif 'Loses' in x:
				self.losses = statsdict[x]
			elif '3 crown wins' in x:
				self.crown3 = statsdict[x]
		self.name = playerName
		self.level = playerLevel
		self.clan = playerClan
		self.clan_url = clan_url
		return self

class InvalidRarity(Exception):
	pass
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

class CRTags:

	def __init__(self, bot):
		
		self.settings = dataIO.load_json(SETTINGS_JSON)
		self.backsettings = dataIO.load_json(BACKSETTINGS_JSON)
		self.clansettings = dataIO.load_json(CLAN_JSON)
		self.bot = bot
		self.author = None
		self.player_data = []
		self.player_datadict = {}
		self.user = None
		self.currentemojiobjs = []
		cremojis = self.allemojis = dataIO.load_json(CREMOJIS_JSON)
		self.emojiservers = []
		for e in cremojis:
			cremojilist.append(cremojis[e])
		for server in self.bot.servers:
			for emoji in server.emojis:
				# print(emoji.name)
				cremojiobjs[emoji.name] = emoji
		
		self.reactionemojislist = [
			'levelbig',
			'trophy',
			'shop',
			'crownshield',
			'battle',
			'search',
			'social',
			'shopgranpagoblin',
			'rank',
			'deck',
		]
		self.utilreactionemojislist = [
			'nocancel',
			'refresh',
			'helpinfo'
		]
		self.reactionemojishelpinfo = {
			'levelbig': 'Experience',
			'trophy': 'Current Trophies',
			'shop': 'Chest Cycle',
			'crownshield': 'General Stats',
			'battle': 'Games',
			'search': 'Player Tag',
			'social': 'Clan',
			'shopgranpagoblin': 'Shop Offers',
			'rank': 'Seasons',
			'deck': 'Deck',
			'nocancel': 'Exit the UI',
			'refresh': 'Refresh the emoji options',
			'helpinfo': 'Shows This message'
		}
		self.reactionemojislist.extend(self.utilreactionemojislist)
		self.emojis2specembeds = {
			'levelbig':'xp',
			'trophy':'trophies',
			'shop':'chestcycle',
			'crownshield':'stats',
			'battle':'games',
			'search':'tag',
			'social':'clan',
			'shopgranpagoblin':'offers',
			'rank':'seasons',
			'deck':'deck'
		}
		self.reactionemojis = {}
		d = {}
		for e in self.reactionemojislist:
			# print(self.reactionemojis[e])
				d[e] = cremojiobjs[e]
		self.reactionemojis = d
		helptitle = "When an emoji is pressed, the embed will change. If you want to remove part of a player profile, unclick the emoji, and click the refresh emoji. Here are what the emojis show:"
		helpemojis = []
		for e in self.reactionemojislist:
			helpemojis.append("{}: {}".format(self.reactionemojis[e], self.reactionemojishelpinfo[e]))
		self.helpembed = discord.Embed(title=helptitle,description='\n'.join(helpemojis),color=discord.Color(0x50d2fe))

	@checks.is_owner()
	@commands.command(pass_context=True)
	async def bestwinstreak(self, ctx):
		highest = []

	@checks.is_owner()
	@commands.command(pass_context=True)
	async def initemojis(self, ctx):
		emojipath = os.path.join(PATH, 'images')
		emojicount = 0
		tempe = []
		allemojis = []
		print(type(emojipath))
		print(emojipath)
		print(dir(os.walk(emojipath)))
		emojiservers = ['','','','','']
		for server in self.bot.servers:
			if 'emojiserver ' in server.name:
				emojiservers[int(server.name[-1])-1] = server

		print('servers:')
		for s in emojiservers:
			print(s)
		print('\nfiles:')
		for root, dirs, files in os.walk(emojipath):
			path = root.split(os.sep)
			print((len(path) - 1) * '---', os.path.basename(root))
			n = 0
			for file in files:
				if '.png' in file:
					emojicount += 1
					print(file, emojicount)
					# print(dir(file))

					# print(type(file))
					# if file == 'watch.png':
					# 	print('hi')
					if len(tempe)<50:
						tempe.append(file)
						with open(os.path.join(emojipath,os.path.basename(root),file), 'rb') as f:
							# print(dir(f))
							# if len(tempe)==1:
							# 	await self.bot.send_file(ctx.message.channel, f)
							pass
					else:
						allemojis.append(tempe)
						tempe = [file]
					# print(len(allemojis))
					# print(len(path) * '---', file)
		if len(tempe)>0:
			allemojis.append(tempe)
		# print(allemojis)

		for l in allemojis:
			print(len(l))
			print(l)
			
		print(emojicount)
		# await self.bot.create_custom_emoji(ctx.message.server, name=emojiname, image=emoji)

	@checks.is_owner()
	@commands.command(pass_context=True, aliases=['emote','e'])
	async def emoji(self, ctx, *, msg):
		"""
		Embed or copy a custom emoji (from any server).
		Usage:
		1) >emoji :smug: [Will display the smug emoji as an image]
		2) >emoji copy :smug: [Will add the emoji as a custom emote for the server]
		"""
		copy_emote_bool = False
		if "copy " in msg:
			msg = msg.split("copy ")[1]
			copy_emote_bool = True
		if msg.startswith('s '):
			msg = msg[2:]
			get_server = True
		else:
			get_server = False
		msg = msg.strip(':')
		if msg.startswith('<'):
			msg = msg[2:].split(':', 1)[0].strip()
		url = emoji = server = None
		exact_match = False
		for server in self.bot.servers:
			for emoji in server.emojis:
				if msg.strip().lower() in str(emoji):
					url = emoji.url
					emote_name = emoji.name
				if msg.strip() == str(emoji).split(':')[1]:
					url = emoji.url
					emote_name = emoji.name
					exact_match = True
					break
			if exact_match:
				break
				
		response = requests.get(emoji.url, stream=True)
		name = emoji.url.split('/')[-1]
		with open(name, 'wb') as img:

			for block in response.iter_content(1024):
				if not block:
					break

				img.write(block)

		if url:
			try:
				if get_server:
					await self.bot.send_message(ctx.message.channel,
												'**ID:** {}\n**Server:** {}'.format(emoji.id, server.name))
				with open(name, 'rb') as fp:
					if copy_emote_bool:
						e = fp.read()
					else:
						await self.bot.send_file(ctx.message.channel, fp)
				if copy_emote_bool:
					try:
						await self.bot.create_custom_emoji(ctx.message.server, name=emote_name, image=e)
						embed = discord.Embed(title="Added new emote", color=discord.Color(0x50d2fe))
						embed.description = "New emote added: " + emote_name
						await self.bot.say("", embed=embed)
					except:
						await self.bot.say("Not enough permissions to do this")
				os.remove(name)
			except:
				await self.bot.send_message(ctx.message.channel, url)
		else:
			await self.bot.send_message(ctx.message.channel, 'Could not find emoji.')

		return await self.bot.delete_message(ctx.message)

	@checks.is_owner()
	@commands.command(pass_context=True)
	async def cremojiinit(self, ctx):
		emojiservers = []
		for server in self.bot.servers:
			emojiservers.append(server)
		cremojis = {}
		for server in emojiservers:
			for emoji in server.emojis:
				cremojis[emoji.name] = "<:{}:{}>".format(emoji.name,emoji.id)
		dataIO.save_json(CREMOJIS_JSON, cremojis)
		await self.bot.say("Initialized")


	async def keyortag2tag(self, keyortag, ctx):
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
		elif originalkey in members or originalkey in membernames or originalkey in memberswithdiscrim:	#if user in members
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
			await self.bot.say('`{}` is not in the database, nor is an acceptable tag.'.format(keyortag))
			return
		if userid != None:
			try:
				usertag = self.settings[userid]
			except KeyError:
				await self.bot.say("That person is not in the database")
				return None
			player = await CRPlayer.create(usertag)			
			tag = player[0].clan.url.replace(crapi_url,'').replace('/clan/', '')
			# print(tag)
		return tag



	def goldcalc(self, cardlvl):
		allgold = 0
		for rarity in cardlvl:
			for lvl in cardlvl[rarity]:
				allgold += totalupgrades[rarity][lvl]
				# totalgold[rarity] += totalupgrades[rarity][lvl]
		return allgold

	def lvlsdict(self, args):
		currentrarity = 'c'
		cardlvl = {
			'c':[],
			'r':[],
			'e':[],
			'l':[]
		}
		for x in args:
			if str(x).isalpha():
				if x in ['c', 'r', 'e', 'l']:
					currentrarity = x
				else:
					ex = InvalidRarity()
					raise ex
			elif str(x).isdigit():
				cardlvl[currentrarity].append(x)
		return cardlvl

	@commands.command(pass_context=True)
	async def gold(self, ctx, *, args):
		totalgold = {'c':0,'r':0,'e':0,'l':0,}
		allgold = 0
		cardlvl = {
			'c':[],
			'r':[],
			'e':[],
			'l':[]
		}
		msg = "It would cost a total of"
		msg2 = "gold to upgrade those cards"
		args = args.strip().split(' ')
		if 'max' in args:
			msg2 = "gold to upgrade all cards to max"
			args = []
			n = 0
			for rarity in numcards:
				args.append(rarity)
				while n < numcards[rarity]:
					args.append(str(maxcards[rarity]))
					n += 1
				n = 0
		if 'tourney' in args:
			msg2 = "gold to upgrade all cards to tourney standard"
			args = []
			n = 0
			for rarity in numcards:
				args.append(rarity)
				while n < numcards[rarity]:
					args.append(str(tourneycards[rarity]))
					n += 1
				n = 0
		if args.count('-') >1:
			await self.bot.say("too many minuses, limit is 1")
			return
		elif args.count('-') == 1:
			cardlvl = []
			allgold = []
			args = ' '.join(args).split('-')
			for index, arg in enumerate(args):
				args[index] = arg.strip().split(' ')
			for arg in args:
				while '' in arg:
					arg.remove('')

				for i, a in enumerate(arg):
					if a.isdigit():
						arg[i] = int(a)-1
			for arg in args:
				try:
					cardlvl.append(self.lvlsdict(arg))
				except InvalidRarity:
					await self.bot.say("Invalid Rarity")
			for c in cardlvl:
				try:
					allgold.append(self.goldcalc(c))
				except IndexError:
					await self.bot.say("Invalid card level")
			formattedgold = '{:,}'.format(allgold[0]-allgold[1])
		else:
			while '' in args:
				args.remove('')

			for i, a in enumerate(args):
				if a.isdigit():
					args[i] = int(a)-1
			currentrarity = 'c'
			try:
				cardlvl = self.lvlsdict(args)
			except InvalidRarity:
				await self.bot.say("Invalid Rarity")
				return
			try:
				allgold = self.goldcalc(cardlvl)
			except IndexError:
				await self.bot.say("Invalid card level")
			formattedgold = '{:,}'.format(allgold)
		await self.bot.say("{} {} {}".format(msg, formattedgold, msg2))
		# for rarity in totalgold:
		#     await self.bot.say("You have spent a total of {} gold on upgrading {} cards".format(totalgold[rarity], rarity))



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

	@commands.command(pass_context=True)
	async def myid(self, ctx, user: discord.Member):
		"""show your discord ID"""
		if user == None:
			user=ctx.message.author
		await self.bot.say("ID: {}".format(user.id))
	
	@checks.is_owner()
	@commands.command(pass_context=True)
	async def copysettings2back(self, ctx):
		for x in self.settings:
			self.backsettings[self.settings[x]] = x
		print(self.backsettings)
		dataIO.save_json(BACKSETTINGS_JSON, self.backsettings)

	@checks.is_owner()
	@commands.command(pass_context=True)
	async def mergejsons(self, ctx):
		tags1 = dataIO.load_json(SETTINGS_JSON)
		tags2 = dataIO.load_json(SETTINGS2_JSON)
		tags3 = {}
		for x in tags1:
			tags3[x] = tags1[x]
		for x in tags2:
			tags3[x] = tags2[x]
		list3 = sorted(tags3)

		tags4 = {}
		for x in list3:
			tags4[x] = tags3[x]
		for x in tags4:
			self.settings[x] = tags4[x]
			dataIO.save_json(SET_JSON, self.settings)
		print(len(self.settings))
		dataIO.save_json(SET_JSON, self.settings)
		
	@checks.is_owner()
	@commands.command(name="cremojis",pass_context=True)
	async def _cremojis(self, ctx):
		
		await self.bot.say('penis')
		for emoji in cremojis:
			print(emoji)
		for emoji in cremojis:
			await self.bot.say(cremojis[emoji])

	@checks.is_owner()
	@commands.command(name="cremoji",pass_context=True)
	async def _cremoji(self, ctx, emojiname):
		try:
			await self.bot.say(self.allemojis[emojiname])
		except KeyError:
			await self.bot.say("{} is not a saved cr emoji".format(emojiname))

	# @commands.command(aliases=['tra'], pass_context=True)
	# async def trapi(self,ctx,clan=None):
	# 	uclan = None
	# 	if clan != None:
	# 		uclan = clan.upper()
	# 	if clan == None:
	# 		clan = racfclanslist
	# 	elif uclan not in racfclans:
	# 		await self.bot.say("the clan, *\u200b{}* is not in racf".format(clan))
	# 		return
	# 	if type(clan) == type(['list']):
	# 		await self.bot.send_typing(ctx.message.channel)
	# 		em = discord.Embed(color=discord.Color(0xFF3844), title="RACF requirements:")
	# 		for c in clan:
	# 			for racfc in racfclanslist:
	# 				if racfc.lower() == c.lower():
	# 					goodcapsclan = racfc
	# 					break
	# 			tag = await self.keyortag2tag(c, ctx)
	# 			clan_data = await CRClan.create(tag)
	# 			trophyreq = await self.parsereq(clan_data.desc)
	# 			if trophyreq==None:
	# 				trophyreq = clan_data.tr_req
	# 			if goodcapsclan == 'eSports':
	# 				trophyreq = self['gitgud']
	# 			em.add_field(name="{}:".format(goodcapsclan), value=trophyreq)

	# 	else:
	# 		tag = await self.keyortag2tag(clan, ctx)
	# 		print("Tag: {}".format(tag))
	# 		clan_data = await CRClan.create(tag)
	# 		# clan_data.desc = "WE are reddit delta, we require a pb 4500 and our feeder is reddit echo"
	# 		#uncomment the above line to test the pb detection
	# 		trophyreq = await self.parsereq(clan_data.desc)
	# 		if trophyreq==None:
	# 			trophyreq = clan_data.tr_req
	# 		for c in racfclanslist:
	# 			if c.lower() == clan.lower():
	# 				goodcapsclan = c
	# 				break
	# 		if goodcapsclan == 'eSports':
	# 			trophyreq = self['gitgud']
	# 		em = discord.Embed(color=discord.Color(0xFF3844), title="{} trophy req:".format(goodcapsclan), description=trophyreq)

	# 	await self.bot.say(embed=em)

	# async def parsereq(self, desc):
	# 	trophynums = []
	# 	n = 0
	# 	for l in desc:
	# 		try:
	# 			if l.isdigit() or (l.lower()=='p' and desc[n+1].lower()=='b')or (l.lower()=='b' and desc[n-1].lower()=='p') or l.lower() == 'o':
	# 				trophynums.append(l)
	# 			elif trophynums[len(trophynums)-1] != " ":
	# 				trophynums.append(' ')
	# 		except IndexError:
	# 			pass
	# 		n+=1
	# 	n = 0
	# 	trnums = ''.join(trophynums)
	# 	trnums = trnums.split(' ')
	# 	while n<len(trnums):
	# 		d = trnums[n]
	# 		# print("trnums: {}".format(trnums))
	# 		# print("{}, len: {}".format(d, len(d)))
	# 		if len(d) == 4 or d.lower() =='pb':
	# 			if d.isdigit():
	# 				trnums[n] = "{:,}".format(int(d))
	# 			n += 1
	# 		else:
	# 			trnums.remove(d)
	# 	print(trnums)
	# 	print(len(trnums))
	# 	n = 0
	# 	for d in trnums:
	# 		trnums[n] = trnums[n].replace('O', '0').replace('o', '0')
	# 		n += 1
	# 	trophyreq = None
	# 	if len(trnums)==0:
	# 		trnums = None
	# 	elif len(trnums) == 1:
	# 		trnums = trnums[0]
	# 	elif len(trnums)==2:
	# 		n = 0
	# 		while n<len(trnums):
	# 			if trnums[n].isdigit():
	# 				trnums[n] = "{:,}".format(int(d))
	# 			n+=1
	# 		trnums = ' '.join(trnums)
	# 	parseddesc = trnums
	# 	if parseddesc == None:
	# 		trophyreq = None
	# 	if type(parseddesc) == type('string'):
	# 		trophyreq = parseddesc
	# 	elif type(parseddesc) == type(['list']):
	# 		trreqs =''
	# 		n = 0
	# 		for d in parseddesc:
	# 			trreqs +=d 
	# 			# print("parseddesc len: {}\nn: {}\nnextone: {}".format(len(parseddesc) ,n, parseddesc[n+1].lower()))
	# 			try:
	# 				if n !=len(parseddesc)-1 and parseddesc[n+1].lower()!='pb':
	# 					trreqs += ', '
	# 				else:
	# 					trreqs += ' '
	# 			except IndexError:
	# 				pass
	# 			n+=1
	# 		trophyreq = trreqs
	# 	return trophyreq



	@commands.group(aliases=["stats"], pass_context=True)
	async def clashroyale(self, ctx):
		"""Display CR profiles."""
		if ctx.invoked_subcommand is None:
			await send_cmd_help(ctx)

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

	@commands.command(pass_context=True)
	async def crsendjson(self, ctx):
		heroku = False
		if 'DYNO_RAM' in os.environ:
			heroku = True
		if heroku:
			await self.bot.send_file(destination=ctx.message.channel, fp=r"/app/data/crtags/settings.json", filename="settings.json")
			await self.bot.send_file(destination=ctx.message.channel, fp=r"/app/data/crtags/backsettings.json", filename="backsettings.json")
			await self.bot.send_file(destination=ctx.message.channel, fp=r"/app/data/crtags/clan.json", filename="clan.json")
		else:
			await self.bot.send_file(destination=ctx.message.channel, fp=r"data\crtags\settings.json", filename="settings.json")
			await self.bot.send_file(destination=ctx.message.channel, fp=r"data\crtags\backsettings.json", filename="backsettings.json")
			await self.bot.send_file(destination=ctx.message.channel, fp=r"data\crtags\clan.json", filename="clan.json")
			# os.environ['playersettings'] = self.settings

			
	@clashroyale.command(name='get', pass_context=True)
	async def gettag(self, ctx, user: discord.Member=None):
		"""Get user tag. If not given a user, get author's tag"""
		if user == None:
			user = ctx.message.author
		tags = dataIO.load_json(SETTINGS_JSON)
		try:
			test = tags[user.id]
		except(KeyError):
			await self.bot.say("{} does not have a tag set.".format(user.display_name))
			return
		if(user==None):
			if tags[ctx.message.author.id]:
				await self.bot.say("Your tag is {}.".format(tags[ctx.message.author.id]))
			else:
				await self.bot.say("You, {} do not have a tag set.".format(ctx.message.author.display_name))
		else:
			if tags[user.id]:
				await self.bot.say("{}'s tag is {}.".format(user.mention, tags[user.id]))
			else:
				await self.bot.say("User {} does not have a tag set.".format(user.display_name))


	@clashroyale.command(aliases=['set'],pass_context=True)
	async def settag(self, ctx, tag):
		"""Save user tag. If not given a user, save tag to author"""
		author = ctx.message.author
		tag = tag.upper()
		tag.replace('O', '0')
		valid = True
		for letter in tag:
			if letter not in validChars:
				valid = False
		if valid: #self.is_valid(tag):
			self.savetag(author.id, tag)
			await self.bot.say("Saved {} for {}".format(tag, author.display_name))
		else:
			await self.bot.say("Invalid tag {}, it must only have the following characters {}".format(author.mention, validChars))

	@clashroyale.command(name='deltag',aliases=['del'],pass_context=True)
	async def _deltag(self, ctx):
		"""Delete user tag."""
		author = ctx.message.author
		valid = True
		self.deltag(author.id, self.settings[author.id])
		await self.bot.say("deleted tag from {}".format( author.display_name))

	@checks.mod_or_permissions()
	@clashroyale.command(pass_context=True)
	async def setusertag(self, ctx, user: discord.Member, tag):
		"""Save user tag. If not given a user, save tag to author"""
		if user == None:
			user = ctx.message.author
		tag = tag.upper()
		tag.replace('O', '0')
		valid = True
		for letter in tag:
			if letter not in validChars:
				valid = False
		if valid: #self.is_valid(tag):
			author = ctx.message.author
			await self.bot.say("Saving {} for {}".format(tag, user.display_name))
			self.savetag(user.id, tag)
		else:
			await self.bot.say("Invalid tag {}, it must only have the following characters {}".format(ctx.message.author.mention, validChars))
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
		else:	#assume member name
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
				await self.bot.say("{} does not have a tag set.".format(user.display_name))
				return None
		return [tag, user]

	def elements2data(self, elements2display, fplayer):
		player_data = []
		player_datadict = {}
		for ele in elements2display:
			thing = eval('fplayer.{}'.format(ele))
			# print(type(thing)==type([]))
			# print(thing)
			# print('\n')
			# print('i am {}'.format(type(thing)))
			if type(thing) == type(['list']):
				player_datadict[ele]=getattr(fplayer, ele)
				player_data.append(getattr(fplayer, ele))

			else:
				thing = str(thing)
				player_datadict[ele] = getattr(fplayer, ele)
				player_data.append(getattr(fplayer, ele))
		return [player_datadict, player_data]

	def react_check(self, reaction, user):
		if user is None or user.id != self.author.id:
			return False

		for emoji in self.currentemojiobjs:
			if reaction.emoji == emoji:
				return True
		return False

	async def reactembeds(self, ctx, message, player, player_data, player_datadict):

		self.author = ctx.message.author
		self.currentemojiobjs = []
		# print(cremojiobjs)
		for e in self.reactionemojislist:
			self.currentemojiobjs.append(cremojiobjs[e])
		# for e in self.currentemojiobjs:
		# 	await self.bot.say(e)
		# self.reactionemojislist = ['😄', reactionemojis[]]
		for e in self.reactionemojislist: #successfully adds custom emojis
			await self.bot.add_reaction(message,self.reactionemojis[e])
		botreactionsmsg = await self.bot.get_message(message.channel, message.id)
		elementspossible = []
		for e in self.reactionemojislist:
			elementspossible.append(e)
		elements2display = []
		u = await self.bot.get_user_info(ctx.message.author.id)
		while True:
			reaction = await self.bot.wait_for_reaction(emoji=self.currentemojiobjs,timeout=30,message=message)#, check=self.react_check)
			if reaction==None:
				await self.bot.edit_message(message,new_content=message.content+' Timed out, UI exited.')
				await asyncio.sleep(30)
				em = discord.Embed(title=player.name,color=discord.Color.blue())
				await self.bot.edit_message(message, embed = em)
				break
			reaction = list(reaction)
			currentuser = reaction[1]
			reaction = list(reaction)[0]
			myreacts = []
			message = await self.bot.get_message(message.channel, message.id)
			emojiclicked = {}
			for r in botreactionsmsg.reactions:
				users = await self.bot.get_reaction_users(r)
				# print(type(r.emoji), r.emoji)
				try:
					emojiclicked[r.emoji.name] = ctx.message.author in users
				except AttributeError:
					pass
			emojiclicked['refresh'] = False
			emojiclicked['helpinfo'] = False
			emojiclicked['nocancel'] = False
			elements2display = []
			for e in elementspossible:
				if emojiclicked[e]:
					elements2display.append(self.emojis2specembeds[e])
			if reaction.emoji.name=='nocancel':
				elements2display = []
			embed = self.data2embed(ctx.message.author, player, player_data, player_datadict, elements2display)
			if reaction.emoji.name=='nocancel':
				await self.bot.edit_message(message, new_content=message.content+ " {} clicked, UI exited.".format(reaction.emoji), embed=embed)
				break

			if reaction.emoji.name == 'helpinfo':
				await self.bot.edit_message(message, embed=self.helpembed)
			else:
				await self.bot.edit_message(message,embed=embed)#specembeds[self.emojis2specembeds[emoji]])

	def data2embed(self, user, player, player_data, player_datadict, elements2display):
		try:
			discordname = user.name if user.nick is None else user.nick
		except:
			discordname = user.name
		# specembeds = {}
		em = discord.Embed(title=player.name, color = discord.Color(0x50d2fe))
		n = 0
		for ele in elements2display:
			chars = 0
			# print(type(self.player_datadict[ele]), self.player_datadict[ele])
			cele = ele
			inline = not( cele == 'seasons' or cele == 'games')
			tempe = discord.Embed(title=player.name, color = discord.Color(0x50d2fe))
			tempe.set_author(icon_url=user.avatar_url,name=discordname)
			tempe.set_footer(text='Data provided by CR-API', icon_url='https://i.imgur.com/Grj2j6D.png')
			if type(player_datadict[ele]) == type(['list']):
				for d in player_datadict[ele]:
					chars += len(d)
				# if chars >256:
				# 	if cele == 'stats':
				# 		tempe.add_field(name = cele.title(), value = '\n'.join(self.player_datadict[ele][:int(len(self.player_datadict[ele])/2)]), inline=False)
				# 	else:
				# 		em.add_field(name = cele.title(), value = '\n'.join(self.player_datadict[ele][:int(len(self.player_datadict[ele])/2)]), inline=inline)
				# 	em.add_field(name = '\u200b', value = '\n'.join(self.player_datadict[ele][int(len(self.player_datadict[ele])/2):]),inline=inline)
				# 	if cele == 'stats':
				# 		tempe.add_field(name = cele.title(), value = '\n'.join(self.player_datadict[ele][:int(len(self.player_datadict[ele])/2)]), inline=False)
				# 	else:
				# 		tempe.add_field(name = cele.title(), value = '\n'.join(self.player_datadict[ele][:int(len(self.player_datadict[ele])/2)]), inline=inline)
				# 	tempe.add_field(name = '\u200b', value = '\n'.join(self.player_datadict[ele][int(len(self.player_datadict[ele])/2):]),inline=inline)
				if False:
					pass
				else:
					em.add_field(name = cele.title(), value = '\n'.join(player_datadict[ele]),inline=inline)
					tempe.add_field(name = cele.title(), value = '\n'.join(player_datadict[ele]),inline=inline)
			elif type(player_datadict[ele]) == type('str'):
				chars += len(player_datadict[ele])
				em.add_field(name = ele.title(), value = player_datadict[ele])
				tempe.add_field(name = ele.title(), value = player_datadict[ele])
			# specembeds[cele] = tempe
			n+=1

		return em

	@clashroyale.command(name='emoji', aliases=['e', 'em'],  pass_context=True)
	async def _emoji(self, ctx, userortag=None):
		"""Get user trophies. If not given a user, get author's data"""
		#fix user, player, player_data, player_data, player_datadict
		tag = await self.keyortag2tag2(userortag, ctx)
		if tag == None:
			return
		if tag[0] == None:
			return
		user = tag[1]
		if user == None:
			user = ctx.message.author
		tag = tag[0]
		player = await CRPlayer.create(tag)
		fplayer = player[1]
		player = player[0]
		elements = []
		elements2display  = [
			'tag',
			'clan',
			'trophies',
			'stats',
			'chestcycle',
			'seasons',
			'xp',
			'deck',
			'games',
			'offers'
		]
		print(fplayer.tag)
		things = self.elements2data(elements2display, fplayer)
		player_datadict = things[0]
		print(player_datadict)
		player_data = things[1]
		# print('{}\n{}'.format(fplayer.stats, type(fplayer.stats)))
		specembeds = {}
		em = self.data2embed(user, player, player_data, player_datadict, elements2display)
		# for key in specembeds:
		# 	await self.bot.say(embed=specembeds[key])
		message = await self.bot.say("React to this for stats! click {} for help.".format(self.reactionemojis['helpinfo']))
		await self.reactembeds(ctx, message, player, player_data, player_datadict)
		# em.set_author(icon_url=user.avatar_url,name=discordname)
		# em.set_thumbnail(url=player.clan.badge)
		# em.set_footer(text='Data provided by CR-API', icon_url='https://i.imgur.com/Grj2j6D.png')
		# await self.bot.say(embed=em)

	def clanelements2data(self, elements2display, fclan):
		clan_data = []
		clan_datadict = {}
		for ele in elements2display:
			thing = getattr(fclan, ele)
			# print(type(thing)==type([]))
			# print(thing)
			# print('\n')
			# print('i am {}'.format(type(thing)))
			if type(thing) == type(['list']):
				clan_datadict[ele]=getattr(fclan, ele)
				clan_data.append(getattr(fclan, ele))

			else:
				thing = str(thing)
				clan_datadict[ele] = getattr(fclan, ele)
				clan_data.append(getattr(fclan, ele))
		return [clan_datadict, clan_data]

	async def clanreactembeds(self, ctx, message, player, clan_data, clan_datadict):

		self.author = ctx.message.author
		self.currentemojiobjs = []
		# print(cremojiobjs)
		for e in self.reactionemojislist:
			self.currentemojiobjs.append(cremojiobjs[e])
		# for e in self.currentemojiobjs:
		# 	await self.bot.say(e)
		# self.reactionemojislist = ['😄', reactionemojis[]]
		for e in self.reactionemojislist: #successfully adds custom emojis
			await self.bot.add_reaction(message,self.reactionemojis[e])
		botreactionsmsg = await self.bot.get_message(message.channel, message.id)
		elementspossible = []
		for e in self.reactionemojislist:
			elementspossible.append(e)
		elements2display = []
		u = await self.bot.get_user_info(ctx.message.author.id)
		while True:
			reaction = await self.bot.wait_for_reaction(emoji=self.currentemojiobjs,timeout=30,message=message)#, check=self.react_check)
			if reaction==None or list(reaction)[0].emoji.name=='nocancel':
				await self.bot.edit_message(message,new_content=message.content+' Timed out, UI exited.')
				break
			reaction = list(reaction)
			currentuser = reaction[1]
			reaction = list(reaction)[0]
			myreacts = []
			message = await self.bot.get_message(message.channel, message.id)
			emojiclicked = {}
			for r in botreactionsmsg.reactions:
				users = await self.bot.get_reaction_users(r)
				# print(type(r.emoji), r.emoji)
				try:
					emojiclicked[r.emoji.name] = ctx.message.author in users
				except AttributeError:
					pass
			emojiclicked['refresh'] = False
			emojiclicked['helpinfo'] = False
			elements2display = []
			for e in elementspossible:
				if emojiclicked[e]:
					elements2display.append(self.emojis2specembeds[e])
			embed = self.data2embed(ctx.message.author, player, clan_data, clan_datadict, elements2display)

			if reaction.emoji.name == 'helpinfo':
				await self.bot.edit_message(message, embed=self.helpembed)
			else:
				await self.bot.edit_message(message,embed=embed)#specembeds[self.emojis2specembeds[emoji]])

	def clandata2embed(self, user, player, clan_data, clan_datadict, elements2display):
		try:
			discordname = user.name if user.nick is None else user.nick
		except:
			discordname = user.name
		# specembeds = {}
		em = discord.Embed(title=player.name, color = discord.Color(0x50d2fe))
		n = 0
		for ele in elements2display:
			chars = 0
			# print(type(self.clan_datadict[ele]), self.clan_datadict[ele])
			cele = ele
			inline = not( cele == 'seasons' or cele == 'games')
			tempe = discord.Embed(title=player.name, color = discord.Color(0x50d2fe))
			tempe.set_author(icon_url=user.avatar_url,name=discordname)
			tempe.set_footer(text='Data provided by CR-API', icon_url='https://i.imgur.com/Grj2j6D.png')
			if type(clan_datadict[ele]) == type(['list']):
				for d in clan_datadict[ele]:
					chars += len(d)
				# if chars >256:
				# 	if cele == 'stats':
				# 		tempe.add_field(name = cele.title(), value = '\n'.join(self.clan_datadict[ele][:int(len(self.clan_datadict[ele])/2)]), inline=False)
				# 	else:
				# 		em.add_field(name = cele.title(), value = '\n'.join(self.clan_datadict[ele][:int(len(self.clan_datadict[ele])/2)]), inline=inline)
				# 	em.add_field(name = '\u200b', value = '\n'.join(self.clan_datadict[ele][int(len(self.clan_datadict[ele])/2):]),inline=inline)
				# 	if cele == 'stats':
				# 		tempe.add_field(name = cele.title(), value = '\n'.join(self.clan_datadict[ele][:int(len(self.clan_datadict[ele])/2)]), inline=False)
				# 	else:
				# 		tempe.add_field(name = cele.title(), value = '\n'.join(self.clan_datadict[ele][:int(len(self.clan_datadict[ele])/2)]), inline=inline)
				# 	tempe.add_field(name = '\u200b', value = '\n'.join(self.clan_datadict[ele][int(len(self.clan_datadict[ele])/2):]),inline=inline)
				if False:
					pass
				else:
					em.add_field(name = cele.title(), value = '\n'.join(clan_datadict[ele]),inline=inline)
					tempe.add_field(name = cele.title(), value = '\n'.join(clan_datadict[ele]),inline=inline)
			elif type(clan_datadict[ele]) == type('str'):
				chars += len(clan_datadict[ele])
				em.add_field(name = ele.title(), value = clan_datadict[ele])
				tempe.add_field(name = ele.title(), value = clan_datadict[ele])
			# specembeds[cele] = tempe
			n+=1

		return em


	

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