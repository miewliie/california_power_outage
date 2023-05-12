from california_power_outage.core.arcgis_api import fetch_power_outages
from california_power_outage.core.power_outage import PowerOutage
from california_power_outage.storage.data_handler import power_outage_encoder


def get_power_outage_data() -> list[PowerOutage]:
    """ Fetch power outage data from ArcGIS API."""
    power_outages: dict[str, str] = fetch_power_outages()
    return power_outage_encoder(power_outages)