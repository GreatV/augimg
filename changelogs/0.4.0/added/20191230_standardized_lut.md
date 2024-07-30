# Standardized LUT Methods #542

* Added `augimg.augimg.apply_lut()`, which applies a lookup table to an image.
* Added `augimg.augimg.apply_lut_()`. In-place version of `apply_lut()`.
* Refactored all augmenters to use these new LUT functions.
  This likely fixed some so-far undiscovered bugs in augmenters using LUT
  tables.
