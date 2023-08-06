# Mathematical Greek for Python

Why write `pi` when you could write `π`?

This package provides - and monkey patches - Greek aliases for builtins and
standard library functions.


## Usage

Either import the Greek aliases from the `greek` module:

```python
from greek import π
```

Or just `import greek` first and use the aliases from the standard library:

```python
import greek
from math import π
```

But what if the taste of importing an English name like `greek` doesn't sit
right with you? We got you:

```python
import ελληνικά
from math import τ
```

```python
from ελληνικά import Π
```


## List of aliases

| Original           | Greek |
| ---                | ---   |
| `sum`              | `Σ`   |
| `sum`              | `𝚺`   |
| `int`              | `ℤ`   |
| `complex`          | `ℂ`   |
| `math.pi`          | `π`   |
| `math.pi`          | `𝜋`   |
| `math.tau`         | `τ`   |
| `math.tau`         | `𝜏`   |
| `math.e`           | `𝑒`   |
| `math.prod`        | `Π`   |
| `math.gamma`       | `Γ`   |
| `statistics.stdev` | `σ`   |
