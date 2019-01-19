import numpy as np
from skimage import io, color, data, measure

from dct import transMat

threshold = 5

img = data.astronaut()
imgGray = color.rgb2gray(img)

# freqM = transMat.dct2(imgGray)
freqM = transMat.dct2(img)
freqClip = np.where(abs(freqM) > threshold, freqM, 0)

# clip3
imgRec = transMat.idct2(freqClip)
imgRec = np.where(imgRec > 255, 255, imgRec)
imgRec = np.where(imgRec < 0, 0, imgRec)
# clip3 end

imgRec = imgRec.astype(np.uint8)

ratio = np.sum(abs(freqM) > threshold) / 512 / 512 / 3
psnr = measure.compare_psnr(img, imgRec)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
x, y = np.meshgrid(range(512), range(512))
freq = transMat.dct2(imgGray)
reso = 64
#ax.plot_surface(x[0:reso, 0:reso], y[0:reso, 0:reso], freq[0:reso, 0:reso])
#plt.show()

