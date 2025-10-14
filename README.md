[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/bpj379cM)
# Radares de tramo"

Decidir si un vehículo recibe OK, MULTA o PUNTOS a partir de distancia, velocidad máxima y tiempo, evitando decimales con comparaciones entre enteros.

[Leelo la descripción completa del problema aqui](https://aceptaelreto.com/problem/statement.php?id=112&cat=4)

## 1. Contexto
Los **radares de tramo** calculan la **velocidad media** entre dos cámaras. Si esa media supera la **velocidad máxima** del tramo, se sanciona.  
Para evitar errores de redondeo, **no usaremos decimales**: compararemos productos de enteros equivalentes a la fórmula de la velocidad media.


## 2. Enunciado
Escribe un programa que procese **múltiples casos**. Cada caso contiene tres enteros:
- **d**: distancia entre cámaras en **metros**  
- **vmax**: velocidad máxima permitida en **km/h**  
- **t**: tiempo empleado en **segundos**

La entrada termina con la línea `0 0 0` (que **no** se procesa).

Para cada caso, el programa imprimirá **una línea** con uno de estos valores exactos:
- `OK` — si la velocidad media **no supera** la velocidad máxima.  
- `MULTA` — si la supera **pero menos del 20%**.  
- `PUNTOS` — si la supera **al 20% o más**.  
- `ERROR` — si los datos del caso son **inválidos** (no enteros o ≤ 0).


## 3. Datos de entrada
- Varias líneas, cada una con **tres enteros** separados por espacios: `d vmax t`.
- Acaba con `0 0 0`.

## 4. Datos de salida
- Una línea por caso con **uno** de los textos: `OK`, `MULTA`, `PUNTOS`, `ERROR`.


## 6. Ejemplo de entrada
```

9165 110 300
9165 110 299
12000 100 433
12000 100 431
12000 100 359
-1000 -50 -100
0 0 0

```

## 7. Ejemplo de salida
```

OK
MULTA
OK
MULTA
PUNTOS
ERROR

````


## 8. Tarea del alumnado
- La **lectura** de líneas desde fichero y el **bucle principal** están **resueltos** por el docente.
- Debes implementar **solo** la función:

**Firma esperada (ejemplo en Python):**
```python
def procesar_linea(linea: str) -> str:
    """
    Recibe: 'd vmax t' (tres enteros en una misma cadena).
    Devuelve: 'OK' | 'MULTA' | 'PUNTOS' | 'ERROR'
    """
```

- Implementa una función test para probar tu función.

```python
def test_procesar_linea(linea, esperado):
    """
    Linea:  tres enteros en una misma cadena.
    esperado: 'OK' | 'MULTA' | 'PUNTOS' | 'ERROR'
    """
```



**Pautas:**

* **No uses listas**: separa la cadena con `split()` y asigna a tres variables.
* Convierte a `int` y **valida** que los tres sean **mayores que 0**.
* Aplica las **comparaciones enteras** del apartado 5.
* Devuelve exactamente las cadenas pedidas (sensible a mayúsculas).



## 10. Verificación (opcional)

El docente proporciona un conjunto de **tests con `pytest`** para verificar tu función.
Ejecuta:

```bash
pip install -U pytest
pytest -q
```

