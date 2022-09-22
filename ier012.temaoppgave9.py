import tkinter

rotvindu = tkinter.Tk()

def ødelegg():
    rotvindu.destroy()

farvel = tkinter.Button(rotvindu, text='Farvel', width=10,
                fg='red', bg='yellow',
                font=('Arial', 12, 'bold italic'), command = ødelegg)

farvel.grid(row=0, column=0)

rotvindu.mainloop()

from tkinter import Tk, Button

rotvindu2 = Tk()

def teller():
    global tall
    tall += 1
    knapp.config(text = tall, fg='purple', bg = 'red', font=('Helvetica', 40))

tall = 0

knapp = Button(rotvindu2, text=tall, width=10,
                fg='red', bg='lightblue',
                font=('Arial', 12, 'bold italic'), command = teller)

knapp.grid(row=0, column=0)

rotvindu.mainloop()




