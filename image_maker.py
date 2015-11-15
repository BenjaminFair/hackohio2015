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
  return int(round((width/8.33),0)-3)

def pick():
  returnThis = []
  for z in range(0, len(x)/2):
    maxLines = int(round((y[z+1]-y[z])/fontHeight,0))
    print maxLines
    cpl = maxCharPerLine(x[z+1]-x[z])
    print maxCharOnLine  
    maxChar = cpl*maxLines
    returnThis.append(maxChar)
  return (comicNum, returnThis)

def make(comic, dialog):
  for n in range(len(dialog)):
    text = dialog[n]
    cpl = maxCharPerLine(x[n+1]-x[n])
    totLines = len(text)/cpl+1
    print totLines
    im = Image.open("%d.png" % comic)
    draw = ImageDraw.Draw(im)

    #fills rectangle of solid cover over text
    draw.rectangle([(x[n],y[n]),(x[n+1],y[n+1])], fill=255, outline=None)

    #writes new text at given position
    for v in range(0, totLines):      
      draw.text((x[n],y[n]+fontHeight*v), text[cpl*v:(cpl*(v+1))], font=font)
    del draw
    # write to stdout
    with open("out.png", 'w') as f:
      im.save(f, "PNG")

  return "out.png"





