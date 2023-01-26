import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import solver


def drawplot(data):

    dataframe = pd.DataFrame(data)

    figure = Figure(figsize=(6, 6), dpi=100)
    ax = figure.add_subplot(111)
    line = FigureCanvasTkAgg(figure, plotFrame)
    line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    dataframe = dataframe[['xvalues', 'yvalues']].groupby('xvalues').sum()
    dataframe.plot(kind='line', legend=False, ax=ax, color='b', fontsize=10)
    ax.set_title('Calculated function:')


def changeplot():

    n = int(nentry.get())
    acc = int(accentry.get())

    if n > 100:
        n = 100
        nentry.delete(0, (len(nentry.get())))
        nentry.insert(0, str(n))

    if n < 3:
        n = 3
        nentry.delete(0, (len(nentry.get())))
        nentry.insert(0, str(n))

    if acc > 500:
        acc = 500
        accentry.delete(0, (len(accentry.get())))
        accentry.insert(0, str(acc))

    if acc < 10:
        acc = 10
        accentry.delete(0, (len(accentry.get())))
        accentry.insert(0, str(acc))

    for widget in plotFrame.winfo_children():
        widget.destroy()

    newdata = solver.solve(n, acc)
    drawplot(newdata)


if __name__ == "__main__":

    root = tk.Tk()
    root.geometry('850x600')

    # leftframe code
    leftFrame = tk.Frame()
    leftFrame.pack(side=tk.LEFT)

    titlelabel1 = tk.Label(leftFrame, text='FINITE', font=("Arial", 30))
    titlelabel2 = tk.Label(leftFrame, text='ELEMENT', font=("Arial", 30))
    titlelabel3 = tk.Label(leftFrame, text='METHOD', font=("Arial", 30))
    titlelabel1.pack(fill="both", expand=True, padx=5, pady=5)
    titlelabel2.pack(fill="both", expand=True, padx=5, pady=5)
    titlelabel3.pack(fill="both", expand=True, padx=5, pady=5)

    nlabel = tk.Label(leftFrame, text="insert n: (3-100)", font=("Arial", 10))
    nlabel.pack()

    nentry = tk.Entry(leftFrame, width=3, relief=tk.FLAT, font=("Arial", 16))
    nentry.pack(ipady=10, pady=10, ipadx=10)
    nentry.insert(0, "10")

    acclabel = tk.Label(leftFrame, text="insert integral accuracy: (10-500)", font=("Arial", 10))
    acclabel.pack()

    accentry = tk.Entry(leftFrame, width=3, relief=tk.FLAT, font=("Arial", 16))
    accentry.pack(ipady=10, pady=10, ipadx=10)
    accentry.insert(0, "100")

    button = tk.Button(leftFrame, text="Calculate", width=10, height=2, bg="white", command=changeplot)
    button.pack(pady=15)

    # plotframe code
    plotFrame = tk.Frame()
    plotFrame.pack(side=tk.LEFT)
    plotFrame.place(x=250, y=0)

    drawplot(solver.solve(10, 100))

    root.mainloop()
