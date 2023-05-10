import unittest
from unittest import mock
from california_power_outage.core.arcgis_api import fetch_power_outages


class TestArcgisApi(unittest.TestCase):
    def test_request_api(self):
        expected_result = {'key': 'value'}

        response = mock.Mock()
        with mock.patch('california_power_outage.core.arcgis_api.requests.get',
                        return_value=response) as mock_request:
            response.json.return_value = expected_result
            result = fetch_power_outages(url='http://test.com')
            self.assertEqual(result, expected_result)
            mock_request.assert_called_once_with('http://test.com')


if __name__ == '__main__':
    unittest.main()