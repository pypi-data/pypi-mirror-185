# Readme of `yasiu.math`

Module with useful math functions that are missing in numpy or scipy.

## Installation

```shell
pip install yasiu.math
```

## Moving average

### Import:

```py
from yasiu_math.math import moving_average
```

### Use example:

```py
moving_average(Union[list, "1d np array"], radius=1, padding="try", kernel_type="avg", kernel_exp=2)
```
