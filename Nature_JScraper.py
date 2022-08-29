import subprocess
import sys
import re
import os
import pyfiglet
import datetime


target_file = sys.argv[1] #Getting Subdomains
project_name = sys.argv[2] #Project Name
command2 = "mkdir "+project_name+"_jsfiles"
p2 = subprocess.Popen(command2,shell=True,stdout=subprocess.PIPE)
def banner():

	out = pyfiglet.figlet_format("Nature_JScraper")
	print(out)
	print("                                                                 v0.01")
	print("                                                                 by br33z3")



	print("Usage: python3 Nature_JScraper.py <file name include domains> <project name>")
# -------------------------------------------------------------
# -----------------------notify--------------------------------

def notify( msg ):

	# https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e
	token  = <ENTER TOKEN>   # "10........71:AA...7b--FbFw...........6YX9Z4"
	chatid = <ENTER CHATID>  # "-444...3432"
	command = "curl -s -X POST"+" \"https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chatid+"&text="+msg+"\""
	p4 = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)

# -----------------------notify--------------------------------
# -------------------------------------------------------------

def send_file ( ): #Change Document Location: @/opt/Na...
	# https://core.telegram.org/bots/api#senddocument
	token  = <ENTER TOKEN>   # "10........71:AA...7b--FbFw...........6YX9Z4"
	chatid = <ENTER CHATID>  # "-444...3432"
	command1 = "curl -F chat_id="+chatid+" -F document=@/opt/Nature_JScraper/"+project_name+"_jsfiles/results.txt"+" \"https://api.telegram.org/bot"+token+"/sendDocument\" 2>/dev/null"
	command2 = "curl -F chat_id="+chatid+" -F document=@/opt/Nature_JScraper/"+project_name+"_jsfiles/results.html"+" \"https://api.telegram.org/bot"+token+"/sendDocument\" 2>/dev/null"
	command3 = "curl -F chat_id="+chatid+" -F document=@/opt/Nature_JScraper/"+project_name+"_jsfiles/results2.html"+" \"https://api.telegram.org/bot"+token+"/sendDocument\" 2>/dev/null"
	os.system(command1)
	os.system(command2)
	os.system(command3)

# -------------------------------------------------------------
# -----------------------waybackurls---------------------------
def waybackurls():

	command = "cat "+target_file+" |"+"waybackurls "
	p1 = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
	output = p1.stdout.read()
	cangil ="waybackurls_out.txt"
	file_waybackurls = open(cangil, "w")
	file_waybackurls.write(output.decode())
	file_waybackurls.close()
	print("[+] All WayBackUrls Found")
	return output
# -----------------------waybackurls---------------------------
# -------------------------------------------------------------



# -------------------------------------------------------------
# -----------------------Convert_List--------------------------
def Convert( outputx ): 
    li = list(outputx.split("\n"))
    print("[+] Files Converted to List in WayBackUrls") 
    return li
# -----------------------Convert_List--------------------------
# -------------------------------------------------------------



# -------------------------------------------------------------
# -----------------------string_parse--------------------------

def string_parse( waybackurls_output ):

	res = list(filter(lambda x: ('.js' in x) and ('.jsp' not in x) and ('.json' not in x), waybackurls_output))
	print("[+] Extracted JavaScript Files in WayBackUrls\n\n")
	for p in range(len(res)):
		print(res[p])
	return res

# -----------------------string_parse--------------------------
# -------------------------------------------------------------


# ------------------------------------------------------------------
# -----------------------Download JS Files--------------------------

def download_files( files ):

	length = len(files)
	print("\n\n[+] Downloading All JavaScript Files in WayBackUrls")
	pwd = os.getcwd()
	for i in range(length):
		here2=files[i].split("//")
		last_but_not_least2=here2[1].replace('/', '\\')
		command = "wget "+"\""+files[i]+"\""+" -O "+pwd+"/"+project_name+"_jsfiles/"+"\""+last_but_not_least2+"\""+" -q --no-check-certificate --timeout=10 --tries=2 2>/dev/null"
		os.system(command)
	print("[+] All WayBackUrls JavaScript Files Downloaded Successfully")


# -----------------------Download JS Files--------------------------
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# -----------------------get JS Function----------------------------

def getJS():

	print("[+] Finding Current JavaScript Files\n\n")
	getJS_list = []
	file_getJS = open(target_file, "r")
	for line in file_getJS:
		add = "http://"+line
		add_2 = "https://"+line
		add = add.rstrip("\n")
		add_2 = add_2.rstrip("\n")	
		getJS_list.append(add)
		getJS_list.append(add_2)

	
	pwd = os.getcwd()
	for x in range(len(getJS_list)):
		i = 0
		command2 = "getJS --url "+getJS_list[x]+" --complete"
		p2 = subprocess.Popen(command2,shell=True,stdout=subprocess.PIPE)
		output = p2.stdout.read()
		output = output.decode().strip() # Find all JavaScript Files
		lima = list(output.split("\n"))  # From raw input to list
		kars=len(lima)
		if kars > 1:
			for m in range(len(lima)):
				print(lima[m])
			for i in range(len(lima)):
				here=lima[i].split("//")
				last_but_not_least=here[1].replace('/', '\\')
				command = "wget "+"\""+lima[i]+"\""+" -O "+pwd+"/"+project_name+"_jsfiles/"+"\""+last_but_not_least+"\""+" -q --no-check-certificate --timeout=15 --tries=2"
				os.system(command)
		else:
			print("no data")
	print("\n\n[+] Downloading All Current JavaScript Files")
	print("[+] Finished Downloading All Current JavaScript Files")
	last_cmd= "find "+pwd+"/"+project_name+"_jsfiles/"+" -type f -empty -delete"
	os.system(last_cmd)
	

# -----------------------get JS Function----------------------------
# ------------------------------------------------------------------

# -------------------------------------------------------------------
# -----------------------LinkFinder----------------------------------

def LinkFinder():

	print("\n[***]Searching For Interesting and Juicy Endpoints,api-keys inside all JavaScript Files")
	command31 = "rm "+project_name+"_jsfiles/*.png  2>/dev/null"
	command32 = "rm "+project_name+"_jsfiles/*.gif  2>/dev/null"
	command33 = "rm "+project_name+"_jsfiles/*.jpg  2>/dev/null"
	command34 = "rm "+project_name+"_jsfiles/*.jsp* 2>/dev/null"
	command35 = "rm "+project_name+"_jsfiles/*.css  2>/dev/null"
	os.system(command31)
	os.system(command32)
	os.system(command33)
	os.system(command34)
	os.system(command35)
	command3 = "python3 linkfinder.py -i '"+project_name+"_jsfiles/*.js*'"+" -o results.html 2>/dev/null"
	command4 = "python3 linkfinder.py -i '"+project_name+"_jsfiles/*.js*'"+" -o cli > results.txt 2>/dev/null"
	os.system(command3)
	os.system(command4)
	print("[***]Search Done Results Saved to results.html")
	cdm="mv results.html "+project_name+"_jsfiles/ 2>/dev/null"
	os.system(cdm)
	command3_2= "python3 SecretFinder.py -i '"+project_name+"_jsfiles/*' -o results2.html 2>/dev/null"
	os.system(command3_2)
	cdm="mv results2.html "+project_name+"_jsfiles/ 2>/dev/null"
	os.system(cdm)
	cdm="mv results.txt "+project_name+"_jsfiles/ 2>/dev/null"
	os.system(cdm)
	dime = datetime.datetime.now()
	tempp= dime.strftime("%x %X")
	tempp="Scan Completed (From Nature_JScraper) "+str(tempp)
	#notify(tempp)

# -----------------------LinkFinder---------------------------------
# ------------------------------------------------------------------




if __name__ == "__main__":

	dime = datetime.datetime.now()
	tempp= dime.strftime("%x %X")
	tempp="Scan Started(From Nature_JScraper) "+str(tempp)
	#notify(tempp)
	banner()
	print("\n\n[+] Finding All WayBackUrls")
	wbu_output = waybackurls() #Execute WayBackUrls
	wbu_output_list = Convert(wbu_output.decode()) #Convert String Output to List
	js_files = string_parse( wbu_output_list ) #Parse List and extract js Files
	download_files(js_files)
	getJS()
	LinkFinder()
	send_file()
