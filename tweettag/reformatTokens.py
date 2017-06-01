#!/usr/bin/env python
import sys

if __name__ == "__main__":
    resultList = sys.stdin.readlines()[0].split('\t') #tokens, tags, times, origninal sentences
    tokens = resultList[0].split(' ')
    tags = resultList[1].split(' ')
    paired_lines = ""
    for i in range(len(tokens)):
        paired_lines += tokens[i]+"\t"+tags[i]+"\n"
        if tokens[i] is '.':
            paired_lines += '\n'
    sys.stdout.write(paired_lines)
