# The implementation of Markov chains is inspired by the one in sadface by
# Benjamin Keith (ben@benlk.com) at https://github.com/benlk/sadface

import random, string
from collections import defaultdict

class Markov():

  def __init__(self, length, file=None):
    self.length = length
    self.data = defaultdict(list)
    self.STOP = '\n'

    if file is not None:
      self.train(file)

  def add(self, msg):
    ngram = [''] * self.length
    for x in msg.split():
      w = string.lower(x)
      self.data[tuple(ngram)].append(w)
      del ngram[0]
      ngram.append(w)
    self.data[tuple(ngram)].append(self.STOP)

  def train(self, file_name):
    with open(file_name) as file:
      for line in file:
        self.add(line)

  def gen(self, start="", max=60):
    l = max+1
    while l > max:
      startWords = start.split(' ')
      startWords = startWords[0:min(len(startWords), self.length)]
      ngram = [word.lower() for word in startWords]
      if len(ngram) < self.length:
        ngram = [''] * (self.length - len(ngram)) + ngram
      msg = [word for word in ngram if word != '']
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
      out = ' '.join(msg)
      l = len(out)

    return out

if __name__ == "__main__":
  m = Markov(2, "lines.txt")

  print m.gen()
