#!/bin/bash
# This is expected to be executed from /augimg, not from /augimg/test.
# That way it is ensured that you use the current code of the library in
# the augimg/augimg/ subfolder, not the installed version of the library.
#
# The command below executes all tests.
# To execute only one specific test, use e.g.
# pytest ./test/augmenters/test_geometric.py::TestRot90::test_empty_polygons
python -m pytest ./test --verbose --xdoctest-modules -s --durations=20 -Walways
