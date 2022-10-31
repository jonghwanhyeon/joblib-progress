# joblib-progress
![joblib-progress](assets/joblib-progress.gif)
A contextmanager to track progress of joblib execution.


## Install
```bash
> pip install joblib-progreess
```

## Usage
### If you know the number of items
```python
from joblib_progress import joblib_progress

from joblib import Parallel, delayed
import time

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
The idea of using `joblib.parallel.BatchCompletionCallBack` is inspired from https://stackoverflow.com/a/58936697/5133167
