from typing import Dict

from geopy.distance import geodesic
from geopy.geocoders import Nominatim, DataBC, Photon

geocoders = [Nominatim(user_agent='fanta_nba'), DataBC(user_agent='fanta_nba'), Photon(user_agent='fanta_nba')]

def get_distance_between_arenas(arena1: Dict, arena2: Dict):
    """
    Get the distance between two arenas.

    :return: The distance between the two arenas.
    """
    query1 = f'{arena1["name"]}, {arena1["city"]}, {arena1["state"]}, {arena1["country"]}'
    query2 = f'{arena2["name"]}, {arena2["city"]}, {arena2["state"]}, {arena2["country"]}'

    arena1_loc = Nominatim(user_agent='fanta_nba').geocode(query1)
    arena2_loc = Nominatim(user_agent='fanta_nba').geocode(query2)

    # if arena1_loc is None:
    #     arena1_loc = Location("Old US Highway 85, Butte County, SD, United States of America", Point(44.967243, -103.771556), {})
    # if arena2_loc is None:
    #     arena2_loc = Location("Old US Highway 85, Butte County, SD, United States of America", Point(44.967243, -103.771556), {})

    if arena1_loc is None or arena2_loc is None:
        return 0

    return geodesic((arena1_loc.latitude, arena1_loc.longitude),
                    (arena2_loc.latitude, arena2_loc.longitude)).km


if __name__ == '__main__':
    ar1 = {'name': 'TD Garden', 'city': 'Boston', 'state': 'MA', 'country': 'US'}
    ar2 = {'name': 'Gainbridge Fieldhouse', 'city': 'Indianapolis', 'state': 'IN', 'country': 'US'}

    print(get_distance_between_arenas(ar1, ar2))
