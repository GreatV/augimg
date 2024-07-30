# Index-based Access to Coordinate-based `*OnImage` Instances #547

Enabled index-based access to coordinate-based `*OnImage` instances, i.e. to
`KeypointsOnImage`, `BoundingBoxesOnImage`, `LineStringsOnImage` and
`PolygonsOnImage`. This allows to do things like
`bbsoi = BoundingBoxesOnImage(...); bbs = bbsoi[0:2];`.

* Added `augimg.augmentables.kps.KeypointsOnImage.__getitem__()`.
* Added `augimg.augmentables.bbs.BoundingBoxesOnImage.__getitem__()`.
* Added `augimg.augmentables.lines.LineStringsOnImage.__getitem__()`.
* Added `augimg.augmentables.polys.PolygonsOnImage.__getitem__()`.
