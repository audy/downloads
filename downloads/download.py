import os
import sys


if sys.version_info > (3, 0):
    # python 3
    from urllib.parse import urlparse
    from urllib.request import urlretrieve
else:
    # python 2
    from urlparse import urlparse
    from urllib import urlretrieve


def progress_hook(current, block_size, total_size):
    ''' a simple progress bar '''

    proportion_downloaded = round((float(current*block_size)-block_size)/total_size, 4)

    pbar_width = int(70 * proportion_downloaded)
    pbar = '#' * pbar_width

    ws_width = int((70 - (70 * proportion_downloaded)))
    ws = ' ' * ws_width

    pbar_line = "{}{}{:7.1f}%\r".format(pbar, ws, 100 * proportion_downloaded)
    sys.stderr.write(pbar_line)


def download(url, out_path=None, progress=False, strip_url_params=True):
    '''

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
    '''

    parsed = urlparse(url)

    if out_path is None:
        if strip_url_params:
            out_basename = os.path.basename(parsed.path)
        else:
            out_basename = parsed.path
        out_path = os.path.join(os.getcwd(), out_basename)

    if progress:
        urlretrieve(url, out_path, reporthook=progress_hook)
        # finish off progress bar
        sys.stderr.write("\n")
    else:
        urlretrieve(url, out_path)

    return out_path
