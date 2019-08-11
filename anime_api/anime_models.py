from flask_restplus import Resource
from .anime_scrapper import get_rating,get_description,get_genre,get_noofepisodes,get_productionStudio,get_animeyears,get_reviewers



class GetAnimeRating(Resource):
    def get(self,anime):
        return {"Title": anime,
            "Rating": get_rating(anime)
        }


class GetAnimeDescription(Resource):
    def get(self,anime):
        try:
            des=get_description(anime)
            return {
            'Title': anime,
            'Description': des
            }
        except:
            return{
                'messsage': 'Please check the anime name'
            }
            
        
        

class GetAnimeGenre(Resource):
    def get(self,anime):
        return {
            "Title": anime,
            "Genre": get_genre(anime)
        }

class GetAnimeEpisodes(Resource):
    def get(self,anime):
        return{
            'Title': anime,
            'No of Episodes': get_noofepisodes(anime)
        }

class GetAnimeStudios(Resource):
    def get(self,anime):
        return {
            'Title': anime,
            'Production House': get_productionStudio(anime)
        }

class GetAnimeYears(Resource):
    def get(self,anime):
        return {
            'Title': anime,
            'Years': get_animeyears(anime)
        }
class GetAnimeReviewers(Resource):
    def get(self,anime):
        return{
            'Title': anime,
            'Reviwers': get_reviewers(anime)
        }