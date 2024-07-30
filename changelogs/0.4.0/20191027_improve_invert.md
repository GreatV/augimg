# Improve Invert #469

* Improved performance of `augimg.augmenters.arithmetic.invert()` and
  `augimg.augmenters.arithmetic.Invert` for `uint8` images.
* Added function `augimg.augmenters.arithmetic.invert_()`, an in-place version
  of `augimg.augmenters.arithmetic.invert()`.
* Added parameters `threshold` and `invert_above_threshold` to
  `augimg.augmenters.arithmetic.invert()`
* Added parameters `threshold` and `invert_above_threshold` to
  `augimg.augmenters.arithmetic.Invert`.
* Added function `augimg.augmenters.arithmetic.solarize()`, a wrapper around
  `solarize_()`.
* Added function `augimg.augmenters.arithmetic.solarize_()`, a wrapper around
  `invert_()`.
* Added augmenter `augimg.augmenters.Solarize`, a wrapper around `Invert`.
