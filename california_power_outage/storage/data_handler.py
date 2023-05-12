import json
import os

from california_power_outage.core.power_outage import PowerOutage

""" Provides functions to handle Power outage data."""


def read_json(file_path: str):
    """ Read data from json file."""
    with open(file_path, 'r', encoding='utf-8') as output_file:
        size = os.path.getsize(file_path)
        return json.loads(output_file.read()) if size > 0 else None


def from_dict_to_power_outage(dict_data: dict) -> PowerOutage:
    """ Convert dictionary into PowerOutage object."""
    return PowerOutage(time=dict_data['attributes']['StartDate'],
                       outage_type=dict_data['attributes']['OutageType'],
                       latitude=dict_data['geometry']['y'],
                       longitude=dict_data['geometry']['x']
                       )


def power_outage_encoder(power_outages: dict[str, str]) -> list[PowerOutage]:
    """ Convert dictionary into list PowerOutage objects."""
    po_features: str = power_outages['features']
    power_outages_list: list[PowerOutage] = []

    po_item: dict
    for po_item in po_features:
        power_outages_list.append(from_dict_to_power_outage(dict_data=po_item))
    return power_outages_list
