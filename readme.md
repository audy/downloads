# downloads

Easier HTTP downloads in Python (2 and 3).

## Motivation

I always forget how to download a file in Python. Also, the standard way of
downloading a file (urllib) is slightly different between Python 2 and 3.

## Features

- automatically strip parameters from URL when generating filename

## Usage

```python
from downloads import download

download('https://www...')

# output path is automatically determined and returned
# but you can specify it manually if that's your thing:

download('https://www...', out_path='blah.txt')

# or, if you want to be fancy:

download('...', progress=True)
```

That's it!

