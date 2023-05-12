import unittest
from datetime import datetime
from unittest import mock

from california_power_outage.core.power_outage import PowerOutage
from california_power_outage.social.social_composer import create_map, compose_message


class TestSocialComposer(unittest.TestCase):

    def test_create_map(self):
        output_path: str = "./outputs/california_output_map.png"
        base_image_path = "assets/california_base_map.png"
        power_outages: list[PowerOutage] = [PowerOutage(time=int(datetime.now().timestamp() * 1000),
                                                        outage_type="Not Planned",
                                                        latitude=37.15032999999999,
                                                        longitude=-120.10193000000001),
                                            PowerOutage(time=int(datetime.now().timestamp() * 1000),
                                                        outage_type="Planned",
                                                        latitude=33.384629742399994,
                                                        longitude=-117.23682746969999)]
        with mock.patch('california_power_outage.social.social_composer.draw_power_outage_points',
                        return_value=output_path) as mock_draw:

            actual_result = create_map(base_image_path=base_image_path,
                                       power_outages=power_outages, output_path=output_path)

            mock_draw.assert_called_once_with(base_image_path=base_image_path, p_outage_data=power_outages,
                                              output_path=output_path)
            self.assertEqual(actual_result, output_path)

    def test_compose_message(self):
        message: str = "More info: https://hub.arcgis.com/datasets/CalEMA::power-outage-incidents/explore \n " \
                "#PowerOutage #California #CaliforniaPowerOutage #PowerOutageCalifornia"
        actual_result = compose_message()
        self.assertEqual(actual_result, message)


if __name__ == '__main__':
    unittest.main()