import pytest


def test_adunare():
    assert 1 + 1 == 2
    assert 2 + 2 == 4
    assert 3 + 3 == 6


@pytest.mark.parametrize(
    'val1, val2, rezultat',
    [
        (1, 1, 2),
        (2, 2, 4),
        (3, 3, 6),
    ]
)
def test_adunare_parametrizata(val1, val2, rezultat):
    assert val1 + val2 == rezultat