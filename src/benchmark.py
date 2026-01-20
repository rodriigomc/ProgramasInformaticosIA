import time
import numpy as np
import cProfile
import pstats
from pathlib import Path


# -------------------------
# Configuración del experimento
# -------------------------
N = 5_000_000  # puedes subir a 10_000_000 o 20_000_000 si tu PC aguanta
REPEATS = 3
SEED = 42


def operation_python_loop(x: np.ndarray) -> float:
    """
    Versión A: bucle Python (for)
    Calcula: sum((x - mean)**2)
    """
    mean = float(np.mean(x))  # mean lo calculo con numpy para no meter más ruido
    total = 0.0
    for v in x:  # iterar numpy array en Python es lento (justo lo que queremos medir)
        d = float(v) - mean
        total += d * d
    return total


def operation_numpy_vectorized(x: np.ndarray) -> float:
    """
    Versión B: NumPy vectorizado
    Calcula: sum((x - mean)**2)
    """
    mean = x.mean()
    return float(((x - mean) ** 2).sum())


def time_func(func, x: np.ndarray, repeats: int = 3) -> tuple[float, list[float], float]:
    """
    Devuelve:
    - promedio
    - lista de tiempos
    - resultado numérico (para comprobar que ambas versiones calculan lo mismo)
    """
    times = []
    result = None
    for _ in range(repeats):
        t0 = time.perf_counter()
        result = func(x)
        t1 = time.perf_counter()
        times.append(t1 - t0)
    avg = sum(times) / len(times)
    return avg, times, float(result)


def write_benchmarks_md(path: str, n: int, dtype: str, results: dict):
    """
    Crea/actualiza benchmarks.md con una tabla y conclusión.
    """
    out = []
    out.append("# Reto 2 — Benchmark: bucle Python vs NumPy\n")
    out.append(f"- Tamaño del array (N): **{n:,}**\n".replace(",", "."))
    out.append(f"- dtype: **{dtype}**\n")
    out.append(f"- Repeticiones por versión: **{REPEATS}**\n\n")

    out.append("## Resultados\n")
    out.append("| Versión | Tiempo 1 (s) | Tiempo 2 (s) | Tiempo 3 (s) | Promedio (s) |\n")
    out.append("|---|---:|---:|---:|---:|\n")

    for name, data in results.items():
        t = data["times"]
        avg = data["avg"]
        out.append(f"| {name} | {t[0]:.6f} | {t[1]:.6f} | {t[2]:.6f} | **{avg:.6f}** |\n")

    ratio = results["Python loop"]["avg"] / results["NumPy vectorizado"]["avg"]
    out.append("\n")
    out.append(f"**Ratio de mejora (Python loop / NumPy):** **{ratio:.2f}×**\n\n")

    out.append("## Conclusión\n")
    out.append(
        "- NumPy es mucho más rápido porque ejecuta operaciones vectorizadas en C/Fortran y evita el coste del bucle en Python.\n"
        "- El bucle Python itera elemento a elemento en el intérprete, lo que introduce una sobrecarga enorme.\n"
        "- Optimizar importa cuando el código se ejecuta muchas veces, con grandes volúmenes de datos o en producción.\n"
        "- Si el cuello de botella está en operaciones numéricas, conviene usar NumPy/SciPy, vectorización o herramientas como Numba.\n"
    )

    Path(path).write_text("".join(out), encoding="utf-8")


def main(dtype=np.float64, profile: bool = False):
    # Generación de datos
    rng = np.random.default_rng(SEED)
    x = rng.random(N, dtype=dtype)  # array grande

    # Ejecutar benchmarks
    results = {}

    # Profilado opcional: perfilar SOLO la versión lenta (bucle)
    if profile:
        print("\n[INFO] Ejecutando perfilado (cProfile) del bucle Python...")
        profiler = cProfile.Profile()
        profiler.enable()
        _ = operation_python_loop(x)
        profiler.disable()

        stats_path = "profile_python_loop.txt"
        with open(stats_path, "w", encoding="utf-8") as f:
            ps = pstats.Stats(profiler, stream=f).sort_stats("tottime")
            ps.print_stats(25)
        print(f"[OK] Perfil guardado en {stats_path}")

    # Medir tiempos
    avg_a, times_a, res_a = time_func(operation_python_loop, x, REPEATS)
    avg_b, times_b, res_b = time_func(operation_numpy_vectorized, x, REPEATS)

    # Guardar resultados
    results["Python loop"] = {"avg": avg_a, "times": times_a, "res": res_a}
    results["NumPy vectorizado"] = {"avg": avg_b, "times": times_b, "res": res_b}

    # Verificación simple (no exacta al 100% por floating point)
    diff = abs(res_a - res_b)
    print("\n=== RESULTADOS ===")
    print(f"Python loop avg: {avg_a:.6f} s  | runs: {times_a}")
    print(f"NumPy vector avg: {avg_b:.6f} s  | runs: {times_b}")
    print(f"Ratio mejora: {avg_a / avg_b:.2f}x")
    print(f"Diferencia resultados |A-B|: {diff:.6f}")

    # Exportar a benchmarks.md
    write_benchmarks_md("benchmarks.md", N, str(dtype), results)
    print("\n[OK] benchmarks.md actualizado.")


if __name__ == "__main__":
    # Cambia a True si quieres perfilado
    main(dtype=np.float64, profile=False)

