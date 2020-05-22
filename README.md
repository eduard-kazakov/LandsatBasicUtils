# LandsatBasicUtils
Metadata reader and basic calibration for Landsat imagery (Landsat 4, 5, 7, 8)

## Requirements

numpy, gdal

## Installation

```bash
pip install git+https://github.com/eduard-kazakov/LandastBasicUtils
```

## How to use

There are two classes:
* LandsatMetadataReader - reads all metadata to convenient dictionary. In addition to basic metadata from *MTL.txt there are added information about wavelenghts and solar irradiances for each band. 
* LandsatBandCalibrator - performs radiometric calibration (radiance, reflectance, brightness temperature)


MetadataReader usage example:
```python
from LandsatBasicUtils.MetadataReader import LandsatMetadataReader

reader = LandsatMetadataReader(metadata_file_path='.../LC08_L1TP_182019_20190830_20190903_01_T1_MTL.txt')

# Now we have everything in reader variable
# reader.metadata - dict with all records
reader.metadata['LANDSAT_SCENE_ID']
>>> 'LC81820192019242LGN00'

# metadata.bands - dict with metadata splitted by bands
reader.bands['11']['wavelength']
>>> 12.05

reader.bands['11']['type']
>>> thermal

reader.bands['4']['reflectance_maximum']
>>> 1.2107

reader.bands['3']['solar_irradiance']
>>> 1820.75

reader.bands['5']['file_name']
>>> LC08_L1TP_182019_20190830_20190903_01_T1_B5.TIF
```

BandCalibrator usage example:
```python
from LandsatBasicUtils.BandCalibrator import LandsatBandCalibrator

calibrator = LandsatBandCalibrator(band_file='.../LC08_L1TP_182019_20190830_20190903_01_T1_B4.TIF',
                                   metadata_file_path='.../LC08_L1TP_182019_20190830_20190903_01_T1_MTL.txt')

# Get radiance and reflectance as arrays - useful for further analysis
radiance = calibrator.get_radiance_as_array()
reflectance = calibrator.get_reflectance_as_array()

# Save to geotif
calibrator.save_array_as_gtiff(radiance,'.../b4_radiance.tif')

# Another band
calibrator = LandsatBandCalibrator(band_file='.../LC08_L1TP_182019_20190830_20190903_01_T1_B11.TIF',
                                   metadata_file_path='.../LC08_L1TP_182019_20190830_20190903_01_T1_MTL.txt')

brightness_temperature = calibrator.get_brightness_temperature_as_array()
calibrator.save_array_as_gtiff(radiance,'.../b11_bt.tif')
```

## Contacts

Feel free to contact me: ee.kazakov@gmail.com

