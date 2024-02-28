import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
hours = response.json()["hours"]
minutes = response.json()["minutes"]
seconds = response.json()["seconds"]

print("Current time: "+ hours + " hrs " + minutes + " min and " + seconds + " sec")