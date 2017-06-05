#!/bin/bash

# Predict with an existing MWE model.
# Usage: ./mwe_identify.sh model input

#set -eu

./predict_sst.sh dummy | unbuffer -p cut -f 2,5 | python3 convertToJSON.py

