import os
from imgurpythn import ImgurClient

import markov
import keys

class ImageMakerGlue():
  def __init__(self, file):
    self.m = markov.Markov(2, file)
    self.client = ImgurClient(keys.imgur_client_id, keys.imgur_client_secret)

  def gen(self, msg, max=None):
    comic, lengths = image_maker.pick()
    dialog = []
    for l in lengths:
      dialog.append(self.m.gen(msg, l))
    file_name = image_maker.make(comic, dialog)
    link = self.client.upload_from_path(file_name)["link"]
    os.unlink(file_name)
    return link
