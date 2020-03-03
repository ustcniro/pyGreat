import tkinter as tk

window = tk.Tk()
window.title = ('my window')
window.geometry('200x200')

canvas = tk.Canvas(window, bg='blue', height=100, width=200)
# 在canvas（画布）上放张图片
# image_file = tk.PhotoImage(file='ins.gif')
# image = canvas.create_image(0, 0, anchor='nw', image=image_file)    # anchor�ο�����ͼ���ĸ��ǣ�n s w e

x0, y0, x1, y1 = 50, 50, 80, 80
# canvas的坐标是以左上角为（0，0），往右为x正半轴，往下为y正半轴
line = canvas.create_line(x0, y0, x1, y1)   # yi根黑线
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')    # 一个红色的圆形
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)    # 一个扇形，角度起始
rect = canvas.create_rectangle(100, 30, 100+50, 30+20)

print(canvas.coords(rect))
print(type(canvas.coords(rect)))

canvas.pack()

def moveit():
    canvas.move(rect, 0, 2) # 往右，下移动

b = tk.Button(window, text='move', command=moveit).pack()

window.mainloop()