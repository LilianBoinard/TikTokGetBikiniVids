from TikTokApi import TikTokApi

api = TikTokApi()
url = "https://www.tiktok.com/@tachavde/video/6902323204312943874"
data = api.get_Video_By_Url(url)
with open("downloads/test.mp4", 'wb') as output:
	output.write(data)
