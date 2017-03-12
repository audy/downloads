# downloads

[![Build Status](https://travis-ci.org/audy/downloads.svg?branch=master)](https://travis-ci.org/audy/downloads)

Easier HTTP downloads in Python.

## Usage

```python
from downloads import download

download('http://i.imgur.com/ij2h06p.png')

# output path is automatically determined and returned
# but you can specify it manually if that's your thing:

download('http://i.imgur.com/i5pJRxX.jpg', out_path='cheezburger.jpg')

# or, if you want to be fancy:

download('https://www.gutenberg.org/files/2600/2600-0.txt', progress=True)
```

That's it!

