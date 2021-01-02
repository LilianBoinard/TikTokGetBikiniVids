from TikTokApi import TikTokApi
import string
import random
from pathlib import Path

Path("downloads").mkdir(exist_ok=True) # creates folder
api = TikTokApi.get_instance(use_test_endpoints=True, debug=True)

username = ""
count = 1000
custom_did = ''.join(random.choice(string.digits) for num in range(19))
tiktoks = api.byUsername(username, count=count, custom_did=custom_did)
for tiktok in tiktoks:
    data = api.get_Video_By_TikTok(tiktok, custom_did=custom_did)
    with open("downloads/{}.mp4".format(str(tiktok.get('id'))), 'wb') as output:
        output.write(data)
