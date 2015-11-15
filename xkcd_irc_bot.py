import image_maker_glue
import irc_bot

i = image_maker_glue.ImageMakerGlue("movie_lines.txt")
irc_bot.Run("irc.freenode.net", 6667, "#bottest", "benjbot", i.gen)

