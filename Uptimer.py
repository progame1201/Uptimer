# -*- coding: utf-8 -*-
import os
from time import sleep
import requests
import configparser
import os.path
import json
print("Uptimer 1.6.0, build 3") #version and build
print()
print("Info") #info
print("progame1201#8037 - general code writer")
print("EVA#1130 - helped with coding and bug fixing at first ")
print("Rysik5318#7967 - helped in the implementation of the idea, as well as in tests with the urllib and request methods")
print("moseechev#6235 - tester")
#config generation
pathhere = os.path.exists(path="config.ini") #config here?
config = configparser.ConfigParser()
if pathhere == True : #regen start
  errorread = False
  try:
    config.read("config.ini") #read
  except AttributeError: # Attribute error?
    print("")
    errorread = True
  if errorread == False : # read error?
    configversion = config.get("Info", "version")
    if configversion != "1.5.0" :
     os.remove("config.ini")
pathhere = os.path.exists(path="config.ini") #config here?
#config generation end
if pathhere == False : #if config not here
 def createConfig(path): #conf create
    config = configparser.ConfigParser()
    config.add_section("Settings") # SETTINGS
    config.set("Settings", "configtrue", "False") # CONF ENABLE?
    config.set("Settings", "ip", "0.0.0.0") # IP
    config.set("Settings", "port", "0000") # PORT for natcat
    config.set("Settings", "method", "ask") #METHOD
    config.set("Settings", "msgtype", "1") #msg type
    config.set("Settings", "discordurl", "discord url here")  # discord url
    config.set("Settings", "discordcont", "discord message here")  # discord msg
    config.set("Settings", "API_URL", "api url")  # api url
    config.set("Settings", "API_JSON", "api json")  # api json
    config.set("Settings", "sleeptime", "30")  # sleep time
    config.add_section("Info")
    config.set("Info", "version", "1.5.0") # cfg version
    with open(path, "w") as config_file:
        config.write(config_file)

 if __name__ == "__main__":
     path = "config.ini"
     createConfig(path)
# config generation end
configtrue = "False"
result = 0
port = 0
sus = 0
sus2 = 0
UpTime = 0
notonline = 0
discordcont = "None"
discordurl = "None"
method = "nul"
ip = "0.0.0.0"
API_URL = "url"
API_JSON = "json here"
errcode = "Incorrect response from the host"
readerror = False
Checksuccesstimes = 0
sleept = 30
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
pathhere = os.path.exists(path="config.ini")
if pathhere == True :
 try:
  config.read("config.ini")
 except AttributeError:
  print("")
  readerror = True

 if readerror == False :
   ip = config.get("Settings", "ip")
   configtrue = config.get("Settings", "configtrue")
   method = config.get("Settings", "method")
   port = config.get("Settings", "port")
   msgtype = config.get("Settings", "msgtype")
   discordurl = config.get("Settings", "discordurl")
   discordcont = config.get("Settings", "discordcont")
   API_URL = config.get("Settings", "API_URL")
   API_JSON = config.get("Settings", "API_JSON")
   sleeptime = config.get("Settings", "sleeptime")
   try:
     sleept = int(sleeptime)
   except ValueError:
       print("")

   try:
    API_JSONR = json.loads(API_JSON)
   except json.JSONDecodeError or json.JSONEncoderError :
     print ("")


if method == "ask" :
 if configtrue == "True" :
  print("methods:") #methods
  print("ping - the easiest verification method !dont work with ports! (can be blocked by host)") # ping method
  print("natcat - UDP/TCP verification method (work only on Unix systems)") # natcat method
  print("request - HTTP/S verification method !dont work with IP and ports! (can be blocked by host)") # HTTP method
  print("urllib - HTTP/S verification method !dont work with IP and ports! (can be blocked by host) needs instaled urllib3 module") # urllib3 method
  print("ping3 - the method is similar to ping, but also compare ms with the set maximum. Needs installed ping3 module") # ping3 method
  print("DEBUG: CONFIG READED")
  method = input("method: ")

sleep(1.5)
if configtrue == "False" :
 print()
 print("methods:") #methods
 print("ping - the easiest verification method !dont work with ports! (can be blocked by host)") # ping method
 print("natcat - UDP/TCP verification method (work only on Unix systems)") # natcat method
 print("request - HTTP/S verification method !dont work with IP and ports! (can be blocked by host)") # HTTP method
 print("urllib - HTTP/S verification method !dont work with IP and ports! (can be blocked by host) needs instaled urllib3 module") # urllib3 method
 print("ping3 - the method is similar to ping, but also compare ms with the set maximum. Needs installed ping3 module") # ping3 method
 print("bytesmax - uses the client's connection to the server to transmit incoming traffic(server its your machine) may not be stable")
 print()
 method = input("method: ")
if method != "bytesmax" :
 print()
 sleept = input("sleep time in sec. (use 30 or 240 to get the best result): ") #sleeptime
 print()
 print("message types: ")
 print("1 - discord webhook")
 print("2 - Using your API")
 print()
 msgtype = input("Type: ")
 if msgtype == "1" :
  discordurl = input("discord webhook url: ") # discord webhook url setting
  print()
  discordcont = input("discord message on error: ") # discord message setting

 if msgtype == "2" :
  API_URL = input("API url: ") # API url
  API_JSON = input("json data: ") # API Json now it's string
  API_JSONR = json.loads(API_JSON) #now it's json type

if method == "ping": # ping method start
 if configtrue == "False" :
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

   if response == 0:
    if notonline == 1 : # conn check
        print("connection established")
        notonline = 0
        param = {
             "content": "",
             "embeds": [
                 {
                     "title": "ping connection established!",
                     "description": "now server online.",
                     "color": 3717716
                 }
             ],
             "attachments": []
        }
        requests.post(discordurl, json = param)
        sus = 0
   if sus == 2 : #sus
     if notonline == 0 :
      if msgtype == "1" :   #DISC. WEBHOOK
       notonline = 1
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
  if configtrue == "False":
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
    if nc == 0:
     if notonline == 1:  # conn check
        print("connection established")
        notonline = 0
        param = {
        "content": "",
        "embeds": [
        {
        "title": "natcat connection established!",
        "description": "now server online.",
        "color": 3717716
        }
        ],
        "attachments": []
        }
        requests.post(discordurl, json=param)
        sus = 0

    if sus == 2 :
     if notonline == 0 :
      if msgtype == "1" :   #DISC. WEBHOOK
       notonline = 1
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
  if configtrue == "False":
   ip = input("URL: ")
  print("requests types:")
  print("1 - HEAD")
  print("2 - POST")
  print("3 - GET")
  rtype = input("Type: ") 
  while True :
    if rtype == "1" :
     r = requests.head(ip) #head
    if rtype == "2" :
     r = requests.post(ip) #post
    if rtype == "3" :
     r = requests.get(ip) #get
    status = r.status_code
    print(status)

    if status == 200 :
         print("server is ok") # OK res
         Checksuccesstimes = Checksuccesstimes + 1

    else:
        print("server error on connect!") # bad res
        sus = sus + 1

    if status == 200 :
        if notonline == 1:  # conn check
            print("connection established")
            notonline = 0
            param = {
                "content": "",
                "embeds": [
                    {
                        "title": "requests connection established!",
                        "description": "now server online.",
                        "color": 3717716
                    }
                ],
                "attachments": []
            }
            requests.post(discordurl, json=param)
            sus = 0

    if sus == 2 :
     if notonline == 0 :
      if msgtype == "1" :   #DISC. WEBHOOK
       notonline = 1
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
   if configtrue == "False":
    ip = input("URL: ")
   print("requests types:")
   print("1 - HEAD")
   print("2 - POST")
   print("3 - GET")
   rtype = input("Type: ") 
   while True :
     http = urllib3.PoolManager()
     if rtype == "1" :
      i100 = http.request('HEAD', ip) #head
     if rtype == "2" :
      i100 = http.request('POST', ip) #post
     if rtype == "3" :
      i100 = http.request('GET', ip) #get
     status = i100.status
     print(i100.status)
     if status == 200 :
         print("server is ok") # OK res
         Checksuccesstimes = Checksuccesstimes + 1

     else:
        print("server error on connect!") # bad res
        errcode2 = str(i100.status)
        sus = sus + 1
     if status == 200:
      if notonline == 1:  # conn check
        print("connection established")
        notonline = 0
        param = {
        "content": "",
        "embeds": [
        {
        "title": "urllib connection established!",
        "description": "now server online.",
        "color": 3717716
        }
        ],
        "attachments": []
        }
        requests.post(discordurl, json=param)
        sus = 0
     if sus == 2:
      if notonline == 0 :
        if msgtype == "1" :  # DISC. WEBHOOK
          notonline = 1
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
    if configtrue == "False":
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
     if i200 != None :
      if notonline == 1:  # conn check
        print("connection established")
        notonline = 0
        param = {
        "content": "",
        "embeds": [
        {
        "title": "ping3 connection established!",
        "description": "now server online.",
        "color": 3717716
        }
        ],
        "attachments": []
        }
        requests.post(discordurl, json=param)
        sus = 0
     if sus == 2 :
      if notonline == 0 :
       if  msgtype == "1" :
        notonline = 1
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
if method == "bytesmax":
    while True:
     print("the project description contains full documentation how to the use of this method")
     import Uptimerbytesmaxserver.py
     sleep(20)
print("")
print("do you know that you need to choose a method?")
