from tkinter import *

'''
Entry         输入框
'''

root = Tk()

'''
frame = Frame(root)
frame.pack(padx=10, pady=10)
'''

def add():
    '''
    print(e1.get() is not None)
    print(e2.get())
    '''
    
    if (e1.get() is not None) and (e2.get() is not None):
        # e3.insert(0, int(e1.get()) + int(e2.get()))
        v3.set(int(e1.get()) + int(e2.get()))
    else:
        print("无法计算")
    
    
def test(content):
    return content.isdigit()
        

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

Label(root, text="+").grid(row=0, column=1, padx=10, pady=5)
Label(root, text="=").grid(row=0, column=3, padx=10, pady=5)

testCMD = root.register(test)
e1 = Entry(root, textvariable=v1, validate="key", validatecommand=(testCMD, '%P'))
e1.grid(row=0, column=0, padx=10, pady=5)

e2 = Entry(root, textvariable=v2, validate="key", validatecommand=(testCMD, '%P'))
e2.grid(row=0, column=2, padx=10, pady=5)

e3 = Entry(root, textvariable=v3, state="readonly")
e3.grid(row=0, column=4, padx=10, pady=5)

Button(root, text="计算结果", command=add).grid(row=1, columnspan=5, padx=10, pady=10, sticky=N)

mainloop()