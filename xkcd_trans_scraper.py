#!/usr/bin/python

import pykcd, io, re

strip = pykcd.XKCDStrip(104)

with io.open('tmp','w') as file:
  file.write(strip.transcript)

with io.open('tmp','r') as file:
  with io.open('tmp2','w') as file2:
    for line in file:
      if not re.match('\[\[', line) and not re.match('\{\{', line) and not re.match('\n', line):
        file2.write(line)

