class Triangulo:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b and self.a == self.c:
            return "equilátero"
        elif self.a != self.b and self.a != self.b and self.c != self.b:
            return "escaleno"
        else:
            return "isósceles"

    def retangulo(self):
        if self.a > self.b and self.a > self.c:
            h = self.a
            c1 = self.b
            c2 = self.c
        elif self.b > self.c:
            h = self.b
            c1 = self.a
            c2 = self.c
        else:
            h = self.c
            c1 = self.b
            c2 = self.a
            
        if h*h == (c1*c1+c2*c2):
            return True
        else:
            return False

    def semelhantes(self,t):#utilizo passagem de parametro q é um obj
        if t.a == self.a:
           return 3
        else:
            return 7
        
