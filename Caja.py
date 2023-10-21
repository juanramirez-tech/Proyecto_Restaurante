from tkinter import *
import tkinter as tk
import sqlite3
from datetime import datetime
import Loguin as Log

mi_conexion = sqlite3.connect("database/Carnivoros.db")
cursor = mi_conexion.cursor()

class PaginaCaja(tk.Frame):

    def ejecutar_login(self):  # Función para abrir ventana de Loguin
        self.pack_forget()
        self.Loguin = Log.PaginaLogin(self.master, self.window)  # Pasa la variable 'window' como un parámetro
        self.Loguin.pack()

    def __init__(self, master, window):
        super().__init__(master)
        self.window = master

        # PARTE DEL PEDIDO ACTUAL

        frame = Frame(window, width=600, height=500, bg='WHITE', bd='25')
        frame.place(x=0, y=0)

        heading = Label(frame, text='PEDIDO SELECIONADO', fg='#F5793B', bg='WHITE', font=('HEAVITAS', 16, 'bold'))
        heading.place(x=85, y=5)

        self.label_id = Label(frame, text='ID Pedido:', fg='#F5793B', bg='WHITE', font=('HEAVITAS', 12, 'bold'))
        self.label_id.place(x=25, y=50)

        self.label_id_respuesta = Label(frame, text='', fg='BLACK', bg='WHITE', font=('HEAVITAS', 12))
        self.label_id_respuesta.place(x=135, y=50)

        self.label_mesa = Label(frame, text='Mesa:', fg='#F5793B', bg='WHITE', font=('HEAVITAS', 12, 'bold'))
        self.label_mesa.place(x=25, y=80)

        self.label_mesa_respuesta = Label(frame, text='', fg='BLACK', bg='WHITE', font=('HEAVITAS', 12))
        self.label_mesa_respuesta.place(x=95, y=80)

        self.label_detalle = Label(frame, text='Detalle:', fg='#F5793B', bg='WHITE', font=('HEAVITAS', 12, 'bold'))
        self.label_detalle.place(x=25, y=110)

        self.label_detalle_respuesta = Label(frame, text='', fg='BLACK', bg='WHITE', font=('HEAVITAS', 12))
        self.label_detalle_respuesta.place(x=60, y=140)

        self.label_total = Label(frame, text='Total:', fg='#F5793B', bg='WHITE', font=('HEAVITAS', 12, 'bold'))
        self.label_total.place(x=25, y=400)

        self.label_total_respuesta = Label(frame, text='', fg='BLACK', bg='WHITE', font=('HEAVITAS', 12))
        self.label_total_respuesta.place(x=100, y=400)

        # PARTE FUNCIONAL DE LA TOMA DE PEDIDOS

        frame1 = Frame(window, width=700, height=500, bg='#F5793B')
        frame1.place(x=500, y=0)

        heading1 = Label(frame1, text='SELECCIONA EL PEDIDO', fg='WHITE', bg='#F5793B', font=('HEAVITAS', 16, 'bold'))
        heading1.place(x=65, y=25)

        self.lista_pedidos = Listbox(frame1, width=15, height=10, font=('HEAVITAS', 18), justify='center')
        self.lista_pedidos.place(x=75, y=70)

        self.lista_pedidos.bind('<<ListboxSelect>>', self.mostrar_detalles_pedido)

        self.obtener_pedidos()

        def pagarpedido_reset():
            print("BOTON DE PAGAR PEDIDO Y RESET")

            global Id_pedido
            global Mesa_pedido
            global Detalle_pedido_tomado
            global Total_pedido

            fecha_actual = datetime.now()
            mi_variable_fecha = fecha_actual.strftime("%Y-%m-%d")

            Consulta = "INSERT INTO Historial_ventas (Id_pedido_caja, Mesa, Detalle_pedido, Total_pedido, Fecha) VALUES (?, ?, ?, ?, ?)"
            print(Id_pedido)
            print(Mesa_pedido)
            print(Detalle_pedido_tomado)
            print(Total_pedido)
            print(mi_variable_fecha)
            cursor.execute(Consulta, (Id_pedido, Mesa_pedido, Detalle_pedido_tomado, Total_pedido, mi_variable_fecha))
            mi_conexion.commit()

            print("DATOS ENVIADOS")

            #AQUÍ VA EL CODIGO QUE ELIMINA EL PEDIDO QUE FUE SELECIONADO DE LA LISTA DE PEDIDOS EN LA TABLA Pedido_caja

            # Eliminar el pedido de la tabla Pedido_Caja
            cursor.execute("DELETE FROM Pedido_Caja WHERE Id_pedido_caja=?", (Id_pedido,))
            mi_conexion.commit()

            # Restablecer los valores globales a vacío
            Id_pedido = ''
            Mesa_pedido = ''

            # Restablecer las etiquetas en la interfaz
            self.label_id_respuesta.config(text='')
            self.label_mesa_respuesta.config(text='')
            self.label_detalle_respuesta.config(text='')
            self.label_total_respuesta.config(text='')

            # Actualizar la lista de pedidos en la interfaz
            self.obtener_pedidos()

        Button(frame1, width=21, pady=10, text='PEDIDO PAGADO', bg='#FFF', fg='#F5793B', border='3',
               font=('HEAVITAS', 9, 'bold'), command=pagarpedido_reset).place(x=110, y=420)

        Button(frame1, width=3, height=1, pady=10, text='.', bg='#FFF', fg='#F5793B', border='1',
               font=('HEAVITAS', 5, 'bold'),
               command=lambda: self.ejecutar_login()).place(x=390, y=460)

    def obtener_pedidos(self):
        cursor.execute("SELECT Id_pedido_caja, Mesa FROM Pedido_Caja")
        pedidos = cursor.fetchall()
        self.lista_pedidos.delete(0, END)
        for pedido in pedidos:
            self.lista_pedidos.insert(END, pedido[1])

    def mostrar_detalles_pedido(self, event):

        global Id_pedido
        global Mesa_pedido
        global Detalle_pedido_tomado
        global Total_pedido

        seleccionado = self.lista_pedidos.get(self.lista_pedidos.curselection())
        cursor.execute("SELECT Id_pedido_caja, Mesa, Detalle, Total FROM Pedido_Caja WHERE Mesa=?", (seleccionado,))
        detalle_pedido = cursor.fetchone()
        if detalle_pedido:
            self.label_id_respuesta.config(text='' + str(detalle_pedido[0]))
            Id_pedido = str(detalle_pedido[0])
            self.label_mesa_respuesta.config(text='' + detalle_pedido[1])
            Mesa_pedido = str(detalle_pedido[1])
            self.label_detalle_respuesta.config(text='' + detalle_pedido[2])
            Detalle_pedido_tomado = str(detalle_pedido[2])
            self.label_total_respuesta.config(text='' + str(detalle_pedido[3]))
            Total_pedido = str(detalle_pedido[3])

if __name__ == '__main__':

    window = tk.Tk()
    window.title("Carnivoros")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    icono = PhotoImage(file="images/Icono.png")
    window.iconphoto(True, icono)

    myapp = PaginaCaja(window, window)
    myapp.mainloop()




