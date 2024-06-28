import json


def agregar_categoria(nombre:str):
    with open("biblioteca.json", mode="r")as lecturajson:
        leerjson = json.load(lecturajson)
    new_categoria = {
        "CategoriaID": len(leerjson["Categoria"])+1,
        "Nombre":nombre
    }

    leerjson["Categoria"].append(new_categoria)

    with open("biblioteca.json", mode="w")as lecturajson:
        json.dump(leerjson,lecturajson,indent=4)

def editar_categoria(id:int):
    with open("biblioteca.json", mode="r")as lecturajson:
        leerjson = json.load(lecturajson)
        contador = 0 

        for p in leerjson["Categoria"]:
            if p["CategoriaID"]== id:
                print("encontrado")
                break
        contador =+ 1
    leerjson["Categoria"][contador]["Nombre"]=input("Ingrese un nombre para editar : ")
    with open("biblioteca.json", mode="w")as lecturajson:
        json.dump(leerjson,lecturajson,indent=4)


def eliminar_categoria(delete_categ:str):
    with open("biblioteca.json", mode="r")as lecturajson:
        leerjson = json.load(lecturajson)
        contador = 0
        for f in leerjson["Categoria"]:
            if f["CategoriaID"]==delete_categ:
             print(f)
             break
        contador =+1
        del leerjson["Categoria"][contador]    
    with open("biblioteca.json", mode="w")as lecturajson:
     json.dump(leerjson,lecturajson,indent=4)


def buscar_categoria():
    with open("biblioteca.json", mode="r")as lecturajson:
        leerjson = json.load(lecturajson)
        for q in leerjson["Categoria"]:
            print(q)



        





