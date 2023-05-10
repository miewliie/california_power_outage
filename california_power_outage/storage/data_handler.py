import json
import os
from typing import Any

from california_power_outage.core.power_outage import PowerOutage

""" Provides functions to handle Power outage data."""


def read_json(file_path: str):
    """ Read data from json file."""
    with open(file_path, 'r', encoding='utf-8') as output_file:
        size = os.path.getsize(file_path)
        return json.loads(output_file.read()) if size > 0 else None


def from_dict_to_power_outage(dict_data: dict[str, Any]) -> PowerOutage:
    """ Convert dictionary into PowerOutage object."""
    return PowerOutage(time=dict_data['attributes']['StartDate'],
                       outage_type=dict_data['attributes']['OutageType'],
                       latitude=dict_data['geometry']['y'],
                       longitude=dict_data['geometry']['x']
                       )


def power_outage_encoder(power_outages: dict[str, Any]) -> list[PowerOutage]:
    """ Convert dictionary into list PowerOutage objects."""
    power_outages_list: list[dict[str, Any]] = power_outages['features']
    power_outages: list[PowerOutage] = []
    for obj in power_outages_list:
        power_outages.append(from_dict_to_power_outage(dict_data=obj))
    return power_outages
