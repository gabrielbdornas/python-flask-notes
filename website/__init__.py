from flask import Flask

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'secret key for our app not share on production'
	return app