"""Test suite for the dayoftheweek module."""

from daydetector.dayoftheweek import DayOfTheWeek

import hypothesis.strategies as st
from hypothesis import given, settings, Verbosity
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
    "valid_days",
    [["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]],
)
@settings(verbosity=Verbosity.verbose)
@given(
    st.text(alphabet=st.characters(whitelist_categories=["L"]), min_size=1, max_size=2)
)
def test_abbreviation_maps_to_name(valid_days, abbreviation):
    """Test that the abbreviation maps to a valid day of the week."""
    day = DayOfTheWeek(abbreviation)
    assert day.name() in valid_days or day.name() is None


valid_days = {"M", "T", "W", "Th", "F", "Sa", "Su"}


@given(
    st.one_of(
        st.sampled_from(list(valid_days)),
        st.text(
            alphabet=st.characters(whitelist_categories=["L"]), min_size=1, max_size=2
        ).filter(lambda x: x not in valid_days),
    )
)
@settings(verbosity=Verbosity.verbose)
def test_abbreviations(abbreviation):
    """Test that the abbreviation is valid."""
    print(abbreviation)
    day = DayOfTheWeek(abbreviation)
    if abbreviation in valid_days:
        assert day.name() is not None
    else:
        assert day.name() is None
