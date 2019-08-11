# Scraped from Cruchyroll and AnimePlanet

from requests import get
from bs4 import BeautifulSoup as bs
import json


# anime='attack on titan'



def get_name(anime):
	name=''
	lanime=anime.lower()
	a=lanime.split()
	for i in a:
		name+=i+'-'
	return name[:-1]

# url1='https://www.crunchyroll.com/en-gb/{}/reviews'.format(get_name())
# url2='https://www.anime-planet.com/anime/{}'.format(get_name())


def get_rating(anime):
	url1='https://www.crunchyroll.com/en-gb/{}/reviews'.format(get_name(anime))
	url2='https://www.anime-planet.com/anime/{}'.format(get_name(anime))
	r1,r2=get(url1),get(url2)
	soup1=bs(r1.content,'html.parser')
	crating=soup1.find('script',attrs={'type':'application/ld+json'})
	cres=json.loads(crating.contents[0])

	soup2=bs(r2.content,'html.parser')
	arating=soup2.find('meta',attrs={'itemprop':'ratingValue'})
	return {'crunchyroll':'{}/5'.format(cres['aggregateRating']['ratingValue']),'animeplanet':'{}/10'.format(arating['content'])}


def get_description(anime):
	url2='https://www.anime-planet.com/anime/{}'.format(get_name(anime))
	response=get(url2)
	soup=bs(response.content,'html.parser')
	desp=soup.find('meta',attrs={'property':'og:description'})
	return desp['content']

def get_genre(anime):
	url2='https://www.anime-planet.com/anime/{}'.format(get_name(anime))
	genrelist=[]
	response=get(url2)
	soup=bs(response.content,'html.parser')
	genre=soup.findAll('meta',attrs={'property':'video:tag'})
	for i in genre:
		genrelist.append(i['content'])
	return genrelist

def get_noofepisodes(anime):
	url2='https://www.anime-planet.com/anime/{}'.format(get_name(anime))
	response=get(url2)
	soup=bs(response.content,'html.parser')
	eps=soup.find('span',attrs={'class':'type'})
	return eps.contents[0]

def get_productionStudio(anime):
	url2='https://www.anime-planet.com/anime/{}'.format(get_name(anime))
	response=get(url2)
	soup=bs(response.content,'html.parser')
	studio=soup.find('a',attrs={'href':'/anime/studios/studio-pierrot'})
	return studio.contents[0]

def get_animeyears(anime):
	url2='https://www.anime-planet.com/anime/{}'.format(get_name(anime))
	response=get(url2)
	soup=bs(response.content,'html.parser')
	year=soup.find('span',attrs={'class':'iconYear'})
	return year.contents[0]

def get_reviewers(anime):
	url2='https://www.anime-planet.com/anime/{}'.format(get_name(anime))
	response=get(url2)
	soup=bs(response.content,'html.parser')
	voters=soup.find('meta',attrs={'itemprop':'ratingCount'})
	return voters['content']