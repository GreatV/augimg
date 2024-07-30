# New brightness augmenters #455

* Added augmenter `augimg.augmenters.color.WithBrightnessChannels`.
* Added augmenter `augimg.augmenters.color.MultiplyAndAddToBrightness`.
* Added augmenter `augimg.augmenters.color.MultiplyBrightness`.
* Added augmenter `augimg.augmenters.color.AddToBrightness`.
* Added method `augimg.parameters.handle_categorical_string_param()`.
* Changed `change_colorspaces_()` to accept any iterable of `str` for
  argument `to_colorspaces`, not just `list`.
