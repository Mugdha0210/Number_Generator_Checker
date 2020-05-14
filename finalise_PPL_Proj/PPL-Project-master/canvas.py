import tkinter
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
from tkinter.ttk import Progressbar
import tkinter.font as tkFont
from PIL import Image
import cv2
import numpy as np
from datetime import datetime
from scipy import ndimage
import math
import time
import numberGeneratorChecker
import convtodeva
import test
#import model
#import tensorflow as tf

class Write_num(object):

    DEFAULT_PEN_SIZE = 10.0
    DEFAULT_COLOUR = 'black'

    def __init__(self):
        self.root = Tk()
        self.root.title("Know your Numbers!")
        self.root.geometry('{}x{}'.format(900, 750))

        #self.label = tkinter.Label(self.root, image = icon)
        #self.label.grid(row = 0, column = 0)

        self.page = Canvas(self.root, bg = 'white', width = 600, height = 600)
        self.page.grid(row = 0, columnspan = 5)
        self.page.config(state = DISABLED)

        new_icon = tkinter.PhotoImage(file = r"./Icons/Rocket.png")
        self.new_button = Button(self.root, image = new_icon, bg = "yellow", command = self.allowDrawing)
        self.new_button.configure(width = 600, height = 600, relief = RAISED)
        self.new_button_window = self.page.create_window(10, 10, window = self.new_button)
        self.new_button.grid(row = 0, columnspan = 5, ipady = 20)

        self.style_bar = ttk.Style()
        self.style_bar.theme_use('default')
        self.style_bar.configure("black.Vertical.TProgressbar", background = 'red', thickness = 50, mode = "percent")
        self.progress_var = tkinter.IntVar()
        self.bar = Progressbar(self.root, length = 600, style = 'black.Vertical.TProgressbar', mode = 'determinate', var = self.progress_var)
        self.bar['orient'] = "vertical"
        self.bar.grid(row = 0, column = 6)
        #self.bar["value"] = 0

        customFont = tkFont.Font(family = 'Noto Sans', size = 50)
        self.display = Text(self.root, font = customFont, foreground = "purple", spacing1 = 10, spacing2 = 10, spacing3 = 10, height = 5)
        self.display.grid(row = 0, column = 7)
        self.display.tag_add("center", "1.0")
        self.display.config(state = DISABLED)

        palette_icon = PhotoImage(file = r"./Icons/palette.png")
        self.color_button = Button(self.root, image = palette_icon, bg = 'white', command = self.chooseColor)
        self.color_button.icon = palette_icon
        self.color_button.grid(row = 1, column = 0, ipadx = 15, ipady = 15, padx = 10, pady = 10)

        eraser_icon = PhotoImage(file = r"./Icons/eraser.png")
        self.clear_button = Button(self.root, image = eraser_icon, bg = 'white', command = self.clear)
        self.color_button.icon = eraser_icon
        self.clear_button.grid(row = 1, column = 2, ipadx = 15, ipady = 15, padx = 10, pady = 10)

        check_icon = PhotoImage(file = r"./Icons/check.png")
        self.check_button = Button(self.root, image = check_icon, bg = 'white', command = self.preprocess)
        self.color_button.icon = check_icon
        self.check_button.grid(row = 1, column = 4, ipadx = 15, ipady = 15, padx = 10, pady = 10)

        self.img_filename = "hand_num"
        #call model
        
        self.model = test.loadModel()
        print("______Model loaded_________")
        
        self.setup()
        self.root.mainloop()

    def setup(self) :
        self.x1 = None
        self.y1 = None
        self.line_width = self.DEFAULT_PEN_SIZE
        self.color = self.DEFAULT_COLOUR
        self.clear_on = False
        self.page.bind('<B1-Motion>', self.write)       #button-1 is left click
        self.page.bind('<ButtonRelease-1>', self.penup)

    def allowDrawing(self) :
        self.new_button.grid_remove()
        self.new_button["state"] = DISABLED
        self.givenNum = numberGeneratorChecker.obtainNumber()
        self.page.config(state = NORMAL)


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
        self.page.config(state = DISABLED)
        img = self.page.postscript(file = self.img_filename + '.eps')
        img = Image.open(self.img_filename + '.eps')
        img.save(self.img_filename + '.png', 'png')
        img = cv2.imread(self.img_filename + '.png', cv2.IMREAD_GRAYSCALE)     #grayscaling
        img = cv2.resize(255 - img, (28, 28), interpolation = cv2.INTER_AREA)      #invert and shrink to 28*28
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

        cv2.imwrite(self.img_filename + '.png', img)
        img = img.flatten() / 255.0
        #name = "imgdata" + str(datetime.now()) + ".csv"
        np.savetxt("imgdata.csv", img, delimiter = ",")
        #pass csv to Mugdha
        arr = test.testPNG(self.model, "imgdata.csv", self.givenNum)
        self.modelAccuracy = arr[0]
        if self.modelAccuracy == 0:
            self.accuracy = 0
        if self.modelAccuracy == 1:
            numProb = arr[1]
            numProb = int(numProb * 100)
            #will return accuracy
            self.accuracy = numProb
        self.showScore()
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

    def showScore(self) :
        k = 0
        if self.accuracy < 50 :
            score = 1
        else :
            (quo, rem) = divmod(self.accuracy, 10)
            if rem == 0 :
                score = self.accuracy // 10
            else :
                score = (self.accuracy // 10) + 1
        for i in range(0, score + 1):
            self.progress_var.set(k)
            #print("STEP", i)
            k += 10
            time.sleep(0.1)
            if self.bar["value"] > 70 :
                self.style_bar.configure("black.Vertical.TProgressbar", background = 'lime green', thickness = 50, mode = "percent")
            elif self.bar["value"] > 40 :
                self.style_bar.configure("black.Vertical.TProgressbar", background = 'yellow', thickness = 50, mode = "percent")
            else :
                self.style_bar.configure("black.Vertical.TProgressbar", background = 'red', thickness = 50, mode = "percent")
            self.bar.update_idletasks()
        #print(self.bar["value"])
        if self.bar["value"] > 40 :
            self.devauni, self.numName = convtodeva.obtaindeva(self.givenNum)
            self.displayNum()
        else :
            print("WRONG")

    def displayNum(self) :
        self.display.config(state = NORMAL)
        #devauni = b'\u096A'
        self.display.insert("1.0", self.devauni.decode('unicode-escape'))
        
        #num_name = "\nfour"
        self.display.insert(END, self.numName)
        self.display.config(state = DISABLED)
        self.root.after(7000, self.reset())
        #time.sleep(4)
        #self.reset()

    def penup(self, event) :
        self.x1, self.y1 = None, None

    def reset(self) :
        print("resetting")
        #self.display.config(state = NORMAL)
        self.progress_var.set(0)
        self.bar.update_idletasks()
        self.page.config(state = NORMAL)
        self.page.delete("all")
        self.page.config(state = DISABLED)
        self.display.config(state = NORMAL)
        self.display.delete(1.0, END)
        self.display.config(state = DISABLED)
        self.new_button.config(state = NORMAL)
        self.new_button.grid()
        print(self.bar['value'])


if __name__ == '__main__':
    Write_num()
