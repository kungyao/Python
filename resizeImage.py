import numpy as np
import cv2
import os

divide_scale = 4

f = open("./pano.txt")
for line in f.readlines():
    line = line.splitlines()[0]
    img = cv2.imread(line)
    
    h = img.shape[0]
    w = img.shape[1]
    
    img = cv2.resize(img, (int(w / divide_scale), int(h / divide_scale)))
    cv2.imwrite(line, img)
f.close()