def tiempo_llegada(distancia, velocidad):
    if velocidad == 0:
        return 0
    tiempo = distancia / velocidad
    return tiempo