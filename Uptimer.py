# -*- coding: utf-8 -*-
import os
from time import sleep
import requests

result = 0
port = 0
sus = 0
sus2 = 0
UpTime = 0
discordcont = "None"
discordurl = "None"
errcode = "Incorrect response from the host"
Checksuccesstimes = 0
param = {
  "content": "Message from the user: " + discordcont,
  "embeds": [
    {
      "title": "Request error!",
      "description": errcode,
      "color": 16711680
    }
  ],
  "attachments": []
} # discord message
print("Uptimer 1.3.2, build 2") #version and build
print()
print("Info") #info
print("progame1201#8037 - general code writer")
print("EVA#1130 - helping in scripting methods and fix errors")
print("Rysik5318#7967 - help in the implementation of the idea, as well as in the method: request")
sleep(1.5)
print()
print("methods:") #methods
print("ping - the easiest verification method !dont work with ports! (can be blocked by host)") # ping method
print("natcat - UDP/TCP verification method (work only on Unix systems)") # natcat method
print("request - HTTP/S verification method !dont work with IP and ports! (can be blocked by host)") # HTTP method
print("urllib - HTTP/S verification method !dont work with IP and ports! (can be blocked by host) needs instaled urllib3 module") # urllib3 method
print("ping3 - the method is similar to ping, but also compare ms with the set maximum. Needs installed ping3 module") # ping3 method
print()
method = input("method: ")
print()
sleept = input("sleep time in sec. (use 30 or 240 to get the best result): ") #sleeptime
print()
print("message types: ")
print("1 - discord webhook")
print("2 - Using your API")
print()
msgtype = input("Type:")
if msgtype == "1" :
 discordurl = input("discord webhook url: ") # discord webhook url setting
 print()
 discordcont = input("discord message on error: ") # discord message setting

if msgtype == "2" :
 import json
 API_URL = input("API url: ") # API url
 API_JSON = input("json data: ") # API Json now it's string
 API_JSONR = json.loads(API_JSON) #now it's json type

if method == "ping": # ping method start
 print()
 ip = input("host: ") # IP
 while True:
   response = os.system("ping -w 2 " + ip) # pinging
   if response == 0:
     print("Server is ok") # OK res
     Checksuccesstimes = Checksuccesstimes + 1

   else:
    print("server error on connect!") # bad res
    sus = sus + 1

    if sus == 2 :
     if msgtype == "1" :   #DISC. WEBHOOK
       param = {
             "content": "Message from the user: " + discordcont,
             "embeds": [
                 {
                     "title": "Ping request error!",
                     "description": "error: " + str(errcode) + " good requests: " + str(Checksuccesstimes),
                     "color": 16711680
                 }
             ],
             "attachments": []
       }
       requests.post(discordurl, json = param)
       sus = 0
       Checksuccesstimes = 0
     if msgtype == "2": #API TYPE
       requests.post(API_URL, json = API_JSONR)
       sus = 0
   sleep(int(sleept)) # ping method end

if method == "natcat" : # natcat method start
  print("Warning! this method working only on unix systems!") #warn
  sleep(1)
  print()
  ip = input("host: ") # IP
  print()
  port = input("Port: ") #port
  print()
  print("use udp - y / tcp - n")
  udptr = input("")
  while True :
    if udptr == "n" : 
     nc = os.system("nc -vz " + ip + " " + port) # using ip and port nat cat

    if udptr == "y" :
     nc = os.system("nc -vnzu " + ip + " " + port) # using ip and port nat cat

    if nc == 0:
         print("Server is ok") # OK res
         Checksuccesstimes = Checksuccesstimes + 1

    else:
        print("server error on connect!") # bad res
        sus = sus + 1

    if sus == 2 :
     if msgtype == "1" :   #DISC. WEBHOOK
      param = {
             "content": "Message from the user: " + discordcont,
             "embeds": [
                 {
                     "title": "Request error!",
                     "description": "error: " + str(errcode) + " good requests: " + str(Checksuccesstimes),
                     "color": 16711680
                 }
             ],
             "attachments": []
      }
      requests.post(discordurl, json = param)
      sus = 0
      Checksuccesstimes = 0
     if msgtype == "2" : #API TYPE
      requests.post(API_URL, json = API_JSONR)
      sus = 0
    sleep(int(sleept)) # natcat method end

if method == "request" : # HTTP method start
  ru = input("URL: ")
  print("requests types:")
  print("1 - HEAD")
  print("2 - POST")
  print("3 - GET")
  rtype = input("Type: ") 
  while True :
    if rtype == "1" :
     r = requests.head(ru) #head
    if rtype == "2" :
     r = requests.post(ru) #post
    if rtype == "3" :
     r = requests.get(ru) #get
    status = r.status_code
    print(status)

    if status == 200 :
         print("server is ok") # OK res
         Checksuccesstimes = Checksuccesstimes + 1

    else:
        print("server error on connect!") # bad res
        sus = sus + 1

    if sus == 2 :
     if msgtype == "1" :   #DISC. WEBHOOK
      errcode2 = str(r.status_code)
      param = {
          "content": "Message from the user: " + discordcont,
          "embeds": [
              {
                  "title": "HTTP error!",
                  "description": "error: " + str(errcode2) + " good requests: " + str(Checksuccesstimes),
                  "color": 16711680
              }
          ],
          "attachments": []
      }
      requests.post(discordurl, json = param)
      sus = 0
      Checksuccesstimes = 0
     if msgtype == "2" : #API TYPE
      requests.post(API_URL, json = API_JSONR)
      sus = 0
    sleep(int(sleept)) # HTTP method end

if method == "urllib" : # urllib method start
   import urllib3
   url = input("URL: ")
   print("requests types:")
   print("1 - HEAD")
   print("2 - POST")
   print("3 - GET")
   rtype = input("Type: ") 
   while True :
     http = urllib3.PoolManager()
     if rtype == "1" :
      i100 = http.request('HEAD', url) #head
     if rtype == "2" :
      i100 = http.request('POST', url) #post
     if rtype == "3" :
      i100 = http.request('GET', url) #get
     status = i100.status
     print(i100.status)
     if status == 200 :
         print("server is ok") # OK res
         Checksuccesstimes = Checksuccesstimes + 1

     else:
        print("server error on connect!") # bad res
        errcode2 = str(i100.status)
        sus = sus + 1

     if sus == 2:
        if msgtype == "1" :  # DISC. WEBHOOK
          errcode2 == str(i100.status)
          param = {
              "content": "Message from the user: " + discordcont,
              "embeds": [
                  {
                      "title": "HTTP error!",
                      "description": "error: " + str(errcode2) + " good requests: " + str(Checksuccesstimes),
                      "color": 16711680
                  }
              ],
              "attachments": []
          }
          requests.post(discordurl, json=param)
          sus = 0
          Checksuccesstimes = 0
        if msgtype == "2" :  # API TYPE
         requests.post(API_URL, json=API_JSONR)
         sus = 0
     sleep(int(sleept)) #urllib method end

if method == "ping3" : #ping3 method start
    from ping3 import ping, verbose_ping
    ip = input("IP: ") #ip

    maxms = input("Max MS: ") #max ms

    while True :
     i200 = ping(ip, unit='ms')
     print(i200)

     if i200 != None :
        print("server is ok!")
        Checksuccesstimes = Checksuccesstimes + 1

     try:
      if float(i200) >= float(maxms) :
         print("Warning: ms > maxms!")
         sus2 = sus2 + 1
     except TypeError :
         print("")

     if i200 == None :
         print("server error on connect!")
         sus = sus + 1

     if sus == 2 :
       if  msgtype == "1" :
        errcode = "Incorrect response from the host"
        param = {
          "content": "Message from the user: " + discordcont,
          "embeds": [
              {
                  "title": "Ping3 request error!",
                  "description": "ping3 response:" + str(i200) + " good requests: " + str(Checksuccesstimes),
                  "color": 16711680
              }
          ],
          "attachments": []
         } #Discord error
        requests.post(discordurl, json = param)
        sus = 0
        Checksuccesstimes = 0

       if msgtype == "2":  # API TYPE
          requests.post(API_URL, json = API_JSONR)
          sus = 0
     if sus2 == 2 :
      if msgtype == "1" : #disc. webhook
        param = {
             "content": "Message from the user: " + discordcont,
             "embeds": [
                 {
                     "title": "Warning! ms > maxms!",
                     "description": "ping = " + str(i200) + "ms",
                     "color": 16763904
                 }
             ],
             "attachments": []
         }  # discord warn
        requests.post(discordurl, json = param)
        sus2 = 0
      if msgtype == "2":  # API TYPE
            requests.post(API_URL, json = API_JSONR)
            sus2 = 0
     sleep(int(sleept)) #ping3 method end
print("")
print("do you know that you need to choose a method?")
