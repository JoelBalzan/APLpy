from PIL import Image
import aplpy
import argparse


### PARSER ###
parser = argparse.ArgumentParser(description="Converts a FITS file to RGB.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-f", "--fits", type=str, help="The FITS file to make RGB.")
args = vars(parser.parse_args())


### IMAGE ###
img = args["fits"]


### CONVERT TO RGB ###
aplpy.make_rgb_image(img, 'aplpy_rgb_out.tiff', stretch_r='log', stretch_g='log', stretch_b='log',
                     vmin_r=0.3, vmin_g=0.2, vmin_b=0.1, vmax_r=73.5, vmax_g=60, vmax_b=17
                     ) # PLAY WITH VMIN AND VMAX IN DS9


### OPEN IMAGE ###
open_image = Image.open('aplpy_rgb_out.tiff')
open_image.show()
