import os
from mastodon import Mastodon
import draw.draw_power_outage as draw_fire
from api.arcgis_api import get_power_outage


USER = os.getenv('MASTODON_EMAIL')
PASSWORD = os.getenv('MASTODON_PASSWORD')
MASTODON_SERVER = os.getenv('MASTODON_SERVER')


def connect_to_mastodon():
    """ Create a connection to your server. And provide account credential. """

    Mastodon.create_app(
        'pytooterapp',
        api_base_url=MASTODON_SERVER,
        to_file='pytooter_clientcred.secret'
    )

    mastodon = Mastodon(client_id='pytooter_clientcred.secret',)
    mastodon.log_in(
        USER,
        PASSWORD)
    return mastodon


def send_new_status_for(power_outage_title: str, power_outage_map_path: str):
    """ Post fire status and fire recent map. """

    mastodon = connect_to_mastodon()

    image_id = mastodon.media_post(power_outage_map_path)
    post_dict = mastodon.status_post(
        power_outage_title, in_reply_to_id=None, media_ids=image_id)
    print("post id: ", post_dict.id)


def get_power_outage_title():
    """ Prepare power outage title for tooting. """

    title_msg = "More info: https://hub.arcgis.com/datasets/CalEMA::power-outage-incidents/explore \n " \
                "#PowerOutage #California #CaliforniaPowerOutage #PowerOutageCalifornia"

    return title_msg


if __name__ == '__main__':
    image_path = "./assets/california_base_map.png"
    output_path = "./outputs/california_output_map.png"

    power_outages = get_power_outage()
    title = get_power_outage_title()

    if power_outages is not None:
        features = power_outages['features']
        draw_fire.draw_fire_points(image_path, output_path, features)
        send_new_status_for(title, output_path)
    else:
        print(" No power outage found")


