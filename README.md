# Uptimer
Uptimer
A simple python program to check if an ip/a domain is available

Requirements:
Python (https://python.org/)
requests module (cmd -> pip install requests)
urllib3 module (cmd -> pip install urllib3) if you need to use the urllib method
ping3 module (cmd -> pip install ping3) if you need to use the ping3 method

you need to write all links with https://

Available methods
ping - simply sends a ping to an ip.
natcat - same as ping but allows ports specification (only available from unix systems).
request - sends a head request to a domain and does not stop until 200 response (may encounter difficulties with anti ddos services).
urllib - sends a head request to a domain and does not stop until 200 response (may encounter difficulties with anti ddos services) (needs urllib3 module cmd -> pip install urllib3). Ping3 - the method is similar to ping, but also compare ms with the set maximum. Needs installed ping3 module (cmd -> pip install ping3)

You can use your API or discord webhook for notifications

Special thanks to: @Rysik5318#7967 and @EVA#1130
