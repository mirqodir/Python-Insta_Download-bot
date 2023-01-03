


def instadownload(link):
	import requests
	import json
	url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"
	querystring = {"url":link}
	headers = {
		"X-RapidAPI-Key": "a5fe30779amshb995e0a423e3022p1472a3jsnb3fa8ee90f11",
		"X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
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
			return dict
		elif rest['Type'] == 'Post-Video':
			dict['type'] = 'video'
			dict['media'] = rest['media']
			return dict
		elif rest['Type'] == 'Carousel':
			dict['type'] = 'carousel'
			dict['media'] = rest['media']
			return dict
		else:
			return 'Bad'



