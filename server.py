from bottle import route, run, template, request
from goal_activator import *

AUDIO_ROOT = "/horns/"
DEFAULT_GOAL_FILE = "rit_horn_short_band.wav"
DEFAULT_PENALTY_FILE = "penalty.wav"

#IO Dict that tracks all IO names, states, and permissions
#Lists to maintain memory reference to value in dict
IO_DICT = {"button":[0], "key"=[0],"software_mode"=[0]}
SOURCE_LIST = ["hardware_event", "software_goal", "remote_control"]

"""
Validates that a source is in the source list.
Returns the source if valid or None if
invalid
"""
def get_source(request):
    try:
        source = request.forms.get('source')
        if(source in SOURCE_LIST):
            return source
    finally:
        return None

@route('/goal/<path>')
def web_goal(path=DEFAULT_GOAL_FILE):
	source = get_source(request)
    
    if(source == None)
        return "Invalid source"
    
    text = "Goal activated by " + str(source)
	print(text)
	goal(path)
    return text

@route('/penalty/<path>')
def web_penalty(path=DEFAULT_PENALTY_FILE):
	source = get_source(request)
    
    if(source == None)
        return "Invalid source"
    
    text = "Penalty activated by " + str(source)
	print(text)
	penalty(AUDIO_ROOT + path)
    return text
    
@route('/io/set/<io>')
def io_handle(io):
	try:
		value = int(request.forms.get('value'))
	except:
		return "Value error"
	
	source = get_source(request)
	if(io not in IO_DICT):
		return "IO Name Not Found"
	
    #Get IO Value
    io_obj = IO_DICT[io]
    
	#Update Value
	io_obj[0] = value

@route('/io/get')
def get_io():
    return "DATA"
    
@route('/io/set_all'):
def set_all_io():
    return None

if(__name__ == "__main__"):
    run(host='horn.student.rit.edu', port=80, debug=True)