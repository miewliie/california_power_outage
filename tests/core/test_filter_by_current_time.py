import unittest
from datetime import datetime

from california_power_outage.core.power_outage import PowerOutage
from main import filter_by_current_time


class TestFilterByCurrentTime(unittest.TestCase):

    def test_all_within_date_time_boundary(self):
        expected_power_outages: list[PowerOutage] = [PowerOutage(time=int(datetime.now().timestamp() * 1000),
                                                                 outage_type="Not Planned",
                                                                 latitude=37.15032999999999,
                                                                 longitude=-120.10193000000001),
                                                     PowerOutage(time=int(datetime.now().timestamp() * 1000),
                                                                 outage_type="Planned",
                                                                 latitude=33.384629742399994,
                                                                 longitude=-117.23682746969999)]
        actual_result = filter_by_current_time(power_outages=expected_power_outages)
        self.assertEqual(actual_result, expected_power_outages)

    def test_none_within_date_time_boundary(self):
        expected_power_outages: list[PowerOutage] = []
        power_outages: list[PowerOutage] = [PowerOutage(time=1683200040000,
                                                        outage_type="Not Planned",
                                                        latitude=37.15032999999999,
                                                        longitude=-120.10193000000001),
                                            PowerOutage(time=1683200040000,
                                                        outage_type="Planned",
                                                        latitude=33.384629742399994,
                                                        longitude=-117.23682746969999)]
        actual_result = filter_by_current_time(power_outages=power_outages)
        self.assertEqual(actual_result, expected_power_outages)

    def test_some_within_date_time_boundary(self):
        expected_power_outages: list[PowerOutage] = [PowerOutage(time=int(datetime.now().timestamp() * 1000),
                                                                 outage_type="Planned",
                                                                 latitude=33.384629742399994,
                                                                 longitude=-117.23682746969999)]

        power_outages: list[PowerOutage] = [PowerOutage(time=1683200040000,
                                                        outage_type="Not Planned",
                                                        latitude=37.15032999999999,
                                                        longitude=-120.10193000000001),
                                            PowerOutage(time=int(datetime.now().timestamp() * 1000),
                                                        outage_type="Planned",
                                                        latitude=33.384629742399994,
                                                        longitude=-117.23682746969999)]
        actual_result = filter_by_current_time(power_outages=power_outages)
        self.assertEqual(actual_result, expected_power_outages)


if __name__ == '__main__':
    unittest.main()
