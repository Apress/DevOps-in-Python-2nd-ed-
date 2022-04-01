#!/usr/bin/env python3
# save as simple.inv
import sys
import json

if '--host' in sys.argv[1:]:
    print(json.dumps({}))
else:
    print(json.dumps(dict(all='localhost')))
