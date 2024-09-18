import cv2
first_img=cv2.imread("background2.jpg")
print("First Image\n")
print(first_img)

second_img=cv2.imread("buddha.jpg")
print("\nsecond Image\n")
print(second_img)

manual_subs=first_img - second_img
cv2.imshow("Manually subtracted ",manual_subs)
print("\n** Manual Subtracted Image **\n")
#print(manual_subs)
subt=cv2.subtract(first_img,second_img)
cv2.imshow("SUBTRCT output1.png",subt)
print("\n** Subtracted Image **\n")
print(subt)

manual_add=second_img + first_img
cv2.imshow("Manually added ",manual_add)
print("\n**Manual ADDED IMAGE **\n")
#print(manual_add)
add_image=cv2.add(second_img,first_img)
cv2.imshow("ADD output2.png",add_image)
print("\n** ADDED IMAGE **\n")
print(add_image)

img=cv2.imread("buddha3.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img=cv2.resize(img,(405,690))
fimg=cv2.multiply(img,7)
cv2.imshow("output_fimg.png",fimg)
print("\n** Multiplied IMAGE **\n")
print(fimg)
