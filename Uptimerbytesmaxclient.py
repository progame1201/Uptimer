import os
import socket
import io
from time import sleep
import psutil
import configparser
#build 23
configtrue = "False"
readerror = False
#config generation
pathhere = os.path.exists(path="configbytesmaxclient.ini") #config here?
config = configparser.ConfigParser()
if pathhere == True : #regen start
  errorread = False
  try:
    config.read("configbytesmaxclient.ini") #read
  except AttributeError: # Attribute error?
    errorread = True
  if errorread == False : # read error?
    configversion = config.get("Info", "build")
    if configversion != "22" :
     os.remove("configbytesmaxclient.ini")
pathhere = os.path.exists(path="configbytesmaxclient.ini") #config here?
#config generation end
if pathhere == False : #if config not here
 def createConfig(path): #conf create
    config = configparser.ConfigParser()
    config.add_section("Settings") # SETTINGS
    config.set("Settings", "configtrue", "False") # CONF ENABLE?
    config.set("Settings", "ip", "0.0.0.0") # IP
    config.set("Settings", "port", "0000") # PORT
    config.add_section("Info")
    config.set("Info", "build", "22") # cfg version
    with open(path, "w") as config_file:
        config.write(config_file)

 if __name__ == "__main__":
     path = "configbytesmaxclient.ini"
     createConfig(path)
# config generation end
if pathhere == True :
 try:
  config.read("configbytesmaxclient.ini")
 except AttributeError:
  print("")
  readerror = True

 if readerror == False :
   ip = config.get("Settings", "ip")
   port = config.get("Settings", "port")
   configtrue = config.get("Settings", "configtrue")

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
unsus = 0
download = "0"
downloadnow = "0"
failed = False
if configtrue == "False" :
 port = input("port= ")
 ip = input("ip=")

def Restart():
  sleeptime = 5
  while True:
   if sleeptime != 0 :
    print("restart in " + str(sleeptime))
    sleep(1)
    sleeptime = sleeptime - 1
   if sleeptime == 0 :
    print("\n" * 100)

    os.system("python Uptimerbytesmaxclient.py")
    exit("exit with error. Auto restarted.")
sleep(2)
try:
 print("DEBUG: Connecting...")
 sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 port = int(port)
 sock.connect((ip, port))
 print("DEBUG: Connected")
except ConnectionError:
 Restart()
 exit("connection error: ConnectionError")
 sleep(999999)
except ConnectionAbortedError:
  Restart()
  exit("connection error: ConnectionAbortedError")
  sleep(999999)
except ConnectionResetError:
 Restart()
 exit("connection error: ConnectionResetError")
 sleep(999999)
except ConnectionRefusedError:
 Restart()
 exit("connection error: ConnectionRefusedError")
 sleep(999999)
except BrokenPipeError:
 Restart()
 exit("connection error: BrokenPipeError")
 sleep(999999)
except TimeoutError:
 Restart()
 exit("connection error: TimeoutError")
 sleep(999999)
except OSError:
 Restart()
 exit("connection error: OSError")
 sleep(999999)
while True :
  UPDATE_DELAY = 1

  net_stat = psutil.net_io_counters()
  net_in_1 = net_stat.bytes_recv
  sleep(1)
  net_stat = psutil.net_io_counters()
  net_in_2 = net_stat.bytes_recv
  net_in = round((net_in_2 - net_in_1) / 1024 / 1024, 3)
  data = str(net_in)
  data = data.encode("utf-8")
  print(str(data)+" MB/S")
  try:

   sock.send(bytearray(data))
   print("data sended")
   data = ""
  except ConnectionAbortedError:
   Restart()
   exit("Disconnection: Connection error: ConnectionAborted")
   sleep(60)
   break
  except ConnectionResetError:
   Restart()
   exit("Disconnection: Connection error: ConnectionReset")
   sleep(60)
   break
  except ConnectionRefusedError:
   Restart()
   exit("Disconnection: Connection error: ConnectionRefused")
   sleep(60)
   break
  except BrokenPipeError:
   Restart()
   exit("Disconnection: Connection error: BrokenPipeError")
   sleep(60)
   break
  except OSError:
   Restart()
   exit("Disconnection: Connection error: OSError")
   sleep(60)
   break
  except:
   Restart()
   exit("Disconnection: Connection error: UndetectedError")
   sleep(60)
   break
  sleep(3)

