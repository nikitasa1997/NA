import csv
import matplotlib.pyplot as plt
import numpy as np
import os
import tkinter as tk
import tkinter.ttk as ttk

values = [u"Двухточечная первого",
          u"Двухточечная второго",
          u"Трехточечная второго"]

def LW_7(event):
    input_path = './input_6.txt'
    output_path = './output_6.csv'
    try:
        a, b, c, d = float(entry_a.get()), float(entry_b.get()), float(entry_c.get()), float(entry_d.get())
        t, n, k = float(entry_t.get()), int(entry_n.get()), int(entry_k.get())
        initial, boundary = values[:-1].index(combobox_initial.get()), values.index(combobox_boundary.get())
    except ValueError:
        label.configure(text = 'a: float, b: float, c: float, d: float, n: int, k: int, t: float')
        return

    with open(input_path, 'w') as file:
        print(a, b, c, d, t, n, k, initial, boundary, file = file)
    os.system('./LW_7 < ' + input_path + ' > ' + output_path)
    with open(output_path, 'r') as file:
        reader = csv.reader(file)
        x, u = [], ([], [], [], [])
        for line in reader:
            x.append(float(line[0]))
            for i in range(0, 3):
                u[i].append(float(line[i + 1]))

        fig = plt.figure()
        subplot = fig.add_subplot(111, facecolor = '#FFFFFF')
        subplot.plot(x, u[0], color = 'red', lw = 2, label = 'u')
        subplot.plot(x, u[1], color = 'green', lw = 2, label = 'explicit')
        subplot.plot(x, u[2], color = 'blue', lw = 2, label = 'implicit')
        plt.legend()
        plt.show()

master = tk.Tk()

label = tk.Label(master, text = 'Введите коэффициенты:')
label.grid(row = 0, column = 0, columnspan = 8)

tk.Label(master, text='a = ').grid(row = 1, column = 0)
entry_a = tk.Entry(master)
entry_a.grid(row = 1, column = 1)

tk.Label(master, text='b = ').grid(row = 1, column = 2)
entry_b = tk.Entry(master)
entry_b.grid(row = 1, column = 3)

tk.Label(master, text='c = ').grid(row = 1, column = 4)
entry_c = tk.Entry(master)
entry_c.grid(row = 1, column = 5)

tk.Label(master, text='d = ').grid(row = 1, column = 6)
entry_d = tk.Entry(master)
entry_d.grid(row = 1, column = 7)

tk.Label(master, text='T = ').grid(row = 2, column = 0)
entry_t = tk.Entry(master)
entry_t.grid(row = 2, column = 1)

tk.Label(master, text='N = ').grid(row = 2, column = 2)
entry_n = tk.Entry(master)
entry_n.grid(row = 2, column = 3)

tk.Label(master, text='K = ').grid(row = 2, column = 4)
entry_k = tk.Entry(master)
entry_k.grid(row = 2, column = 5)

tk.Label(master, text='начальные: ').grid(row = 3, column = 1)
combobox_initial = ttk.Combobox(master, values = values[:-1])
combobox_initial.set(values[0])
combobox_initial.grid(row = 3, column = 2)

tk.Label(master, text='граничные: ').grid(row = 3, column = 5)
combobox_boundary = ttk.Combobox(master, values = values)
combobox_boundary.set(values[0])
combobox_boundary.grid(row = 3, column = 6)

button_apply = tk.Button(master, text = 'Построить график')
button_apply.grid(row = 4, column = 0, columnspan = 8)

button_apply.bind('<Button-1>', LW_7)
master.bind('<Return>', LW_7)

master.mainloop()