from setuptools import find_packages, setup

setup(
    name="perlin-numpy",
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3',
    url="https://github.com/pvigier/perlin-numpy",
    author="pvigier",
    license="MIT",
    install_requires=[
        "numpy>=1.15"
    ],
    zip_safe=False
)
