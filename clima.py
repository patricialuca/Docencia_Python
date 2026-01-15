def es_seguro_lanzar(velocidad_viento, esta_lloviendo):
    if (velocidad_viento < 30) and (esta_lloviendo =="no"):
        return True
    else:
        return False