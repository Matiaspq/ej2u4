from tkinter import *
from tkinter import ttk, messagebox

class Aplicacion(object):
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.configure(bg = 'beige')
        self.__ventana.title('Calculo de IVA')
        self.__ventana.geometry("341x341")
        mainframe = ttk.Frame(self.__ventana, padding= "5 10 5 10")
        mainframe.grid(column=0, row = 0, sticky=(N,W,E,S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2

        self.precioSinIVA = StringVar()
        self.IVA = StringVar()
        self.precioConIVA = StringVar()
        self.resultadoIVA = StringVar
        self.resultadoPrecioIVA = StringVar()
        self.tipoIVA = StringVar()


        self.titleLbl = ttk.Label(text = 'Calculo de IVA').grid(column=2,row=1,sticky=(W))

        self.precioLbl = ttk.Label(mainframe, text = 'Precio sin IVA').grid(column=1,row=2,sticky=(W))
        self.ivaLbl = ttk.Label(mainframe, text = 'IVA').grid(column=1,row=5,sticky=(W))      
        self.precioConIvaLbl = ttk.Label(mainframe, text = 'Precio Con IVA').grid(column=1,row=6,sticky=(W))   

        self.botonIVA21 = ttk.Radiobutton(mainframe, text = 'IVA 21%', value=0,variable=self.tipoIVA,command=self.cambiaTipoIVA).grid(column=1,row=3,sticky=(W))
        self.botonIVA105 = ttk.Radiobutton(mainframe, text = 'IVA 10.5%',value=1,variable=self.tipoIVA,command=self.cambiaTipoIVA).grid(column=1,row=4,sticky=(W))   

        self.boton1 = ttk.Button(mainframe, text = 'Calcular', command=self.calcularIVA).grid(column=1,row=7, sticky=(W)) 
        self.boton2 = ttk.Button(mainframe, text = 'Salir', command=self.__ventana.destroy).grid(column=3,row=7, sticky=(W))

        
        self.precioSinIVAE = ttk.Entry(mainframe,textvariable=self.precioSinIVA)
        self.precioSinIVAE.grid(column=3,row=2,sticky=(W))

        self.precioIVAE = ttk.Label(mainframe, textvariable= str(self.resultadoIVA)).grid(column=3,row=5,sticky=(W))

        self.precioConIVAE = ttk.Label(mainframe, textvariable= str(self.resultadoPrecioIVA)).grid(column=3,row=6,sticky=(W))



        for child in mainframe.winfo_children():
            child.grid_configure(padx=7, pady=3)
        self.precioSinIVAE.focus()
        self.__ventana.mainloop


        

    def calcularIVA(self):
        try:
            sinIVA=float(self.precioSinIVAE.get())

        except ValueError:
            messagebox.showerror(title='Error de Ingreso', message='Debe ingresar datos numericos.')

        lIVA21=sinIVA*0.21
        lIVA105=sinIVA*0.105

        precio21=sinIVA+lIVA21
        precio105=sinIVA+lIVA105


        if self.tipoIVA.get()==0:
            self.resultadoIVA.set(round(lIVA21,2))
            self.resultadoPrecioIVA.set(round(precio21,2))

        elif self.tipoIVA.get()==1:
            self.resultadoIVA.set(round(lIVA105,2))
            self.resultadoPrecioIVA.set(round(precio105,2))   



    def cambiaTipoIVA(self):
        if self.tipoIVA.get()==0:
            self.tipoIVA=21

        elif self.tipoIVA.get()==1:
            self.tipoIVA=105
