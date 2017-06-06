use ss_tagger.py

note: initialization of a tagger object can take up to a minute
        lexicons take up 1.34gb of memory per tagger object.

tagger.pairs(sentence) returns list of token/supersense pairs.

tagger.json(in) converts pairs or sentence to JSON formatted list of pairs.

modifies
pysupersensetagger
by Nathan Scheider

