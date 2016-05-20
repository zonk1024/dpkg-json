#!/usr/bin/env python
import os
import json

lines = os.popen('dpkg -l | grep "^ii"').read().split('\n')[5:-1]
i = 0
while len([l for l in lines[i].split('  ') if l]) != 4:
   i += 1
offsets = [lines[i].index(l) for l in lines[i].split('  ') if len(l)]
pkgs = {}
for line in lines:
    parsed = []
    for i in range(len(offsets)):
        if len(offsets) == i + 1:
            parsed.append(line[offsets[i]:].strip())
        else:
            parsed.append(line[offsets[i]:offsets[i + 1]].strip())
    pkgs.update({parsed[1]:{'state':parsed[0],'version':parsed[2],'description':parsed[3]}})

print json.dumps(pkgs)
