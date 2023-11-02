import sys
import pytest


@pytest.mark.skip
def test_doi():
    assert 1 + 1 == 2


@pytest.mark.skip(sys.version_info.minor >= 10, reason='Testul merge doar pe < 3.10')
def test_skip():
    assert 1 + 1 == 2


@pytest.mark.xfail
def test_doi():
    assert 1 == 2

