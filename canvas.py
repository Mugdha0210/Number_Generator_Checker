import tkinter
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
from tkinter.ttk import Progressbar
from PIL import Image
import numpy

class Write_num(object):

    DEFAULT_PEN_SIZE = 10.0
    DEFAULT_COLOUR = 'black'

    def __init__(self):
        self.root = Tk()
        self.root.title("Know your Numbers!")

        icon = tkinter.PhotoImage(file = "Rocket.png")
        self.label = tkinter.Label(self.root, image = icon)
        self.label.grid(row = 0, column = 0)

        self.pen_button = Button(self.root, text = 'pen')
        self.pen_button.grid(row = 0, column = 1)

        self.color_button = Button(self.root, text = 'color', command = self.chooseColor)
        self.color_button.grid(row = 0, column = 2)

        self.clear_button = Button(self.root, text = 'clear', command = self.clear)
        self.clear_button.grid(row = 0, column = 3)

        self.check_button = Button(self.root, text = 'check', command = self.saveImage)
        self.check_button.grid(row = 0, column = 4)

        self.img_filename = "hand_num"

        style = ttk.Style()
        style.theme_use('default')
        style.configure("black.Horizontal.TProgressbar", background = 'blue')
        self.bar = Progressbar(self.root, length=200, style='black.Horizontal.TProgressbar')
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

    def saveImage(self):
        self.page.postscript(file = self.img_filename + '.eps')
        img = Image.open(self.img_filename + '.eps')
        img.save(self.img_filename + '.jpeg', 'jpeg')
        img = img.resize((28, 28))
        img = img.convert('L')
        img = numpy.array(img)
        Image.fromarray(img).save(self.img_filename + '.jpeg')

    def reset(self, event):
        self.x1, self.y1 = None, None


if __name__ == '__main__':
    Write_num()
