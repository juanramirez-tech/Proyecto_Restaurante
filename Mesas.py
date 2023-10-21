from tkinter import *
import tkinter as tk
import customtkinter
import sqlite3
import Loguin as Log

mi_conexion = sqlite3.connect("database/Carnivoros.db")
cursor = mi_conexion.cursor()

class PaginaMesas(tk.Frame):

    # EJECUTAR LOGIN

    def ejecutar_login(self):  # Función para abrir ventana de Loguin
        self.pack_forget()
        self.Loguin = Log.PaginaLogin(self.master, self.window)  # Pasa la variable 'window' como un parámetro
        self.Loguin.pack()

    def __init__(self, master, window):
        super().__init__(master)
        self.window = master

        #PARTE DEL PEDIDO ACTUAL

        frame = Frame(window, width=320, height=500, bg='#F5793B', bd='25')
        frame.place(x=0, y=0)

        heading = Label(frame, text='PEDIDO ACTUAL', fg='WHITE', bg='#F5793B', font=('HEAVITAS', 16, 'bold'))
        heading.place(x=25, y=0)

        framepedido = Frame(frame, width=250, height=350, bg='WHITE')
        framepedido.place(x=0, y=40)


        #PARTE FUNCIONAL DE LA TOMA DE PEDIDOS

        frame1 = Frame(window, width=700, height=500, bg='white')
        frame1.place(x=300, y=0)

        heading1 = Label(frame1, text='SELECIONAR MESA A FACTURAR', fg='#F5793B', bg='WHITE', font=('HEAVITAS', 16, 'bold'))
        heading1.place(x=110, y=40)

        #Botones para selecionar la mesa

        Mesa_seleccionada = None
        valor_variable = None

        def asignar_valor(valor):
            global valor_variable
            global Mesa_seleccionada

            valor_variable = valor

            # Ejecuta la consulta SQL para buscar coincidencias
            consulta = "SELECT * FROM Mesas WHERE Numero_mesa = ? "
            cursor.execute(consulta, valor_variable)

            # Recupera los resultados de la consulta
            resultado = cursor.fetchone()

            if resultado is not None:
                Mesa_seleccionada = valor
            else:
                print("Ninguna mesa selecionada")

            # Muestra del pedido actual

            Texto_Texto_Mesa = 'Mesa seleccionada: ' + (Mesa_seleccionada if Mesa_seleccionada is not None else "")
            TextoMesa = Label(frame, text=Texto_Texto_Mesa, fg='black', bg='WHITE',
                              font=('HEAVITAS', 11))
            TextoMesa.place(x=21, y=50)

            # PARTE DE LA TOMA DE PEDIDO

            if Mesa_seleccionada != None:

                heading3 = Label(frame1, text='PRODUCTO', fg='#F5793B', bg='WHITE',
                                 font=('HEAVITAS', 16, 'bold'))
                heading3.place(x=110, y=170)

                heading4 = Label(frame1, text='PRECIO', fg='#F5793B', bg='WHITE',
                                 font=('HEAVITAS', 16, 'bold'))
                heading4.place(x=330, y=170)

                heading5 = Label(frame1, text='CANTIDAD', fg='#F5793B', bg='WHITE',
                                 font=('HEAVITAS', 16, 'bold'))
                heading5.place(x=460, y=170)

                # PARTE DE LOS NOMBRES DE LOS PEDIDOS + CANTIDAD

                cursor.execute('SELECT Nombre_producto, Precio FROM Productos')
                filas = cursor.fetchall()

                i = 0

                for fila in filas:
                    valor1 = fila[0]  # Valor de la primera columna
                    valor2 = fila[1]  # Valor de la primera columna

                    if i == 0:
                        Texto_prueba = str(valor1)
                        heading6 = Label(frame1, text=Texto_prueba, fg='black', bg='WHITE',
                                         font=('HEAVITAS', 11))
                        heading6.place(x=20, y=210)

                        Texto_prueba = str(valor2)
                        heading61 = Label(frame1, text=Texto_prueba, fg='black', bg='WHITE',
                                          font=('HEAVITAS', 11))
                        heading61.place(x=350, y=210)

                        Cantidad1 = customtkinter.CTkEntry(master=frame1, width=50, height=30, text_color='black',
                                                           font=('HEAVITAS', 16), placeholder_text='Cant',
                                                           fg_color='white', border_color='#F5793B', justify='center')
                        Cantidad1.place(x=500, y=205)

                        i = i + 1

                    elif i == 1:

                        Texto_prueba = str(valor1)
                        heading7 = Label(frame1, text=Texto_prueba, fg='black', bg='WHITE',
                                         font=('HEAVITAS', 11))
                        heading7.place(x=20, y=260)

                        Texto_prueba = str(valor2)
                        heading71 = Label(frame1, text=Texto_prueba, fg='black', bg='WHITE',
                                          font=('HEAVITAS', 11))
                        heading71.place(x=350, y=260)

                        Cantidad2 = customtkinter.CTkEntry(master=frame1, width=50, height=30, text_color='black',
                                                           font=('HEAVITAS', 16), placeholder_text='Cant',
                                                           fg_color='white', border_color='#F5793B', justify='center')
                        Cantidad2.place(x=500, y=255)

                        i = i + 1
                    elif i == 2:
                        Texto_prueba = str(valor1)
                        heading8 = Label(frame1, text=Texto_prueba, fg='black', bg='WHITE',
                                         font=('HEAVITAS', 11))
                        heading8.place(x=20, y=310)

                        Texto_prueba = str(valor2)
                        heading81 = Label(frame1, text=Texto_prueba, fg='black', bg='WHITE',
                                          font=('HEAVITAS', 11))
                        heading81.place(x=350, y=310)

                        Cantidad3 = customtkinter.CTkEntry(master=frame1, width=50, height=30, text_color='black',
                                                           font=('HEAVITAS', 16), placeholder_text='Cant',
                                                           fg_color='white', border_color='#F5793B', justify='center')
                        Cantidad3.place(x=500, y=305)

                        i = i + 1
                    elif i == 3:
                        Texto_prueba = str(valor1)
                        heading9 = Label(frame1, text=Texto_prueba, fg='black', bg='WHITE',
                                         font=('HEAVITAS', 11))
                        heading9.place(x=20, y=360)

                        Texto_prueba = str(valor2)
                        heading91 = Label(frame1, text=Texto_prueba, fg='black', bg='WHITE',
                                          font=('HEAVITAS', 11))
                        heading91.place(x=350, y=360)

                        Cantidad4 = customtkinter.CTkEntry(master=frame1, width=50, height=30, text_color='black',
                                                           font=('HEAVITAS', 16), placeholder_text='Cant',
                                                           fg_color='white', border_color='#F5793B', justify='center')
                        Cantidad4.place(x=500, y=355)

                        i = i + 1

                    print(valor1, valor2)

                    # BOTON PARA COMPLETAR PEDIDO



                    def imprimir_pedido():

                            global Detalle_pedido
                            global Precio_Total


                            #PRIMER PRODUCTO

                            nombre = heading6['text']  # Obtiene el nombre del producto
                            precio1 = heading61['text']  # Obtiene el precio del producto
                            cantidad = Cantidad1.get()  # Obtiene la cantidad ingresada en el CTkEntry

                            if cantidad == '':
                                cantidad = 0  # Asigna 0 si no se ingresó ningún valor

                            if cantidad != 0:
                                texto_pedido = f'{nombre} \nPrecio: {precio1} \nCantidad: {cantidad}'
                                # Aquí puedes hacer lo que desees con la variable de texto "texto_pedido"
                                print(texto_pedido)
                                MostarTextopedido = Label(framepedido, text=texto_pedido, fg='black', bg='WHITE',
                                                          font=('HEAVITAS', 10))
                                MostarTextopedido.place(x=6, y=50)
                                precio1total = int(precio1) * int(cantidad)

                                Detalle_pedido = texto_pedido + "\n"

                            #SEGUNDO PRODUCTO

                            nombre = heading7['text']  # Obtiene el nombre del producto
                            precio2 = heading71['text']  # Obtiene el precio del producto
                            cantidad = Cantidad2.get()  # Obtiene la cantidad ingresada en el CTkEntry

                            if cantidad == '':
                                cantidad = 0  # Asigna 0 si no se ingresó ningún valor

                            if cantidad != 0:
                                texto_pedido = f'{nombre} \nPrecio: {precio2} \nCantidad: {cantidad}'
                                # Aquí puedes hacer lo que desees con la variable de texto "texto_pedido"
                                print(texto_pedido)
                                MostarTextopedido = Label(framepedido, text=texto_pedido, fg='black', bg='WHITE',
                                                          font=('HEAVITAS', 10))
                                MostarTextopedido.place(x=1, y=120)
                                precio2total = int(precio2) * int(cantidad)

                                Detalle_pedido =  Detalle_pedido + texto_pedido + "\n"

                            #TERCER PRODUCTO

                            nombre = heading8['text']  # Obtiene el nombre del producto
                            precio3 = heading81['text']  # Obtiene el precio del producto
                            cantidad = Cantidad3.get()  # Obtiene la cantidad ingresada en el CTkEntry

                            if cantidad == '':
                                cantidad = 0  # Asigna 0 si no se ingresó ningún valor

                            if cantidad != 0:
                                texto_pedido = f'{nombre} \nPrecio: {precio3} \nCantidad: {cantidad}'
                                # Aquí puedes hacer lo que desees con la variable de texto "texto_pedido"
                                print(texto_pedido)
                                MostarTextopedido = Label(framepedido, text=texto_pedido, fg='black', bg='WHITE',
                                                          font=('HEAVITAS', 10))
                                MostarTextopedido.place(x=1, y=190)
                                precio3total = int(precio3) * int(cantidad)

                                Detalle_pedido = Detalle_pedido + texto_pedido + "\n"

                            #CUARTO PRODUCTO

                            nombre = heading9['text']  # Obtiene el nombre del producto
                            precio4 = heading91['text']  # Obtiene el precio del producto
                            cantidad = Cantidad4.get()  # Obtiene la cantidad ingresada en el CTkEntry

                            if cantidad == '':
                                cantidad = 0  # Asigna 0 si no se ingresó ningún valor

                            if cantidad != 0:
                                texto_pedido = f'{nombre} \nPrecio: {precio4} \nCantidad: {cantidad}'
                                # Aquí puedes hacer lo que desees con la variable de texto "texto_pedido"
                                print(texto_pedido)
                                MostarTextopedido = Label(framepedido, text=texto_pedido, fg='black', bg='WHITE',
                                                          font=('HEAVITAS', 10))
                                MostarTextopedido.place(x=1, y=260)
                                precio4total = int(precio4) * int(cantidad)

                                Detalle_pedido = Detalle_pedido + texto_pedido + "\n"

                            Precio_Total = int(precio1total) + int(precio2total) + int(precio3total) + int(precio4total)
                            MostrarTotalProductos = "Total: " + str(Precio_Total)
                            headingTotalPrecio = Label(framepedido, text=MostrarTotalProductos, fg='black', bg='WHITE',
                                              font=('HEAVITAS', 10))
                            headingTotalPrecio.place(x=70, y=330)

                    Button(frame1, width=21, pady=10, text='COMPLETAR PEDIDO', bg='#FFF', fg='#F5793B', border='3',
                           font=('HEAVITAS', 11, 'bold'), command=imprimir_pedido).place(x=180, y=400)



                    # BOTON DE PARA ENVIAR EL PEDIDO A LA DB Y RESECT
                    
                    def enviarpedido_reset():

                        global Mesa_seleccionada
                        global Detalle_pedido
                        global Precio_Total

                        Consulta = "INSERT INTO Detalle_pedido (Mesa, Detalle, Total) VALUES (?, ?, ?)"
                        print(Mesa_seleccionada)
                        print(Detalle_pedido)
                        print(Precio_Total)
                        cursor.execute(Consulta, (Mesa_seleccionada, Detalle_pedido, Precio_Total))
                        mi_conexion.commit()

                        print("Se mandó el pedido")

                        #PARA REINICIAR LA VENTANA MESAS

                        self.pack_forget()
                        self.Mesas = PaginaMesas(self.master, self.window)
                        self.Mesas.pack()

                    Button(frame, width=21, pady=10, text='ENVIAR PEDIDO', bg='#FFF', fg='#F5793B', border='3',
                           font=('HEAVITAS', 9, 'bold'), command=enviarpedido_reset).place(x=17, y=410)


        Boton1 = customtkinter.CTkButton(frame1, text="1", width=50, height=50, font=('HEAVITAS', 35),
                                         fg_color='#F5793B', command=lambda: asignar_valor("1"))
        Boton1.place(x=40, y=90)

        Boton2 = customtkinter.CTkButton(frame1, text="2", width=50, height=50, font=('HEAVITAS', 35),
                                         fg_color='#F5793B', command=lambda: asignar_valor("2"))
        Boton2.place(x=110, y=90)

        Boton3 = customtkinter.CTkButton(frame1, text="3", width=50, height=50, font=('HEAVITAS', 35),
                                         fg_color='#F5793B', command=lambda: asignar_valor("3"))
        Boton3.place(x=180, y=90)

        Boton4 = customtkinter.CTkButton(frame1, text="4", width=50, height=50, font=('HEAVITAS', 35),
                                         fg_color='#F5793B', command=lambda: asignar_valor("4"))
        Boton4.place(x=250, y=90)

        Boton5 = customtkinter.CTkButton(frame1, text="5", width=50, height=50, font=('HEAVITAS', 35),
                                         fg_color='#F5793B', command=lambda: asignar_valor("5"))
        Boton5.place(x=320, y=90)

        Boton6 = customtkinter.CTkButton(frame1, text="6", width=50, height=50, font=('HEAVITAS', 35),
                                         fg_color='#F5793B', command=lambda: asignar_valor("6"))
        Boton6.place(x=390, y=90)

        Boton7 = customtkinter.CTkButton(frame1, text="7", width=50, height=50, font=('HEAVITAS', 35),
                                         fg_color='#F5793B', command=lambda: asignar_valor("7"))
        Boton7.place(x=460, y=90)

        Boton8 = customtkinter.CTkButton(frame1, text="8", width=50, height=50, font=('HEAVITAS', 35),
                                         fg_color='#F5793B', command=lambda: asignar_valor("8"))
        Boton8.place(x=530, y=90)

        #BOTON PARA VOLVER AL LOGUIN

        Button(frame1, width=3, height=1, pady=10, text='.', bg='#F5793B', fg='WHITE', border='1',
            font=('HEAVITAS', 5, 'bold'),
            command=lambda: self.ejecutar_login()).place(x=590, y=460)


if __name__ == '__main__':

    window = tk.Tk()
    window.title("Carnivoros")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    icono = PhotoImage(file="images/Icono.png")
    window.iconphoto(True, icono)

    myapp = PaginaMesas(window, window)
    myapp.mainloop()

