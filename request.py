import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Please enter the news text you want to verify': 'modi is president'})

print(r.json())