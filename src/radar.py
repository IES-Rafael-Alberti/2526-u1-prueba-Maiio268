# programa.py
# -*- coding: utf-8 -*-
"""
Radares de tramo — Esqueleto para alumnos
- Lectura de fichero YA resuelta (función leer_casos).
- main() itera sobre las líneas y llama a procesar_linea(linea).
- procesar_linea(linea) está VACÍA; los alumnos deben implementarla.
"""

from typing import List
import sys
from pathlib import Path


def leer_casos(ruta_fichero: str) -> List[str]:
    """
    Lee un fichero de texto con casos de prueba, devolviendo
    una lista de líneas (str) ya limpias, sin la línea de terminación "0 0 0".
    Ignora líneas en blanco y comentarios que empiecen por '#'.
    """
    ruta = Path(ruta_fichero)
    if not ruta.exists():
        raise FileNotFoundError(f"No existe el fichero: {ruta_fichero}")

    casos: List[str] = []
    with ruta.open(encoding="utf-8") as f:
        for raw in f:
            linea = raw.strip()
            if not linea or linea.startswith("#"):
                continue
            if linea == "0 0 0":
                break
            casos.append(linea)
    return casos


def procesar_linea(linea: str) -> str:
    """
    TODO: Implementar por el alumnado.

    Recibe:
        linea (str): cadena con tres enteros: distancia_m, vmax_kmh, tiempo_s,
                     separados por espacios.

    Debe devolver uno de los textos EXACTOS:
        - "OK"
        - "MULTA"
        - "PUNTOS"
        - "ERROR"

    Recomendación:
    1) Parsear ints; si hay problema o valores inválidos -> "ERROR".
    2) Calcular la velocidad media y compararla con los umbrales.
    3) Devolver el texto pedido.
    """
    # Primero separo la cadena en variables, despues convierto las variables a int
    texto = "ERROR"
    partes_linea = linea.split(" ")

    if len(partes_linea) != 3:
        return texto

    if not (partes_linea[0].isdigit() and partes_linea[1].isdigit() and partes_linea[2].isdigit()):
        return texto

    distancia_m = partes_linea[0]
    vmax_kmh = partes_linea[1]
    tiempo_s = partes_linea[2]
    
    # Las convierto a enteros
    distancia = int(distancia_m)
    velocidad_max = int(vmax_kmh)
    tiempo = int(tiempo_s)
    if distancia <= 0 or velocidad_max <= 0 or tiempo <= 0:
        return texto
    
    # Calculo velocidad media
    velocidad_media = (distancia/tiempo) * 3.6
    
    # Comparo velocidad media con velocidad maxima
    diferencia = velocidad_media-velocidad_max
    if velocidad_media <= velocidad_max:
        texto = "OK"
    elif velocidad_media > velocidad_max and diferencia < velocidad_max*0.2:
        texto = "MULTA"
    elif velocidad_media > velocidad_max and diferencia >= velocidad_max*0.2:
        texto = "PUNTOS"

    return texto
    
    # --- Implementación del alumnado aquí ---
    raise NotImplementedError("Función aún no implementada por el alumnado.")

# a main se llama de la siguiente forma  main(sys.argv)
def main(argv: List[str]) -> None:
    if len(argv) < 2:
        print("Uso: python programa.py <ruta_entrada.txt>")
        sys.exit(1)

    ruta = argv[1]
    for linea in leer_casos(ruta):
        resultado = procesar_linea(linea)   # <- llamada a la función de los alumnos
        print(resultado)                     # <- impresión del resultado

if __name__ == "__main__":
    main(sys.argv)
