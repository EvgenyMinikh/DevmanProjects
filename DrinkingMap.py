import json
from yandex_geocoder import Client as geo
from geopy import distance


NUMBER_OF_PUBS_TO_SEARCH = 5


def get_pub_distances(pub):
  return pub['distance']


with open("data.json", encoding='cp1251') as json_file:
  json_content = json.load(json_file)

my_address = input("Enter your address: ")
my_position = geo.coordinates(my_address)

pubs_with_distance = []

for pub in json_content:
  pub_details = {}
  
  pub_name = pub["Name"]
  pub_latitude = pub['geoData']['coordinates'][1]
  pub_longitude = pub['geoData']['coordinates'][0]
  distance_to_pub = distance.distance(my_position, (pub_longitude, pub_latitude)).km

  pub_details["title"] = pub_name
  pub_details["longitude"] = pub_longitude
  pub_details["latitude"] = pub_latitude
  pub_details["distance"] = distance_to_pub

  pubs_with_distance.append(pub_details)

nearest_pubs = sorted(pubs_with_distance, key=get_pub_distances)[0:NUMBER_OF_PUBS_TO_SEARCH]

for pub in nearest_pubs:
  print(pub['title'])