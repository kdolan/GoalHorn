from bottle import route, run, template
from goalbutton import *

@route('/goal/<path>')
def web_gaol(path='/horns/rit_horn_short_band.wav'):
	goal(path)

@route('/penalty/<path>')
def web_penalty(path='/horns/penalty.wav'):
	penalty(path)