import datetime as dt

class Cambio:
  TAXAS = 0.9 / 100

  def __init__(self, moeda_original, moeda_destino, valor_cambio, transacao):
    self.moeda_original = moeda_original
    self.moeda_destino = moeda_destino
    self.valor_cambio = valor_cambio
    self.transacao = transacao
    self.total = self.calcular_cambio(transacao, valor_cambio)
    self.data = dt.datetime.now().date()
    self.hora = dt.datetime.now().time()
    
  @staticmethod
  def calcular_cambio(transacao, valor_cambio):
    return transacao * valor_cambio * (1 - Cambio.TAXAS)