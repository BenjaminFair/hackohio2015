from PIL import Image, ImageDraw, ImageFont
import sys

comicNum = 1603
fontHeight = 19
#x and y coordinates of upper-left + bottom-right vertex of rectangle
x = [4, 186]
y = [11, 69]
totLines = 0
maxCharOnLine = 0
offset = 0
textStr = "QWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPSDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKL" 


def pick():
  returnThis = []
  for z in range(0, len(x)/2):
    maxLines = int(round((y[z+1]-y[z])/fontHeight,0))
    maxCharOnLine = int(round(((x[z+1]-x[z])/9),0)-totLines)
    print maxCharOnLine  
    maxChar = maxCharOnLine*maxLines
    returnThis.append(maxChar)
  return (comicNum, returnThis)

def make(comic, dialog):
  for text in dialog:    
    totLines = len(text)
    im = Image.open("%d.png" % comicNum)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("xkcd.ttf", fontHeight)

    #fills rectangle of solid cover over text
    for c in range(0, len(x)/2):
      draw.rectangle([(x[c],y[c]),(x[c+1],y[c+1])], fill=255, outline=None)

    #writes new text at given position
    xCtr=0
    yCtr=0
    loops=0
    maxCharOnLine = int(maxCharOnLine)

    for v in range(0, int(totLines)):
      for b in range(0, len(x)/2):
        draw.text((x[b],y[b]), text[v*maxCharOnLine:(maxCharOnLine*(v+1))], font=font)
        y[b]+=fontHeight
    del draw
    # write to stdout
    with open("out.png", 'w') as f:
      im.save(f, "PNG")

  return "out.png"





