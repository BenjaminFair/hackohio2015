import random
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
    for w in msg.split():
      self.data[tuple(ngram)].append(w)
      del ngram[0]
      ngram.append(w)
    self.data[tuple(ngram)].append(self.STOP)

  def train(self, file_name):
    with open(file_name) as file:
      for line in file:
        self.add(line)

  def gen(self, start="", max=40):
    ngram = start.split(' ')
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

    return ' '.join(msg)

if __name__ == "__main__":
  m = Markov(2, "lines.txt")

  print m.gen()
