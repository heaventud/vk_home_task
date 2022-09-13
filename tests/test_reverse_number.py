import sys

import pytest

import app.reverse_number as lib


if sys.version_info[0] < 3:
    MAX_INT = sys.maxint
else:
    MAX_INT = sys.maxsize


@pytest.mark.parametrize('data, expected', [
    (1, 1),
    (123, 321),
    (456951782, 287159654),
    (7777, 7777),
    (24000000, 42),
    (2400000042, 2400000042),
    pytest.param(MAX_INT, int(str(MAX_INT)[::-1]), id='maximum integer'),
    pytest.param(MAX_INT * 10, int(str(MAX_INT * 10)[::-1])),
])
def test_reverse_numbers(data, expected):
    """
    Test checks that the method works correctly
    """
    assert lib.reverse_number(data) == expected


@pytest.mark.parametrize('data', [
    pytest.param(0, id='zero input'),
    pytest.param('123456789', id='string input'),
    pytest.param(0.343, id='float input'),
    pytest.param(-2312312, id='negative input'),
])
def test_reverse_failed(data):
    """
    Test checks that method raises an exception in case
    of unsupported input
    """
    with pytest.raises(lib.UnsupportedInput) as excinfo:
        lib.reverse_number(data)
