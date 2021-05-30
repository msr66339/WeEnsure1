import tkinter
from tkinter import *
import pygame, random
from PIL import Image,ImageTk
x=00

class alarm(Tk):
    def __init__(self):
        super().__init__()
        global x
        y = "300x350+" + str(x) + "+200"
        self.geometry(y)
        x = x + 200
        if (x == 1000):
            x = 0
        self.previous=0
        self.x=self.previous+500

        #
        self.title("new window")
        self.file = 'audio.mp3'
        self.overrideredirect(1)
        self.player=pygame.mixer
        self.player.init()
        self.player.music.load(self.file)
        self.player.music.play()
        #
        btn = Button(self,
        text="Stop Alarm",
               command=self.close)
        btn2 = Button(self,
                     text="Ignore",
                     command=self.ignore)





        logo=ImageTk.PhotoImage(master=self, width=20, height=20,file="warning.png")
        mylabel=Label(self,image=logo)
        mylabel.pack()


        label=Label(self,text="Warning")
        label.pack()
        btn.pack(pady=10)
        btn2.pack(pady=10)
        self.mainloop()






    def close(self):
        self.player.music.stop()
        self.withdraw()

    def ignore(self):
        self.player.music.stop()
        self.withdraw()

    #def __init__(self):
      #  self.label = Label(self,text="This is the Alarm Stub")
       # self.label.pack(pady=10)
        # a button widget which will open a
        # new window on button click
      #  self.btn = Button(self,text="Raise Alarm",command=self.openNewWindow)
       # self.btn.pack(pady=10)