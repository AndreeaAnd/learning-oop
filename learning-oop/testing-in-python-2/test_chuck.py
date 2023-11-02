import pytest
from chuck_jokes import main, get_jokes

from unittest import mock


@mock.patch('chuck_jokes.requests')
def test_get_10_items(mock_request):
    mock_request.get.json.return_value = lambda *args, **kwargs: {'cheie': 'valoare'}
    jokes = main()
    assert len(jokes) == 10


@pytest.mark.parametrize('jokes_nr', [0, 10, 20, 30])
def test_returned_jokes_nr(jokes_nr):
    with mock.patch('chuck_jokes.requests'):
        jokes = get_jokes(jokes_nr)
        assert len(jokes) == jokes_nr

