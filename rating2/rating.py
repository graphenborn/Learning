import tkinter as tk
from turtle import color

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Создаем окно
        canv = tk.Canvas(self, width=500, height=500)

        # Рисуем систему координат
        canv.create_line(15,160,15,10, width=2, arrow=tk.LAST, fill="red")
        canv.create_line(10,150,150,150, width=2, arrow=tk.LAST, fill="red")
        canv.create_text(20,170, text="(0; 0)", fill="red", font=("Helvectica", "10"))
        canv.create_text(25, 10, text="y", fill="red", font=("Helvectica", "10"))
        canv.create_text(150, 160, text="x", fill="red", font=("Helvectica", "10"))

        # Вводим переменные
        ID = "70174464"
        FIO = "Серебряков Юрий Владимирович"
        y0 = 150
        x0 = 10
        color = "blue"

        # Считаем координаты
        x1 = int(ID[2:4])
        x2 = int(ID[4:6])
        x3 = int(ID[6:8])
        yID = str(int(ID)/3)
        y1 = int(yID[2:4])
        y2 = int(yID[4:6])
        y3 = int(yID[6:8])
        var = tk.IntVar()
  

        # Рисуем треугольник
        canv.create_polygon([x0+x1,y0-y1], [x0+x2,y0-y2], [x0+x3,y0-y3], fill=color)

        colFrame = tk.Frame(self)
        colFrame.pack()

        col1 = tk.Radiobutton(colFrame, text = "Blue", value=1, variable=var)
        col2 = tk.Radiobutton(colFrame, text = "Red", value=2, variable=var)
        col3 = tk.Radiobutton(colFrame, text = "Green", value=3, variable=var)
        col4 = tk.Radiobutton(colFrame, text = "Yellow", value=4, variable=var)
        col5 = tk.Radiobutton(colFrame, text = "Orange", value=5, variable=var)
        col6 = tk.Radiobutton(colFrame, text = "Pink", value=6, variable=var)

        col1.pack()
        col2.pack()
        col3.pack()
        col4.pack()
        col5.pack()
        col6.pack()

        canv.pack()


aboba = App()
aboba.mainloop()
