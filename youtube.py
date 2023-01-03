


import requests
import json


url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"

querystring = {"url":'https://youtu.be/5z0r2PgGzEc'}

headers = {
	"X-RapidAPI-Key": "a5fe30779amshb995e0a423e3022p1472a3jsnb3fa8ee90f11",
	"X-RapidAPI-Host": "ytstream-download-youtube-videos.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
rest = json.loads(response.text)
	
if 'error' in rest:
	return 'Bad'
else:
	dict = {}
	if rest['Type'] == 'Post-Image':
		dict['type'] = 'image'
		dict['media'] = rest['media']
		print(dict)
	elif rest['Type'] == 'Post-Video':
		dict['type'] = 'video'
		dict['media'] = rest['media']
		print(dict)
	elif rest['Type'] == 'Carousel':
		dict['type'] = 'carousel'
		dict['media'] = rest['media']
		print(dict)
	else:
		print('Bad')
