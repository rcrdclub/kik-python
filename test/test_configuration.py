from unittest import TestCase

from kik import Configuration
from kik.messages import SuggestedResponseKeyboard, TextResponse


class ConfigurationTest(TestCase):
    def test_from_json(self):
        config = Configuration.from_json({
            'webhook': 'https://mybot.com/incoming',
            'features': {
                'manuallySendReadReceipts': True
            },
            'staticKeyboard': {
                'type': 'suggested',
                'responses': [
                    {
                        'type': 'text',
                        'body': 'foo'
                    }
                ]
            }
        })
        self.assertEqual(config.webhook, 'https://mybot.com/incoming')
        self.assertEqual(config.features, {'manuallySendReadReceipts': True})
        self.assertIsInstance(config.static_keyboard, SuggestedResponseKeyboard)
        self.assertEqual(config.static_keyboard, SuggestedResponseKeyboard(
            responses=[
                TextResponse('foo')
            ]
        ))

    def test_to_json(self):
        config = Configuration(
            webhook='https://mybot.com/incoming',
            features={'manuallySendReadReceipts': True},
            static_keyboard=SuggestedResponseKeyboard(
                responses=[
                    TextResponse('foo')
                ]
            )
        )

        self.assertEqual(config.to_json(), {
            'webhook': 'https://mybot.com/incoming',
            'features': {
                'manuallySendReadReceipts': True
            },
            'staticKeyboard': {
                'type': 'suggested',
                'responses': [
                    {
                        'type': 'text',
                        'body': 'foo'
                    }
                ]
            }
        })

    def test_to_json_no_features(self):
        config = Configuration(
            webhook='https://mybot.com/incoming'
        )

        self.assertEqual(config.to_json(), {
            'webhook': 'https://mybot.com/incoming',
            'features': {}
        })
