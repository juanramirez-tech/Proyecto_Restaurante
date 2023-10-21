from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import ttk
import Loguin as Log

mi_conexion = sqlite3.connect("database/Carnivoros.db")
cursor = mi_conexion.cursor()

class PaginaHistotial(tk.Frame):

    def ejecutar_login(self):  # Función para abrir ventana de Loguin
        self.pack_forget()
        self.Loguin = Log.PaginaLogin(self.master, self.window)  # Pasa la variable 'window' como un parámetro
        self.Loguin.pack()

    def __init__(self, master, window):
        super().__init__(master)
        self.window = master

        frame = Frame(window, width=950, height=500, bg='WHITE', bd='25')
        frame.place(x=0, y=0)

        frame1 = Frame(window, width=950, height=70, bg='#F5793B', bd='15')
        frame1.place(x=0, y=0)

        heading = Label(frame1, text='PEDIDO SELECCIONADO', fg="WHITE", bg='#F5793B', font=('HEAVITAS', 24, 'bold'))
        heading.place(x=240, y=0)

        # Crear el Treeview para mostrar la tabla
        treeview = ttk.Treeview(frame, columns=(
        "id_historial", "id_pedido_caja", "mesa", "detalle_pedido", "total_pedido", "fecha"), show="headings")
        treeview.place(x=6, y=70, width=890, height=350)  # Ajustar las coordenadas y dimensiones aquí

        # Configurar las columnas
        treeview.heading("id_historial", text="ID Historial", anchor=CENTER)
        treeview.column("id_historial", width=100, anchor=CENTER)

        treeview.heading("id_pedido_caja", text="ID Pedido Caja", anchor=CENTER)
        treeview.column("id_pedido_caja", width=100, anchor=CENTER)

        treeview.heading("mesa", text="Mesa", anchor=CENTER)
        treeview.column("mesa", width=50, anchor=CENTER)

        treeview.heading("detalle_pedido", text="Detalle Pedido", anchor=CENTER)
        treeview.column("detalle_pedido", width=200, anchor=CENTER)

        treeview.heading("total_pedido", text="Total Pedido", anchor=CENTER)
        treeview.column("total_pedido", width=100, anchor=CENTER)

        treeview.heading("fecha", text="Fecha", anchor=CENTER)
        treeview.column("fecha", width=100, anchor=CENTER)

        # Obtener los datos de la tabla y mostrarlos en el Treeview
        cursor.execute("SELECT * FROM Historial_ventas")
        rows = cursor.fetchall()
        for row in rows:
            # Truncar el valor en la columna "detalle_pedido" a 50 caracteres
            detalle_pedido = row[3][:25] + "..." if len(row[3]) > 25 else row[3]
            row_values = (*row[:3], detalle_pedido, *row[4:])
            treeview.insert("", "end", values=row_values)

        Button(frame, width=3, height=1, pady=10, text='.', bg='#F5793B', fg='#FFF', border='1',
               font=('HEAVITAS', 5, 'bold'),
               command=lambda: self.ejecutar_login()).place(x=890, y=435)

if __name__ == '__main__':
    window = tk.Tk()
    window.title("Carnivoros")
    window.geometry('950x500+300+200')
    window.configure(bg='#fff')
    icono = PhotoImage(file="images/Icono.png")
    window.iconphoto(True, icono)

    myapp = PaginaHistotial(window, window)
    myapp.mainloop()




