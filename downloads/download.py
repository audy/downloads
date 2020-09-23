import os
import sys
from urllib.parse import urlparse
from urllib.request import urlretrieve

from typing import Optional

from tempfile import TemporaryDirectory


def _progress_bar(
    current: int, block_size: int, total_size: int, bar_width: int = 100
) -> str:

    proportion_downloaded = round(
        (float(current * block_size)) / total_size, 8
    )

    pbar_width = int(bar_width * proportion_downloaded)
    pbar = "#" * pbar_width

    ws_width = int((bar_width - (bar_width * proportion_downloaded)))
    ws = " " * ws_width

    pbar_line = "{}{}{:7.1f}%".format(pbar, ws, 100 * proportion_downloaded)
    return pbar_line


def _progress_hook(current: int, block_size: int, total_size: int) -> None:
    """ a simple progress bar """

    sys.stderr.write(
        _progress_bar(
            current=current, block_size=block_size, total_size=total_size
        )
        + "\r"
    )


def download(
    url: str, out_path: Optional[str] = None, progress: bool = False
) -> str:
    """

    Download a file given a URL. Returns the downloaded file's local path:

    >>> download('http://i.imgur.com/ij2h06p.png')
    'ij2h06p.png'

    URL parameters are stripped out before saving:

    >>> download('http://i.imgur.com/ij2h06p.png?foo=bar')
    'ij2h06p.png'

    You can override the output path:

    >>> download('http://i.imgur.com/ij2h06p.png', out_path='computer.png')
    'computer.png'

    There's even a fancy progress bar:
    >>> download('http://i.imgur.com/ij2h06p.png', out_path='computer.png', progress=True)
    'computer.png'
    """

    parsed = urlparse(url)

    out_path = (
        os.path.join(os.getcwd(), os.path.basename(parsed.path))
        if out_path is None
        else out_path
    )

    with TemporaryDirectory() as tmpdir:
        temp_out_path = os.path.join(tmpdir, os.path.basename(out_path))

        if progress:
            urlretrieve(url, temp_out_path, reporthook=_progress_hook)
            # finish off progress bar
            sys.stderr.write("\n")
        else:
            urlretrieve(url, temp_out_path)

        os.rename(temp_out_path, out_path)

    return out_path
