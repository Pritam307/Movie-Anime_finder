from flask import Flask
from anime_api import anime_blueprint
from movie_api import movie_blueprint
app=Flask(__name__)


if __name__=='__main__':
	app.register_blueprint(anime_blueprint,url_prefix='/api/v0.1/anime')
	app.register_blueprint(movie_blueprint,url_prefix='/api/v0.1/movie')
	app.run(debug=True,use_reloader=True)



