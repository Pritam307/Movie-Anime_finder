from flask_restplus import Api
from .movie_models import GetMovieRating,GetMovieDetails,GetMovieCharacters,GetMovieGenre,GetMovieDescription
from flask import Blueprint

movie_blueprint=Blueprint("movie_api",__name__)

api_movie=Api(movie_blueprint)


api_movie.add_resource(GetMovieRating,'/ratings/<string:movie>')
# api_movie.add_resource(GetMovieDetails,'/api/v0.1/movies/details/<string:movie>')
api_movie.add_resource(GetMovieCharacters,'/characters/<string:movie>')
api_movie.add_resource(GetMovieGenre,'/genre/<string:movie>')
api_movie.add_resource(GetMovieDescription,'/description/<string:movie>')

