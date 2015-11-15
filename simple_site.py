#!/usr/bin/python

from twisted.web import server, resource
from twisted.internet import reactor

import cgi, image_maker_glue

HTML = """<!DOCTYPE html>
<html>
<body>

<img src="%s" alt="">

<form>
  Seed: <input type="text" name="seed"><br>
  <input type="submit" formmethod="post" value="Submit using POST">
</form>

</body>
</html>"""

i = image_maker_glue.ImageMakerGlue("movie_lines.txt")

class Simple(resource.Resource):
  isLeaf = True
  def __init__(self):
    self.i = image_maker_glue.ImageMakerGlue("movie_lines.clean.txt")
  def render_GET(self, request):
    return HTML
  def render_POST(self, request):
    s = cgi.escape(request.args["seed"][0]),
    link = self.i.gen(s[0])
    return HTML % link


site = server.Site(Simple())
reactor.listenTCP(8080, site)
reactor.run()
