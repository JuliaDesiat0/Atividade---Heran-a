class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)
        self.num_portas = num_portas

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

carro1 = Carro("Toyota", "Corolla", 2023, 4)
print(f"Carro: {carro1.marca} {carro1.modelo}, Ano: {carro1.ano}, Número de Portas: {carro1.num_portas}")

moto1 = Moto("Honda", "CBR 600", 2022, 600)
print(f"Moto: {moto1.marca} {moto1.modelo}, Ano: {moto1.ano}, Cilindradas: {moto1.cilindradas}")
