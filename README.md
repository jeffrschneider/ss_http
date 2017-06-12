Entirely built off of Nathan Schneider’s AMALGrAM 2.0 /
pysupersensetagger:
<https://github.com/nschneid/pysupersensetagger>

See also: <http://www.cs.cmu.edu/~ark/LexSem/>





**ss\_http**
====================

A python HTTP server for tagging supersenses.

-   Enables rapid input by keeping lexicons in memory.
-   Provides convenient python wrapper for shell scripts to ease
    interoperation.



Supports:
-   Multiple sentences
-   Unicode white spaces
-   Full and half width characters.
-   Punctuation: . ! ? ; : ‘ “

If an unsupported character is used, \[\[“INVALID”\], \[”CHARACTER”\]\]
will be returned and the server will live on.



For use of tagger without a server, see **Advanced Use**



Supersenses tagged

Nouns (capitalized): COGNITION, COMMUNICATION, PHENOMENON, PROCESS,
EVENT, ACT, RELATION, ATTRIBUTE, STATE, ARTIFACT, MOTIVE, FEELING,
QUANTITY, RELATION, TIME, OBJECT, POSSESSION, SUBSTANCE, OTHER, ANIMAL,
PERSON, PLANT, BODY, FOOD, GROUP, LOCATION, SHAPE, OBJECT



Verbs (lowercase): \`a, \`j, body, change, cognition, communication,
competition, consumption, contact, creation, emotion, motion,
perception, possession, social, stative, weather



For more information on tags and how they are chosen, see the resources
folder.



**Easy start with Docker installed:**

docker pull brombach/ss\_http

-   or build your own image with the dockerfile

docker run -p **xx**:8080 brombach/ss\_http

-   The image will expose port 8080 of its container. *-p xx:8080* maps
    the connection to port **xx** of your choosing on the host machine.
-   NOTE: \~1.4gb of data must be loaded into memory before the server
    is initialized. This can take between 30 and 90 seconds.



Send GET requests with a single key-value pair of data=*sentence*

-   **Example request**: curl
    localhost:**xx**/?data=This%20is%20a%20sample%20sentence.

-   To edit the port exposed on the container, change the EXPOSE command
    in Dockerfile and PORT\_NUMBER in ss\_http.py, then rebuild.



**Without Docker / Advanced use:**

Requirements: python2 and python3. \[nltk, cython\] installed by
pip**2** for python **\*2\***



Running ss\_http.py with python3 will initialize the HTTP server in the
same way as above, including 30-90 second spin-up time. To edit the
port, change the PORT\_NUMBER constant in ss\_http.py.



Send GET requests with a single key-value pair of data=*sentence*

**Example request**: curl
localhost:8080/?data=This%20is%20a%20sample%20sentence.


**Using the tagger offline:**

**from ss\_tagger import tagger**

**t = tagger**

-   this command will take 30-90 seconds as lexicons are loaded into
    memory

**t.json(“*sentence*”)**

-   returns an array of \[token,supersense\] pairs in json compatible
    format.

**t.pairs(“*sentence”*)**

-   returns an array of array of \[token,supersense\] pairs

t.tag\_sentence(“*sentence”*)

returns tab seperated columns in the form:

-   num | token | lowercase\_token | POS\_tag |
    multiword\_phrase\_info-supersense | is\_part\_of\_MWP | supersense

t.extract\_raw\_pairs(tab\_seperated\_columns)

-   input is output of tag\_sentence
-   returns pairs made from 2nd (token) and 5th (MWP-supersense) columns
    of each row.

t.clean\_up\_iob(pairs)

-   input is output of extract\_raw\_pairs(tsc): \[\[tok, MWP-SS\],
    \[tok, MWP-SS\], ... \]
-   uses multiword-phrase info to attach supersense of beginning of
    phrase to all components.


