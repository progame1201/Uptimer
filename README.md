# Uptimer
Uptimer - a simple python program that tracks server crashes or DDoS (DoS).

You need to run:
Python(3.9-3.10).
requests module (https://pypi.org/project/requests/).
OS: Wndows or Linux(the program tested in ubuntu).

Methods:
ping - Just an implemented method, uses a regular ping.
natcat - The netcat method can use ports, but is only available on Unix systems.
http - Sends a head request to the site and waits for a 200 response (If you use CloudFlare to protect your site, allow the IP address from which the request will be sent).

Opportunities:
Set the time after which the request will be sent.
link a discord webhook with your own error message.
Maximum number of incorrect answers of host: 2.

In the future, the program will be refined and use newer methods.

Thank you very much: Rysik5318#7967 and EVA#1130 for assistance in the implementation of the project.
