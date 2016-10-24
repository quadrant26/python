'''
Tk PanedWinow
'''

from tkinter import *

m = PanedWindow(orient=VERTICAL)
m.pack(fill=BOTH, expand=1)

top = Label(m, text="top paned")
m.add(top)

bottom = Label(m, text="bottom pane")
m.add(bottom)

mainloop()
