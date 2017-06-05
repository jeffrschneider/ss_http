#!/bin/bash

# Predict with an existing MWE model.
# Usage: ./mwe_identify.sh model input

set -eu
set -o pipefail

input=$1 # word and POS tag on each line (tab-separated)


./predict_sst.sh $input # direct to stdout instead of > $input.pred.tags

# src/tags2sst.py -l $input.pred.tags > $input.pred.sst

