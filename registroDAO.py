import os
import csv
from cambio import Cambio

def criar_csv():
  if not os.path.exists("registros.csv"):
    open("registros.csv", "w")

  if os.path.getsize("registros.csv") == 0:
    with open("registros.csv", "w", newline="", encoding="utf-8") as arq:
      c = csv.writer(arq)
      c.writerow(["moeda_original", "moeda_destino", "data", "hora", "valor_cambio", "transacao", "total"])

def registrar_cambio(cambio: Cambio):
  try:
    with open("registros.csv", "a", newline="", encoding="utf-8") as arq:
      c = csv.writer(arq)
      c.writerow([
        cambio.moeda_original,
        cambio.moeda_destino,
        cambio.data,
        cambio.hora,
        cambio.valor_cambio,
        cambio.transacao,
        cambio.total
      ])

  except FileNotFoundError:
    print("O arquivo não existe! Criando novo arquivo\n")
    criar_csv()

def visualizar_registros():
  try:
    with open("registros.csv", "r", newline="", encoding="utf-8") as arq:
      c = csv.DictReader(arq)

      print("\nORIGEM | DESTINO |    DATA    | VALOR ORIGINAL | VALOR CAMBIADO")
      for registro in c:
        print(f"{registro["moeda_original"]:<6} | {registro["moeda_destino"]:<7} | {registro["data"]} | "
              f"${float(registro["transacao"]):<13.2f} | ${float(registro["total"]):<14.2f}")
      print()

  except FileNotFoundError:
    print("O arquivo não existe! Criando novo arquivo\n")
    criar_csv()