from pprint import pprint
import googlemaps

API_KEY = 'AIzaSyCNgZ4vqkNiSw5jTDRzam1dAFqjFgkVWRs'

map_client = googlemaps.Client(API_KEY)

work_place_address = "9450 Gilman Drive, La Jolla, CA"

response = map_client.geocode(work_place_address)

pprint(response)
print(response[0]['geometry'])