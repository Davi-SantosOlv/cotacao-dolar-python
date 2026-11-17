import requests
from Cambio import Cambio

def trocar_moedas(moeda_original, moeda_destino):
  while True:
    try:
      transacao = float(input("Digite o valor a ser trocado: ").replace(",", "."))
      if transacao <= 0:
        print("Digite um valor maior que zero!")
        continue
      else:
        break
          
    except ValueError:
      print("Digite um valor numérico!")
  
  r = requests.get("https://economia.awesomeapi.com.br/json/last/" + moeda_original + "-" + moeda_destino)
  cotacao = r.json()
  
  valor_cambio = float(cotacao[moeda_original + moeda_destino]["ask"])
  total = Cambio.calcular_cambio(transacao, valor_cambio)
  
  conf = input(f"Você receberá R${total:.2f} neste câmbio. Confirmar Transação? (Y/n): ").capitalize()
  if conf == "N":
    print("A transação não foi efetuada.\n")
  else:   
    cambio = Cambio(moeda_original, moeda_destino, valor_cambio, transacao)
    print("Câmbio concluído com sucesso!")

def main():
  while True:
    print("*** CASA DE CÂMBIO ***")
    print("[1] Trocar USD -> BRL")
    print("[2] Trocar BRL -> USD")
    print("[3] Visualizar câmbios")
    print("[4] Sair")
    op = input("Digite uma opção: ")

    if op == "1":
      trocar_moedas("USD", "BRL")

    elif op == "2":
      trocar_moedas("BRL", "USD")

    elif op == "3":
      pass

    elif op == "4":
      pass

    else:
      print("Opção inválida!\n")


if __name__ == "__main__":
  main()