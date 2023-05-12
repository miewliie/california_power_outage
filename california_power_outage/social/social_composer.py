from california_power_outage.core.power_outage import PowerOutage
from california_power_outage.draw.draw_power_outage import draw_power_outage_points


def create_map(base_image_path: str, power_outages: list[PowerOutage], output_path: str) -> str:
    """ Create map with power outage points. """
    map_output_path: str = draw_power_outage_points(base_image_path=base_image_path, p_outage_data=power_outages,
                                                    output_path=output_path)
    return map_output_path


def compose_message() -> str:
    """ Prepare static status message for social media. """

    status_message = "More info: https://hub.arcgis.com/datasets/CalEMA::power-outage-incidents/explore \n " \
                     "#PowerOutage #California #CaliforniaPowerOutage #PowerOutageCalifornia"

    return status_message
