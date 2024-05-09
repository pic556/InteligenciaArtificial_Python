import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from os import unlink
import pandas as pd

###
datos = pd.read_csv("argentina.csv")
print(datos)

###
lista=datos.to_numpy( ).tolist( )
print(lista)
###

lista.remove(['AC', 'ayala', 'roberto'])
print(lista)
print()


def escalaDeGrises(largo):
    if largo == 2:
        return "es de una escala de grises"
    else:
        return "es de colores"
def Graficar():    
    plt.subplot(4,4,1)
    img=mpimg.imread("fotos/emiliano martinez.jpg")
    plt.imshow(img)
    dim = img.shape
    print("emiliano martinez.jpg  es ",  escalaDeGrises(len(dim)))
    
    plt.subplot(4,4,2)
    img=mpimg.imread("fotos/cristian romero.jpg")
    plt.imshow(img)
    dim = img.shape
    print("cristian romero.jpg  es ",  escalaDeGrises(len(dim)))
    
    plt.subplot(4,4,3)
    img=mpimg.imread("fotos/nicolas tagliafico.jpg")
    plt.imshow(img)
    dim = img.shape
    print("nicolas tagliafico.jpg  es ",  escalaDeGrises(len(dim)))
    
    plt.subplot(4,4,4)
    img=mpimg.imread("fotos/gonzalo montiel.jpg")
    plt.imshow(img)
    dim = img.shape
    print("gonzalo montiel.jpg es ",  escalaDeGrises(len(dim)))
    
    
    plt.subplot(4,4,5)
    img=mpimg.imread("fotos/leandro paredes.jpg")
    plt.imshow(img)
    dim = img.shape
    print("leandro paredes.jpg  es ",  escalaDeGrises(len(dim)))
    
    
    plt.subplot(4,4,6)
    img=mpimg.imread("fotos/nicolas otamendi.jpg")
    plt.imshow(img)
    dim = img.shape
    print("nicolas otamendi.jpg  es ",  escalaDeGrises(len(dim)))
    
    plt.subplot(4,4,7)
    img=mpimg.imread("fotos/rodrigo de paul.jpg")
    plt.imshow(img)
    dim = img.shape
    print("rodrigo de paul.jpg  es ",  escalaDeGrises(len(dim)))
    
    
    plt.subplot(4,4,8)
    img=mpimg.imread("fotos/giovanni lo celso.jpg")
    plt.imshow(img)
    dim = img.shape
    print("giovanni lo celso.jpg  es ",  escalaDeGrises(len(dim)))
    
    plt.subplot(4,4,9)
    img=mpimg.imread("fotos/lautaro martinez.jpg")
    plt.imshow(img)
    dim = img.shape
    print("lautaro martinez.jpg es ",  escalaDeGrises(len(dim)))
    
    
    plt.subplot(4,4,10)
    img=mpimg.imread("fotos/leonel messi.jpg")
    plt.imshow(img)
    dim = img.shape
    print("leonel messi.jpg es ",  escalaDeGrises(len(dim)))
    
    
    plt.subplot(4,4,11)
    img=mpimg.imread("fotos/angel di maria.jpg")
    plt.imshow(img)
    dim = img.shape
    print("angel di maria.jpg  es ",  escalaDeGrises(len(dim)))
    
    
    plt.subplot(4,4,12)
    img=mpimg.imread("fotos/lionel scaloni.jpg")
    plt.imshow(img)
    dim = img.shape
    print("lionel scaloni.jpg es ",  escalaDeGrises(len(dim)))

listadoDeImagenes = [
    ("fotos/emiliano martinez.jpg", "1"),
    ("fotos/cristian romero.jpg", "2"),
    ("fotos/nicolas tagliafico.jpg", "3"),
    ("fotos/gonzalo montiel.jpg", "4"),
    ("fotos/leandro paredes.jpg", "5"),
    ("fotos/nicolas otamendi.jpg", "6"),
    ("fotos/rodrigo de paul.jpg", "7"),
    ("fotos/giovanni lo celso.jpg", "8"),
    ("fotos/lautaro martinez.jpg", "9"),
    ("fotos/leonel messi.jpg", "10"),
    ("fotos/angel di maria.jpg", "11"),
    ("fotos/lionel scaloni.jpg", "DT")
]


Graficar()
####

class Pedido:
    def __init__(self):
        pass

    def eleccion(self, datos):
        opciones = ['1) Ver un Jugador ',
                    '2) Ver Todos los jugadores', 
                    '3) Borrar un jugador']
        while True:
            # Mostrar las opciones al usuario
            print("Opciones disponibles:")
            for i, opcion in enumerate(opciones, 1):
                print(f"{i}. {opcion}")

            try:
                # Solicitar la elección al usuario
                eleccion = int(input("Seleccione una opción (1-4): "))
                if eleccion == 1:
                    jugador_seleccionado = str(input("Numero del jugador: "))
                    if jugador_seleccionado in datos["num"].values:
                        for imagen_lis, numero_lis in listadoDeImagenes:
                            if jugador_seleccionado == numero_lis:
                                plt.subplot(4,4,1)
                                img=mpimg.imread(imagen_lis)
                                plt.imshow(img)
                                plt.axis('off')  # Oculta los ejes
                                plt.title(imagen_lis)                                                                
                        break
                                
                elif eleccion == 2:
                    Graficar()
                    break
                elif eleccion == 3:
                    nombre_jugador  = str(input("Nombre del jugador: "))
                    apellido_jugador = str(input("Apellido del jugador: "))
                    if nombre_jugador in datos["nombre"].values and apellido_jugador in datos["apellido"].values:
                        lisJugNom= set(datos.loc[datos['nombre'] == nombre_jugador, 'num'].values)
                        lisJugApe= set(datos.loc[datos['apellido'] == apellido_jugador, 'num'].values)
                        interseccion = list(lisJugApe & lisJugNom)
                        if interseccion[0] in datos["num"].values:
                            for imagen_lis, numero_lis in listadoDeImagenes:
                                if interseccion[0] == numero_lis:
                                    unlink(imagen_lis)
                                    eliminacionMatrixfinal =[interseccion[0],apellido_jugador,nombre_jugador]
                                    lista.remove(eliminacionMatrixfinal)
                                    print(lista)
                    break
            except ValueError:
                print("Por favor, ingrese un número entero válido.")

            elegir = input("¿Quieres volver a seleccionar? (s o n): ")
            if elegir.lower() != "s":
                print("Adiós")
                break
                
pedido = Pedido()
pedido.eleccion(datos)