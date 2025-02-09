from unittest import TestCase
from desk_booker.src.desk import Desk


class TestDesk(TestCase):

    def test__init__(self):
        desk = Desk("bob")
        self.assertEqual(desk.name, "bob")
