#Autor: Katia Hernández Barrera
#Programa que dibuja figuras simulando un espirógrafo

import pygame   # Librería de pygame
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
VIOLETA = (139,0,139)

# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r,R,l):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde diRbujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        for angulo in range(0, 360 * (r // math.gcd(r, R))):
            a = math.radians(angulo)
            k = r / R
            x = R * (((1*k)*math.cos(a)) + (l*k*math.cos(((l-k)*a)/k)))
            y = R * (((1*k)*math.sin(a)) - (l*k*math.sin(((l-k)*a)/k)))
            pygame.draw.circle (ventana, VIOLETA , (int(x + ANCHO // 2), int(ALTO // 2 - y)), 1)





        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    R = int(input("inserte R: "))
    r = int(input("inserte r: "))
    l = float(input("inserte l: "))
    dibujar(r,R,l)



# Llamas a la función principal
main()