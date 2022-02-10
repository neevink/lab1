import pytest
import main


@pytest.mark.parametrize("coef, b, expected", [
    (
        [
            [10, 1, 1],
            [2, 10, 1],
            [2, 2, 10],
        ],
        [12, 13, 14],
        [1.0, 1.0, 1.0],
    ),
    (
        [
            [16, 12, 300],
            [-3, 6, 90],
        ],
        [300, 90],
        [5.46, 17.73],
    ),
])
def test_solving(coef, b, expected):
    assert main.solve(coef, b) == expected
