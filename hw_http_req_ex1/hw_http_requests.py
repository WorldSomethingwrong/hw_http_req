import requests
url = "https://akabab.github.io/superhero-api/api/"
resp = requests.get(url + 'all.json')
res_js = resp.json()
for somebody in res_js:
    if somebody['name'] == 'Hulk':
        hulk_int = somebody['powerstats']['intelligence']
    if somebody['name'] == 'Captain America':
        Captain_int = somebody['powerstats']['intelligence']
    if somebody['name'] == 'Thanos':
        Thanos_int = somebody['powerstats']['intelligence']

mx = hulk_int
if Captain_int > mx:
    mx = Captain_int
elif Thanos_int > mx:
    mx = Thanos_int

if mx == hulk_int:
    print(f'Самый умный супергерой - Hulk. Его intelligence = {mx}')
elif mx == Captain_int:
        print(f'Самый умный супергерой - Captain America. Его intelligence = {mx}')
elif mx == Thanos_int:
    print(f'Самый умный супергерой - Thanos. Его intelligence = {mx}')

