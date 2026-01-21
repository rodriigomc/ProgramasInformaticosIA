import json
from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris  # puedes cambiar por load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix


def main():
    # -------------------------
    # 1) Cargar dataset
    # -------------------------
    data = load_iris()  # alternativa: load_breast_cancer()

    # -------------------------
    # 2) Convertir a DataFrame
    # -------------------------
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target, name="target")

    df = X.copy()
    df["target"] = y

    # -------------------------
    # 3) Info básica
    # -------------------------
    print("\n=== HEAD ===")
    print(df.head())

    print("\n=== DESCRIBE ===")
    print(df.describe())

    # -------------------------
    # 4) EDA mínima: 1 gráfico
    # -------------------------
    # Histograma de una feature (ej: sepal length)
    col = data.feature_names[0]
    plt.figure()
    df[col].hist(bins=20)
    plt.title(f"Histograma: {col}")
    plt.xlabel(col)
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.savefig("eda_plot.png", dpi=150)
    plt.close()

    # Comentario de observación (obligatorio):
    # Observación: el histograma muestra que hay rangos de valores con más frecuencia;
    # en iris suele haber solapamiento entre clases en algunas features, lo que sugiere
    # que el modelo necesitará combinar varias características para separar bien las clases.

    # -------------------------
    # 5) Entrenamiento: split
    # -------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # -------------------------
    # 6) Pipeline: scaler + modelo
    # -------------------------
    pipeline = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("model", LogisticRegression(max_iter=1000, random_state=42)),
        ]
    )

    pipeline.fit(X_train, y_train)

    # -------------------------
    # 7) Evaluación
    # -------------------------
    y_pred = pipeline.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average="macro")  # multiclase => macro
    cm = confusion_matrix(y_test, y_pred)

    print("\n=== MÉTRICAS ===")
    print(f"accuracy: {acc:.4f}")
    print(f"f1_macro: {f1:.4f}")
    print("confusion_matrix:")
    print(cm)

    # -------------------------
    # 8) Persistencia: modelo + métricas
    # -------------------------
    joblib.dump(pipeline, "model.joblib")

    metrics = {
        "dataset": "iris",
        "model": "LogisticRegression",
        "accuracy": acc,
        "f1_macro": f1,
        "confusion_matrix": cm.tolist(),  # JSON no soporta numpy arrays
        "test_size": 0.2,
        "random_state": 42,
    }

    Path("metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    print("\n[OK] Guardado model.joblib y metrics.json")
    print("[OK] Guardado eda_plot.png (gráfico EDA)")


if __name__ == "__main__":
    main()
