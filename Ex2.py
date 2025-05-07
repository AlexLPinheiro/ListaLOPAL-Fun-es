#2. Crie uma função chamada maior_n() que recebe um número inteiro como argumento e retorna o maior número entre os n números digitados pelo usuário.

def maior_n(listaNumeros):
    maior = listaNumeros[0]
    for n in range(len(listaNumeros)):
        if listaNumeros[n]> maior:

            maior = listaNumeros[n]
    return maior

listaNumeros = []
print("==BEM VINDO A CALCULADORA DE MAIOR NUMERO!==\n")
qtdNumeros = int(input("Quantos números serão comparados?"))

for i in range(qtdNumeros):
    listaNumeros.append(float(input(f"Digite o {i+1}° Número: ")))

print(f"\nO maior número da lista é {maior_n(listaNumeros)} ")