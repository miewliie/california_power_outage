from california_power_outage.core.network_manager import get_power_outage_data
from california_power_outage.core.power_outage import PowerOutage
from california_power_outage.social.social_manager import social_manager

output_path = "./outputs/california_output_map.png"


def in_date_time_boundary(power_outages: list[PowerOutage]) -> list[PowerOutage]:
    return power_outages


def main():
    power_outages: list[PowerOutage] = get_power_outage_data()
    power_outages = in_date_time_boundary(power_outages)

    if not power_outages:
        print("No power outages found.")
        return

    social_manager(output_path=output_path, power_outages=power_outages)


if __name__ == '__main__':
    main()
