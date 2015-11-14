import random
from collections import defaultdict

class Markov():

  def __init__(self, length):
    self.length = length
    self.data = defaultdict(list)
    self.STOP = '\n'

  def add(self, msg):
    ngram = [''] * self.length
    for w in msg.split():
      self.data[tuple(ngram)].append(w)
      del ngram[0]
      ngram.append(w)
    self.data[tuple(ngram)].append(self.STOP)

  def gen(self, max=20, ngram=None):
    msg = []
    if ngram is None:
      ngram = [''] * self.length
    for i in xrange(max):
      try:
        next = random.choice(self.data[tuple(ngram)])
      except IndexError:
        continue
      if next == self.STOP:
        break
      msg.append(next)
      del ngram[0]
      ngram.append(next)

    return ' '.join(msg)
