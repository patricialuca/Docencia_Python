def calcular_combustible(distancia, peso):
   consumo = (distancia * peso) / 500
   if peso > 5000:
      return consumo * 1.5
   else:
      return consumo