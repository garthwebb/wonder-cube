from wonder.core import Core

import sys

if len(sys.argv) == 2:
    wonder = Core(sys.argv[1])
else:
    wonder = Core()

wonder.run()
