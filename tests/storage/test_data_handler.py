import unittest
from unittest import mock

from california_power_outage.core.power_outage import PowerOutage
from california_power_outage.storage.data_handler import read_json, json, from_dict_to_power_outage, \
    power_outage_encoder


class TestDataHandler(unittest.TestCase):

    def test_read_json_output_json_if_content_exist(self):
        input_value: str = repr({"type": "FeatureCollection", "features": []})
        expected_value: str = repr({"type": "FeatureCollection", "features": []})
        file_path: str = 'tests/storage/test_data/read_json.json'

        mock_file = mock.mock_open(read_data=json.dumps(input_value))
        with mock.patch('california_power_outage.storage.data_handler.open', mock_file) as mock_open:
            result = read_json(file_path)
            mock_open.assert_called_once_with(file_path, 'r', encoding='utf-8')
            self.assertEqual(result, expected_value)

    def test_read_json_output_none_if_content_not_exist(self):
        input_value: str = 'Any content here'
        expected_value: str = None
        file_path: str = 'tests/storage/test_data/read_json.json'

        mock_file = mock.mock_open(read_data=json.dumps(input_value))
        with mock.patch('california_power_outage.storage.data_handler.open', mock_file) as mock_open, \
                mock.patch('california_power_outage.storage.data_handler.os.path.getsize',
                           return_value=0) as mock_getsize:
            value = read_json(file_path=file_path)
            mock_getsize.assert_called_once_with(file_path)
            self.assertEqual(expected_value, value)

    def test_from_dict_to_power_outage(self):
        power_outage_dict = {'attributes': {'StartDate': 1683200040000, 'OutageType': 'Not Planned'},
                             'geometry': {'x': -120.10193000000001, 'y': 37.15032999999999}}
        expected_power_outages: list[PowerOutage] = [PowerOutage(time=1683200040000,
                                                                 outage_type="Not Planned",
                                                                 latitude=37.15032999999999,
                                                                 longitude=-120.10193000000001)]
        with mock.patch('california_power_outage.storage.data_handler.PowerOutage',
                        return_value=expected_power_outages) as mock_power_outage:
            actual_result = from_dict_to_power_outage(power_outage_dict)
            mock_power_outage.assert_called_once_with(time=power_outage_dict['attributes']['StartDate'],
                                                      outage_type=power_outage_dict['attributes']['OutageType'],
                                                      latitude=power_outage_dict['geometry']['y'],
                                                      longitude=power_outage_dict['geometry']['x'])
            self.assertEqual(actual_result, expected_power_outages)

    def test_one_power_outage_encoder(self):
        power_outage_dict: dict = {"features": [{
            "attributes": {
                "StartDate": 1683200040000,
                "OutageType": "Not Planned"
            },
            "geometry": {
                "x": -120.10193000000001,
                "y": 37.15032999999999
            }
        }]
        }
        power_outages: PowerOutage = PowerOutage(time=1683200040000,
                                                 outage_type="Not Planned",
                                                 latitude=37.15032999999999,
                                                 longitude=-120.10193000000001)
        expected_po: list[PowerOutage] = [PowerOutage(time=1683200040000,
                                                      outage_type="Not Planned",
                                                      latitude=37.15032999999999,
                                                      longitude=-120.10193000000001)]
        with mock.patch('california_power_outage.storage.data_handler.from_dict_to_power_outage',
                        return_value=power_outages) as mock_from_dict_to_power_outage:
            actual_result = power_outage_encoder(power_outages=power_outage_dict)
            mock_from_dict_to_power_outage.assert_called_once_with(dict_data=power_outage_dict['features'][0])
            self.assertEqual(actual_result, expected_po)

    def test_two_power_outage_encoder(self):
        power_outage_dict: dict = {
            "features": [{"attributes": {"StartDate": 1683200040000, "OutageType": "Not Planned"},
                          "geometry": {
                              "x": -120.10193000000001,
                              "y": 37.15032999999999}},
                         {"attributes": {"StartDate": 1683707400000, "OutageType": "Planned"},
                          "geometry": {
                              "x": -117.23682746969999,
                              "y": 33.384629742399994
                          }}]}
        expected_power_outages: list[PowerOutage] = [PowerOutage(time=1683200040000,
                                                                 outage_type="Not Planned",
                                                                 latitude=37.15032999999999,
                                                                 longitude=-120.10193000000001),
                                                     PowerOutage(time=1683707400000,
                                                                 outage_type="Planned",
                                                                 latitude=33.384629742399994,
                                                                 longitude=-117.23682746969999)]
        actual_result = power_outage_encoder(power_outages=power_outage_dict)
        self.assertEqual(actual_result, expected_power_outages)


if __name__ == '__main__':
    unittest.main()
