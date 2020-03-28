import requests
url = "https://restcountries.eu/rest/v2/all"

data = requests.get(url).json()


flags = '''
    <h1 algin="center">Flags</h1>
    
    <p>{}</p>
'''.format(i.['flag'], i.['name'])

with open("flags.html","a") as file:
    for i in data:
        file.write(<img src={}>)
        
