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
    (
        [
            [-5, 1, 2, 2],
            [1, 6, 1, 2],
            [1, 2, 8, 2],
            [1, 2, 3, 6],
        ],
        [14, 10, 21, 22],
        [-0.85, 0.61, 1.92, 2.65],
    ),
])
def test_solving(coef, b, expected):
    assert main.solve(coef, b) == expected
