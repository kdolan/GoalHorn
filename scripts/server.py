from bottle import route, run, template, request
from goal_activator import *
import json
import constants
import subprocess
import thread

#IO Dict that tracks all IO names, states, and permissions
#Lists to maintain memory reference to value in dict
IO_DICT = {"button":[0], "key":[0],"software_mode":[0]}
SOURCE_LIST = ["hardware", "software", "remote_control", "web_dash", "localhost"]

#Most recent thread
last_goal_id = 0

def format_path(urlPath):
    return urlPath.replace("+","/")

"""
Validates that a source is in the source list.
Returns the source if valid or None if
invalid
"""
def get_source(request):
    source = None
    try:
        source = request.query['source']
        if(source in SOURCE_LIST):
            return source
    finally:
        if(source == None):
            return None
            
@route('/goal')
@route('/goal/<path>')
def web_goal(path=constants.DEFAULT_GOAL_FILE):
    global last_goal_id
    source = get_source(request)
    
    if(source == None):
        return "Invalid source"
    
    text = "Goal activated by " + str(source)
    print(text)
    
    last_goal_id += 1
    thread.start_new_thread(goal, (constants.AUDIO_ROOT + format_path(path),last_goal_id))
    
    return text

@route('/penalty')
@route('/penalty/<path>')
def web_penalty(path=constants.DEFAULT_PENALTY_FILE):
    global last_goal_id
    source = get_source(request)
    
    if(source == None):
        return "Invalid source"
    
    text = "Penalty activated by " + str(source)
    print(text)
    
    last_goal_id += 1
    thread.start_new_thread(goal,(constants.AUDIO_ROOT + format_path(path),last_goal_id))
    
    return text

@route('/stop')
@route('/stop/') 
def stop():
    source = get_source(request)
    
    if(source == None):
        return "Invalid source"
    
    text = "Stopping all active goals " + str(source)
    print(text)
    subprocess.Popen("killall aplay", shell=True)
    deactivate_goal_light()
    
    return text
    
@route('/finish/<id>')
def finish_goal(id):
    global last_goal_id
    source = get_source(request)
    
    if(source == None):
        return "Invalid source"
    
    print("Checking finish goal. Last goal="+str(last_goal_id)+", ID="+str(id))
    
    if(int(id) == int(last_goal_id)):
        #Stop turn off the light
        text = "Disabling goal light for" + id
        deactivate_goal_light()
    else:
        text = "Goal id " + id + " no longer active. Ignore light disable"
    print(text)
    return text
    
@route('/io/set/<io>')
def io_handle(io):
    try:
        value = int(request.forms.get('value'))
    except Error:
        return "Value error"
    
    source = get_source(request)
    if(source == None):
        return "Invalid source"
    if(io not in IO_DICT):
        return "IO Name Not Found"
    
    #Get IO Value
    io_obj = IO_DICT[io]
    
    #Update Value
    io_obj[0] = value
    return "100"

@route('/io/get')
def get_io():
    source = get_source(request)
    if(source == None):
        return "Invalid source"
    return json.dumps(IO_DICT)
    
@route('/io/set_all')
def set_all_io():
    source = get_source(request)
    if(source == None):
        return "Invalid source"    
    
    json_data = json.loads(request.query['data'])
    
    for key in json_data:
        IO_DICT[key] = json_data[key]
    
    return "100"

if(__name__ == "__main__"):
    deactivate_goal_light()
    run(host='0.0.0.0', port=80, debug=True)