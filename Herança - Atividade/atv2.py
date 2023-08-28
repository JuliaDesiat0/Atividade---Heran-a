class Forma:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

class Retangulo(Forma):
    def calcular_area(self):
        return self.largura * self.altura

class Triangulo(Forma):
    def calcular_area(self):
        return 0.5 * self.largura * self.altura

retangulo1 = Retangulo(6, 12)
area_retangulo = retangulo1.calcular_area()
print(f"Área do retângulo: {area_retangulo}")

triangulo1 = Triangulo(4, 6)
area_triangulo = triangulo1.calcular_area()
print(f"Área do triângulo: {area_triangulo}")
