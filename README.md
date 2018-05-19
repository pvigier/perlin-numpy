# perlin-numpy

## Description

A fast and simple perlin noise generator using numpy.

All the code is contained in the function `generate_2d_perlin`.

Parameters:

* `shape`: shape of the generated array (tuple of ints)
* `res`: number of periods of noise to generate along each axis (tuple of ints)
* `octaves`: number of octaves in the noise (int)
* `persistance`: scaling factor between two octaves (float)

Note: `shape` must be a multiple of `res*octaves`

## Gallery

![](https://github.com/pvigier/perlin-numpy/raw/master/examples/simple.png)
![](https://github.com/pvigier/perlin-numpy/raw/master/examples/several_octaves.png)
