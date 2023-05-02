from tkinter import *
from tkinter import messagebox
import time
from typing import Self
from library import *
import matplotlib.pyplot as plt
import numpy as np
from tkinter import colorchooser


class LandingPage:
    def __init__(self, parent, title):
        self.parent = parent
        self.settingWindow(title)
        self.settingComponent()

    def settingWindow(self, title):
        # atur ukuran window
        self.parent.geometry('500x300')
        
        # atur title
        self.parent.title(title)
        
    def settingComponent(self):
        main_frame = Frame(self.parent, bd=5)
        main_frame.pack(fill=BOTH, expand=YES)
        # start = partial(SecondPage, main_frame)

        Label(main_frame, text="Selamat Datang Project Sederhana Kami").place(x=130, y=30)
        
        self.btn_start = Button(main_frame, text='Start', command=self.onClickStart, activeforeground='red', width=20, bd=5)
        self.btn_exit = Button(main_frame, text='Exit', command=self.onClickKeluar, activeforeground='red', width=20, bd=5)
        
        self.btn_start.pack(side='left')
        self.btn_exit.pack(side='right')
        
    def onClickKeluar(self, event=None):
        if messagebox.askyesno('Exit', 'Keluar dari program?', parent=self.parent):
            self.parent.destroy()

    def onClickStart(self):
        self.parent.destroy()
        root = Tk()
        app = MenuPage(root)
        root.mainloop()   

class MenuPage:
    def __init__(self, parent):
        self.parent = parent
        self.settingWindow()
        self.settingComponent()

    def settingWindow(self):
        self.parent.geometry('800x300')
        self.parent.resizable(0, 0)
        self.parent.title(':: Menu Akses ::')
        
    def settingComponent(self):
        main_frame = Frame(self.parent, bd=5)
        main_frame.pack(fill=BOTH, expand=YES)
        
        # set back button
        self.imgKembali = PhotoImage(file=r'C:\Users\Rhnas\kuliah\Kelompok D\img\bek.png')
        self.btn_back = Button(main_frame, image=self.imgKembali, command=self.kembali, activeforeground='red', width=18, height=18)
        self.btn_back.place(x=20,)
    
        Label(main_frame, text='Select User Yang Diinginkan').place(x=350, y=40)
        
        
        # Set User
        self.imgUser = PhotoImage(file=r'C:\Users\Rhnas\kuliah\Kelompok D\img\user.png')
        self.btnUser = Button(main_frame, text='User', image=self.imgUser, compound='top', command=self.onClickUser, width=100, height=100)
        # self.btnSquare.pack(side='left', fill=Y)
        self.btnUser.place(x=375, y=100)
        
        
    def onClickUser(self, event=None):
        self.parent.destroy()
        root = Tk()
        root.geometry('800x300')
        root.title(':: Menu User ::')\
            
        # set back button
        self.imgKembali = PhotoImage(file=r'C:\Users\Rhnas\kuliah\Kelompok D\img\bek.png')
        self.btn_back = Button(image=self.imgKembali, command=self.kembali, activeforeground='red', width=18, height=18)
        self.btn_back.place(x=20,)
    
        Label(text='Tentukan Pilihan Kamu').place(x=350, y=40)

        self.imgGaris = PhotoImage(file=r'C:\Users\Rhnas\kuliah\Kelompok D\img\Garis.png')
        self.btnGaris = Button(text='Garis', image=self.imgGaris, compound='top', command=self.onClickGaris, width=100, height=100)
        # self.btnSquare.pack(side='left', fill=Y)
        self.btnGaris.place(x=225, y=100)
        
        self.imgTitik = PhotoImage(file=r'C:\Users\Rhnas\kuliah\Kelompok D\img\Titik.png')
        self.btnTitik = Button(text='Titik', image=self.imgTitik, compound='top', command=self.onClickTitik, width=100, height=100)
        self.btnTitik.place(x=450, y=100)
            
        
    def onClickGaris(self, event=None):
        color=(255,255,255)
        def choose_color():
            nonlocal color
            color = colorchooser.askcolor(title="Choose color")[0]
        root = Tk()
        root.geometry('400x600')
        root.title(':: Menu Garis ::')
        Title = Label(root, text="Tentukan Ukuran dan Ketebalan Sesuai Kebutuhan").place(x=60, y= 20)
        Label(root, text="Warna?").place(x=20, y=100)
        choose_color_button = Button(root, text='Pilih warna', command=choose_color)
        choose_color_button.place(x=20, y=135)
        Label(root, text="Tebal?").place(x=300, y=100)
        tebal_garis = Entry(root, width=10)
        tebal_garis.place(x=300, y=135)
        
        label_x1=Label(root, text="X1")
        label_x1.place(x=20, y=300)
        kolom_x1 = Entry(root, width=10)
        kolom_x1.place(x=20, y=335)
        label_x2=Label(root, text="X2")
        label_x2.place(x=300, y=300)
        kolom_x2 = Entry(root, width=10)
        kolom_x2.place(x=300, y=335)
        
        label_y1=Label(root, text="Y1")
        label_y1.place(x=20, y=400)
        kolom_y1 = Entry(root, width=10)
        kolom_y1.place(x=20, y=435)
        label_y2=Label(root, text="Y2")
        label_y2.place(x=300, y=400)
        kolom_y2 = Entry(root, width=10)
        kolom_y2.place(x=300, y=435)
        
        def submit():
            gambar = np.zeros((1000, 1000, 3), dtype=np.uint8)
            gambar[:,:,:] = 0
            # global label_x1, label_y1, label_x2, label_y2
            # y1 = int(input("Masukkan nilai y1: "))
            # x1 = int(input("Masukkan nilai x1: "))
            # y2 = int(input("Masukkan nilai y2: "))
            # x2 = int(input("Masukkan nilai x2: "))

            vertikal(gambar, int(kolom_y1.get()), int(kolom_x1.get()), int(kolom_y2.get()), int(kolom_x2.get()), int(tebal_garis.get()), int(tebal_garis.get()), *color, *color)
            
        submit = Button(root, text='submit', command=submit).place(x=180, y=500)
    
    def onClickTitik(self, event=None):
        color=(255,255,255)
        def choose_color():
            nonlocal color
            color = colorchooser.askcolor(title="Choose color")[0]
        root = Tk()
        root.geometry('400x600')
        root.title(':: Menu Titik ::')
        Title = Label(root, text="Tentukan Ukuran dan Ketebalan Sesuai Kebutuhan").place(x=60, y= 20)
        Label(root, text="Warna?").place(x=20, y=100)
        choose_color_button = Button(root, text='Pilih warna', command=choose_color)
        choose_color_button.place(x=20, y=135)
        Label(root, text="Jari-Jari").place(x=300, y=100)
        jari = Entry(root, width=10)
        jari.place(x=300, y=135)
        
        Label(root, text="X").place(x=20, y=300)
        kolom_X = Entry(root, width=10)
        kolom_X.place(x=20, y=335)
        Label(root, text="Y").place(x=300, y=300)
        kolom_Y = Entry(root, width=10)
        kolom_Y.place(x=300, y=335)

        
        def proses():
            gambar = np.zeros((1000, 1000, 3), dtype=np.uint8)
            gambar[:,:,:] = 0

            titik(gambar, color, int(jari.get()), int(kolom_X.get()), int(kolom_Y.get()))
            
        submit = Button(root, text='submit', command=proses).place(x=180, y=500)
        
    def kembali(self):
        self.parent.destroy()
        # if messagebox.askyesno('Kembali', 'Yakin ingin kembali?', parent=self.parent):
        #     self.parent.destroy()
        root = Tk()
        app = LandingPage(root, 'Halaman Pertama')
        root.mainloop()

# call main function
if __name__ == '__main__':
    root = Tk()
    app = MenuPage(root)
    root.resizable(0, 0) # resizeable 0 maka tidak dapat di resize kembali (FIX)
    root.mainloop()