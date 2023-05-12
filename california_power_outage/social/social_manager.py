from california_power_outage.core.power_outage import PowerOutage
from california_power_outage.social.social_composer import create_map, compose_message
from california_power_outage.social.toot import send_new_toot


def social_manager(base_image_path: str, output_path: str, power_outages: list[PowerOutage]):
    image_path: str = create_map(base_image_path=base_image_path, power_outages=power_outages, output_path=output_path)
    status_message: str = compose_message()
    send_new_toot(message=status_message, image_path=image_path)