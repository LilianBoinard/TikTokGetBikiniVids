from TikTokApi import TikTokApi
from pathlib import Path
import sys
import random
import string
api = TikTokApi()
Path("downloads").mkdir(exist_ok=True)

try:
	option = sys.argv[1]
except IndexError:
	print("You have to type a option")
else:
	if option == '-url':
		try:
			url = sys.argv[2]
		except IndexError:
			print("You have to type a URL")
		else:
			data = api.get_Video_By_Url(url)
			with open("downloads/test.mp4", 'wb') as output:
				output.write(data)
	elif option == '-user':
		try:
			username = sys.argv[2]
		except IndexError:
			print("You have to type a username")
		else:
			count = 1000
			custom_did = ''.join(random.choice(string.digits) for num in range(19))
			tiktoks = api.byUsername(username, count=count, custom_did=custom_did)
			for tiktok in tiktoks:
				data = api.get_Video_By_TikTok(tiktok, custom_did=custom_did)
				with open("downloads/{}.mp4".format(str(tiktok.get('id'))), 'wb') as output:
					output.write(data)
					
	elif option == '-tag':
		try:
			tag = sys.argv[2]
		except IndexError:
			print("You have to type a tag")
		else:
			count = 10
			custom_did = ''.join(random.choice(string.digits) for num in range(19))
			tiktoks = api.byHashtag(tag, count=count, custom_did=custom_did)
			for tiktok in tiktoks:
				data = api.get_Video_By_TikTok(tiktok, custom_did=custom_did)
				with open("downloads/{}.mp4".format(str(random.randint(1,10000))), 'wb') as output: 
					output.write(data)
	else:
		print("Invalid option")
