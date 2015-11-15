# some code from sadface by Benjamin Keith (ben@benlk.com)
#     https://github.com/benlk/sadface

from twisted.words.protocols import irc
from twisted.internet import protocol, reactor
import re

class xkcdBot(irc.IRCClient):
  def _get_nickname(self):
    return self.factory.nickname
  nickname = property(_get_nickname)

  def signedOn(self):
    print "Joining " + self.factory.channel
    self.join(self.factory.channel)

  def joined(self, channel):
    print "Joined " + channel
    self.msg(channel, "Hai everyone!")

  def privmsg(self, user, channel, msg):
    user_nick = user.split('!', 1)[0]
    if self.nickname in msg:
      msg = re.compile(self.nickname + "[:,]* ?", re.I).sub('', msg)
      reply = user_nick + ": " + self.factory.generator(msg)
      self.msg(channel, reply)

class xkcdBotFactory(protocol.ClientFactory):
  protocol = xkcdBot

  def __init__(self, channel, nick, generator):
    self.channel = channel
    self.nickname = nick
    self.generator = generator

  def clientConnectionLost(self, connector, reason):
    print "Lost connection: %s. Attempting to reconnect." % (reason,)
    connector.connect()

  def clientConnectionFailed(self, connector, reason):
    print "Failed to connect: %s." % (reason,)
    quit()

def Run(host, port, channel, nickname, generator):
  factory = xkcdBotFactory(channel, nickname, generator)
  reactor.connectTCP(host, port, factory)
  reactor.run()

if __name__ == "__main__":
  Run("irc.freenode.net", 6667, "#bottest", "benjbot", None)
