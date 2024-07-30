# Fixed `MultiplyHueAndSaturation` RNG #493

* Fixed `MultiplyHueAndSaturation` crashing if the RNG provided via
  `random_state` was not `None` or `augimg.random.RNG`.
