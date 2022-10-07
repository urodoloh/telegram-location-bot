import json
import math
import random


EARTH_RADIUS = 6371000  # meters
DEG_TO_RAD = math.pi / 180.0  # degrees to radians
THREE_PI = math.pi * 3
TWO_PI = math.pi * 2

# returns a decimal number {float()} and checks for a finite number {finite()}
def is_float_number(n):
    if ~math.isnan(float(n)) & math.isfinite(n):
        return True


def callback_radians(value):
    value * DEG_TO_RAD
    return value


def callback_degrees(value):
    value // DEG_TO_RAD
    return value


def recursive_convert(input, callback):
    if isinstance(input, list):
        for el in input:
            recursive_convert(el, callback)

    if isinstance(input, dict):
        input = json.loads(json.dumps(input))
        for key in input:
            if key in input:
                input[key] = recursive_convert(input[key], callback)
        return input

    if is_float_number(input):
        return callback(input)


# input going to val
def to_radians(input):
    return recursive_convert(input, callback_radians)


# input going to val
def to_degrees(input):
    return recursive_convert(input, callback_degrees)


# coords is an object: {latitude: y, longitude: x}
# toRadians() and toDegrees() convert all values of the object
def point_at_distance(input_coords, distance):
    result = {}
    # from coordinates to radians
    coords = to_radians(input_coords)
    # sin(radian latitude)
    sinLat = math.sin(coords["latitude"])
    # cos(radian latitude)
    cosLat = math.cos(coords["latitude"])

    # go fixed distance in random direction
    azimuth = random.random() * TWO_PI
    theta = distance / EARTH_RADIUS
    sinAzimuth = math.sin(azimuth)
    cosAzimuth = math.cos(azimuth)
    sinTheta = math.sin(theta)
    cosTheta = math.cos(theta)

    result["latitude"] = math.asin(sinLat * cosTheta + cosLat * sinTheta * cosAzimuth)
    result["longitude"] = coords["longitude"] + math.atan2(
        sinAzimuth * sinTheta * cosLat, cosTheta - sinLat * math.sin(result["latitude"])
    )

    # normalize -PI -> +PI radians
    result["longitude"] = ((result["longitude"] + THREE_PI) % TWO_PI) - math.pi

    return to_degrees(result)


def point_in_circle(coord, distance):
    rnd = random.random()
    # se square root of random number to avoid high density at the center
    random_distance = math.sqrt(rnd) * distance
    # print(random_distance)
    return point_at_distance(coord, random_distance)


# DISTANCE BETWEEN
def distance_between(start, end):
    start_point = to_radians(start)
    end_point = to_radians(end)
    # formulas
    # 	startPoint: a, b = A
    # 	endPoint: c, d = B

    # 	latitide 1 = a; latitude 2 = c
    # 	longitude 1 = b; longitude 2 = d

    # 	delta A = c - a; delta B = b - d
    delta = {
        "latitude": math.sin((end_point["latitude"] - start_point["latitude"]) / 2),
        "longitude": math.sin((end_point["longitude"] - start_point["longitude"]) / 2),
    }

    # theta = The central angle θ(theta) between any two points on the sphere is the Haversin formula
    # h(theta) = hav(delta A) + cos(a)*cos(b)*hav(delta B)
    # d = DISTANCE
    # d =2*r * arcsin sqrt(h(theta))

    haversinus = delta["latitude"] * delta["latitude"] + delta["longitude"] * delta[
        "longitude"
    ] * math.cos(start_point["latitude"]) * math.cos(end_point["latitude"])

    return (
        EARTH_RADIUS * 2 * math.atan2(math.sqrt(haversinus), math.sqrt(1 - haversinus))
    )


# GENERATE
fixed_num = 16


def get_random_long():
    num = round(random.random() * 180, fixed_num)
    minusOrPlus = random.randrange(0, 2)

    if minusOrPlus == 0:
        num = num * -1

    return num


# LATITUDE -90 to +90
def get_random_lat():
    num = round(random.random() * 90, fixed_num)
    minusOrPlus = random.randrange(0, 2)

    if minusOrPlus == 0:
        num = num * -1

    return num


def get_random_distance(min: int, max: int):
    min = math.ceil(min)
    max = math.floor(max)

    return math.floor(random.random() * (max - min)) + min


# def tests():
#     # print(is_float_number(0.0314e2))
#     # print(is_float_number(nan))
#     # print("random distance", get_random_distance(10000, 11001))
#     # print("random lat", get_random_lat())
#     # print("random long", get_random_long())

#     point_a = {"latitude": 24.3981552395868, "longitude": -46.32115695668249}
#     # end = {"latitude": -55.16875441233561, "longitude": 18.570534937768855}
#     random_dist = get_random_distance(10999, 11001)
#     # start = {"latitude": get_random_lat(), "longitude": get_random_lat()}
#     # end = {"latitude": get_random_long(), "longitude": get_random_long()}
#     # print("start:", start, "end:", end)
#     # print(
#     #     "distance between", distance_between(point_a, point_in_circle(point_a, 10000))
#     # )
#     # print("point at distance:", point_at_distance(point_a, 10000))
#     print(random_dist)
#     # print(random.randrange(0, 2))

#     # print(random.randrange(0, 2))

#     # print(random.randrange(0, 2))

#     # print(random.randrange(0, 2))

#     # print("start", start)
#     point_b = point_in_circle(point_a, 100)
#     # print("point in circle", point_in_circle(point_a, 10000))
#     print("distance between", distance_between(point_a, point_b))


# tests()

# -24.3981552395868 lat
# -46.32115695668249 long

# -55.16875441233561 lat
# -18.570534937768855 long

# 0.07350571379573101
