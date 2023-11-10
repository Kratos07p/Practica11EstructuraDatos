def suma(num1,num2):
    resultado = num1 + num2
    return f"Resultado: {resultado}"

def resta(num1,num2):
    resultado = num1 - num2
    return f"Resultado: {resultado}"

def multiplicacion(num1,num2):
    resultado = (num1 * num2)
    return f"Resultado: {resultado}"

def division(num1,num2):
    if num2 != 0:
        resultado = (num1 / num2)
        return f"Resultado: {resultado}"
    else:
        print("Error, No se puede dividir entre 0")