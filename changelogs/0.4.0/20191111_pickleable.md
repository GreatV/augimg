# All Augmenters Pickle-able #493 #575

Ensured that all augmenters can be pickled.

* Added function `augimg.testutils.runtest_pickleable_uint8_img()`.
* Fixed `augimg.augmenters.blur.MotionBlur` not being pickle-able.
* Fixed `augimg.augmenters.meta.AssertLambda` not being pickle-able.
* Fixed `augimg.augmenters.meta.AssertShape` not being pickle-able.
* Fixed `augimg.augmenters.color.MultiplyHueAndSaturation` not supporting
  all standard RNG datatypes for `random_state`.
