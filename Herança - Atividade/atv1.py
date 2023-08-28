class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

#objeto Pessoa
pessoa1 = Pessoa("Julia", 16)
print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}")

#objeto Aluno
aluno1 = Aluno("Artur", 18, "2023A123")
print(f"Nome: {aluno1.nome}, Idade: {aluno1.idade}, Matrícula: {aluno1.matricula}")

