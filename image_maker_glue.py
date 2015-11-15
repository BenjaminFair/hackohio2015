import os
from imgurpython import ImgurClient

import markov
import keys
import image_maker

class ImageMakerGlue():
  def __init__(self, file):
    self.m = markov.Markov(2, file)
    self.client = ImgurClient(keys.imgur_client_id, keys.imgur_client_secret)

  def gen(self, msg, max=None):
    comic, lengths = image_maker.pick()
    dialog = []
    for l in lengths:
      dialog.append(self.m.gen(msg, l))
    print dialog
    file_name = image_maker.make(comic, dialog)
    link = str(self.client.upload_from_path(file_name)["link"])
    os.unlink(file_name)
    return link

if __name__ == "__main__":
  i = ImageMakerGlue("lines.txt")
  print i.gen("")
