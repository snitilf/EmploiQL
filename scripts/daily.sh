#!/bin/bash
# script ran daily to fetch jobs

python3 src/jsearch.py --preset software --live
python3 src/jsearch.py --preset developer --live
python3 src/jsearch.py --preset data --live
python3 src/jsearch.py --preset cyber --live
python3 src/jsearch.py --preset frontend --live
python3 src/jsearch.py --preset backend --live
python3 src/jsearch.py --preset fullstack --live
python3 src/jsearch.py --preset ml --live
python3 src/jsearch.py --preset devops --live
python3 src/jsearch.py --query "python intern" --live
python3 src/jsearch.py --query "java intern" --live

# load all fetched jobs into the database
echo ""
echo "loading jobs into database"

# capture output and extract the "Loaded" count
LOAD_OUTPUT=$(python3 scripts/load_jsearch.py --all --mock 2>&1)
echo "$LOAD_OUTPUT"

# extract the number of jobs loaded 
# handle both ANSI color codes and plain text
JOBS_LOADED=$(echo "$LOAD_OUTPUT" | grep -E "Loaded:" | sed -E 's/.*Loaded:[^0-9]*([0-9]+).*/\1/' | head -1)

# display final summary
echo ""
echo "============================================================"
if [ -n "$JOBS_LOADED" ]; then
    echo "✓ total jobs added to database: $JOBS_LOADED"
else
    echo "✓ jobs loaded (see summary above for details)"
fi
echo "============================================================"