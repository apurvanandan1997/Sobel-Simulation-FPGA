from matplotlib.image import imread
import numpy as np

img = imread('123.jpg')
img = np.array(list(img))
pad = 1;
[x,y,z] = np.shape(img)
im = np.zeros([x+2*pad,y+2*pad],dtype=np.uint8)
print(np.shape(img))
print(np.shape(im))

for i in range(x):
    for j in range(y):
            im[i + pad][j + pad] = img[i][j][0]/3+img[i][j][1]/3+img[i][j][2]/3
file = open('a.txt','w')
for i in range(x+2*pad):
    for j in range(y+2*pad):
            #out[i][j][k] =
        file.write( '{0:08b}'.format(im[i][j])+' ')
    #file.write( '{0:08b}'.format(im[i][y+2*pad-1][0])+' '+'{0:08b}'.format(im[i][y+2*pad-1][1])+' '+'{0:08b}'.format(im[i][y+2*pad-1][2])+'\n\n')
    file.write('\n')
file.close()
