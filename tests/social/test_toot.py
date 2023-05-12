import unittest
from unittest import mock
from unittest.mock import MagicMock

from california_power_outage.social.toot import send_new_toot, Mastodon


class TestToot(unittest.TestCase):

    def test_toot(self):
        message: str = "More info: https://hub.arcgis.com/datasets/CalEMA::power-outage-incidents/explore \n " \
                       "#PowerOutage #California #CaliforniaPowerOutage #PowerOutageCalifornia"
        image_path: str = "outputs/california_output_map.png"
        expected_response = {'id': '1234'}

        mastodon_mock = MagicMock(spec=Mastodon)
        mastodon_mock.media_post.return_value = {'id': '1234'}
        with mock.patch('california_power_outage.social.toot.send_new_toot',
                        return_value=expected_response), \
                mock.patch('california_power_outage.social.toot.connect_to_mastodon',
                           return_value=mastodon_mock) as mock_connect_to_mastodon:
            send_new_toot(message=message, image_path=image_path)
            mock_connect_to_mastodon.assert_called_once()
            mastodon_mock.media_post.assert_called_once_with(media_file=image_path)
            mastodon_mock.status_post.assert_called_once_with(status=message, in_reply_to_id=None,
                                                              media_ids={'id': '1234'})


if __name__ == '__main__':
    unittest.main()
