# Downloads

[![test](https://github.com/audy/downloads/workflows/test/badge.svg)](https://github.com/audy/downloads/actions?query=workflow%3Atest)
[![PyPI version](https://badge.fury.io/py/downloads.svg)](https://badge.fury.io/py/downloads)
[![Downloads](https://pepy.tech/badge/downloads/month)](https://pepy.tech/project/downloads)

Easier HTTP downloads in Python 3.5+

## Features

1. Easier to remember than `urllib`
2. Files are not written unless download finishes
3. Progress bar!

## Installation

```
pip install downloads==1.0.0
```

## Usage

```python
from downloads import download

download("http://i.imgur.com/ij2h06p.png")

# output path is automatically determined and returned
# but you can specify it manually if that"s your thing:

download("http://i.imgur.com/i5pJRxX.jpg", out_path="cheezburger.jpg")

# or, if you want to be fancy:

download("https://www.gutenberg.org/files/2600/2600-0.txt", progress=True)
```

That's it!

