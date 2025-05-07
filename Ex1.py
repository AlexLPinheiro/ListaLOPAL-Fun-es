#1. Calculadora de IMC. Crie uma função que calcule o Índice de Massa Corporal (IMC) de uma pessoa. A fórmula do IMC é: peso/altura ao quadrado

def calcularIMC(peso,altura):
    imc = peso / (altura**2)
    return imc

print("==Bem vindo a sua calculadora de IMC!==\n\n")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em m: "))
print(f"\nSeu IMC atual é de : {calcularIMC(peso,altura):.2f}")
