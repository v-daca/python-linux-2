import bottle
from bottle import route, run, Response, template
import json
from image import process

app = bottle.app()

@app.route('/')
def index():
	directoryName = 'photos'
	"""Home page"""
	title = "Image Processor App"
	process(directoryName)
	return template('index.tpl',data="Request completed!", title=title)

if __name__ == '__main__':
	run(app, host='0.0.0.0', port=8000, debug=False, reloader=True)
