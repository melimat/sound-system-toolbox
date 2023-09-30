import os
import math
import requests
import time
#import OpenSSL


def downloadImagery(width_min, length_min, width_max, length_max, resolution, folder_path, product_name):
    os.mkdir(folder_path)

    width = width_min
    length = length_min
    count = 1

    while (length <= length_max):
        while (width <= width_max):

            url = "https://mapy.cz/screenshoter?attach=1&width=2000&height=2000&p=1&url=https%3A%2F%2Fmapy.cz%2Fletecka%3Fx%3D" + str(length) + "%26y%3D" + str(width) + "%26z%3D19%26l%3D0"
            r = requests.get(url, allow_redirects=True)
            time.sleep(5)

            file = open(folder_path + product_name + "_" + str(count) + ".jpg", "wb")
            file.write(r.content)
            file.close()

            wordFile = open(folder_path + product_name + "_" + str(count) + ".jgw", "w")
            coords = to3857(length, width, resolution)
            wordFile.write(coords)
            wordFile.close()

            width += 0.003
            count += 1

        length += 0.005
        width = width_min


def to3857(x_longitude, y_latitude, resolution):
    x = x_longitude * 0.017453292519943295 * 6378137
    a = y_latitude * 0.017453292519943295
    y = 3189068.5 * math.log((1.0 + math.sin(a)) / (1.0 - math.sin(a)))
    offset = resolution * 1000
    x, y = x-offset, y + offset
    coords = str(resolution) + '\r\n0.0\r\n0.0\r\n-' + str(resolution) + '\r\n' + str(x) + '\r\n' + str(y)
    return coords


