from http.client import HTTPConnection
import urllib.parse
import re

con = HTTPConnection('vps796621.ovh.net', 8635)

proxy = input("proxy ? ")
side = input("side ? ")
value = input("value ? ")
print("")

params = urllib.parse.urlencode({'value': value, 'sides': side, 'proxy': proxy})
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

con.request("POST", "/intervention", params, headers)

r1 = con.getresponse()
print(r1.status, r1.reason)

con.close()