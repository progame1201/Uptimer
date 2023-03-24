import os
from time import sleep
import requests 
result = 0
port = 0
sus = 0
print("Uptimer 1.0 build 4") #version
print()
print("Info") #info
print("progame1201#8037 - general code writer")
print("EVA#1130 - helping in scripting methods and fix errors")
print("Rysik5318#7967 - help in the implementation of the idea, as well as in the method: HTTP")
sleep(2)
print()
print("methods:") #methods
print("ping - the easiest verification method !dont work with ports!. Can be blocked by host") # ping method
print("natcat - UDP/TCP verification method. Work only on Unix systems") # natcat method
print("HTTP - HTTP/S verification method !dont work with IP and ports!. Can be blocked by host") # HTTP method

method = input("method: ")
print()
sleept = input("sleep time in sec. (use 30 or 240 to get the best result): ") #sleeptime
print()
discordurl = input("discord wbhook url: ") # discord webhook url setting

discordcont = input("discord message on error: ") # discord messege setting

param = {"content": discordcont} # discord messege

if method == "ping": # ping method start
 print()
 ip = input("host: ") # IP
 while True:
   response = os.system("ping -w 2 " + ip) # pinging

   if response == 0:
     print("Server is ok") # OK res
     result = True

   else:
    print("server error on connect!") # bad res
    sus = sus + 1
    result = False

    if sus == 2 :
     requests.post(discordurl, data=param)
     sus = 0
   sleep(int(sleept)) # ping method end

if method == "natcat" : # natcat method start
  print("Warning! this method working only on unix systems!") #warn
  sleep(1)
  print()
  ip = input("host: ") # IP
  print()
  port = input("Port: ") #port
  while True :
    nc = os.system("nc -vz " + ip + " " + port) # using ip and port nat cat

    if nc == 0:
         print("Server is ok") # OK res
         result = True

    else:
        print("server error on connect!") # bad res
        result = False
        sus = sus + 1

    if sus == 2 :
     requests.post(discordurl, data=param)
     sus = 0
    sleep(int(sleept)) # natcat method end

if method == "http" : # HTTP method start
  ru = input("URL: ")
  while True :
    r = requests.head(ru)
    print("The URL error")

    status = r.status_code
    print(status)

    if status == 200 :
         print("server is ok") # OK res
         result = True

    else:
        print("server error on connect!") # bad res
        result = False
        errcode = r.status_code
        sus = sus + 1

    if sus == 2 :
     requests.post(discordurl, data=param)
     sus = 0
    sleep(int(sleept)) # HTTP method end