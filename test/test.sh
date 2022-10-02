#!/bin/bash

# build docker image
cd ../scripts && ./build.sh

# run docker image
docker run -it --rm --device /dev/dri -p 8000:8000 -p 2303:2303 -p 1905:1905 -p 8765:8765 -p 6080:6080 -p 1108:1108 jderobot/robotics-academy &
sleep 10

# run selenium scripts
cd ../test && python test.py
