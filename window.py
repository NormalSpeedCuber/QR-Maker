from tkinter import *
from tkinter import ttk
import qrcode

def get_data():
    string = data.get()
    return string

def make_qr():
    image = qrcode.make(get_data())
    image.save("qrcode.png")

root = Tk()
root.title("QR Maker")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
make = ttk.Button(frm, text="Make", command=make_qr).grid(column=1, row=1)
data = ttk.Entry(frm)

data.grid(column=0, row=1)

root.mainloop()