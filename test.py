import markov

m = markov.Markov(2)
with open('lines.txt') as f:
  for line in f:
    m.add(line)

