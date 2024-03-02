from FUNCIONES import *

def preguntar():

    print("BIENVENIDO A LA TIENDA")

    while True:
        print("""
            [P] - Perfumeria
            [F] - Farmacia
            [C] - Cosmeticos""")
        
        try:
            mi_rubro = input("elija su rubro: ").upper()
            ["P", "F", "C"].index(mi_rubro)
        except:
            print("esa no es una opción valida")
        else:
            break
    numeros = decorador(mi_rubro)

def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("quieres sacar otro turno? [S] [N]").upper()
            ["S", "N"].index(otro_turno)
        except:
            print("Esa no es una opción valida")
        else:
            if otro_turno =="N":
                print("Gracias por su visita")
                break
inicio()
