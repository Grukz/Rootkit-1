# Rootkit
This is a quick and dirty rootkit implementation with Python.
Rootkits are usually used to create a reverse TCP connection from remote targets to an attacker. It allow shell command execution on the victim OS. 
The main benefit of this kind of malicious programs is the fatc that they are able to hide process ID when being executed on the victim computer. This script can be executed after having root access privileges in the victim OS by exploiting some vulnerabilities. 
Idea behind that is very simple. As we know, once a new process is created, OS stores its process ID as the name of a new folder in /proc path.
All we have to do is a bind mount of the folder correspending with process ID of our reverse shell with an empty folder. 
Once doing that, victim OS will be unable to detect our script when it shows running processes.
 
