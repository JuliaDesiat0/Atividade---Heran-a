class Empregado:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente(Empregado):
    def __init__(self, nome, salario, empresa):
        super().__init__(nome, salario)
        self.empresa = empresa


empregado1 = Empregado ('Julia', 1000.00)
print(f"Empregado: {empregado1.nome}, Salário: R${empregado1.salario}")

gerente1 = Gerente ('Julia', 1500.00, 'SENAI')
print(f"Gerente: {gerente1.nome}, Salário: R${gerente1.salario}, Empresa: {gerente1.empresa}")
