class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor

class Eletronico(Produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem

livro1 = Livro("A Culpa É das Estrelas", 29.90, "John Green")
print(f"Livro: {livro1.nome}, Preço: R${livro1.preco}, Autor: {livro1.autor}")

eletronico1 = Eletronico("Notebook", 2500.00, "110V")
print(f"Eletrônico: {eletronico1.nome}, Preço: R${eletronico1.preco}, Voltagem: {eletronico1.voltagem}")
