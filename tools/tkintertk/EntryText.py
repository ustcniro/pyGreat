# coding=gbk
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')
e = tk.Entry(window, show='*' )   # tk.Entry（）输入框，show='*',以*代替输入, = None,原始显示，不会被代替
e.pack()

def insert_point():
    var = e.get()
    t.insert('insert', var)

def insert_end():
    var = e.get()
    t.insert('end', var)
    # t.insert(1.1, var)  # 在（1，1）位置插入（索引从0开始）

b1 = tk.Button(window, text='inster point', width=15, height=2, command=insert_point)
b1.pack()    # 放置Button
b2 = tk.Button(window, text='inster end', width=15, height=2, command=insert_end)
b2.pack()    # 放置Button

t = tk.Text(window, height=2)
t.pack()

window.mainloop()   # 主循环，不停地刷新？