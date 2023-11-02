import pytest
from functions import sum_from_args
from decorators import multiply_by_decorator

sequences = (
    (1, 2, 3),
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    (-1, -2)
)
@pytest.mark.parametrize('sequence, expected_result', [
    (sequences[0], 6),
    (sequences[1], 55),
    (sequences[2], -3),
])

def test_original_sum_from_args(sequence, expected_result):
    result = sum_from_args.__wrapped__(1, 2, 3)
    assert result == 6

@pytest.mark.parametrize('sequence, expected_result', [
    (sequences[0], 12),
    (sequences[1], 110),
    (sequences[2], -6),
])
def test_sum_from_args(sequence, expected_result):
    result = sum_from_args(1, 2, 3)
    assert result == 12

@pytest.mark.parametrize('multiplier, customs_function_result, expected_result', [
    (2, 5, 10),
    (3, 8, 24),
    (-4, -3, 12),
])
def multiply_by_decorator(multiplier, customs_function_result, expected_result):
    decorated_function = multiply_by_decorator(multiplier)(lambda: customs_function_result)
    result=decorated_function()
    assert result == expected_result


