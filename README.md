# joblib-progress
A contextmanager to track progress of [`joblib`](https://joblib.readthedocs.io) execution using [`rich.progress`](https://rich.readthedocs.io).
[![joblib-progress](https://asciinema.org/a/Ufe9v8MKfxIzMuvlv2IwCk29l.svg)](https://asciinema.org/a/Ufe9v8MKfxIzMuvlv2IwCk29l)

## Why
The vanilla `multiprocessing` does not work when an object to multiprocess is not `pickle-able`. The `joblib` solves this, but then its progress is not tracked nicely. This library solves that tracking issue with `joblib`.

## Install
```bash
> pip install joblib-progress
```

## Usage
### If you know the number of items
```python
import time

from joblib import Parallel, delayed
from joblib_progress import joblib_progress


def slow_square(i):
    time.sleep(i / 2)
    return i ** 2

with joblib_progress("Calculating square...", total=10):
    Parallel(n_jobs=4)(delayed(slow_square)(number) for number in range(10))
```

### If you don't know the number of items
```python
with joblib_progress("Calculating square..."):
    Parallel(n_jobs=4)(delayed(slow_square)(number) for number in range(10))
```

# Acknowledgments
The idea of using `joblib.parallel.BatchCompletionCallBack` is referenced from https://stackoverflow.com/a/58936697/5133167
