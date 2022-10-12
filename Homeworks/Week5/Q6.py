import requests

url = "http://localhost:4545/predict"

client = {
    "reports": 0, 
    "share": 0.245, 
    "expenditure": 3.438, 
    "owner": "yes"
}

result = requests.post(url, json=client).json()
result