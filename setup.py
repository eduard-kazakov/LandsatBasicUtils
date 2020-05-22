import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    'gdal',
    'numpy'
]

setuptools.setup(
    name="LandsatBasicUtils",
    version="1.0",
    author="Eduard Kazakov",
    author_email="ee.kazakov@gmail.com",
    description="Simple classes for reading Landsat imagery metadata and perform radiometric calibration (calculate radiance, reflectance, brightness temperatures)",
    long_description=long_description,
    keywords='landsat',
    long_description_content_type="text/markdown",
    url="https://github.com/eduard-kazakov/Landsat8_LST_PSWA",
    install_requires=requires,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
)