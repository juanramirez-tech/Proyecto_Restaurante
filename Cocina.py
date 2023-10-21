from tkinter import *
import tkinter as tk
import sqlite3
import Loguin as Log

mi_conexion = sqlite3.connect("database/Carnivoros.db")
cursor = mi_conexion.cursor()

class PaginaCocina(tk.Frame):

    def ejecutar_login(self):  # Función para abrir ventana de Loguin
        self.pack_forget()
        self.Loguin = Log.PaginaLogin(self.master, self.window)  # Pasa la variable 'window' como un parámetro
        self.Loguin.pack()

    def __init__(self, master, window):
        super().__init__(master)
        self.window = master

        #Ventana completa

        global mesa
        global detalle
        global total

        frame = Frame(window, width=1000, height=500, bg='white')
        frame.place(x=0, y=0)

        Header = Frame(window, width=1000, height=70, bg='#F5793B')
        Header.place(x=0, y=0)
        

        heading1 = Label(Header, text='PEDIDO POR PREPARAR', fg="white", bg='#F5793B', font=('HEAVITAS', 20, 'bold'))
        heading1.place(x=280, y=15)

        heading2 = Label(frame, text='MESA', fg='#F5793B', bg='WHITE', font=('HEAVITAS', 18))
        heading2.place(x=100, y=90)

        heading3 = Label(frame, text='DETALLE DEL PEDIDO', fg='#F5793B', bg='WHITE', font=('HEAVITAS', 18))
        heading3.place(x=320, y=90)

        heading4 = Label(frame, text='TOTAL', fg='#F5793B', bg='WHITE', font=('HEAVITAS', 18))
        heading4.place(x=750, y=90)

        # Realizar la consulta
        cursor.execute("SELECT Mesa, Detalle, Total FROM Detalle_pedido")

        # Obtener el primer registro devuelto por la consulta
        resultado = cursor.fetchone()

        # Verificar si se encontró algún registro
        if resultado:

            mesa, detalle, total = resultado
            print("Mesa:", mesa)
            print("Detalle:", detalle)
            print("Total:", total)

            headingMesa = Label(frame, text=mesa, fg='black', bg='WHITE', font=('HEAVITAS', 12))
            headingMesa.place(x=130, y=130)

            headingDetalle = Label(frame, text=detalle, fg='black', bg='WHITE', font=('HEAVITAS', 12))
            headingDetalle.place(x=310, y=130)

            headingTotal = Label(frame, text=total, fg='black', bg='WHITE', font=('HEAVITAS', 12))
            headingTotal.place(x=750, y=130)

        else:
            print("No se encontraron registros en la tabla Detalle_pedido.")


        #BOTON DE ENVIAR PEDIDO A CAJA Y RESET

        FOOTER = Frame(window, width=1000, height=100, bg='#F5793B')
        FOOTER.place(x=0, y=420)

        def EnviarCaja_Reset():
            print("BOTON DE ENVIAR PEDIDO A CAJA Y RESET")

            global mesa
            global detalle
            global total

            Consulta = "INSERT INTO Pedido_Caja (Mesa, Detalle, Total, Estado) VALUES (?, ?, ?, ?)"
            Estado_pedido = "Completado"
            print(mesa)
            print(detalle)
            print(total)
            print(Estado_pedido)
            cursor.execute(Consulta, (mesa, detalle, total, Estado_pedido))
            mi_conexion.commit()

            print("Se mandó el pedido a caja")

            #ELIMINAR LA PRIMERA FILA DE DETALLE_PEDIDO PARA QUE SE CAMBIEN LOS PEDIDOS

            # Consulta para borrar la primera fila
            cursor.execute("DELETE FROM Detalle_pedido WHERE Id_detalle_pedido = (SELECT MIN(Id_detalle_pedido) FROM Detalle_pedido)")

            # Guardar los cambios
            mi_conexion.commit()

            #RESETEAR LA PAGINA COCINA PARA CARGAR NUEVO PEDIDO

            self.pack_forget()
            self.Cocina = PaginaCocina(self.master, self.window)
            self.Cocina.pack()

        Button(FOOTER, width=21, pady=10, text='PEDIDO PREPARADO', bg='#FFF', fg='#F5793B', border='3',
               font=('HEAVITAS', 9, 'bold'), command=EnviarCaja_Reset).place(x=350, y=15)

        Button(FOOTER, width=3, height=1, pady=10, text='.', bg='#FFF', fg='#F5793B', border='1',
               font=('HEAVITAS', 5, 'bold'),
               command=lambda: self.ejecutar_login()).place(x=890, y=40)

if __name__ == '__main__':

    window = tk.Tk()
    window.title("Carnivoros")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    icono = PhotoImage(file="images/Icono.png")
    window.iconphoto(True, icono)

    myapp = PaginaCocina(window, window)
    myapp.mainloop()