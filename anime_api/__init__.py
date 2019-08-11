from flask_restplus import Api
from .anime_models import GetAnimeRating,GetAnimeDescription,GetAnimeGenre,GetAnimeStudios,GetAnimeYears,GetAnimeReviewers
from flask import Blueprint


anime_blueprint=Blueprint('anime_api',__name__)
api_anime=Api(anime_blueprint)

api_anime.add_resource(GetAnimeRating,'/ratings/<string:anime>')
api_anime.add_resource(GetAnimeDescription,'/description/<string:anime>')
api_anime.add_resource(GetAnimeGenre,'/genre/<string:anime>')
api_anime.add_resource(GetAnimeStudios,'/studios/<string:anime>')
api_anime.add_resource(GetAnimeYears,'/years/<string:anime>')
api_anime.add_resource(GetAnimeReviewers,'/voters/<string:anime>')