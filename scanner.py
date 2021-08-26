#!/bin/python
import sys
import socket #for node to node connection 
from datetime import datetime

#define the target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4
    
else:
     print("invalied amount of arguments. ")
     print("syntax:python3 scanner.py <ip>")

#Add a banner
print("_" * 50)
print("scanning target " + target)
print("Time started: "+str(datetime.now()))
print("_" * 50)

try:
    
    for port in range(40,85): #scanning port range
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #establish connection to connect to ipv4
            socket.setdefaulttimeout(1) #time to connect is only 2 sec and stop and see next port
            result = s.connect_ex((target,port)) #connect to the port and target and if port close return an error indicator and close the connection
            if result == 0:
                    print("port {} is open".format(port))
            s.close() 
 
 
except keyboardInterrupt:
        print("\nExiting program")
        sys.exit()
except socket.gaierror:
       print("hostname cant be resolved")
       sys.exit()
       
except socket.error:
        print("cant connect to server")
        sys.exit()
        
        