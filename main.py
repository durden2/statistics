from PIL import Image
import numpy
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

im = Image.open('1.jpg', 'r')
width, height = im.size
pixel_values = list(im.getdata())
pixel_values = numpy.array(pixel_values).reshape((width, height))


im2 = Image.open('2.jpg', 'r')
width2, height2 = im.size
pixel_values2 = list(im2.getdata())
pixel_values2 = numpy.array(pixel_values2).reshape((width2, height2))

tolerance = 3
difference = [[]]

W = []
H = []
D = []

def lookForReference(pixelValue, w, h):
    distance = 1000;
    for i in range(w, width):
        for j in range(h, height):
            if (pixel_values2[i][j] in range(pixelValue - tolerance, pixelValue + tolerance)):
                val = (w - i)**2 + (h - j)**2
                newDistance = math.sqrt(val)
                if (newDistance < distance):
                    distance = newDistance

    #difference.append([w, h, distance]);
    W.append(w);
    H.append(h);
    if (distance != 1000):
        D.append(distance)
    else:
        D.append(0)

for i in range(0, width):
    for j in range(0, height):
        lookForReference(pixel_values[i][j], i, j)


print(D)
#
# plt.axis([0, width, 0, height])
# plt.scatter(W, D)
# plt.ylabel('some numbers')
# plt.show()

W = numpy.asarray(W)
H = numpy.asarray(H)
D = numpy.asarray(D)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(W, H, D)
plt.show()