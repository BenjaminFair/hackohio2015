#!/usr/bin/python

import io, re, os, string
from sets import Set

spcl_set = Set(['!','\'','"',',','-','.',';',':','=','.','?',' '])
badwords = ['FUCK', 'ASS', 'SHIT', 'NIGGER', 'BITCH']

INFILE = 'movie_lines.txt'
OUTFILE = 'movie_lines.clean.txt'
TMPFILE = 'tmp'

try:
  os.unlink(OUTFILE)
except OSError:
  pass

with open(INFILE, 'r') as ifile:
  with open(OUTFILE, 'w') as ofile:
    for line in ifile:
      line = string.upper(line)
      line = re.sub('<.*?>', '', line)
      line = re.sub('\+\+\+\$\+\+\+ *', '', line)
      for word in badwords:
        line = re.sub(word, word[0]+'-'*(len(word)-1), line)
      nline = ''
      for ch in line:
        if ch in string.uppercase or ch in string.digits or ch in spcl_set:
          nline += ch
      nline += '\n'
      ofile.write(nline)

try:
  os.unlink(TMPFILE)
except OSError:
  pass
