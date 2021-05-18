from tkinter import *
from tkinter import ttk
import tkinter.font as tf
import pickle
from tkinter import filedialog
import tkinter as tk
import evaluation_metrics

def upload_file():
    selectFile = filedialog.askopenfilename()
    entry1.insert(0, selectFile)

def reg_and_localization():
    if entry1.get():
        label = evaluation_metrics.metri_label(evaluation_metrics.label_classes)
        back_result.delete(1.0,END)
        back_result.insert('insert', label)
    else:
        back_result.delete(1.0,END)
        back_result.insert('insert', "请选择正确的音频数据输入")

root = Tk()
root.title("音频识别与定位系统")
root.geometry('550x400')

ft = tf.Font(family='华文隶书', size=30,weight=tf.BOLD,slant=tf.ITALIC,\
             underline=1,overstrike=1)
inner_title = Label(root, text='欢迎使用音频识别与定位系统', font = ft, compound='center').grid()

frm = tk.Frame(root)
frm.grid(padx='20', pady='30')
btn1 = Button(frm, text='上传文件', command=upload_file)
btn1.grid(row=2, column=0, ipadx='3', ipady='3', padx='10', pady='20')
entry1 = Entry(frm, width='40')
entry1.grid(row=2, column=1) # row=0, column=1
btn2 = Button(frm, text='检测', command=reg_and_localization)
btn2.grid(row=2, column=2, ipadx='3', ipady='3', padx='10', pady='20')

back_result = Text(root, width=55, height=12)
back_result.grid(row=4, column=0)
root.mainloop()
