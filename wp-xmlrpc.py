import requests
import argparse
'''
*********************************
* version 1.0 
* feature : active scanner only
*
*********************************
'''
# arguments setup

argument = argparse.ArgumentParser()
argument.add_argument("--url","-u",type=str)
argument.add_argument("--check","-c",action="store_true")
argument.add_argument("--get-methods","-gm",help="get xmlrpc methods",action="store_true")
options = argument.parse_args()

# get functions xmlrpc protocal
def get_functions():
    getFunctions = "system.listMethods"
    payload = f'''
    <methodCall>
      <methodName>{getFunctions}</methodName>
      <params></params>
    </methodCall>
    '''
    r = requests.post(options.url + "/xmlrpc.php",data=payload,headers={"Content-Type":"application/xml","User-Agent":"Mozilla Firefox"})
    return r.text
if options.get_methods:
	print(get_functions())
if options.check:
	s = requests.post(options.url + "/xmlrpc.php").status_code
	if s == 200 :
		print("this web app is vulnerable")
	else:
		print("this web app is not vulnerable")
