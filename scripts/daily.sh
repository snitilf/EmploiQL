#!/bin/bash
# script run daily to fetch jobs

python3 src/jsearch.py --preset software --pages 2 --live
python3 src/jsearch.py --preset developer --pages 2 --live
python3 src/jsearch.py --preset cyber --live
python3 src/jsearch.py --preset frontend --live
python3 src/jsearch.py --preset backend --live
python3 src/jsearch.py --preset fullstack --pages 2 --live
python3 src/jsearch.py --preset ml --live
python3 src/jsearch.py --preset devops --pages 2 --live

