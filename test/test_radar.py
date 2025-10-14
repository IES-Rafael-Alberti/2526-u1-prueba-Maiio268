# test_radares.py
# -*- coding: utf-8 -*-

import pytest
from solucion import procesar_linea

@pytest.mark.parametrize(
    "linea, esperado",
    [
        # Casos del enunciado:
        ("9165 110 300", "OK"),
        ("9165 110 299", "MULTA"),
        ("12000 100 433", "OK"),
        ("12000 100 431", "MULTA"),
        ("12000 100 359", "PUNTOS"),
        ("-1000 -50 -100", "ERROR"),

        # Bordes y sanity checks:
        ("1000 100 36", "OK"),        # v = 100 km/h exacto -> OK
        ("1000 100 30", "PUNTOS"),    # v = 120 km/h exacto -> PUNTOS (>= 20%)
        ("1000 100 35", "MULTA"),     # entre 100 y 120 -> MULTA
        ("1000 100 0", "ERROR"),      # tiempo cero -> ERROR
        ("0 100 30", "ERROR"),        # distancia cero -> ERROR
        ("1000 0 30", "ERROR"),       # vmax cero -> ERROR
        ("  9165   110   300  ", "OK"),  # espacios extra
        ("abc def ghi", "ERROR"),     # parseo inválido
    ]
)

# Debes darle contenido a la siguiente función
def test_procesar_linea(linea, esperado):
   
