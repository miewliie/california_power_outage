import math

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

from california_power_outage.core.power_outage import PowerOutage

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


def draw_power_outage_points(base_image_path: str, output_path: str, p_outage_data: list[PowerOutage]):
    image = Image.open(base_image_path).convert('RGBA')
    im_width = image.size[0]
    im_height = image.size[1]

    icon_image = Image.open("./assets/power.png").convert('RGBA')
    icon_image = icon_image.resize((50, 50))

    for item in p_outage_data:
        x, y = item.longitude, item.latitude

        lon_x_pixel = convert_lon_to_x_pixel(im_width, x)
        lat_y_pixel = convert_lat_to_y_pixel(im_height, y)

        image.alpha_composite(icon_image, dest=(int(lon_x_pixel), int(lat_y_pixel) - 25))

    image.save(output_path)
    return output_path
