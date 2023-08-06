# spectra2rgb
Converting multi-spectra numpy array to RGB format

## Usage

```python
from spectra2rgb import SpectralData
spectral_data = SpectralData(multi_spectra_data, axis=0)
rgb_data = spectral_data.to_rgb()
```

Where:
* `multi_spectra_data` is of shape (48, 100, 250) and first dimension represents the spectral bands (in this case there are 48 spectra bands)
* `rgb_data` will be of shape (3, 100, 250) and will have values between 0 and 255
* 0th index in spectral dimension will be considered as the lowest wavelength (violet) and last index will be considered as longest wavelength (red)
