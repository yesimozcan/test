#!/usr/bin/python3
import requests
import re
with open("ll.txt") as url:
	for i in url.read().split("\n"):
		dblist=[]
		response=requests.get(i)
		if response.status_code == 200 and re.search('couchdb',str(response.content)) != None:
			allDbs=requests.get(i+"/_all_dbs")
			dblist.append(allDbs.content)
print (dblist)
