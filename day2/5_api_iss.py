import requests
import pandas as pd
import json

url = "http://api.open-notify.org/iss-now.json"
header = {
    "User-Agent":"Nasa"
}

data = requests.get(url,headers=header)
print(data)
print(data.text)
json_da = json.loads(data.text)
timea =json_da["timestamp"]
lat = json_da["iss_position"]["latitude"]
long = json_da["iss_position"]["longitude"]
print(timea)
print(lat)
print(long)
#df = pd.DataFrame
mew_js = [
    {"time":str(timea),
     "lat":str(lat),
     "long":str(long)
     }
]

df = pd.DataFrame(mew_js)
df.to_csv("out.csv")