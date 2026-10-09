import csv
from pathlib import Path
import joblib
from .contracts import Entrada, Salida


def leer_csv(ruta: Path) -> list[Entrada]:
    # TODO
    with open(ruta_archivo, mode='r', encoding='utf-8') as f: 
        reader=csv.DictReader(f)

        for row_dict in reader:
            print(row_dict)

            data = Entrada(**row_dict)
            peso_kg = round(data["peso_kg"], ndigits=1)
            distancia_km = round(data["distancia_km"], ndigits=1)

        
def preprocesar(entrada: Entrada) -> list[float]:
    # TODO
        
    peso_kg = round(number=Entrada.peso_kg, ndigits=1)
    distancia_km = round(number=Entrada.peso_kg, ndigits=1)
        

def cargar_modelo(ruta: Path):
    # TODO
    model = joblib.load(Path)

def predecir(entrada: Entrada, modelo) -> Salida:
    # TODO
    


def guardar_csv(resultados: list[Salida], ruta: Path) -> None:
    # TODO
    raise NotImplementedError


def ejecutar(entrada: Path, modelo: Path, salida: Path) -> None:
    # TODO
    raise NotImplementedError


if __name__ == "__main__":
    ejecutar(
        Path("data/raw/paquetes.csv"),
        Path("models/modelo.joblib"),
        Path("resultados.csv"),
    )
