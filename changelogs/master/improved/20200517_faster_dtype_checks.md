# Improved Performance of dtype checks #663

This patch improves the performance of dtype checks
throughout the library. The new method verifies input
arrays around 10x to 100x faster than the previous one.

Add functions:
* `augimg.dtypes.gate_dtypes_strs()`
* `augimg.dtypes.allow_only_uint8()`

Add decorators:
* `augimg.testutils.ensure_deprecation_warning`

Deprecate functions:
* `augimg.dtypes.gate_dtypes()`
