from clientes import Cliente
from equipos import Equipo
import os

def menu():
    cliente = Cliente()
    opc = 0
    
    while opc != 5:
        os.system("cls")
        print("------------MENU------------")
        print("1. Ingresar Cliente")
        print("2. Ver Cliente")
        print("3. Agregar Equipo")
        print("4. Ver Equipos Por Cliente")
        print("5. Salir")
        print("-" * 30)
        opc = int(input("Ingrese una opcion valida: "))
        
        if opc == 1:
            os.system("cls")
            nombre = input("Ingrese el nombre del cliente  : ")
            apellido = input("Ingrese el apellido del cliente: ")
            telefono =input("Ingrese el telefono del cliente: ")
            cliente.AgregarCliente(apellido, nombre, telefono)
            input()
        elif opc == 2:
            os.system("cls")
            print(cliente)
            input()
        elif opc == 3:
            os.system("cls")
            equipo = Equipo()
            numero_part = input("Ingrese el Numero de Parte: ")
            tipo = input("Ingrese el tipo del equipo: ")
            descripcion = input("Describa el problema del equipo: ")
            equipo.AgregarEquipo(numero_part, tipo, descripcion)
            cliente.AgregarEquipoCliente(equipo)
        elif opc == 4:
            os.system("cls")
            cliente.MostrarEquipos()
            input()
        elif opc == 5:
            os.system("cls")
            print("Gracias por usar el programa!!")
            input()
            os.system("cls")
            break
        else:
            print("Ingrese una opcion valida!!")
            
menu()