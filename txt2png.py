import numpy as np
from PIL import Image

table = np.loadtxt('c.txt',skiprows=0,dtype = np.str)
int_table = [[int(j,2) for j in i] for i in table]
[a,b] = np.shape(table)

color = [[j for j in i] for i in int_table]
[x,y] = np.shape(color)

print(np.shape(table))

img = np.zeros([x,y,3],dtype= np.uint8)
for j in range(y):
    for i in range(x):
        img[i][j][0] = color[i][j]
        img[i][j][1] = color[i][j]
        img[i][j][2] = color[i][j]

print(np.shape(img))
data = Image.fromarray(img, 'RGB')
data.save('my.jpg')
data.show()
