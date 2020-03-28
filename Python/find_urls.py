import re
import requests

data = str(requests.get("https://restcountries.eu/rest/v2/all").json())

rs = re.findall("https://\w+.\w+.\w+.\w+.\w+",data)
print(rs)