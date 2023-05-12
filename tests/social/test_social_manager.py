import unittest
from datetime import datetime
from unittest import mock

from california_power_outage.core.power_outage import PowerOutage
from california_power_outage.social.social_manager import social_manager


class TestSocialManager(unittest.TestCase):
    def test_social_manager(self):
        output_path: str = "outputs/california_output_map.png"
        base_image_path = "assets/california_base_map.png"
        message: str = "test status"
        power_outages: list[PowerOutage] = [PowerOutage(time=int(datetime.now().timestamp() * 1000),
                                                        outage_type="Not Planned",
                                                        latitude=37.15032999999999,
                                                        longitude=-120.10193000000001),
                                            PowerOutage(time=int(datetime.now().timestamp() * 1000),
                                                        outage_type="Planned",
                                                        latitude=33.384629742399994,
                                                        longitude=-117.23682746969999)]

        with mock.patch('california_power_outage.social.social_manager.create_map',
                        return_value=output_path) as mock_create_map, \
                mock.patch('california_power_outage.social.social_manager.compose_message',
                           return_value=message) as mock_compose_message, \
                mock.patch('california_power_outage.social.social_manager.send_new_toot') as mock_send_new_toot:

            social_manager(base_image_path=base_image_path, output_path=output_path, power_outages=power_outages)

            mock_create_map.assert_called_once_with(base_image_path=base_image_path,
                                                    power_outages=power_outages, output_path=output_path)
            mock_compose_message.assert_called_once_with()
            mock_send_new_toot.assert_called_once_with(message=message, image_path=output_path)


if __name__ == '__main__':
    unittest.main()
