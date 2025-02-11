from unittest import TestCase
from desk_booker.src.desk import Desk
from desk_booker.src.constants_project import DeskState


class TestDesk(TestCase):

    def test__init__(self):
        desk = Desk("bob")
        self.assertEqual(desk.name, "bob")

    def test_reserve(self):
        """
        Test to make sure reserve works as expected
        """
        desk = Desk("Desk1")

        # Test to make sure an Available desk can be selected
        self.assertEqual(desk.state, DeskState.AVAILABLE)
        self.assertTrue(desk.reserve("user1"), "Should be able to book available desk")
        self.assertEqual(desk.state, DeskState.SELECTED)
        self.assertEqual(desk.person, "user1")

        # Test to make sure a Selected Desk cannot be selected by someone else
        self.assertFalse(desk.reserve("user2"), "Should not be able to book desk")
        # Test to make sure that if you already have a selected desk then you can still select it
        self.assertTrue(desk.reserve("user1"), "Should be able to book reserved desk")

        # Test to make sure that if a desk is booked only the user that booked it is able to get a True resposne
        desk.state = DeskState.BOOKED
        self.assertTrue(desk.reserve("user1"), "Should be able to get True")
        self.assertEqual(desk.state, DeskState.BOOKED, "State should not change")
        self.assertFalse(
            desk.reserve("user2"), "Should not be able to reserve this desk"
        )

    def test_book(self):
        """
        Test to make sure book function works as expected
        """
        desk = Desk("Desk1")

        # Test to make sure an Available desk can be booked
        self.assertEqual(desk.state, DeskState.AVAILABLE)
        self.assertTrue(desk.book("user1"), "Should be able to book available desk")
        self.assertEqual(desk.state, DeskState.BOOKED, "Should change state to BOOKED")
        self.assertEqual(
            desk.person, "user1", "Should set the user that booked the desk"
        )

        # Test to make sure a Booked Desk cannot be Booked by someone else
        self.assertFalse(desk.book("user2"), "Should not be able to book desk")

        # Test to make sure that if a desk is booked only the user that booked it is able to get a True resposne
        desk.state = DeskState.SELECTED
        self.assertFalse(desk.book("user2"), "Should not be able to book this desk")

        self.assertTrue(desk.book("user1"), "Should be able to get True")
        self.assertEqual(desk.state, DeskState.BOOKED, "State should not change")
        self.assertFalse(desk.book("user2"), "Should not be able to reserv this desk")
        self.assertTrue(
            desk.book("user1"), "Should be able to get True if booked already"
        )

    def test_unbook(self):
        """
        Test to make sure a desk object can be unbooked
        """

        desk = Desk("Desk1")

        self.assertTrue(desk.unbook("user1"), "Should be able to unbook a desk that is not booked")

        desk.state = DeskState.SELECTED
        desk.person = "user1"
        self.assertFalse(desk.unbook("user2"), "Unable to unbook a desk that was not booked by the user")
        self.assertTrue(desk.unbook("user1"), "Should be able to unbook a desk that was booked by the user")
        self.assertEqual(desk.state,DeskState.AVAILABLE)

    def test__str__(self):

        desk = Desk("desk1")
        self.assertEqual(str(desk),"Desk desk1 is available to be booked.")
        desk.state = DeskState.SELECTED
        desk.person = "user1"
        self.assertEqual(str(desk),"Desk desk1 has been selected by user1.")
        desk.state = DeskState.BOOKED
        self.assertEqual(str(desk),"Desk desk1 has been booked by user1.")
        desk.special_requirements = ["mouse","keyboard"]
        self.assertEqual(str(desk), "Desk desk1 has been booked by user1. This desk has the following accomodations mouse,keyboard.")