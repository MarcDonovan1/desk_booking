from desk import Desk
from constants_project import DeskAccomodations


class Floor:
    """
    This is a class used to represent a floor in a building

    The floor will be able to determine the following
        - How many desks are left
        - If it can book the required ammount of desks needed
        - Shuffle peoples spot arround if there are more desks available
        - Account for peoples vacation
    """

    name: str
    desks: list[Desk]

    def __init__(self, name: str):
        self.name = name

    def add_desk(self, desk_information: dict[str, str]) -> None:
        """
        This function allows you to add a new desk to a floor

        Raises:
            ValueError: If desk_information is incomplete or invalid
        """
        new_desk = Desk(desk_information)
        self.desks.append(new_desk)

    def desks_left(self, type_of_requirements: list[Desk]) -> int:
        """
        Returns the number of available desks on a floor

        Args:

        Returns:
            int: [description]
        """
        result = sum(1 for desk in self.desks if not desk.booked)
        print(f"There are ")
        return sum(1 for desk in self.desks if not desk.booked)
