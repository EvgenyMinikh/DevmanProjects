import json
import folium
from yandex_geocoder import Client as geo
from geopy import distance
from flask import Flask

NUMBER_OF_PUBS_TO_SEARCH = 5


def get_pub_distances(pub):
    return pub['distance']


def get_pub_map():
    with open('index.html') as file:
        return file.read()


def get_my_coordinates():
    my_address = input("Enter your address: ")
    my_position = geo.coordinates(my_address)

    return my_position[1], my_position[0]


with open("data.json", encoding='cp1251') as json_file:
    json_content = json.load(json_file)

my_position_latitude, my_position_longitude = get_my_coordinates()

pubs_with_distance = []
for pub in json_content:
    pub_details = {}

    pub_name = pub["Name"]
    pub_latitude = pub['geoData']['coordinates'][1]
    pub_longitude = pub['geoData']['coordinates'][0]
    distance_to_pub = distance.distance((my_position_latitude, my_position_longitude), (pub_latitude, pub_longitude)).km

    pub_details["title"] = pub_name
    pub_details["longitude"] = pub_longitude
    pub_details["latitude"] = pub_latitude
    pub_details["distance"] = distance_to_pub

    pubs_with_distance.append(pub_details)

nearest_pubs = sorted(pubs_with_distance, key=get_pub_distances)[0:NUMBER_OF_PUBS_TO_SEARCH]

m = folium.Map(location=[my_position_latitude, my_position_longitude], zoom_start=15)

for pub in nearest_pubs:
    folium.Marker([
        pub["latitude"],
        pub["longitude"]
    ],
        popup='<b>{}</b>'.format(pub["title"]),
        tooltip=pub["title"]
    ).add_to(m)

folium.Marker([
    my_position_latitude,
    my_position_longitude
],
    popup='<b>{}</b>'.format("My position"),
    tooltip="I'm here",
    icon=folium.Icon(color='red')
).add_to(m)

m.save('index.html')
app = Flask(__name__)
app.add_url_rule('/', 'hello', get_pub_map)
app.run('0.0.0.0')
