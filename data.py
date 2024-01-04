import requests
params={
    "amount":10,
    "type":"boolean"
}
response=requests.get("https://opentdb.com/api.php",params=params)
data = response.json()['results']

question_data = data