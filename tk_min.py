import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="Hello World!")
label.pack(padx=20, pady=20)
root.after(5000, root.destroy)    # Close the Window after 5 seconds
root.mainloop()


import tkinter
import _tkinter

header = _tkinter.TK_VERSION
lib = tkinter.Tk().getvar('tk_version')

if lib != header:
  print('header version=' + header)
  print('lib version=' + lib)
  exit(1)