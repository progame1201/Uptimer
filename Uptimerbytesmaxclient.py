import os
import socket
import io
from time import sleep
#build 20
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
unsus = 0
download = "0"
downloadnow = "0"
failed = False
port = int(input("port= "))
ip = input("ip=")
sleep(2)
try:
 print("DEBUG: Connecting...")
 sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 sock.connect((ip, port))
 print("DEBUG: Connected")
except ConnectionError:
 print("connection error: ConnectionError")
 sleep(999999)
except ConnectionAbortedError:
  print("connection error: ConnectionAborted")
  sleep(999999)
except ConnectionResetError:
 print("connection error: ConnectionReset")
 sleep(999999)
except ConnectionRefusedError:
 print("connection error: ConnectionRefused")
 sleep(999999)
except BrokenPipeError:
 print("connection error: BrokenPipeError")
 sleep(999999)
except TimeoutError:
 print("connection error: TimeoutError")
 sleep(999999)
except OSError:
 print("connection error: OSError")
 sleep(999999)
while True :
  import psutil
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
   print("Disconnection: Connection error: ConnectionAborted")
   sleep(60)
   break
  except ConnectionResetError:
   print("Disconnection: Connection error: ConnectionReset")
   sleep(60)
   break
  except ConnectionRefusedError:
   print("Disconnection: Connection error: ConnectionRefused")
   sleep(60)
   break
  except BrokenPipeError:
   print("Disconnection: Connection error: BrokenPipeError")
   sleep(60)
   break
  except OSError:
   print("Disconnection: Connection error: OSError")
   sleep(60)
   break
  except:
   print("Disconnection: Connection error: UndetectedError")
   sleep(60)
   break
  sleep(3)

