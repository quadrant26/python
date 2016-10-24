'''
Tk PanedWinow
'''

from tkinter import *

m1 = PanedWindow(showhandle=True, sashrelief=SUNKEN, handlesize=80)
m1.pack(fill=BOTH, expand=1)
 
left = Label(m1, text="left pane")
m1.add(left)

m2 = PanedWindow(orient=VERTICAL, showhandle=True, sashrelief=SUNKEN)
m1.add(m2)

top = Label(m2, text="right top pane")
m2.add(top)

bottom = Label(m2, text="right bottom pane")
m2.add(bottom)



mainloop()
