#!/bin/bash

set -x
set +e

/bin/bash -c 'cd python && ./main.py'
/bin/bash -c 'cd java && ./run.sh'
/bin/bash -c 'cd go && ./run.sh'
/bin/bash -c 'cd js && ./run.sh'
/bin/bash -c 'cd js && open ./index.html'
