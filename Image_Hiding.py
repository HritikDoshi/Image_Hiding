import cv2
import numpy as np
og_img = cv2.imread(r'a.jpeg')
a_img = cv2.imread(r'WIN_20190921_20_52_35_Pro.jpg',-1)
blended_img=cv2.addWeighted(og_img,0.7,a_img,0.3,0)

cv2.imshow('transform',blended_img)
cv2.waitKey(0)
cv2.destroyAllWindows()