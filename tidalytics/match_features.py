from helpers import *

# get features of input image
input_img_path = "input path here"
img = read_color_image(input_img_path)
orb = cv2.ORB_create()
kp, des = get_features(img, orb)

# get features of model
model_img_path = "model path here"



