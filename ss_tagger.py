#!/usr/bin/env python3
from subprocess import Popen, PIPE, STDOUT
import sys
import json
import time

class tagger:

    def __init__(self):
        self.p = Popen(['./predict_sst.sh', 'dummy'], stdout=PIPE, stderr=PIPE,stdin=PIPE, bufsize=1, universal_newlines=True)
        for line in self.p.stderr:
            if "Ready" in line:
                break

    def tag_sentence(self, sentence):
        sentence += '\n' #to trigger readline()
        self.p.stdin.write(sentence)
        tsv = ""
        for line in self.p.stdout:
            if line == '\n':
                continue
            tsv += line
            if "$NEXT" in line:
                break
        return tsv

    def extract_raw_pairs(self, tsv): #will not clean up IOB
        pairs = []
        rows = tsv.split('\n')
        for line in rows:
            if line == '$NEXT':
                continue
            
            if len(line.split('\t')) < 5:
                continue
            
            cols = line.split('\t')
            pair = [cols[1],cols[4]]
            pairs.append(pair)
        return pairs

    def clean_up_iob(self, raw_pairs): #cleans up IOB
        for i in range(len(raw_pairs)):
            tag = raw_pairs[i][1]
            if '-' in tag:
                tag = tag[2:]
            if 'B' == tag:
                tag = 'O'
            if 'Ī' == tag:
                tag = raw_pairs[i-1][1]
            if '`a' == tag:
                tag = 'O'
            raw_pairs[i][1] = tag
        return raw_pairs

    def pairs(self, sentence):
        return self.clean_up_iob(
                                 self.extract_raw_pairs(
                                                        self.tag_sentence(
                                                                          sentence ) ) )

    def json(self, source):
        kind = type(source).__name__
        if kind == 'str':
            return json.dumps(self.pairs(source))
        elif kind == 'list':
            return json.dumps(source)
        else:
            return "ERROR: not a list or string"
