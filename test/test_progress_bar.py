import pytest

from downloads.download import _progress_bar


@pytest.mark.parametrize(
    "current,block_size,total_size",
    [
        (
            100,
            32,
            100 * 32,
        ),
        (
            75,
            32,
            100 * 32,
        ),
        (
            50,
            32,
            100 * 32,
        ),
        (
            25,
            32,
            100 * 32,
        ),
        (
            0,
            32,
            100 * 32,
        ),
    ],
)
def test_progress_bar(current, block_size, total_size):
    bar = _progress_bar(
        current=current, block_size=block_size, total_size=total_size
    )

    assert bar.count("#") == current
    assert bar.split()[-1] == f"{current:.1f}%"
