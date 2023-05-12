import unittest
from unittest import mock

from california_power_outage.core.network_manager import get_power_outage_data
from california_power_outage.core.power_outage import PowerOutage
from california_power_outage.storage.data_handler import read_json


class TestNetworkManager(unittest.TestCase):

    def test_fetch_power_outage_data(self):
        power_outages = read_json('tests/core/test_data/power_outage_data.json')
        expected_power_outages: list[PowerOutage] = [PowerOutage(time=1683200040000,
                                                                 outage_type="Not Planned",
                                                                 latitude=37.15032999999999,
                                                                 longitude=-120.10193000000001),
                                                     PowerOutage(time=1683707400000,
                                                                 outage_type="Planned",
                                                                 latitude=33.384629742399994,
                                                                 longitude=-117.23682746969999)]

        with mock.patch('california_power_outage.core.network_manager.fetch_power_outages',
                        return_value=power_outages) as mock_fetch_power_outages, \
                mock.patch('california_power_outage.core.network_manager.power_outage_encoder',
                           return_value=expected_power_outages) as mock_power_outage_encoder:
            result = get_power_outage_data()
            mock_fetch_power_outages.assert_called_once()
            mock_power_outage_encoder.assert_called_once_with(power_outages)

            self.assertEqual(result, expected_power_outages)

    def test_fetch_empty_power_outage_data(self):
        power_outages = read_json('tests/core/test_data/empty_power_outage_data.json')
        expected_power_outages: list[PowerOutage] = []

        with mock.patch('california_power_outage.core.network_manager.fetch_power_outages',
                        return_value=power_outages) as mock_fetch_power_outages, \
                mock.patch('california_power_outage.core.network_manager.power_outage_encoder',
                           return_value=expected_power_outages) as mock_power_outage_encoder:
            result = get_power_outage_data()
            mock_fetch_power_outages.assert_called_once()
            mock_power_outage_encoder.assert_called_once_with(power_outages)

            self.assertEqual(result, expected_power_outages)


if __name__ == '__main__':
    unittest.main()
