from PIL import Image, ImageTk
from tkinter import Tk, Canvas, Frame, BOTH, NW, ALL, Button,GROOVE,StringVar,END,PhotoImage
from tkinter.ttk import *
from tkinter.font import Font
import tkinter as tk
import os
import Find
HEIGHT=768
POSX=300
POSY=340
WIDTH=1366
# CREATE FLASH SCREEN
class Result(Canvas):
    def __init__(self,parent,rank=[],file_path=[]):
        Canvas.__init__(self,parent)
        self.parent=parent
        self.rank=rank
        self.file_path=file_path
        self.Flash_Screen()
        self.pack()
    def Flash_Screen(self):
        self.pack(fill=BOTH, expand=1)
        button=[0 for x in range(len(self.rank))]
        self.img = Image.open("bg2.png")
        self.place = ImageTk.PhotoImage(self.img)
        canvas = Canvas(self, width=self.img.size[0] + 10, height=self.img.size[1] + 20)
        canvas.create_image(0, 0, anchor=NW, image=self.place)
        canvas.pack()
        myFont = Font(family="Choco Cooky", size=52)
        canvas.create_text(650, 100,fill="White", font=myFont,text="Ranking")
        for i in range(5):
            button[i] = tk.Button(self, relief=GROOVE,text=self.file_path[self.rank[i]],width=100,height=3,command=lambda t=i:self.Show(t))
            button[i].pack()
            button[i].place(x=POSX+30,y=POSY-120+100*i)
        button1=tk.Button(self, relief=GROOVE,text="Back",width=7,height=3,command= self.Back)
        button1.pack()
        button1.place(x=25, y=25)
    def Back(self):
        self.destroy()
        Screen(self.parent)
    def Show(self,t=0):
        os.system('cls')
        file = open(path_file[t])
        temp1 = file.read()
        print(temp1)
        file.close()
class Screen(Canvas):
    def __init__(self,parent):
        Canvas.__init__(self,parent)
        self.parent=parent
        self.Flash_Screen()
        self.pack()
    def Flash_Screen(self):
        ''' data: string after split(" ")
            word_dict: sum of words of all document
            data_dict: data after dict.fromkeys()
            main_dict: dict of main_data
            '''
        def Move():
            p = Player1.get()
            self.main_data=p.split(" ")
            self.main_dict=dict.fromkeys(word_dict, 0)
            for word in self.main_data:
                check=self.main_dict.get(word)
                if check!=None:
                    self.main_dict[word]+=1
            self.array_distance=Find.Distance(word_dict, data_dict, self.main_dict)
            self.place=Find.Find_Min(self.array_distance)
            self.destroy()
            Result(self.parent,self.place,path_file)
        self.pack(fill=BOTH, expand=1)
        self.img = Image.open("bg2.png")
        self.place = ImageTk.PhotoImage(self.img)
        canvas = Canvas(self, width=self.img.size[0] + 10, height=self.img.size[1] + 20)
        canvas.create_image(0, 0, anchor=NW, image=self.place)
        canvas.pack()
        myFont = Font(family="Choco Cooky", size=24)
        Player1 = tk.Entry(self,width=40,font=myFont)
        Player1.pack()
        Player1.place(x=POSX,y=POSY)
        button = tk.Button(self, relief=GROOVE,text='Find',width=7,height=3,command=Move)
        button.pack()
        button.place(x=POSX+720,y=POSY-5)
# Delete screen and move to MENU
class GUI(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent=parent
        self.parent.title("Search Engine")
        self.board=Screen(parent)
        self.pack()
data,word_dict,path_file=Find.Load_Data()
data_dict=Find.Save_Value(data,word_dict)
data_dict,sum_word=Find.Calculate(data_dict, word_dict)
root =Tk()
text=tk.Text(root)
root.geometry(("%dx%d+0+0")%(WIDTH,HEIGHT))
ex = GUI(root)
root.mainloop()
