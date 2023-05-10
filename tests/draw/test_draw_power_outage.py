import unittest
from unittest import mock
from unittest.mock import MagicMock

from california_power_outage.draw.draw_power_outage import convert_lon_to_x_pixel, \
    convert_lat_to_y_pixel, ImageDraw, Image, draw_power_outage_points, datetime


class TestDrawPowerOutage(unittest.TestCase):
    def test_convert_lon_to_x_pixel(self):
        im_width = 1600
        longitude = -118.0585835
        expected = 887.0309241515766

        result = convert_lon_to_x_pixel(image_width=im_width, longitude=longitude)
        self.assertEqual(result, expected)

    def test_convert_lat_to_y_pixel(self):
        im_height = 1200
        latitude = 34.011356
        expected = 940.9545772935094

        result = convert_lat_to_y_pixel(image_height=im_height, latitude=latitude)
        self.assertEqual(result, expected)

    def test_draw_power_outage(self):
        output_path = "./outputs/california_output_map.png"
        outage_data = [{'attributes': {'StartDate': int(datetime.now().timestamp() * 1000)},
                        'geometry': {'x': -118.0585835, 'y': 34.011356}}]
        mocked_image = 'mocked_image'
        with mock.patch('california_power_outage.draw.draw_power_outage.Image.open') as mock_open, \
                mock.patch.object(Image.Image, 'convert', return_value=mocked_image) as mock_convert, \
                mock.patch('california_power_outage.draw.draw_power_outage.convert_lon_to_x_pixel') as mock_lon, \
                mock.patch('california_power_outage.draw.draw_power_outage.convert_lat_to_y_pixel') as mock_lat:

            mock_open.resize.return_value = mock.MagicMock(spec=Image, size=(50, 50), mode='RGBA')
            mock_convert.return_value = mock.MagicMock(spec=Image, size=(1600, 1200), mode='RGBA')

            mock_lon.return_value = 887.0309241515766
            mock_lat.return_value = 940.9545772935094

            actual_result = draw_power_outage_points(image_path='./assets/map.png',
                                                     output_path=output_path, p_outage_data=outage_data)

            mock_open.assert_called()
            mock_open.assert_called()
            mock_lon.assert_called_once()
            mock_lat.assert_called_once()
            # mock_convert.alpha_composite.assert_called_once()
            self.assertEqual(actual_result, output_path)


if __name__ == '__main__':
    unittest.main()
