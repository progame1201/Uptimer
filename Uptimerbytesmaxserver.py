import os
import socket
from time import sleep
import requests
import configparser
#build 21
configtrue = "False"
readerror = False
#config generation
pathhere = os.path.exists(path="configbytesmaxserver.ini") #config here?
config = configparser.ConfigParser()
if pathhere == True : #regen start
  errorread = False
  try:
    config.read("configbytesmaxserver.ini") #read
  except AttributeError: # Attribute error?
    errorread = True
  if errorread == False : # read error?
    configversion = config.get("Info", "build")
    if configversion != "21" :
     os.remove("configbytesmaxserver.ini")
pathhere = os.path.exists(path="configbytesmaxserver.ini") #config here?
#config generation end
if pathhere == False : #if config not here
 def createConfig(path): #conf create
    config = configparser.ConfigParser()
    config.add_section("Settings") # SETTINGS
    config.set("Settings", "configtrue", "False") # CONF ENABLE?
    config.set("Settings", "ip", "0.0.0.0") # IP
    config.set("Settings", "port", "0000") # PORT
    config.set("Settings", "maxdata2", "1000") # IP
    config.set("Settings", "discordurl", "None") # PORT for natcat
    config.set("Settings", "discordcont", "sus")  # PORT for natcat
    config.add_section("Info")
    config.set("Info", "build", "21") # cfg version
    with open(path, "w") as config_file:
        config.write(config_file)

 if __name__ == "__main__":
     path = "configbytesmaxserver.ini"
     createConfig(path)
# config generation end
if pathhere == True :
 try:
  config.read("configbytesmaxserver.ini")
 except AttributeError:
  print("")
  readerror = True

 if readerror == False :
   ip = config.get("Settings", "ip")
   port = config.get("Settings", "port")
   configtrue = config.get("Settings", "configtrue")
   maxdata2 = config.get("Settings", "maxdata2")
   discordurl = config.get("Settings", "discordurl")
   discordcont = config.get("Settings", "discordcont")

sus = False
unsus = 0
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if configtrue == "False" :

 port = input("port= ")
 ip = input("ip= ")
 print("note that the maximum traffic should be specified in megabytes and not megabits")
 maxdata2 = input("max data per sec= ")
 discordurl = input("discord webhook url: ") # discord webhook url setting
 print()
 discordcont = input("discord message on error: ") # discord message setting
port = int(port)
sock.bind((ip, port))
sock.listen(1)
while True :
 print("DEBUG: WAITING FOR CONNECTION")
 connect = conn, addr = sock.accept()
 print("DEBUG: SOCKET CONNECTED")
 while True:

    data = conn.recv(5)
    data = data.decode("utf-8")
    print(data)
    if not data:
        data = None
        param = {
            "content": "Message from the user: " + discordcont,
            "embeds": [
                {
                    "title": "bytesmax Connection reset",
                    "description": "Connection reset",
                    "color": 16763904
                }
            ],
            "attachments": []
        }  # Discord error
        requests.post(discordurl, json=param)
        break
    data = float(data)
    if data  >= float(maxdata2):
      if sus == False :
         print("data > maxdata2")
         sus = True
         param = {
             "content": "Message from the user: " + discordcont,
             "embeds": [
                 {
                     "title": "bytesmax data > maxdata2",
                     "description": "incoming traffic:" + str(data) +"MB/s",
                     "color": 16711680
                 }
             ],
             "attachments": []
         }  # Discord error
         requests.post(discordurl, json=param)
    if sus == True:
      if data <=float(maxdata2) :
       unsus = unsus + 1
       if unsus == 3:
          unsus = 0
          sus = False
          param = {
             "content": "",
             "embeds": [
                 {
                     "title": "bytesmax connection established!",
                     "description": "now server ok.",
                     "color": 3717716
                 }
             ],
             "attachments": []
          }
          requests.post(discordurl, json=param)
