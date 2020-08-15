from setuptools import setup, find_packages

with open("requirements.txt") as f:
    dependencies = f.readlines()

setup(
    name="perlin-numpy",
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3',
    url="https://github.com/pvigier/perlin-numpy",
    author="pvigier",
    license="MIT",
    entry_points={
        "console_scripts":
        [
            "perlin-2d-noise=perlin_numpy.perlin2d:main",
            "perlin-3d-noise=perlin_numpy.perlin3d:main"
        ],
    },
    install_requires=dependencies,
    zip_safe=False
)
