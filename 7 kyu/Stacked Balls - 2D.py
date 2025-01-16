```
Given the number of layers of my stack, what is the total height?

Return the height as multiple of the ball diameter.

Example
The image above shows a stack of 5 layers.

Notes
layers >= 0
approximate answers (within 0.001) are good enough
```

import math

def stack_height_2d(layers: int) -> float:
    if layers == 0:
        return 0.0
    return 1 * (1 + (layers - 1) * (math.sqrt(3) / 2))