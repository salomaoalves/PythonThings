import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = (b*b) - (4*a*c)

if delta > 0:
    raiz = math.sqrt(delta)
    x = (-b + raiz) / (2*a)
    y = (-b - raiz) / (2*a)
    if x < y:
        print("as raízes da equação são",x,"e",y)
    else:
        print("as raízes da equação são",y,"e",x)
else:
    if delta == 0:
        x = -b / (2*a)
        print("a raiz desta equação é",x)
    else:
        print("esta equação não possui raízes reais")

        
