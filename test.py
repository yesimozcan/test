#!/usr/bin/python3
import requests
import re
import json
with open("list") as url:
	for i in url.read().split("\n"):
		try:
			response=requests.get(i)
			if response.status_code == 200 and re.search('couchdb',str(response.content)) != None:
				allDbs=requests.get(i+"/_all_dbs").json()
				for x in allDbs:
					response2=requests.get(i+"/"+x)
					if (len(allDbs) > 1) and (response2.status_code == 200):
						sonuc=(response2.url,response2.status_code)
						f=open("ciktim.txt","a")
						f.write(str(sonuc)+"\n")
						f.close()
		except IOError as e:
			pass
