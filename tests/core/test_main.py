import unittest
from datetime import datetime
from unittest import mock
from california_power_outage.core.power_outage import PowerOutage
from main import main


class TestMain(unittest.TestCase):

    def test_main_function(self):
        output_path = "./outputs/california_output_map.png"
        base_image_path = "../../assets/california_base_map.png"
        expected_power_outages: list[PowerOutage] = [PowerOutage(time=int(datetime.now().timestamp() * 1000),
                                                                 outage_type="Not Planned",
                                                                 latitude=37.15032999999999,
                                                                 longitude=-120.10193000000001),
                                                     PowerOutage(time=int(datetime.now().timestamp() * 1000),
                                                                 outage_type="Planned",
                                                                 latitude=33.384629742399994,
                                                                 longitude=-117.23682746969999)]

        with mock.patch('main.get_power_outage_data',
                        return_value=expected_power_outages) as mock_get_power_outage_data, \
                mock.patch('main.filter_by_current_time', return_value=expected_power_outages) as mock_time_boundary, \
                mock.patch('main.social_manager') as mock_social_manager:

            main()
            mock_get_power_outage_data.assert_called_once()
            mock_time_boundary.assert_called_once()
            mock_social_manager.assert_called_once_with(base_image_path=base_image_path,
                                                        output_path=output_path, power_outages=expected_power_outages)


if __name__ == '__main__':
    unittest.main()