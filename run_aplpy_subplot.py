import aplpy
import sys
from PIL import Image
import matplotlib.pyplot as mpl


def fix_aplpy_fits(aplpy_obj, dropaxis=2):
    """This removes the degenerated dimensions in APLpy 2.X...
    The input must be the object returned by aplpy.FITSFigure().
    `dropaxis` is the index where to start dropping the axis (by default it assumes the 3rd,4th place).
    """
    temp_wcs = aplpy_obj._wcs.dropaxis(dropaxis)
    temp_wcs = temp_wcs.dropaxis(dropaxis)
    aplpy_obj._wcs = temp_wcs


### READ IN IMAGES ###
img1 = sys.argv[1]
con1 = sys.argv[2]
con2 = sys.argv[3]
con3 = sys.argv[4]
con4 = sys.argv[5]
objs = sys.argv[6] # object list
region = sys.argv[7] # ds9 region file
img2 = sys.argv[8] # rgb image

### PLOT IMAGE ###
fig = mpl.figure(figsize=(15,15))
gc = aplpy.FITSFigure(img1, slices=('x', 'y', 0, 0), figure=fig)
#fix_aplpy_fits(gc)
gc.show_grayscale()
#centre image on coordinates (degrees)
#gc.recenter(85.4552415,-64.3038121,radius=0.001) # NGC 2082 compact source
gc.recenter(85.4662921,-64.3003553,radius=0.0013) # NGC 2082 compact source opposite
gc.ticks.hide()
gc.tick_labels.hide()
gc.axis_labels.hide()
# over plot RGB image
gc.show_rgb(img2)



### PLOT CONTOURS ###
# contour 1
gc.show_contour(con1, colors='#0571b0', layer='con1',
                levels=[0.00034, 0.0005, 0.0007, 0.0009, 0.0013, 0.0014, 0.0021],
                overlap=True, linewidths=5)
# contour 2
gc.show_contour(con2, colors='#92c5de', layer='con2',
                levels=[0.0004, 0.001, 0.0015],
                overlap=True, linewidths=5)
# contour 3
gc.show_contour(con3, colors='#f4a582', layer='con32',
                levels=[0.0005, 0.001, 0.0015],
                overlap=True, linewidths=5)
# contour 4
gc.show_contour(con4, colors='#ca0020', layer='con42',
                levels=[0.0004346, 0.00151983,0.003,0.0034],
                overlap=True, linewidths=5)


### SET THEME ###
#gc.set_theme('publication')


### SAVE IMAGE ###
#gc.save('NGC2082_ASKAP_ATCA_sub.pdf', dpi=300)
#gc.save('NGC2082_ASKAP_ATCA_sub.png', dpi=300)
#gc.save('NGC2082_ASKAP_ATCA_sub.eps', dpi=300)
gc.save('NGC2082_ASKAP_ATCA_sub_opposite.pdf', dpi=300)
gc.save('NGC2082_ASKAP_ATCA_sub_opposite.png', dpi=300)
gc.save('NGC2082_ASKAP_ATCA_sub_opposite.eps', dpi=300)



### OPEN IMAGE ###
#open_image = Image.open('NGC2082_ASKAP_ATCA_sub.png')
#open_image.show()