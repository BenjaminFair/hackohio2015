from PIL import Image, ImageDraw, ImageFont
import sys

comicNum = 1603
fontHeight = 19
font = ImageFont.truetype("xkcd.ttf", fontHeight)
#x and y coordinates of upper-left + bottom-right vertex of rectangle
x = [4, 186]
y = [11, 69]
maxCharOnLine = 0
offset = 0
textStr = "QWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPSDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKL" 

def maxCharPerLine(width):
  return int(round((width/8.33),0))

def getMaxLines(height):
  return int(round(height/fontHeight,0))

def pick():
  returnThis = []
  for z in range(0, len(x)/2):
    maxLines = getMaxLines(y[z+1]-y[z])
    print maxLines
    cpl = maxCharPerLine(x[z+1]-x[z])
    print maxCharOnLine  
    maxChar = cpl*maxLines
    returnThis.append(maxChar)
  return (comicNum, returnThis)

def make(comic, dialog):
  for n in range(len(dialog)):
    cpl = maxCharPerLine(x[n+1]-x[n])
    maxLines = getMaxLines(y[n+1]-y[n])
    print maxLines
    im = Image.open("%d.png" % comic)
    draw = ImageDraw.Draw(im)

    #fills rectangle of solid cover over text
    draw.rectangle([(x[n],y[n]),(x[n+1],y[n+1])], fill=255, outline=None)

    #writes new text at given position
    words = dialog[n].split(' ')
    curWord = 0
    for v in range(0, maxLines):      
      startWord = curWord
      curChars = 0
      while curWord < len(words):
        curChars += len(words[curWord])+1
        if curChars > cpl:
          break
        curWord += 1
      draw.text((x[n],y[n]+fontHeight*v), ' '.join(words[startWord:curWord]), font=font)
    del draw
    # write to output
    with open("out.png", 'w') as f:
      im.save(f, "PNG")

  return "out.png"

if __name__ == "__main__":
  num, lengths = pick()
  print num, lengths
  print make(num, ["a" * length for length in lengths])
