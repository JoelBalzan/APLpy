import aplpy
import matplotlib.pyplot as mpl
from PIL import Image
import numpy as np
from astropy.wcs import WCS
import argparse


def fix_aplpy_fits(aplpy_obj, dropaxis=2):
    """This removes the degenerated dimensions in APLpy 2.X...
    The input must be the object returned by aplpy.FITSFigure().
    `dropaxis` is the index where to start dropping the axis (by default it assumes the 3rd,4th place).
    """
    temp_wcs = aplpy_obj._wcs.dropaxis(dropaxis)
    temp_wcs = temp_wcs.dropaxis(dropaxis)
    aplpy_obj._wcs = temp_wcs


### READ IN IMAGES/CONTOURS/REGIONS ###
parser = argparse.ArgumentParser(description="Runs APLpy.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-f", "--fits", type=str, help="FITS image.")
parser.add_argument("-f2", "--rgb", type=str, help="RBG image to overlay.")
parser.add_argument("-c1", "--contour1", type=float, help="Contour 1 levels in Jy/beam.")
parser.add_argument("-c2", "--contour2", type=float, help="Contour 2 levels in Jy/beam.")
parser.add_argument("-c3", "--contour3", type=float, help="Contour 3 levels in Jy/beam.")
parser.add_argument("-c4", "--contour4", type=float, help="Contour 4 levels in Jy/beam.")
parser.add_argument("-o", "--objects", type=str, help="Text file with object coordinates in degrees.")
parser.add_argument("-r", "--regions", type=str, help="Region file.")
args = vars(parser.parse_args())


### ASSIGNING VARIABLES ###
## fits image ##
img = args["fits"]
## rgb image ##
rgb = args["rgb"]
## contours ##
c1 = args["contour1"]
c2 = args["contour2"]
c3 = args["contour3"]
c4 = args["contour4"]
##  object list ##
objs = args["objects"]
## ds9 region file ##
region = args["regions"]



### PLOT IMAGE ###
fig = mpl.figure(figsize=(15,15))
gc = aplpy.FITSFigure(img, slices=('x', 'y', 0, 0),
                      figure=fig
                      )
#fix_aplpy_fits(gc)
gc.show_grayscale()
gc.add_grid()
## centre image on coordinates (degrees) ##
gc.recenter(85.4625,-64.3011,radius=0.012) # NGC 2082 centre
gc.tick_labels.set_font(size='x-large')
gc.axis_labels.set_font(size='x-large')
## over plot RGB image ##
gc.show_rgb(rgb)
## set scale bar ##
# gc.add_scalebar()
# gc.scalebar.set_length(0.004)
# gc.scalebar.set_label()

# gc.add_beam()
# gc.beam.set_color('yellow')


### PLOT CONTOURS ###
## contour 1 ##
gc.show_contour(c1, colors='#0571b0', layer='con1',
                levels=[0.00034, 0.0005, 0.0007, 0.0009, 0.0013, 0.0014, 0.0021],
                overlap=True, linewidths=2.5)

## contour 2 ##
gc.show_contour(c2, colors='#92c5de', layer='con2',
                levels=[0.0004, 0.001, 0.0015],
                overlap=True, linewidths=2.25)
## contour 3 ##
gc.show_contour(c3, colors='#f4a582', layer='con3',
                levels=[0.0005, 0.001, 0.0015],
                overlap=True, linewidths=2)
## contour 4 ##
gc.show_contour(c4, colors='#ca0020', layer='con4',
                levels=[0.0004346, 0.00151983,0.003,0.0034],
                overlap=True, linewidths=1.75)


### OBJECT POSITIONS ###
ra, dec = np.loadtxt(objs,unpack=True)
gc.show_markers(ra, dec, edgecolor='magenta', facecolor='none', marker='^', s=150, linewidth=2.5)
#error_radius = 0.000138889
#gc.show_circles(ra, dec, error_radius, edgecolor='magenta',linewidth=4)



### SUBPLOTS ###
gc.show_regions(region) #load region file
#
#  Read fits file.
# hdulist = fits.open(img1)
# hdu = hdulist[0].data
# # Header
# hdr = hdulist[0].header
# hdulist.close()
# # Read original WCS
# wcs = WCS(hdr)
#
# # Some center and box to crop
# xc, yc, xbox, ybox = 3625., 2016., 80., 80.
# # Crop image.
# hdu_crop = Cutout2D(hdu, (xc, yc), (xbox, ybox), wcs=WCS(hdr))
# # Cropped WCS
# wcs_cropped = hdu_crop.wcs
# # Update WCS in header
# hdr.update(wcs_cropped.to_header())
#
# #plot subplot
# gc2 = aplpy.FITSFigure(hdu_crop,figure=fig,subplot=[0.6,0.6,0.15,0.2])
# gc2.show_colorscale()
# gc2.ticks.hide()
# gc2.tick_labels.hide()
# gc2.axis_labels.hide()





### SET TITLE ###
#gc.set_title('MeerKat 900 MHz and ATCA 2.1, 5.5, and 9 GHz Contours on HST Image of NGC 2082')


### SET THEME ###
#gc.set_theme('publication')


### SAVE IMAGE ###
gc.save('NGC2082_ASKAP_ATCA_FINAL.pdf', dpi=300)
gc.save('NGC2082_ASKAP_ATCA_FINAL.eps', dpi=300)
gc.save('NGC2082_ASKAP_ATCA_FINAL.png', dpi=300)


### OPEN IMAGE ###
open_image = Image.open('NGC2082_MK_ATCA_FINAL.png')
open_image.show()