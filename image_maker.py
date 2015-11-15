from PIL import Image, ImageDraw, ImageFont
import sys

comicNum = 1603
fontHeight = 20
font = ImageFont.truetype("xkcd.ttf", fontHeight)
#x and y coordinates of upper-left + bottom-right vertex of rectangle
x = [4, 186, 100, 186, 195, 357, 197, 327, 247, 340, 564, 727, 624, 731, 583, 678]
y = [11, 69, 135, 153,  10,  66,  77, 115, 129, 145,   8,  47,  57,  95, 115, 154]
color = [255, 255, 255, 255, 255, 0, 0, 0]
maxCharOnLine = 0
offset = 0
textStr = "QWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPSDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKL" 

def maxCharPerLine(width):
  return int(round((width/8.33),0))

def getMaxLines(height):
  return height/fontHeight+1

def pick():
  returnThis = []
  for z in range(0, len(x), 2):
    maxLines = getMaxLines(y[z+1]-y[z])
    cpl = maxCharPerLine(x[z+1]-x[z])
    print maxLines, cpl
    maxChar = cpl*maxLines
    returnThis.append(maxChar)
  return (comicNum, returnThis)

def make(comic, dialog):
  im = Image.open("%d.png" % comic)
  draw = ImageDraw.Draw(im)
  for n in range(0, len(x), 2):
    maxLines = getMaxLines(y[n+1]-y[n])
    cpl = maxCharPerLine(x[n+1]-x[n])

    #fills rectangle of solid color over text
    draw.rectangle([(x[n],y[n]),(x[n+1],y[n+1])], fill=color[n/2], outline=None)

    #writes new text at given position
    words = dialog[n/2].split(' ')
    curWord = 0
    for v in range(0, maxLines):      
      startWord = curWord
      curChars = 0
      while curWord < len(words):
        curChars += len(words[curWord])+1
        if curChars > cpl:
          break
        curWord += 1
      draw.text((x[n],y[n]+fontHeight*v), ' '.join(words[startWord:curWord]), fill=255-color[n/2], font=font)
  del draw
  # write to output
  with open("out.png", 'w') as f:
    im.save(f, "PNG")

  return "out.png"

if __name__ == "__main__":
  num, lengths = pick()
  print num, lengths
  print make(num, ["a " * length for length in lengths])
