import math

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

TOP = 43.009518
BOTTOM = 31.534156
LEFT = -130.409591
RIGHT = -108.131211


def convert_lon_to_x_pixel(image_width: float, longitude: float):
    range_of_x = RIGHT - LEFT
    norm_value = longitude - LEFT
    pct_of_x = norm_value / range_of_x
    xp = pct_of_x * image_width
    return xp


def convert_lat_to_y_pixel(image_height: float, latitude: float):
    range_of_y = TOP - BOTTOM
    norm_value = latitude - BOTTOM
    pct_of_y = norm_value / range_of_y
    yp = image_height - (pct_of_y * image_height)
    return yp


def draw_fire_points(image_path, output_path, p_outage_data):
    image = Image.open(image_path).convert('RGBA')
    im_width = image.size[0]
    im_height = image.size[1]

    icon_image = Image.open("./assets/power.png").convert('RGBA')
    icon_image = icon_image.resize((50, 50))

    for item in p_outage_data:

        second = item['attributes']['StartDate'] / 1000
        date_time = datetime.fromtimestamp(second).replace(microsecond=0)
        h_today = datetime.now().hour
        today = datetime.now().date()

        if date_time.date() == today and date_time.hour == h_today:

            x, y = item['geometry']['x'], item['geometry']['y']

            lon_x_pixel = convert_lon_to_x_pixel(im_width, x)
            lat_y_pixel = convert_lat_to_y_pixel(im_height, y)

            image.alpha_composite(icon_image, dest=(int(lon_x_pixel), int(lat_y_pixel) - 25))

    image.save(output_path)
