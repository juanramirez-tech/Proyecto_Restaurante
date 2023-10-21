from tkinter import *
import tkinter as tk
import Loguin as Log

class PaginaInicio(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.window = master

        def ejecutar_login(self): #Función para abrir ventana de Loguin
            self.pack_forget()
            self.Loguin = Log.PaginaLogin(self.master, self.window)  #Pasa la variable 'window' como un parámetro
            self.Loguin.pack()

        frame = Frame(window, width=450, height=400, bg='white')
        frame.place(x=50, y=50)

        img = PhotoImage(file="images/Logo.png")
        self.Imagen = Label(frame, image=img, border=0, bg='white')
        self.Imagen.image = img  #Mantenemos una referencia al objeto PhotoImage
        self.Imagen.place(x=50, y=40)

        frame1 = Frame(window, width=350, height=390, bg='white')
        frame1.place(x=510, y=50)

        self.Boton = Button(frame1, width=30, pady=10, text='INICIAR SESIÓN', bg='#F5793B', fg='white', border='0', font=('HEAVITAS', 9, 'bold'), command=lambda: ejecutar_login(self)).place(x=15, y=170)
        self.pack()

if __name__ == '__main__':

    window = tk.Tk()
    window.title("Carnivoros")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    icono = PhotoImage(file="images/Icono.png")
    window.iconphoto(True, icono)

    myapp = PaginaInicio(window)
    myapp.mainloop()










