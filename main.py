
import requests

token = '2619421814940190'

urls = [ f'https://www.superheroapi.com/api.php/{token}/search/Hulk',
    f'https://www.superheroapi.com/api.php/{token}/search/Thanos',
    f'https://www.superheroapi.com/api.php/{token}/search/Captain_America']


def intelligence():
    iq = []
    for link in urls:
        r = requests.get(link).json()
        results = r.get('results')
        for new_itog in results:
            new_dict = {}
            iq = new_itog['powerstats']['intelligence']
            new_dict[new_itog['name']] = iq



            itog = {f'Самый умный супергерой'}



print(intelligence())