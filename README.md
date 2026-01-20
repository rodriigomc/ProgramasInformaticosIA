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



---

## Extensión — Dos matrices: entrenamiento vs despliegue (+ coste operación)

### Matriz 1: Lenguaje para **entrenamiento** (ML/EDA/pipeline offline)
**Objetivo:** máxima productividad y ecosistema IA/ML.

| Criterio | Peso (1–5) | Python (1–5) | R (1–5) | Java (1–5) | Node (1–5) |
|---|---:|---:|---:|---:|---:|
| Ecosistema IA/ML (librerías, comunidad) | 5 | 5 | 4 | 3 | 2 |
| Productividad / prototipado | 5 | 5 | 4 | 3 | 3 |
| Rendimiento / latencia | 2 | 3 | 2 | 4 | 3 |
| Concurrencia / I-O / servicios | 1 | 3 | 2 | 4 | 4 |
| Integración Big Data (Spark, conectores) | 3 | 4 | 3 | 5 | 3 |
| Despliegue y portabilidad | 2 | 4 | 3 | 4 | 4 |
| Mantenibilidad / tipado / tooling | 2 | 3 | 2 | 5 | 3 |
| Talento disponible (equipo) | 3 | 5 | 2 | 4 | 4 |
| Coste operación / infraestructura | 2 | 4 | 4 | 3 | 4 |
| **TOTAL ponderado** |  |  |  |  |  |

#### Cálculo del total ponderado (Entrenamiento)
- **Python** = 5×5 + 5×5 + 2×3 + 1×3 + 3×4 + 2×4 + 2×3 + 3×5 + 2×4  
  = 25 + 25 + 6 + 3 + 12 + 8 + 6 + 15 + 8 = **108**
- **R** = 5×4 + 5×4 + 2×2 + 1×2 + 3×3 + 2×3 + 2×2 + 3×2 + 2×4  
  = 20 + 20 + 4 + 2 + 9 + 6 + 4 + 6 + 8 = **79**
- **Java** = 5×3 + 5×3 + 2×4 + 1×4 + 3×5 + 2×4 + 2×5 + 3×4 + 2×3  
  = 15 + 15 + 8 + 4 + 15 + 8 + 10 + 12 + 6 = **93**
- **Node** = 5×2 + 5×3 + 2×3 + 1×4 + 3×3 + 2×4 + 2×3 + 3×4 + 2×4  
  = 10 + 15 + 6 + 4 + 9 + 8 + 6 + 12 + 8 = **78**

| Lenguaje | Total ponderado (Entrenamiento) |
|---|---:|
| **Python** | **108** |
| Java | 93 |
| R | 79 |
| Node | 78 |

**Conclusión (Entrenamiento, 8–10 líneas)**  
Para entrenamiento, **gana Python** claramente por su superioridad en **ecosistema IA/ML** (librerías, comunidad, ejemplos, soporte) y por la **productividad** que ofrece para iterar modelos rápido.  
R es fuerte en análisis y estadística, pero se queda atrás en tooling general y despliegue.  
Java y Node pueden entrenar, pero suelen ser menos eficientes para experimentación y acceso a librerías punteras.  
Riesgo técnico: que el entorno Python se vuelva “frágil” por dependencias, versiones y reproducibilidad.  
Mitigación: usar **requirements.txt**, entornos virtuales, fijar versiones, y si el proyecto crece, contenedores (Docker) y buenas prácticas de MLOps.

---

### Matriz 2: Lenguaje para **despliegue** (API de predicciones en producción)
**Objetivo:** baja latencia, buena concurrencia, robustez y operaciones.

| Criterio | Peso (1–5) | Python (1–5) | R (1–5) | Java (1–5) | Node (1–5) |
|---|---:|---:|---:|---:|---:|
| Ecosistema IA/ML (librerías, comunidad) | 2 | 5 | 4 | 3 | 2 |
| Productividad / prototipado | 2 | 4 | 3 | 3 | 4 |
| Rendimiento / latencia | 5 | 3 | 2 | 5 | 4 |
| Concurrencia / I-O / servicios | 5 | 3 | 2 | 5 | 5 |
| Integración Big Data (Spark, conectores) | 3 | 4 | 3 | 5 | 3 |
| Despliegue y portabilidad | 4 | 4 | 3 | 5 | 4 |
| Mantenibilidad / tipado / tooling | 4 | 3 | 2 | 5 | 3 |
| Talento disponible (equipo) | 3 | 5 | 2 | 4 | 4 |
| Coste operación / infraestructura | 4 | 4 | 3 | 3 | 4 |
| **TOTAL ponderado** |  |  |  |  |  |

#### Cálculo del total ponderado (Despliegue)
- **Python** = 2×5 + 2×4 + 5×3 + 5×3 + 3×4 + 4×4 + 4×3 + 3×5 + 4×4  
  = 10 + 8 + 15 + 15 + 12 + 16 + 12 + 15 + 16 = **119**
- **R** = 2×4 + 2×3 + 5×2 + 5×2 + 3×3 + 4×3 + 4×2 + 3×2 + 4×3  
  = 8 + 6 + 10 + 10 + 9 + 12 + 8 + 6 + 12 = **81**
- **Java** = 2×3 + 2×3 + 5×5 + 5×5 + 3×5 + 4×5 + 4×5 + 3×4 + 4×3  
  = 6 + 6 + 25 + 25 + 15 + 20 + 20 + 12 + 12 = **141**
- **Node** = 2×2 + 2×4 + 5×4 + 5×5 + 3×3 + 4×4 + 4×3 + 3×4 + 4×4  
  = 4 + 8 + 20 + 25 + 9 + 16 + 12 + 12 + 16 = **122**

| Lenguaje | Total ponderado (Despliegue) |
|---|---:|
| **Java** | **141** |
| Node | 122 |
| Python | 119 |
| R | 81 |

**Conclusión (Despliegue, 8–12 líneas)**  
Para desplegar una API de predicción en producción, **gana Java** por su rendimiento, baja latencia, concurrencia sólida y tooling maduro para servicios.  
Node también es muy competitivo en servicios I/O y escalado, quedando cerca cuando el cuello es la capa web.  
Python puede servir modelos rápido, pero puede requerir más cuidado para escalar y mantener latencias estables bajo carga.  
Riesgo técnico: si despliegas en Java/Node, debes asegurar compatibilidad entre el entrenamiento (Python) y el servicio.  
Mitigación: separar en microservicios: **Python para entrenar y preparar el modelo** + **Java/Node como API**; además, usar un formato de exportación/serving o un servicio de inferencia dedicado.  
Así se consigue un sistema equilibrado: velocidad de ML + robustez operativa.

