import sys
import json

if __name__ == "__main__":
    
    pairs = []
    for line in sys.stdin:
        line = line.strip()
        if line == '$NEXT':
            pairs_json = json.dumps(pairs)
            print(pairs_json, file=sys.stdout)
            
            pairs = []
            continue
        
        if len(line.split('\t')) is not 2:
            continue
        
        pair = line.split('\t')
        if "0-" in pair[1]:
            pair[1] = pair[1][2:]
        pairs.append(pair)


