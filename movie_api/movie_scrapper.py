import requests
from bs4 import BeautifulSoup as bs
import json

# Movie Raitng, Description, and Genre extracted from rottentommatos
# And form IMDB rating from OMDB Api


def get_name(mname):
	name=''
	lanime=mname.lower()
	a=lanime.split()
	for i in a:
		name+=i+'-'
	return name[:-1]

def get_rating_rottenTomato(movie):
	URL="https://www.rottentomatoes.com/m/{}".format(get_name(movie))
	r=requests.get(URL)
	soup=bs(r.content,'html5lib')
	script=soup.find('script',attrs={'type':'application/ld+json'})
	data=json.loads(script.contents[0])
	return data['aggregateRating']['ratingValue']

def get_rating_imdb(movie):
	url='http://www.omdbapi.com/?apikey=65dbf45c&t={}'.format(movie)
	response=requests.get(url)
	data=json.loads(response.content)
	return data['Ratings'][0]['Value']

def get_genre(movie):
	url="https://www.rottentomatoes.com/m/{}".format(get_name(movie))
	r=requests.get(url)
	soup=bs(r.content,'html5lib')
	script=soup.find('script',attrs={'type':'application/ld+json'})
	data=json.loads(script.contents[0])
	return data['genre']

def get_characters(name):
	url="https://www.rottentomatoes.com/m/{}".format(get_name(name))
	r=requests.get(url)
	soup=bs(r.content,'html5lib')
	script=soup.find('script',attrs={'type':'application/ld+json'})
	data=json.loads(script.contents[0])
	return data['character']


def get_description(movie):
	url="https://www.rottentomatoes.com/m/{}".format(get_name(movie))
	r=requests.get(url)
	soup=bs(r.content,'html5lib')
	des=soup.find('meta',attrs={'name':'description'})
	return {'description':des['content']}
	
