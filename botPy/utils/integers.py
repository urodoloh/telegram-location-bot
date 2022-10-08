from random import randrange
from random import uniform
from math import radians, cos, sin, asin, sqrt

SPREAD_NUMBER = 16

TEN_KM_LAT = 0.04021889 * 2
TEN_KM_LONG = 0.08043778 * 2

ELEVEN_KM_LAT = 0.044240779 * 2
ELEVEN_KM_LONG = 0.088481558 * 2


def get_random_long():
    num = round(uniform(0, 180), SPREAD_NUMBER)
    minusOrPlus = randrange(0, 2)

    if minusOrPlus == 1:
        num = num * -1

    return num


# LATITUDE -90 to +90
def get_random_lat():
    num = round(uniform(0, 90), SPREAD_NUMBER)
    minusOrPlus = randrange(0, 2)

    if minusOrPlus == 1:
        num = num * -1

    return num


random_coordinates = {"latitude": get_random_lat(), "longitude": get_random_long()}

# distance between 10 and 11 km
range_ten_eleven_x = uniform(TEN_KM_LAT, ELEVEN_KM_LAT)
range_ten_eleven_y = uniform(TEN_KM_LONG, ELEVEN_KM_LONG)

range_zero_eleven_x = uniform(0, ELEVEN_KM_LAT)
range_zero_eleven_y = uniform(0, ELEVEN_KM_LONG)


minus_or_plus = randrange(0, 1)
minus_or_plus_two = randrange(0, 1)


x_or_y = randrange(0, 1)


def point_at_distance(input):
    coord = {}
    latitude = input["latitude"]
    longitude = input["longitude"]

    if x_or_y == 0:
        if minus_or_plus == 0:
            coord["latitude"] = latitude - range_ten_eleven_x
        if minus_or_plus == 1:
            coord["latitude"] = latitude - range_ten_eleven_x

        if minus_or_plus_two == 0:
            coord["longitude"] = longitude - range_zero_eleven_x
        if minus_or_plus_two == 1:
            coord["longitude"] = longitude + range_zero_eleven_x

        return coord

    if x_or_y == 1:
        if minus_or_plus == 0:
            coord["longitude"] = longitude - range_ten_eleven_y
        if minus_or_plus == 1:
            coord["longitude"] = longitude + range_ten_eleven_y

        if minus_or_plus_two == 0:
            coord["latitude"] = latitude - range_zero_eleven_x
        if minus_or_plus_two == 1:
            coord["latitude"] = latitude + range_zero_eleven_x

        return coord


def tests():
    # print(x_or_y)
    # print(range_ten_eleven_x, range_zero_eleven_y)
    print(random_coordinates)
    print(point_at_distance(random_coordinates))


# x or y
# left of right,
# if 0: x без ограничений
# if 1: y без ограничений


def distance_between(start, end):

    point_a = {}
    point_b = {}
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(start["longitude"])
    lon2 = radians(end["longitude"])
    lat1 = radians(start["latitude"])
    lat2 = radians(end["latitude"])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    c = 2 * asin(sqrt(a))

    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371

    # calculate the result
    return c * r


def tests_distance():
    coordin = {}
    coordin = point_at_distance(random_coordinates)
    # driver code
    # lat1 = 53.32055555555556
    # lat2 = 53.31861111111111
    # lon1 = -1.7297222222222221
    # lon2 = -1.6997222222222223
    lat1 = random_coordinates["latitude"]
    lon1 = random_coordinates["longitude"]
    lat2 = coordin["latitude"]
    lon2 = coordin["longitude"]

    print(distance_between(random_coordinates, coordin), "K.M")
