from desk_booker.src.constants_project import DeskAccomodations


class Desk:
    """
    This class is used to represent a Desk object

    It stores the number of the desk and what special accomodations it has
    """

    name: str
    special_requirements: list[DeskAccomodations]
    location: tuple[int]
    booked: bool

    def __init__(self, name: str, special_requirements: list[str] | None = None):
        self.name = name
        self.special_requirements = DeskAccomodations(special_requirements)

    def book(self, requirements: list[DeskAccomodations]) -> bool:
        """
        This function allows you to book a desk on a floor

        Args:
            requirements: list of DeskAccomodations that are needed for a spot
        Returns:
            True if the desk can be book, False otherwise
        """
        if self.booked or all(
            item in self.special_requirements for item in requirements
        ):
            return False

        self.booked = True
        return True
