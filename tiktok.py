
def tk(link):
	import requests
	import json
	url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

	querystring = {"url":link}

	headers = {
		"X-RapidAPI-Key": "a5fe30779amshb995e0a423e3022p1472a3jsnb3fa8ee90f11",
		"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	result = response.text
	rest = json.loads(result)
	return {'video':rest['video'][0],'music':rest['music'][0]}
	# return type(rest)
