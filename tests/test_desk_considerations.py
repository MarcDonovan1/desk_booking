from desk_booker.src.constants_project import DeskAccomodations
from unittest import TestCase


class TestDeskAccomodations(TestCase):

    def test__init__(self):

        expected_results = {
            None: DeskAccomodations.NONE,
            "sit_stand_desk": DeskAccomodations.SIT_STAND_DESK,
            "ergo_keyboard" : DeskAccomodations.ERGO_KEYBOARD,
            "ergo_mouse" : DeskAccomodations.ERGO_MOUSE,
            "sun_shades" : DeskAccomodations.SUN_SHADES,

        }

        for key, value in expected_results.items():
            self.assertEqual(
                DeskAccomodations(key),
                value,
                f"Unexpected result of {DeskAccomodations(key)}, should be {value}",
            )
