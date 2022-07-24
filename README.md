# perlin-numpy

I wrote two articles on my blog about this project, the [first one](https://pvigier.github.io/2018/06/13/perlin-noise-numpy.html)  is about the generation of 2D noise while the [second one](https://pvigier.github.io/2018/11/02/3d-perlin-noise-numpy.html) is about the generation of 3D noise, feel free to read them!

You can find implementations using [numba](https://numba.pydata.org/) [here](https://github.com/pvigier/perlin-numpy/issues/9).

## Description

A fast and simple perlin noise generator using numpy.

## Installation

You can install this package via:

```
pip3 install git+https://github.com/pvigier/perlin-numpy
```

## Usage

```python
from perlin_numpy import (
    generate_fractal_noise_2d, generate_fractal_noise_3d,
    generate_perlin_noise_2d, generate_perlin_noise_3d
)
```

### 2D noise

The function `generate_perlin_noise_2d` generates a 2D texture of perlin noise. Its parameters are:

* `shape`: shape of the generated array (tuple of 2 ints)
* `res`: number of periods of noise to generate along each axis (tuple of 2 ints)
* `tileable`: if the noise should be tileable along each axis (tuple of 2 bools)

Note: `shape` must be a multiple of `res`

The function `generate_fractal_noise_2d` combines several octaves of 2D perlin noise to make 2D fractal noise. Its parameters are:

* `shape`: shape of the generated array (tuple of 2 ints)
* `res`: number of periods of noise to generate along each axis (tuple of 2 ints)
* `octaves`: number of octaves in the noise (int)
* `persistence`: scaling factor between two octaves (float)
* `lacunarity`: frequency factor between two octaves (float)
* `tileable`: if the noise should be tileable along each axis (tuple of 2 bools)

Note: `shape` must be a multiple of `lacunarity^(octaves-1)*res`


### 3D noise

The function `generate_perlin_noise_3d` generates a 3D texture of perlin noise. Its parameters are:

* `shape`: shape of the generated array (tuple of 3 ints)
* `res`: number of periods of noise to generate along each axis (tuple of 3 ints)
* `tileable`: if the noise should be tileable along each axis (tuple of 3 bools)

Note: `shape` must be a multiple of `res`

The function `generate_fractal_noise_2d` combines several octaves of 3D perlin noise to make 3D fractal noise. Its parameters are:

* `shape`: shape of the generated array (tuple of 3 ints)
* `res`: number of periods of noise to generate along each axis (tuple of 3 ints)
* `octaves`: number of octaves in the noise (int)
* `persistence`: scaling factor between two octaves (float)
* `lacunarity`: frequency factor between two octaves (float)
* `tileable`: if the noise should be tileable along each axis (tuple of 3 bools)

Note: `shape` must be a multiple of `lacunarity^(octaves-1)*res`

## Recipes

Note these snippets require [matplotlib](https://matplotlib.org/).

### 2D Perlin and Fractal Noise

```python
import matplotlib.pyplot as plt
import numpy as np
from perlin_numpy import (
    generate_perlin_noise_2d, generate_fractal_noise_2d
)

np.random.seed(0)
noise = generate_perlin_noise_2d((256, 256), (8, 8))
plt.imshow(noise, cmap='gray', interpolation='lanczos')
plt.colorbar()

np.random.seed(0)
noise = generate_fractal_noise_2d((256, 256), (8, 8), 5)
plt.figure()
plt.imshow(noise, cmap='gray', interpolation='lanczos')
plt.colorbar()
plt.show()
```

![2D Perlin noise](https://github.com/pvigier/perlin-numpy/raw/master/examples/perlin2d.png)
![2D fractal noise](https://github.com/pvigier/perlin-numpy/raw/master/examples/fractal2d.png)

### 3D Fractal Noise

```python
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from perlin_numpy import generate_fractal_noise_3d

np.random.seed(0)
noise = generate_fractal_noise_3d(
    (32, 256, 256), (1, 4, 4), 4, tileable=(True, False, False)
)

fig = plt.figure()
images = [
    [plt.imshow(
        layer, cmap='gray', interpolation='lanczos', animated=True
    )]
    for layer in noise
]
animation_3d = animation.ArtistAnimation(fig, images, interval=50, blit=True)
plt.show()
```


![3D fractal noise](https://github.com/pvigier/perlin-numpy/raw/master/examples/fractal3d.gif)

### 3D Perlin Noise

```python
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from perlin_numpy import generate_perlin_noise_3d

np.random.seed(0)
noise = generate_perlin_noise_3d(
    (32, 256, 256), (1, 4, 4), tileable=(True, False, False)
)

fig = plt.figure()
images = [
    [plt.imshow(
        layer, cmap='gray', interpolation='lanczos', animated=True
    )]
    for layer in noise
]
animation_3d = animation.ArtistAnimation(fig, images, interval=50, blit=True)
plt.show()
```


![3D Perlin noise](https://github.com/pvigier/perlin-numpy/raw/master/examples/perlin3d.gif)
