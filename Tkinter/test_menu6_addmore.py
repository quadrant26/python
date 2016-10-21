from tkinter import *

root = Tk()

OPTIONS = [
    "CSI",
    "MIAMI",
    "Vages",
    "NEWYWORK",
    "LA"
    ]

variable = StringVar()
variable.set(OPTIONS[0])

w = OptionMenu(root, variable, *OPTIONS)  # 自动拆开 一个 Set
w.pack()

root.mainloop()