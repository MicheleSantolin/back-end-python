# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
# Crie uma instância da classe carro.


class Carro:
    def __init__(self, cor, modelo, ligado=False, velocidade=0):
        self.ligado = ligado
        self.cor = cor
        self.modelo = modelo
        self.velocidade = velocidade

    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False

    def acelera(self):
        if self.ligado:
            self.velocidade += 10

    def desacelera(self):
       if self.ligado and self.velocidade > 0:
           self.velocidade -= 10   

# Crie uma instância da classe carro:
meu_carro = Carro(cor="Prata", modelo="Ônix")

meu_carro.ligar()

# Faça o carro "andar" utilizando os métodos da sua classe.
meu_carro.acelera()
###VOCÊ TAMBÉM PODE ACELERAR ELE ASSIM:
##[meu_carro.acelera() for _ in range(5)]

print(f"Velocidade atual:", meu_carro.velocidade)

# Faça o carro "parar" utilizando os métodos da sua classe.
meu_carro.desacelera()

print(f"Velocidade após desacelerar:", meu_carro.velocidade)






