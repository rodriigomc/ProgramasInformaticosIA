# Reto 2 — Benchmark: bucle Python vs NumPy
- Tamaño del array (N): **5.000.000**
- dtype: **<class 'numpy.float64'>**
- Repeticiones por versión: **3**

## Resultados
| Versión | Tiempo 1 (s) | Tiempo 2 (s) | Tiempo 3 (s) | Promedio (s) |
|---|---:|---:|---:|---:|
| Python loop | 0.442226 | 0.425846 | 0.385117 | **0.417729** |
| NumPy vectorizado | 0.030852 | 0.030630 | 0.030705 | **0.030729** |

**Ratio de mejora (Python loop / NumPy):** **13.59×**

## Conclusión
- NumPy es mucho más rápido porque ejecuta operaciones vectorizadas en C/Fortran y evita el coste del bucle en Python.
- El bucle Python itera elemento a elemento en el intérprete, lo que introduce una sobrecarga enorme.
- Optimizar importa cuando el código se ejecuta muchas veces, con grandes volúmenes de datos o en producción.
- Si el cuello de botella está en operaciones numéricas, conviene usar NumPy/SciPy, vectorización o herramientas como Numba.
