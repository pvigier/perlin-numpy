# perlin-numpy

## Description

A fast and simple perlin noise generator using numpy.

The function `generate_perlin_noise_2d` generates the classical perlin noise. Its parameters are:

* `shape`: shape of the generated array (tuple of ints)
* `res`: number of periods of noise to generate along each axis (tuple of ints)

Note: `shape` must be a multiple of `res`

Moreover the function `generate_fractal_noise_2d` combines several octaves of perlin noise to make fractal noise. Its parameters are:

* `shape`: shape of the generated array (tuple of ints)
* `res`: number of periods of noise to generate along each axis (tuple of ints)
* `octaves`: number of octaves in the noise (int)
* `persistence`: scaling factor between two octaves (float)

Note: `shape` must be a multiple of `octaves*res`

## Gallery

![Perlin noise](https://github.com/pvigier/perlin-numpy/raw/master/examples/perlin.png)
![Fractal noise](https://github.com/pvigier/perlin-numpy/raw/master/examples/fractal.png)
