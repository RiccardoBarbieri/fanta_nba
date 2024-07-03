from typing import Dict

from geopy.distance import geodesic
from geopy.geocoders import Nominatim


def get_distance_between_arenas(arena1: Dict, arena2: Dict):
    """
    Get the distance between two arenas.

    :return: The distance between the two arenas.
    """
    query1 = f'{arena1["name"]}, {arena1["city"]}, {arena1["state"]}'
    query2 = f'{arena2["name"]}, {arena2["city"]}, {arena2["state"]}'
    arena1_loc = Nominatim(user_agent='fanta_nba').geocode(query1, timeout=10)
    arena2_loc = Nominatim(user_agent='fanta_nba').geocode(query2, timeout=10)

    return geodesic((arena1_loc.latitude, arena1_loc.longitude),
                    (arena2_loc.latitude, arena2_loc.longitude)).km


if __name__ == '__main__':
    ar1 = {'name': 'TD Garden', 'city': 'Boston', 'state': 'MA'}
    ar2 = {'name': 'Madison Square Garden', 'city': 'New York', 'state': 'NY'}

    print(get_distance_between_arenas(ar1, ar2))
