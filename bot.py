from twisted.words.protocols import irc
from twisted.internet import protocol, reactor

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
    pass

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

if __name__ == "__main__":
  factory = xkcdBotFactory("#bottest", "benjbot", None)
  reactor.connectTCP("irc.freenode.net", 6667, factory)
  reactor.run()
