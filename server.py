from bottle import route, run, template, request
from goal_activator import *

AUDIO_ROOT = "/horns/"
DEFAULT_GOAL_FILE = "rit_horn_short_band.wav"
DEFAULT_PENALTY_FILE = "penalty.wav"

#IO Dict that tracks all IO names, states, and permissions
IO_DICT = {"button":0, "key"=0,"software_mode"=0}

@route('/goal/<path>')
def web_goal(path=DEFAULT_GOAL_FILE):
	source = request.forms.get('source')
	print("Goal activated by " + str(source))
	goal(path)

@route('/penalty/<path>')
def web_penalty(path=DEFAULT_PENALTY_FILE):
	source = request.forms.get('source')
	print("Penalty activated by " + str(source))
	penalty(AUDIO_ROOT + path)

@route('/io/<io>')
def io_handle(io):
	try:
		value = int(request.forms.get('value'))
	except:
		return "Value error"
	
	source = request.forms.get('source')
	if(io not in IO_DICT):
		return "IO Name Not Found"
	
	#Update Value
	client_ip = request.environ.get('REMOTE_ADDR')
	io_obj = IO_DICT[io]
	if(io_obj[0] == "localhost" and client_ip != "127.0.0.1"):
		return "Access Error"

	#Assign Value
	io_obj[1] = value
	