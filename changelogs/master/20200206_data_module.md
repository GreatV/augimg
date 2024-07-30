# Add New `data` Module #606

This patch moves the example data functions from `augimg.augimg` to
the new module `augimg.data`.

Add Modules:
* `augimg.data`

Add Functions:
* `augimg.data.quokka()`
* `augimg.data.quokka_square()`
* `augimg.data.quokka_heatmap()`
* `augimg.data.quokka_segmentation_map()`
* `augimg.data.quokka_keypoints()`
* `augimg.data.quokka_bounding_boxes()`
* `augimg.data.quokka_polygons()`

Deprecated Functions:
* `augimg.augimg.quokka()`.
  Use `augimg.data.quokka()` instead.
* `augimg.augimg.quokka_square()`.
  Use `augimg.data.quokka_square()` instead.
* `augimg.augimg.quokka_heatmap()`.
  Use `augimg.data.quokka_heatmap()` instead.
* `augimg.augimg.quokka_segmentation_map()`.
  Use `augimg.data.quokka_segmentation_map()` instead.
* `augimg.augimg.quokka_keypoints()`.
  Use `augimg.data.quokka_keypoints()` instead.
* `augimg.augimg.quokka_bounding_boxes()`.
  Use `augimg.data.quokka_bounding_boxes()` instead.
* `augimg.augimg.quokka_polygons()`.
  Use `augimg.data.quokka_polygons()` instead.

Removed Constants:
* [rarely breaking] `augimg.augimg.FILE_DIR`
* [rarely breaking] `augimg.augimg.QUOKKA_FP`
* [rarely breaking] `augimg.augimg.QUOKKA_ANNOTATIONS_FP`
* [rarely breaking] `augimg.augimg.QUOKKA_DEPTH_MAP_HALFRES_FP`
