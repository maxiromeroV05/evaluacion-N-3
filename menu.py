import funciones
import os
import time
def menu():

 while True:
    print("****************************************************")
    print("*                  MUNDO LIBRO                     *")
    print("****************************************************")
    print("[1]-Mantenedor de categorias")
    print("[2]-reportes")
    print("[3]-salir")
    print("****************************************************")
    opp = int(input("Ingrese una opcion : "))
    match opp:

     case 1:
        print("****************************************************")
        print("*              MANTENEDOR CATEGORIAS               *")
        print("****************************************************")
        print("[1] Agregar categoria")
        print("[2] Editar categoria")
        print("[3] Eliminar categoria")
        print("[4] buscar categoria")
        print("[5] volver")
        print("****************************************************")

        global opc

        opc = int(input("Ingrese una opcion :"))

        if opc == 1:

            nombreR = input("Ingrese un nuevo nombre :")

            funciones.agregar_categoria(nombre=nombreR)
            print("se agrego correctamente")

        if opc == 2:
            
            funciones.editar_categoria(int(input("ingrese la Id :")))

        if opc == 3:
           
           funciones.eliminar_categoria(int(input("Ingresa la ID que deseas eliminar :")))

        if opc == 4:
           
           funciones.buscar_categoria()

        if opc == 5:
           menu()
        
        if opc >= 5:
           
           print("ingrese una opcion valida")
           menu()
           
     case 2:
        print("ni idea")

     case 3:
        SystemExit
        break
       
     case _:
          
          print("Ingrese una opcion valida")
          break
menu()