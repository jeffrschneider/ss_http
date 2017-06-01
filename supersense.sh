#!/bin/bash

# Predict with an existing MWE model.
# Usage: ./mwe_identify.sh model input

#set -eu

cd tweettag && ./runTagger.sh --model ewtb_pos.model sentences.txt | python reformatTokens.py > tagged

cd .. && ./sst.sh tweettag/tagged

cd tweettag && cut -f 2,5  tagged.pred.tags > tokenAndSenses