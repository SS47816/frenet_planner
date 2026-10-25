"""frenet_planner is now fiss_planner (https://github.com/SS47816/fiss_planner).

This package only keeps old imports working: `import frenet_planner` returns the
`fiss_planner` module. Install and import `fiss_planner` instead.
"""

import sys
import warnings

import fiss_planner

warnings.warn(
    "frenet_planner has been renamed to fiss_planner: `pip install fiss-planner` and `import fiss_planner`.",
    DeprecationWarning,
    stacklevel=2,
)
sys.modules[__name__] = fiss_planner
