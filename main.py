# Importamos las librerías
import motor
import clima
import fisica
import seguridad
# importamos una libreria predefinida
import time

# Fase 1  --> Autenticación en el módulo de seguridad
# El programa se inicia y da la bienvenida
print("--- NASA CONTROL CENTER ---")

# Solicitamos al usuario la contraseña
pass_usuario = input("Introduzca la contraseña de lanzamiento: ")

# ahora comprobamos si la contraseña introducida es correcta
if seguridad.verificar_codigo(pass_usuario) == False:
    print("Acceso denegado")
else:
    print("Acceso conseguido")
    # Fase 2 --> Chequeo atmosférico
    # solicitamos al usuario las condiciones meteorológicas
    vel_viento = float(input("Velocidad del viento actual (km/h): "))
    hay_lluvia = input("¿Está lloviendo? (si/no): ")

    if clima.es_seguro_lanzar(vel_viento, hay_lluvia) == False:
        print("Condiciones climáticas adversas, Misión abortada")
    else:
        # Fase 3 -->
        # Planificamos el vuelo y pedimos los datos técnicos de la misión
        distancia_lunar = float(input("Distancia al objetivo (km): "))
        peso_nave = float(input("Peso de la nave (kg): "))
        velocidad_nave = float(input("Velocidad de la nave (km/h): "))

        # Realizamos los calculos
        combustible = motor.calcular_combustible(distancia_lunar, peso_nave)
        tiempo = fisica.tiempo_llegada(distancia_lunar, velocidad_nave)

        # Mostramos los resultados finales

    print("----------------- RESUMEN DE LA MISIÓN ------------------")
    print(f"Combustible necesario: {round(combustible, 2 )} litros")
    print(f"Tiempo estimado de vuelo: {round(tiempo, 2 )} horas")
    print("----------------- RESUMEN DE LA MISIÓN ------------------")

    print("Preparados para el lanzamiento...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    print("Ignición, buen viaje artemisa!")