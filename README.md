# perlin-numpy

I wrote an [article](https://pvigier.github.io/2018/06/13/perlin-noise-numpy.html) about this project on my blog, feel free to read it!

## Description

A fast and simple perlin noise generator using numpy.

### 2D noise

The function `generate_perlin_noise_2d` generates a 2D texture of perlin noise. Its parameters are:

* `shape`: shape of the generated array (tuple of 2 ints)
* `res`: number of periods of noise to generate along each axis (tuple of 2 ints)

Note: `shape` must be a multiple of `res`

The function `generate_fractal_noise_2d` combines several octaves of 2D perlin noise to make 2D fractal noise. Its parameters are:

* `shape`: shape of the generated array (tuple of 2 ints)
* `res`: number of periods of noise to generate along each axis (tuple of 2 ints)
* `octaves`: number of octaves in the noise (int)
* `persistence`: scaling factor between two octaves (float)

Note: `shape` must be a multiple of `octaves*res`


### 3D noise

The function `generate_perlin_noise_3d` generates a 3D texture of perlin noise. Its parameters are:

* `shape`: shape of the generated array (tuple of 3 ints)
* `res`: number of periods of noise to generate along each axis (tuple of 3 ints)

Note: `shape` must be a multiple of `res`

The function `generate_fractal_noise_2d` combines several octaves of 3D perlin noise to make 3D fractal noise. Its parameters are:

* `shape`: shape of the generated array (tuple of 3 ints)
* `res`: number of periods of noise to generate along each axis (tuple of 3 ints)
* `octaves`: number of octaves in the noise (int)
* `persistence`: scaling factor between two octaves (float)

Note: `shape` must be a multiple of `octaves*res`

## Gallery

![2D Perlin noise](https://github.com/pvigier/perlin-numpy/raw/master/examples/perlin2d.png)
![2D fractal noise](https://github.com/pvigier/perlin-numpy/raw/master/examples/fractal2d.png)
![3D Perlin noise](https://github.com/pvigier/perlin-numpy/raw/master/examples/perlin3d.gif)
![3D fractal noise](https://github.com/pvigier/perlin-numpy/raw/master/examples/fractal3d.gif)
