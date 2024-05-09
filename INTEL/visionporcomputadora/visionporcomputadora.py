import cv2
import random

img1 = cv2.imread("1.png")
img2 = cv2.imread("2.png")
img3 = cv2.imread("3.png")


def rojo():
    cv2.imshow("Rojo",img1)
    cv2.waitKey(2000)
    cv2.destroyAllWindows( )
    print("DETENERSE")
    
def amarillo():
    cv2.imshow("Amarillo",img2)
    cv2.waitKey(2000)
    cv2.destroyAllWindows( )
    print("ATENCION")

def verde():    
    cv2.imshow("Verde",img3)
    cv2.waitKey(2000)
    cv2.destroyAllWindows( )
    print("AVANZAR")


def ciclosAleatoriosSemaforoRandom(numero_ciclos):
    for i in range(numero_ciclos):
        lista_numeros = [random.randint(1, 3) for j in range(3)]
        for numero_random in lista_numeros:
            if(numero_random == 1):
                verde()
            elif(numero_random == 2):
                amarillo()
            else:
                rojo()

numero_ciclos = int(input("Por favor, ingresa un número de ciclos: "))

ciclosAleatoriosSemaforoRandom(numero_ciclos)