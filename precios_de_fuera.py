import requests

url = "https://gas-price.p.rapidapi.com/europeanCountries"

headers = {
	"X-RapidAPI-Key": "74c27fb50emsh28a88b9fd265ffep17e183jsn435ba4475174",
	"X-RapidAPI-Host": "gas-price.p.rapidapi.com"
}

response = requests.get(url, headers=headers)



print(response.join())