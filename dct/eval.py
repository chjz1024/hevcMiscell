import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, data

from dct import transMat

img = data.astronaut()
imgGray = color.rgb2gray(img)

freqM = transMat.dct2(imgGray)
freqClip = np.where(abs(freqM) > 0.01, freqM, 0)
# clip3
imgRec = transMat.idct2(freqClip)
imgRec = np.where(imgRec > 1, 1, imgRec)
imgRec = np.where(imgRec < 0, 0, imgRec)
# clip3 end
