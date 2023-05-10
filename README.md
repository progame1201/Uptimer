# Uptimer
Uptimer
A simple python program to check if an ip/a domain is available

#Requirements:
Python (https://python.org/)
requests module (cmd -> pip install requests)
urllib3 module (cmd -> pip install urllib3) if you need to use the urllib method
ping3 module (cmd -> pip install ping3) if you need to use the ping3 method
configparser module (cmd -> pip install configparser) 
Or you can use my sh or bat files to install all modules

you need to write all links with https://

#Available methods
ping - simply sends a ping to an ip.
natcat - same as ping but allows ports specification (only available from unix systems).
request - sends a head request to a domain and does not stop until 200 response (may encounter difficulties with anti ddos services).
urllib - sends a head request to a domain and does not stop until 200 response (may encounter difficulties with anti ddos services) (needs urllib3 module cmd -> pip install urllib3). Ping3 - the method is similar to ping, but also compare ms with the set maximum. Needs installed ping3 module (cmd -> pip install ping3)
bytesmax - uses the client's connection to the server to transmit incoming traffic(server its your machine) may not be stable

You can use your API or discord webhook for notifications

#CONFIG:
```
[Settings] # Settings
configtrue = False # config is on?
ip = 0.0.0.0 # IP. if you need to use the site, write the full link https://example.com
port = 0000 # port only for method: natcat
method = ask #method. the ask method will ask which method you need
msgtype = 1 # message type 1 - discord webhook. 2 - your api.
discordurl = discord url here #discord webhook url
discordcont = discord message here #custom discord message
api_url = api url # api url
api_json = api json # api json code to be sent
sleeptime = 30 #sleep time

[Info] # INFO
version = 1.5.0 #if you change the value the config will be regenerated
```
Special thanks to: @Rysik5318#7967 and @EVA#1130
