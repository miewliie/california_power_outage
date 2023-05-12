from datetime import datetime

from california_power_outage.core.network_manager import get_power_outage_data
from california_power_outage.core.power_outage import PowerOutage
from california_power_outage.social.social_manager import social_manager

output_path = "outputs/california_output_map.png"
base_image_path = "assets/california_base_map.png"


def filter_by_current_time(power_outages: list[PowerOutage]) -> list[PowerOutage]:

    power_outages_list: list[PowerOutage] = []
    for power_outage in power_outages:
        power_o_datetime = datetime.fromtimestamp(power_outage.time / 1000).replace(microsecond=0)

        today_date = datetime.now().date()
        current_hour = datetime.now().hour

        if power_o_datetime.date() == today_date and power_o_datetime.hour == current_hour:
            power_outages_list.append(power_outage)
    return power_outages_list


def main():
    power_outages: list[PowerOutage] = get_power_outage_data()

    if not power_outages:
        print("No new power outages found.")
        return

    power_outages = filter_by_current_time(power_outages=power_outages)

    if not power_outages:
        print("No power outages in this hour after filter.")
        return

    social_manager(base_image_path=base_image_path, output_path=output_path, power_outages=power_outages)


if __name__ == '__main__':
    main()
