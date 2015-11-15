import markov
import irc_bot

m = markov.Markov(2, "lines.txt")
irc_bot.Run("irc.freenode.net", 6667, "#bottest", "benjbot", m.gen)

