import GPS
import os

log = GPS.Logger("alire")

def on_project(a,b):
    stream = os.popen('cd ' + b.directory() + ' && alr setenv')
    output = stream.read()
    log.log(output)
    print(output)
    if "alr setenv unsuccessful" in output:
	GPS.setenv("GPR_PROJECT_PATH",'')
	log.log('No alire project found')
	return
    log.log('Alire project found! Setting env vars...')
    res = output.splitlines()[0].split('=')[1].split('"')[1]
    log.log('GPR_PROJECT_PATH is: ' + res)
    GPS.setenv("GPR_PROJECT_PATH", res)
    
GPS.Hook("project_changing").add(on_project)