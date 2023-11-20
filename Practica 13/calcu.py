#                                        Ensenada, Baja California a 19 de Noviembre del 2023#
#Actividad 13                                                                                #
#REALIZA LOS EJERCICIOS EN PYTHON USANDO LIBRERIA TKINTER                                    #
#Nombre:     Luis Fernando Ochoa Angulo                                                      #
#Matricula:  372205                                                                          #
#Programa:   calculadora basica usando tkinter                                               #
#Nombre de la actividad: LF0A_ACT13_01_432_PYTHON                                            #



import tkinter as tk
    
def sumar_numeros():
    # Obtener los números ingresados por el usuario
    numero1 = float(ety_num1.get())
    numero2 = float(ety_num2.get())
    try:
        # Realizar la suma
        suma = numero1 + numero2

        # Mostrar el resultado en la etiqueta de resultado
        lbl_oper.config(text="+")
        lbl_resul.config(text=f"{suma}")
    except ValueError:
        # Manejar el caso en que la entrada no sea un número válido
        lbl_resul.config(text="SyntaxError")
        
def restar_numeros():
    # Obtener los números ingresados por el usuario
    numero1 = float(ety_num1.get())
    numero2 = float(ety_num2.get())
    try:
        # Realizar la suma
        suma = numero1 - numero2

        # Mostrar el resultado en la etiqueta de resultado
        lbl_oper.config(text="-")
        lbl_resul.config(text=f"{suma}")
    except ValueError:
        # Manejar el caso en que la entrada no sea un número válido
        lbl_resul.config(text="SyntaxError")

def multi_numeros():
    # Obtener los números ingresados por el usuario
    numero1 = float(ety_num1.get())
    numero2 = float(ety_num2.get())
    try:
        # Realizar la suma
        suma = numero1 * numero2

        # Mostrar el resultado en la etiqueta de resultado
        lbl_oper.config(text="*")
        lbl_resul.config(text=f"{suma}")
    except ValueError:
        # Manejar el caso en que la entrada no sea un número válido
        lbl_resul.config(text="SyntaxError")
        
def divi_numeros():
    # Obtener los números ingresados por el usuario
    numero1 = float(ety_num1.get())
    numero2 = float(ety_num2.get())
    try:
        # Realizar la suma
        suma = numero1 / numero2

        # Mostrar el resultado en la etiqueta de resultado
        lbl_oper.config(text="/")
        lbl_resul.config(text=f"{suma}")
    except ValueError:
        # Manejar el caso en que la entrada no sea un número válido
        lbl_resul.config(text="SyntaxError")
        
        
        
        




# Crear la ventana
ventana = tk.Tk()
ventana.title("Calculadora basicas zzz")
#ventana.configure(background="gray25")
ventana.geometry("500x500")

# Crear etiquetas y entradas para los números
lbl_num1 = tk.Label(ventana, text="NUMERO 1:")
lbl_num2 = tk.Label(ventana, text="NUMERO 2:")
lbl_oper = tk.Label(ventana, text= " ")




ety_num1 = tk.Entry(ventana)
ety_num2 = tk.Entry(ventana)


# Crear un botón para realizar la suma
btn_resul = tk.Button(ventana, text="RESULTADO")

btn_suma = tk.Button(ventana, text=" SUMA ", font=("Arial", 12),command=sumar_numeros)
btn_resta = tk.Button(ventana, text="RESTA", font=("Arial", 12), command=restar_numeros)
btn_multi = tk.Button(ventana, text="MULTI", font=("Arial", 12), command=multi_numeros)
btn_divi = tk.Button(ventana, text="DIVI", font=("Arial", 12),command=divi_numeros)


# Crear una etiqueta para mostrar el resultado
lbl_resul = tk.Label(ventana, text="")

# Configuracion de las ventanas 
lbl_num1.configure(background="dark orange")
lbl_num2.configure(background="dark orange")


btn_suma.configure(background="tan1",bd=5)
btn_resta.configure(background="tan1",bd=5)
btn_multi.configure(background="tan1",bd=5)
btn_divi.configure(background="tan1",bd=5)
btn_resul.configure(background="dark orange",bd = 5)

lbl_oper.config(width=3,height=1)
lbl_resul.config(width=10,height=1)

btn_suma.config(width=10,height=2)
btn_resta.config(width=10,height=2)
btn_divi.config(width=10,height=2)
btn_multi.config(width=10,height=2)
btn_resul.config(width=10,height=1)

# Union de botones,entry, y label a la ventana padre con el uso de place
ety_num1.place(x=10,y=45)
ety_num2.place(x=200,y=45)

lbl_num1.place(x=10,y=20)
lbl_num2.place(x=200,y=20)
lbl_oper.place(x=150,y=45)
lbl_resul.place(x=350,y=45)


btn_resul.place(x=350,y=15)

btn_suma.place(x=10,y=70)
btn_resta.place(x=10,y=140)
btn_divi.place(x=150,y=70)
btn_multi.place(x=150,y=140)



# Iniciar el bucle principal de la ventana
ventana.mainloop()
