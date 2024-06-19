import cv2
from cvzone.ClassificationModule import Classifier
from tkinter import filedialog
from tkinter import Tk
import os
import numpy as np
Tk().withdraw()

mc=Classifier('keras_model.h5','labels.txt')
class_names = open("labels.txt", "r").readlines()
def main():
    if True:
        filename = filedialog.askopenfilename()
        
        img=cv2.imread(filename)
        p=mc.getPrediction(img)
        
        # Print prediction and confidence score
        if p[1]==0:
            print(p)
            print('Weather Classified...')
            print('CLOUD')
        elif p[1]==1:
            print(p)
            print('Weather Classified...')
            print('RAIN')
        elif p[1]==2:
            print(p)
            print('Weather Classified...')
            print('SHINE')
        elif p[1]==3:
            print(p)
            print('Weather Classified...')
            print('SUN_RISE')
        cv2.imshow("out",img)
        cv2.waitKey(5)
        #cv2.destroyAllWindows()
def choose_file():
    filename = filedialog.askopenfilename(
            title="Choose a file",
            filetypes=(("All Files", "*.*"),
                        ("Text files", "*.txt"))
            )
    return filename

def choose_directory():
    dirname = filedialog.askdirectory(title="Choose directory.")
    return dirname
def open():
    file = choose_file()
    os.startfile(file)
    img=cv2.imread('cloudy8.jpg')
    prediction = mc.getPrediction(img)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    main()
while (str(input("continue  press [ y ] : "))=='y'):
    main()
else:
    exit()
