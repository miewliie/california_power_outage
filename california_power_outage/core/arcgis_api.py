import requests

URL = 'https://services.arcgis.com/BLN4oKB0N1YSgvY8/arcgis/rest/services/Power_Outages_(' \
      'View)/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json '


def fetch_power_outages(url: str = URL):
    response = requests.get(url)
    return response.json()



