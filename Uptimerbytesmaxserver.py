import os
import socket
from time import sleep
import requests
#build 20
sus = False
unsus = 0
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
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
