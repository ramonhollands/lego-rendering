#!/bin/bash

set -e

/snap/bin/blender --background --python ./setup.py

cd /snap/bin/blender/Resources/3.5/python/bin

./python3.10 -m pip install pillow
