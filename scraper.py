#!/usr/bin/python

import pykcd, io, re, os, string
from sets import Set

OUTFILE = 'xkcd_transcripts'
TMPFILE = 'tmp'
NEWEST = 1604

blacklist = Set([404])

try:
  os.unlink(OUTFILE)
except OSError:
  pass

for i in range(1, NEWEST):

  if i in blacklist:
    continue

  print 'Getting Transcript for ' + str(i)

  strip = pykcd.XKCDStrip(i)

# Remove scene descriptions [[*]] and alt text {{*}}
  trans = re.sub('[\[{(]+.+?[\]})]+', '', strip.transcript, flags=re.DOTALL)
  trans = trans.encode('ascii', 'ignore')
#  print trans,
  with open(TMPFILE,'w') as file:
    file.write(trans)

  with open(TMPFILE,'r') as file:
    with open(OUTFILE,'a') as file2:
      for line in file:
# Find lines with speaker:
        if re.match('.*?: ', line):
#          print line,
# Remove speaker: statements
          line = re.sub('.*?: ', '', line, count=1)
	  if line and line!='\n':
            file2.write(line)

  os.unlink(TMPFILE)
