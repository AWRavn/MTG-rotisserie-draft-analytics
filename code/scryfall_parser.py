import requests, urllib.request

def get_url():

	req = requests.get("https://api.scryfall.com/bulk-data")
	for line in req.json()["data"]:
		if line["type"] == "default_cards":
			return line["download_uri"]

def download_data(url):

	data = urllib.request.urlretrieve(url, "../data/scryfall_data.json")
	return data

if __name__ == '__main__':
	url = get_url()
	download_data(url)