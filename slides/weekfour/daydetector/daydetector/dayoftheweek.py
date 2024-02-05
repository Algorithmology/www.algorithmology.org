"""A class to represent a day of the week."""


class DayOfTheWeek:
    """Map a shortcut name for a day of the week with the full name."""

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
        """Return the name of the day when provided with the abbreviation."""
        return self.name_map.get(self.abbreviation)
