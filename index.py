import bottle
from bottle import route, run, Response, template
import json
import image
import cProfile, pstats, io
from pstats import SortKey

def call_service():
	directoryName = 'photos'
	image.process(directoryName)
	
@route('/')
def index():
	"""Home page"""
	title = "Image Processor App"
	pr = cProfile.Profile()
	pr.enable()
	
	call_service()
	
	pr.disable()
	
	s = io.StringIO()
	sortby = SortKey.CUMULATIVE
	ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
	ps.print_stats()
	print(s.getvalue())
	
	return template('index.tpl',data="Request completed!", title=title)
	
serverApp = bottle.default_app()
