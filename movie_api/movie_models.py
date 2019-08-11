from flask_restplus import Resource

from .movie_scrapper import get_rating_imdb,get_rating_rottenTomato,get_characters,get_genre,get_description




class GetMovieRating(Resource):
	def get(self,movie):
		r1=get_rating_imdb(movie)
		r2=get_rating_rottenTomato(movie)
		
		return {'Title': movie,"imdb rating":r1,'rottentommatoes rating':str(r2)+'%'},200

class GetMovieDetails(Resource):
	def get(self,movie):
			return {'Title':movie,
				'Ratings':[{'imdb':get_rating_imdb(movie)},{'rottenTommatoes':str(get_rating_rottenTomato(movie))+'%'}],
				'Description':get_description(movie),
				'Genre':get_genre(movie),
				'Charaters':get_characters(movie)},200

class GetMovieCharacters(Resource):
	def get(self,movie):
		return {
		'Title': movie,
		'Charaters': get_characters(movie)},200

class GetMovieGenre(Resource):
	def get(self,movie):
		return {
			'Title': movie,
			'Genre': get_genre(movie)
		},200

class GetMovieDescription(Resource):
	def get(self,movie):
		return {"Title": movie,
				"Description": get_description(movie)
		},200