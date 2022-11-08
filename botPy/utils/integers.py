from random import randrange
from random import uniform
from math import radians, cos, sin, asin, sqrt

SPREAD_NUMBER = 16

TEN_KM_LAT = 0.04021889 * 2
TEN_KM_LONG = 0.08043778 * 2

ELEVEN_KM_LAT = 0.044240779 * 2
ELEVEN_KM_LONG = 0.088481558 * 2

# LONGITUDE -180 to +180
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
def range_ten_eleven_x():
    return uniform(TEN_KM_LAT, ELEVEN_KM_LAT)


def range_ten_eleven_y():
    return uniform(TEN_KM_LONG, ELEVEN_KM_LONG)


def range_zero_eleven_x():
    return uniform(0, ELEVEN_KM_LAT)


def range_zero_eleven_y():
    return uniform(0, ELEVEN_KM_LONG)


MINUS = "minus"
PLUS = "plus"


def minus_or_plus():
    if randrange(0, 1) == 0:
        return -1
    return 1


x = 0
y = 1


def x_or_y():
    if randrange(0, 1) == 0:
        return x
    return y


def point_at_distance(input):
    # dict for return result
    coords = {}
    latitude = input["latitude"]
    longitude = input["longitude"]

    # it will store the random distance which we add to input coords:
    randomSide = {}

    # this is a function, because you need to call
    #  it for each variable separately:
    def minus_or_plus():
        if randrange(0, 2) == 0:
            return -1
        return 1

    # called once:
    xOrY = randrange(0, 2)  # 0 - x, 1 - y

    if xOrY == 0:  # X
        # plus or minus X on 10~11 kilometers
        randomSide["latitude"] = range_ten_eleven_x() * minus_or_plus()
        # plus or minus Y on 0~11 kilometers
        randomSide["longitude"] = range_zero_eleven_y() * minus_or_plus()
    elif xOrY > 0:  # Y
        # plus or minus Y on 10~11 kilometers
        randomSide["latitude"] = range_ten_eleven_y() * minus_or_plus()
        # plus or minus X on 0~11 kilometers
        randomSide["longitude"] = range_zero_eleven_x() * minus_or_plus()

    coords["latitude"] = latitude + randomSide["latitude"]
    coords["longitude"] = longitude + randomSide["longitude"]

    return coords


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
    lat1 = 53.32055555555556
    # lat2 = 53.31861111111111
    lon1 = -1.7297222222222221
    # lon2 = -1.6997222222222223
    coordinates = {
        "longitude": lon1,
        "latitude": lat1,
    }

    print(point_at_distance(coordinates))

    print(distance_between(random_coordinates, coordinates), "K.M")


tests_distance()
