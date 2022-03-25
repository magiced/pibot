import tkinter as tk

"""
# TODO
* [ ] rewrite as library
* [ ] create command methods
* [ ] place in wider frame, several times
"""

def fwd_button_clicked():
    print('')

root = tk.Tk()
frame_d_pad = tk.Frame(root)

frame_d_pad.columnconfigure([0,1,2],minsize=30)
frame_d_pad.rowconfigure([0,1,2],minsize=30)

btn_fwd = tk.Button(frame_d_pad,text='^')
btn_rev = tk.Button(frame_d_pad,text='V')
btn_left = tk.Button(frame_d_pad,text='<')
btn_right = tk.Button(frame_d_pad,text='>')

# 3x3 grid

btn_fwd.grid(row=0, column=1)
btn_rev.grid(row=2, column=1)
btn_left.grid(row=1, column=0)
btn_right.grid(row=1, column=2)

test_label = tk.Label(root, text='d-pad')
test_label.pack()

frame_d_pad.pack()

root.mainloop()