def circulo(diametro):
    pi = 3.1416
    perimetro = pi * diametro
    area = pi * (diametro / 2)**2
    return f"El perimetro es: {perimetro}, el area es: {area}"

def rectangulo(longitud,ancho):
    perimetro = (2 * longitud) + (2 * ancho)
    area = (longitud * ancho)
    return f"El perimetro es: {perimetro}, el area es: {area}"

def triangulo(lado1,lado2,base, altura):
    perimetro = lado1 + lado2 + base
    area = (base * altura) / 2
    return f"El perimetro es: {perimetro}, el area es: {area}"