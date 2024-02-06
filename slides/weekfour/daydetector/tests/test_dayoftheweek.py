"""Test suite for the dayoftheweek module."""

from daydetector.dayoftheweek import DayOfTheWeek

import hypothesis.strategies as st
from hypothesis import given
import pytest


def test_init():
    """Test the DayOfTheWeek class."""
    d = DayOfTheWeek("F")
    assert d.name() == "Friday"
    d = DayOfTheWeek("Th")
    assert d.name() == "Thursday"
    d = DayOfTheWeek("W")
    assert d.name() == "Wednesday"
    d = DayOfTheWeek("T")
    assert d.name() == "Tuesday"
    d = DayOfTheWeek("M")
    assert d.name() == "Monday"


@pytest.mark.parametrize(
    "abbreviation, expected",
    [
        ("M", "Monday"),
        ("T", "Tuesday"),
        ("W", "Wednesday"),
        ("Th", "Thursday"),
        ("F", "Friday"),
        ("Sa", "Saturday"),
        ("Su", "Sunday"),
        ("X", None),
    ],
)
def test_day_name(abbreviation, expected):
    """Use parameterized testing to confirm that lookup works correctly."""
    day = DayOfTheWeek(abbreviation)
    assert day.name() == expected


@pytest.mark.parametrize(
    "valid_days",
    [["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]],
)
@given(st.text(alphabet=st.characters(), min_size=1, max_size=2))
def test_abbreviation_maps_to_name(valid_days, abbreviation):
    """Use property-based testing to confirm that the abbreviation maps to a valid day of the week."""
    day = DayOfTheWeek(abbreviation)
    assert day.name() in valid_days or day.name() is None
