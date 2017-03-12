import os

from urllib.request import urlretrieve
from urllib.parse import urlparse

import sys

def progress_hook(current, block_size, total_size):
    sys.stderr.write('{:.2f}\n'.format(100*float(current*block_size)/total_size))


def download(url, out_path=None, progress=False):

    parsed = urlparse(url)

    if out_path is None:
        out_path = os.path.join(os.getcwd(), os.path.basename(parsed.path))

    if progress:
        urlretrieve(url, out_path, reporthook=progress_hook)
    else:
        urlretrieve(url, out_path)

    return out_path
