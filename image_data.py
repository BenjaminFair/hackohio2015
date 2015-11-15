
x =     {1603: [  4, 186, 100, 186, 195, 357, 197, 327, 247, 340, 564, 727, 624, 731, 583, 678],
         1543: [ 17, 257,  17, 238,  17, 195],
         1154: [  9, 141, 156, 360, 372, 529, 412, 561],
          904: [ 14, 246,  92, 238,  34, 229],
          705: [  8, 178,  78, 169, 204, 444, 298, 430, 469, 630, 514, 626]}
y =     {1603: [ 11,  69, 135, 153,  10,  66,  77, 115, 129, 145,   8,  47,  57,  95, 115, 154],
         1543: [ 13,  92, 103, 162, 175, 213],
         1154: [  6,  94,   6,  93,   6,  40,  49,  84],
          904: [ 12,  71,  90, 130, 322, 342],
          705: [  8,  83, 134, 208,   6,  82, 178, 230,   8, 100, 168, 222]}
color = {1603: [255,      255,      255,      255,      255,        0,        0,        0],
         1543: [255,      255,      255,      255],
         1154: [255,      255,      255,      255],
          904: [255,      255,      255],
          705: [255,      255,      255,      255,      255,      255]}

def getComics():
  return x.keys()

def getData(comic):
  return (x[comic], y[comic], color[comic])
