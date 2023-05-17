import bottle
from bottle import route, run, Response, template
import json
from image import process
import concurrent.futures

app = bottle.app()

def call_service():
    directoryName = 'photos'
    with concurrent.futures.ThreadçpoolExecutor() as executor:
		executor.submit(process, directoryName)
    image.process(directoryName)

@app.route('/')
def index():
    """Home page"""
    title = "Image Processor App"
    call_service()
    return template('index.tpl',data="Request completed!", title=title)

if __name__ == '__main__':
	run(app, host='0.0.0.0', port=8000, debug=False, reloader=True)
