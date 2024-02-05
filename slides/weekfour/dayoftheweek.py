"""A class to represent a day of the week."""


class DayOfTheWeek:
    """A class to represent a day of the week."""
    def __init__(self, abbreviation):
        """Create a new DayOfTheWeek object."""
        self.abbreviation = abbreviation
        self.name_map = {
            "M": "Monday",
            "T": "Tuesday",
            "W": "Wednesday",
            "Th": "Thursday",
            "F": "Friday",
            "Sa": "Saturday",
            "Su": "Sunday",
        }

    def name(self):
        return self.name_map.get(self.abbreviation)
