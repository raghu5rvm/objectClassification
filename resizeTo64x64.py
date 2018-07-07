"""********************************************************************
Instructions						
. place this file along with images that we need to resize and run
. this will create a new directory in parent folder to store resized images
. check for image extensions(case sensitive)

*********************************************************************"""

#!/usr/bin/env python

from PIL import Image, ImageOps
import os, sys

def resizeImage(infile, output_dir, size=(64,64)):
     outfile = os.path.splitext(infile)[0]+"_r"
     extension = os.path.splitext(infile)[1]

     if (cmp(extension, ".jpg")):
        return

     if infile != outfile:
        try :
            im = Image.open(infile)
            im=ImageOps.fit(im,size, Image.ANTIALIAS)
            im.save(output_dir+outfile+extension)
        except IOError:
            print "cannot reduce image for ", infile


if __name__=="__main__":
    
    dir = os.getcwd()
    output_dir = os.path.join(dir+"R32/")
    print "dir ="+dir+" --- \n output dir== "+output_dir+"\n\n"
    if not os.path.exists(os.path.join(dir,output_dir)):
        os.mkdir(output_dir)
    for file in os.listdir(dir):
		resizeImage(file,output_dir)
