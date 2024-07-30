# Added Module `augimg.augmenters.pillike` #479 #480 #538

* Added module `augimg.augmenters.pillike`, which contains augmenters and
  functions corresponding to commonly used PIL functions. Their outputs
  are guaranteed to be identical to the PIL outputs.
* Added the following functions to the module:
  * `augimg.augmenters.pillike.equalize`
  * `augimg.augmenters.pillike.equalize_`
  * `augimg.augmenters.pillike.autocontrast`
  * `augimg.augmenters.pillike.autocontrast_`
  * `augimg.augmenters.pillike.solarize`
  * `augimg.augmenters.pillike.solarize_`
  * `augimg.augmenters.pillike.posterize`
  * `augimg.augmenters.pillike.posterize_`
  * `augimg.augmenters.pillike.enhance_color`
  * `augimg.augmenters.pillike.enhance_contrast`
  * `augimg.augmenters.pillike.enhance_brightness`
  * `augimg.augmenters.pillike.enhance_sharpness`
  * `augimg.augmenters.pillike.filter_blur`
  * `augimg.augmenters.pillike.filter_smooth`
  * `augimg.augmenters.pillike.filter_smooth_more`
  * `augimg.augmenters.pillike.filter_edge_enhance`
  * `augimg.augmenters.pillike.filter_edge_enhance_more`
  * `augimg.augmenters.pillike.filter_find_edges`
  * `augimg.augmenters.pillike.filter_contour`
  * `augimg.augmenters.pillike.filter_emboss`
  * `augimg.augmenters.pillike.filter_sharpen`
  * `augimg.augmenters.pillike.filter_detail`
  * `augimg.augmenters.pillike.warp_affine`
* Added the following augmenters to the module:
  * `augimg.augmenters.pillike.Solarize`
  * `augimg.augmenters.pillike.Posterize`.
    (Currently alias for `augimg.augmenters.color.Posterize`.)
  * `augimg.augmenters.pillike.Equalize`
  * `augimg.augmenters.pillike.Autocontrast`
  * `augimg.augmenters.pillike.EnhanceColor`
  * `augimg.augmenters.pillike.EnhanceContrast`
  * `augimg.augmenters.pillike.EnhanceBrightness`
  * `augimg.augmenters.pillike.EnhanceSharpness`
  * `augimg.augmenters.pillike.FilterBlur`
  * `augimg.augmenters.pillike.FilterSmooth`
  * `augimg.augmenters.pillike.FilterSmoothMore`
  * `augimg.augmenters.pillike.FilterEdgeEnhance`
  * `augimg.augmenters.pillike.FilterEdgeEnhanceMore`
  * `augimg.augmenters.pillike.FilterFindEdges`
  * `augimg.augmenters.pillike.FilterContour`
  * `augimg.augmenters.pillike.FilterEmboss`
  * `augimg.augmenters.pillike.FilterSharpen`
  * `augimg.augmenters.pillike.FilterDetail`
  * `augimg.augmenters.pillike.Affine`
