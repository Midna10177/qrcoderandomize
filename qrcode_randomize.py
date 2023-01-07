#!/usr/bin/python3
import string
from PIL import Image
from itertools import combinations
from random import randint
from random import choice as randchoice
from sys import argv

argv.pop(0)

if not argv:
 imagefiles = [ 'qrcode.png' ]
else:
 imagefiles = argv

#program will only run on one image despite it looking like the contrary

images = [ Image.open(x) for x in imagefiles ]


CHANGE_WHITE_PIXELS = True
CHANGE_BLACK_PIXELS = True


WHITE = ( 255, 255, 255 )
BLACK = ( 0, 0, 0 )

COLORS = [ (0,0,0), (255,255,255), (0,0,255), (0,255,0), (255,0,0), (0,255,255), (255,0,255), (255,255,0) ]


#get the max width and max height from our list of images
newimgsize = ( max( map( lambda x:x.size[0], images ) ), max( map( lambda x:x.size[1], images ) ) )


print( "input image sizes: " )

for i in images:
 print( ' +',  i.size, 'mode: ', i.mode )

print( "\noutput image size:", newimgsize )






#Now we're onto the juicy stuff! we have to decide for each image, which colors will correspond to being black or white

#we will begin by looping through our colors, deciding randomly for our first image which colors will translate to black and which will translate to white

IMGCOLORPROFILES = []
for img in images:
 thisprofile = { "black": [], "white": [] }
 for color in COLORS:
  if randint(0,1):
   thisprofile["black"].append(color)
  else:
   thisprofile["white"].append(color)
 IMGCOLORPROFILES.append( thisprofile )

for i in IMGCOLORPROFILES: print(i,'\n')





#after creating our color profile, we can go through, and actually create our new image by randomly changing all the black pixels to values from our array labeled black
newimg = Image.new( images[0].mode, newimgsize )
newdata = newimg.load()

data=images[0].load()

#only doing a single image unless someone wants to change that :) just kidding i dont even wanna touch it
for x in range( images[0].size[0] ):
 for y in range( images[0].size[1] ):
  currentcolor = data[x,y]
  if currentcolor == WHITE:
   if CHANGE_WHITE_PIXELS:
    newdata[x,y] = randchoice( IMGCOLORPROFILES[0]["white"] )
   else:
    newdata[x,y] = WHITE
  
  else:
   if CHANGE_BLACK_PIXELS:
    newdata[x,y] = randchoice( IMGCOLORPROFILES[0]["black"] )
   else:
    newdata[x,y] = BLACK

outfile = ''.join([ randchoice(string.ascii_lowercase) for _ in range(6) ]) + '.png'

print('Saving to',outfile)
newimg.save( outfile )









