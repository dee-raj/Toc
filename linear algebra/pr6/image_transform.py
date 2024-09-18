import cv2 as c
import numpy as np
import matplotlib.pyplot as plt
# img0=c.imread("vector.jpg")
# img=c.imread("moon.jpg")
img2=c.imread("ambitionless.png")
# print(img)
# print(img0)
print("matrix represemtation\n",img2)

# img=c.cvtColor(img,c.COLOR_BGR2LUV)
img=c.cvtColor(img2,c.COLOR_BGR2LAB)
# img=c.cvtColor(img0,c.COLOR_LBGR2LUV)
# plt.axis('off')
# plt.show()

rows,cols,dim=img.shape
M=np.float32([[1,0,1],[0,1,1],[0,0,1]])
timg=c.warpPerspective(img,M,(cols,rows))
plt.axis('on')
plt.imshow(timg)
plt.title("Color Transformed Image",None,'right',20)
plt.xlabel("X-axis => width",None,10)
plt.ylabel("Y-axis => height",None,10)
# plt.show()
# plt.imsave("transparent_vector.png",timg)
# plt.imsave("MR_knight.png",timg)
plt.imsave("toxic.jpg",img2)