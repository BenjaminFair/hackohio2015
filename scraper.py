#!/usr/bin/python

import pykcd, io, re, os, string
from sets import Set

OUTFILE = 'xkcd_transcripts'

blacklist = Set([404,1002, 1005, 1007, 1011])

os.system('rm -f '+OUTFILE)

for i in range(1500, 1589):

  if i in blacklist:
    continue

  out = 'Getting Transcript for ' + str(i)
  print out

  strip = pykcd.XKCDStrip(i)

# Remove scene descriptions [[*]] and alt text {{*}}
  trans = re.sub('[\[{(]+.+?[\]})]+', '', strip.transcript, flags=re.DOTALL)

  with io.open('tmp','w') as file:
    file.write(trans)

  with io.open('tmp','r') as file:
    with io.open(OUTFILE,'a') as file2:
      for line in file:
# Find lines with speaker:
        if re.match('.*?: ', line):
          print line,
# Remove speaker: statements
          line = re.sub('.*?: ', '', line, count=1)
	  if line and line!='\n':
            file2.write(line)

  os.system('rm -f tmp')
