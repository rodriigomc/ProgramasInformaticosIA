## Reto 1 — Matriz de decisión: ¿qué lenguaje elegirías y por qué?
**Escenario elegido:** A) Entrenar un modelo y desplegarlo como API para predicciones.

| Criterio | Peso (1–5) | Python (1–5) | R (1–5) | Java (1–5) | Node (1–5) |
|---|---:|---:|---:|---:|---:|
| Ecosistema IA/ML (librerías, comunidad) | 5 | 5 | 4 | 3 | 2 |
| Productividad / prototipado | 5 | 5 | 4 | 3 | 4 |
| Rendimiento / latencia | 4 | 3 | 2 | 5 | 4 |
| Concurrencia / I-O / servicios | 4 | 3 | 2 | 5 | 5 |
| Integración Big Data (Spark, conectores) | 3 | 4 | 3 | 5 | 3 |
| Despliegue y portabilidad | 4 | 4 | 3 | 5 | 4 |
| Mantenibilidad / tipado / tooling | 3 | 3 | 2 | 5 | 3 |
| Talento disponible (equipo) | 3 | 5 | 2 | 4 | 4 |
| **TOTAL ponderado** |  |  |  |  |  |

### Cálculo del total ponderado
- **Python** = 5×5 + 5×5 + 4×3 + 4×3 + 3×4 + 4×4 + 3×3 + 3×5  
  = 25 + 25 + 12 + 12 + 12 + 16 + 9 + 15 = **126**
- **R** = 5×4 + 5×4 + 4×2 + 4×2 + 3×3 + 4×3 + 3×2 + 3×2  
  = 20 + 20 + 8 + 8 + 9 + 12 + 6 + 6 = **89**
- **Java** = 5×3 + 5×3 + 4×5 + 4×5 + 3×5 + 4×5 + 3×5 + 3×4  
  = 15 + 15 + 20 + 20 + 15 + 20 + 15 + 12 = **132**
- **Node** = 5×2 + 5×4 + 4×4 + 4×5 + 3×3 + 4×4 + 3×3 + 3×4  
  = 10 + 20 + 16 + 20 + 9 + 16 + 9 + 12 = **112**

| Lenguaje | Total ponderado |
|---|---:|
| **Java** | **132** |
| Python | 126 |
| Node | 112 |
| R | 89 |

### Conclusión (8–12 líneas)
En el escenario A (entrenar y desplegar como API), **gana Java** por su ventaja técnica en **latencia, concurrencia, robustez en servicios y portabilidad** en producción, además de su buena integración con ecosistemas de Big Data como **Spark**.  
**Python queda muy cerca** gracias a su dominio absoluto en **IA/ML** y rapidez de prototipado, pero sufre más cuando la API requiere **alto rendimiento y escalado** en producción.  
El principal **riesgo técnico** de elegir Java como lenguaje principal es perder velocidad en experimentación y acceso directo a librerías punteras de ML (muchas nacen primero en Python).  
Para **mitigarlo**, la estrategia más sólida es **Python para entrenamiento y experimentación** (notebooks, pipelines de ML) y **Java (o Node) para servir el modelo** como API en producción.  
El modelo puede exportarse (por ejemplo, a un formato interoperable) o servirse mediante un microservicio dedicado.  
Así se combina lo mejor de ambos mundos: **productividad y ecosistema ML** en Python + **rendimiento y escalabilidad** en Java/Node.
