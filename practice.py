# import cv2

# # load an image
# path = r"C:\Users\danie\OneDrive\Desktop\Tensorflow\opencv\assets\chocolate.jpg"
# img = cv2.imread(path, 0) # read images
# resized_img = cv2.resize(img,(0,0), fx=0.5, fy=0.5)
# rotated_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# cv2.imshow("Image", img)
# cv2.imshow("resized image", resized_img)
# cv2.imshow("rotated_image", rotated_img)

# cv2.imwrite("new_img.jpg", resized_img) # save image to a file

# cv2.waitKey(0) # wait infinitely
# cv2.destroyAllWindows() # prevents windows from running in the background 


# EDITING IMAGES

# import cv2
# import random as rd
# image = cv2.imread(r"C:\Users\danie\OneDrive\Desktop\Tensorflow\opencv\assets\pink_ice_cream.jpg")

# # resize image
# scaled_image = cv2.resize(image, (0,0), fx=0.25, fy=0.25)
# cv2.imshow("scaled_image", scaled_image)

# for i in range(100):
#     for j in range(scaled_image.shape[1]):
#         scaled_image[i][j] = [rd.randint(0,120), rd.randint(120,180), rd.randint(180,255)]


# cv2.imshow("distorted_img.jpg", scaled_image)
# cv2.imwrite("distorted_img.png", scaled_image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# USNG THE WEBCAM
import cv2
import numpy as np 


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3)) #width of your frame -> 3
    height = int(cap.get(4)) # height of your frame -> 4


    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180) # top left
    image[height//2:, :width//2] = smaller_frame # bottom left
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180) # top right
    image[height//2:, width//2:] = smaller_frame # bottom right


    # cv2.imshow("camera", frame)00
    cv2.imshow("camera", image)


    if cv2.waitKey(1) == ord("q"):
        break

cap.release() # releases camera resource
cv2.destroyAllWindows()