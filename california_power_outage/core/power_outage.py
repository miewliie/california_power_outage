from typing import NamedTuple

""" Provides a data structure for storing power outage data. """


class PowerOutage(NamedTuple):
    """ Represents a power outage. """

    time: int
    """ The time of the power outage in millisecond. """

    outage_type: str
    """ The type of the power outage."""

    longitude: float
    """ The longitude of the power outage. """

    latitude: float
    """ The latitude of the power outage."""
