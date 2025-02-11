from desk_booker.src.constants_project import DeskAccomodations, DeskState


class Desk:
    """
    This class is used to represent a Desk object

    It stores the number of the desk and what special accomodations it has
    """

    name: str
    person: str
    special_requirements: list[str]
    location: tuple[int]
    state: DeskState

    def __init__(self, name: str, special_requirements: list[str] | None = None):
        self.name = name
        self.special_requirements = special_requirements
        self.state = DeskState.AVAILABLE

    def reserve(self, username: str) -> bool:
        """
        This method will reserve a desk object.

        This will prevent anyone else from trying to book this spot

        Args:
            username: The user that wished to reserve this desk
        Returns:
            True if it was able to be reserved, False otherwise
        """
        match self.state:
            case DeskState.AVAILABLE:
                self.person = username
                self.state = DeskState.SELECTED
                return True
            case _:
                if self.person != username:
                    return False
                if self.state == DeskState.BOOKED:
                    print("desk is already booked by you, why are you reserving?")
                return True

    def book(self, username: str) -> bool:
        """
        This function allows you to book a desk on a floor

        Args:
            requirements: list of DeskAccomodations that are needed for a spot
        Returns:
            True if the desk can be book, False otherwise
        """
        match self.state:
            case DeskState.AVAILABLE:
                self.state = DeskState.BOOKED
                self.person = username
                return True
            case DeskState.SELECTED:
                if self.person != username:
                    return False
                self.state = DeskState.BOOKED
                return True
            case DeskState.BOOKED:
                if self.person != username:
                    return False
                return True

    def unbook(self, username: str) -> bool:
        """
        This function will clear the state of the desk

        Args:
            usernmae: user that is wanting to clear the desk
        Returns:
            True is the desk was unbooked, False otherwise
        """
        match self.state:
            case DeskState.AVAILABLE:
                return True
            case _:
                if self.person != username:
                    return False
                self.state = DeskState.AVAILABLE
                return True

    def __str__(self):
        result: str = ""
        match self.state:
            case DeskState.AVAILABLE:
                result = f"Desk {self.name} is available to be booked."
            case DeskState.SELECTED:
                result = f"Desk {self.name} has been selected by {self.person}."
            case DeskState.BOOKED:
                result = f"Desk {self.name} has been booked by {self.person}."
        if self.special_requirements and len(self.special_requirements) > 0:
            result += f" This desk has the following accomodations {','.join(self.special_requirements)}."
        return result
