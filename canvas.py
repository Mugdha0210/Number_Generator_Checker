import tkinter
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
from tkinter.ttk import Progressbar
from PIL import Image
import cv2
import numpy as np
from datetime import datetime
from scipy import ndimage
import math
#import tensorflow as tf

class Write_num(object):

    DEFAULT_PEN_SIZE = 10.0
    DEFAULT_COLOUR = 'black'

    def __init__(self):
        self.root = Tk()
        self.root.title("Know your Numbers!")

        #icon = tkinter.PhotoImage(file = "Rocket.png")
        #self.label = tkinter.Label(self.root, image = icon)
        #self.label.grid(row = 0, column = 0)

        self.pen_button = Button(self.root, text = 'pen')
        self.pen_button.grid(row = 0, column = 1)

        self.color_button = Button(self.root, text = 'color', command = self.chooseColor)
        self.color_button.grid(row = 0, column = 2)

        self.clear_button = Button(self.root, text = 'clear', command = self.clear)
        self.clear_button.grid(row = 0, column = 3)

        self.check_button = Button(self.root, text = 'check', command = self.preprocess)
        self.check_button.grid(row = 0, column = 4)

        self.img_filename = "hand_num"

        style = ttk.Style()
        style.theme_use('default')
        style.configure("black.Horizontal.TProgressbar", background = 'blue')
        self.bar = Progressbar(self.root, length = 200, style ='black.Horizontal.TProgressbar')
        self.bar['value'] = 70
        self.bar.grid(row = 2, column = 0)

        self.page = Canvas(self.root, bg = 'white', width = 600, height = 600)
        self.page.grid(row = 1, columnspan = 5)

        self.setup()
        self.root.mainloop()

    def setup(self) :
        self.x1 = None
        self.y1 = None
        self.line_width = self.DEFAULT_PEN_SIZE
        self.color = self.DEFAULT_COLOUR
        self.clear_on = False
        self.active_button = self.pen_button
        self.page.bind('<B1-Motion>', self.write)       #button-1 is left
        self.page.bind('<ButtonRelease-1>', self.reset)

    def write(self, event):
        self.line_width = self.DEFAULT_PEN_SIZE
        write_color = self.color
        if self.x1 and self.y1:
            self.page.create_line(self.x1, self.y1, event.x, event.y,
                               width = self.line_width, fill = write_color,
                               capstyle = ROUND, smooth = TRUE, splinesteps = 36)
        self.x1 = event.x
        self.y1 = event.y

    def chooseColor(self):
        self.clear_on = False
        self.color = askcolor(color = self.color)[1]

    def clear(self):
        self.page.delete("all")

    def preprocess(self):
        img = self.page.postscript(file = self.img_filename + '.eps')
        img = Image.open(self.img_filename + '.eps')
        #img = img.convert('L')
        img.save(self.img_filename + '.png', 'png')
        img = cv2.imread(self.img_filename + '.png', cv2.IMREAD_GRAYSCALE)     #grayscaling
        img = cv2.resize(255 - img, (28, 28), interpolation = cv2.INTER_AREA)      #invert and shrink to 28*28
        #arr_255 = np.full((28, 28), 255)
        #img = arr_255 - img     #invert
        (thresh, img) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)   #thresholding

        while np.sum(img[0]) == 0:     #cropping
            img = img[1:]
        while np.sum(img[:,0]) == 0:
            img = np.delete(img,0,1)
        while np.sum(img[-1]) == 0:
            img = img[:-1]
        while np.sum(img[:,-1]) == 0:
            img = np.delete(img,-1,1)
        rows,cols = img.shape

        if rows > cols:         #fit to 20*20, adjust for aspect ratio
            factor = 20.0/rows
            rows = 20
            cols = int(round(cols*factor))
            img = cv2.resize(img, (cols,rows))
        else:
            factor = 20.0/cols
            cols = 20
            rows = int(round(rows*factor))
            img = cv2.resize(img, (cols, rows))

        colsPadding = (int(math.ceil((28-cols)/2.0)),int(math.floor((28-cols)/2.0)))    #padding to get 28*28
        rowsPadding = (int(math.ceil((28-rows)/2.0)),int(math.floor((28-rows)/2.0)))
        img = np.lib.pad(img,(rowsPadding,colsPadding),'constant')

        shift_x, shift_y = self.getBestShift(img)        #centering in 28*28
        shifted = self.shift(img, shift_x, shift_y)
        img = shifted

        cv2.imwrite(self.img_filename + str(datetime.now()) + '.png', img)
        img = img.flatten() / 255.0
        np.savetxt("imgdata" + str(datetime.now()) + ".csv", img, delimiter = ",")
        #shrunk = np.array(shrunk)
        #Image.fromarray(shrunk).save(self.img_filename + '.png')

        #Titles =["Original", "Shrunk"]
        #images =[image, shrunk]
        #count = 2
        #for i in range(count):
        #    plt.subplot(2, 2, i + 1)
        #    plt.title(Titles[i])
        #    plt.imshow(images[i])
        #plt.show()

    def getBestShift(self, img):      #get adjustment for center of mass
        cy,cx = ndimage.measurements.center_of_mass(img)
        rows,cols = img.shape
        shift_x = np.round(cols/2.0-cx).astype(int)
        shift_y = np.round(rows/2.0-cy).astype(int)
        return shift_x,shift_y

    def shift(self, img, sx, sy):     #shift according to center of mass
        rows, cols = img.shape
        M = np.float32([[1, 0, sx], [0, 1, sy]])
        shifted = cv2.warpAffine(img, M, (cols, rows))
        return shifted

    def reset(self, event):
        self.x1, self.y1 = None, None


if __name__ == '__main__':
    Write_num()
