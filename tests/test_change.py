import pytest

from change import calculate_change
from exceptions import CalculateChangeError


@pytest.mark.change
def test_returns_when_exact_match():
    result = calculate_change(5, [1,2,3,4,5])
    assert type(result) is list
    assert result[0] == 5
    assert len(result) == 1


@pytest.mark.change
def test_raise_error_when_no_change_available():
    with pytest.raises(CalculateChangeError):
        calculate_change(50, [1,2,3,4,5])


@pytest.mark.change
def test_target_is_zero():
    with pytest.raises(CalculateChangeError):
        calculate_change(0, [1,3,4,5])


@pytest.mark.change
def test_change_success():
    args = [
        (60, [50, 25, 25, 25, 10, 10, 10, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1], [50, 10])
    ]
    for arg in args:
        result = calculate_change(arg[0], arg[1])
        assert result == arg[2]


@pytest.mark.change
def test_change_failure():
    args = [
        (60, [50, 25, 25, 25]),
        (40, [25, 5, 5, 1])
    ]
    for arg in args:
        with pytest.raises(CalculateChangeError):
            calculate_change(arg[0], arg[1])
