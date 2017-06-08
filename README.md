Run ss_http.py to initialize. 
Port is currently 8080. 

send requests as URL/?data=SENTENCE, 
where SENTENCE is ASCII escaped sentence with or without quotes.


using ss_tagger.py directly

note: initialization of a tagger object can take up to a minute
        lexicons take up 1.34gb of memory per tagger object.

tagger.pairs(sentence) returns list of token/supersense pairs.

tagger.json(in) converts pairs or sentence to JSON formatted list of pairs.

Supersenses tagged:

Nouns (capitalized): COGNITION, COMMUNICATION, PHENOMENON, PROCESS, EVENT, ACT, RELATION, ATTRIBUTE, STATE, ARTIFACT, MOTIVE, FEELING, QUANTITY, RELATION, TIME, OBJECT, POSSESSION, SUBSTANCE, OTHER, ANIMAL, PERSON, PLANT, BODY, FOOD, GROUP, LOCATION, SHAPE, OBJECT

Verbs (lowercase): \`a, \`j, body, change, cognition, communication, competition, consumption, contact, creation, emotion, motion, perception, possession, social, stative, weather

For more details on tags, see the Resources folder.

modifies
pysupersensetagger
by Nathan Scheider

