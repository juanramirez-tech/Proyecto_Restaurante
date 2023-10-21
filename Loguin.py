from tkinter import *
import tkinter as tk
import customtkinter
import Mesas as Mes
import Caja as Caj
import Cocina as Coci
import Historial_ventas as Histo
import sqlite3

mi_conexion = sqlite3.connect("database/Carnivoros.db")
cursor = mi_conexion.cursor()

class PaginaLogin(tk.Frame):
    def __init__(self, master, window):
        super().__init__(master)
        self.window = master

        #PARTE DE LA IMAGEN

        frame_fondo = Frame(window, width=1000, height=1000, bg='white')
        frame_fondo.place(x=0, y=0)

        frame = Frame(window, width=450, height=400, bg='white')
        frame.place(x=50, y=50)

        img = PhotoImage(file='images/Logo.png')
        self.Imagen = Label(frame, image=img, border=0, bg='white')
        self.Imagen.image = img
        self.Imagen.place(x=40, y=40)

        #PARTE DE LOS DATOS DEL LOGIN

        frame1 = Frame(window, width=350, height=390, bg='#fff')
        frame1.place(x=480, y=50)

        heading = Label(frame1, text='Iniciar sección', fg='#F5793B', bg='white', font=('HEAVITAS', 16, 'bold'))
        heading.place(x=90, y=70)

        def on_enter(e):
            entry1.delete(0, 'end')
        def on_leave(e):
            if entry1.get()=='':
                entry1.insert(0, 'Usuario')

        entry1 = customtkinter.CTkEntry(master=frame1, width=295, height=40, text_color='black',
                                        font=('Microsoft Yahei UI Light', 14), placeholder_text='Usuario',
                                        fg_color='white', border_color='#F5793B')
        entry1.place(x=55, y=120)
        entry1.bind('<FocusIn>', on_enter)
        entry1.bind('<FocusOut>', on_leave)

        def on_enter(e):
            entry2.delete(0, 'end')
        def on_leave(e):
            if entry2.get()=='':
                entry2.insert(0, 'Contraseña')

        entry2 = customtkinter.CTkEntry(master=frame1, width=295, height=40, text_color='black',
                                        font=('Microsoft Yahei UI Light', 14), placeholder_text='Contraseña',
                                        fg_color='white', border_color='#F5793B')
        entry2.place(x=55, y=170)
        entry2.bind('<FocusIn>', on_enter)
        entry2.bind('<FocusOut>', on_leave)

        #VERIFICACIÓN DE DATOS Y BOTON

        def ejecutar_mesas(self):
            self.pack_forget()
            self.Mesas = Mes.PaginaMesas(self.master, self.window)  # Pasa la variable 'window' como un parámetro
            self.Mesas.pack()

        def ejecutar_caja(self):
            self.pack_forget()
            self.Caja = Caj.PaginaCaja(self.master, self.window)  # Pasa la variable 'window' como un parámetro
            self.Caja.pack()

        def ejecutar_cocina(self):
            self.pack_forget()
            self.Cocina = Coci.PaginaCocina(self.master, self.window)  # Pasa la variable 'window' como un parámetro
            self.Cocina.pack()

        def ejecutar_historial(self):
            self.pack_forget()
            self.Historial_ventas = Histo.PaginaHistotial(self.master, self.window)  # Pasa la variable 'window' como un parámetro
            self.Historial_ventas.pack()



        def ejecutar():

            usuario = entry1.get()
            contrasena = entry2.get()

            # Ejecuta la consulta SQL para buscar coincidencias
            consulta = "SELECT * FROM usuarios WHERE Usuario = ? AND contrasena = ?"
            cursor.execute(consulta, (usuario, contrasena))

            # Recupera los resultados de la consulta
            resultado = cursor.fetchone()

            if resultado is not None:
                # Acción específica para cada usuario
                if usuario == "Mesa":
                    # Acción para el usuario "Mesa"
                    ejecutar_mesas(self)
                    print("Acción específica para el usuario Mesa")
                elif usuario == "Cocina":
                    # Acción para el usuario "Cocina"
                    ejecutar_cocina(self)
                    print("Acción específica para el usuario Cocina")
                elif usuario == "Caja":
                    # Acción para el usuario "Caja"
                    ejecutar_caja(self)
                    print("Acción específica para el usuario Caja")
                elif usuario == "Historial":
                    # Acción para el usuario "Caja"
                    ejecutar_historial(self)
                    print("Acción específica para el usuario Caja")

            else:
                print("Usuario y/o contraseña incorrectos")
                heading = Label(frame1, text='Usuario o Contraseña incorrectos', fg='#F5793B', bg='white', font=('HEAVITAS', 8))
                heading.place(x=80, y=280)


        Button(frame1, width= 30, pady=10, text='Iniciar', bg='#F5793B', fg='white', border='0', font=('HEAVITAS', 9,'bold'), command=ejecutar).place(x=57, y=225)

if __name__ == '__main__':

    window = tk.Tk()
    window.title("Carnivoros")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    icono = PhotoImage(file="images/Icono.png")
    window.iconphoto(True, icono)

    myapp = PaginaLogin(window, window)
    myapp.mainloop()

