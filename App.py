import tkinter as tk
from tkinter import filedialog
import os
import sys
path = 'D:\KULIAH\2022\ORBIT\FINALPROAPP\Traffic Sign Detection'
sys.path.append(path)

root = tk.Tk()
root.title('Real Time Traffic Sign Detector')
#root.geometry('500x500')
height = 100
width = 300


label= tk.Label(root, text="Real Time Traffic Sign Detector")
label.pack()

def run():
    os.system('python Test.py')

canvas = tk.Canvas(root,height=height, width=width)
canvas.pack()

frame = tk.Frame(root)
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

run = tk.Button(root, text="Detect", padx=10,
                     pady=5, fg="black", bg="white", command=run)
run.pack(padx=50, pady=50)


root.mainloop()