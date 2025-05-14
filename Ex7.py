#7. Contagem Regressiva. Crie uma função chamada contagem_regressiva que receba um
# número inteiro n. A função deve imprimir uma contagem regressiva a partir de n até 1 usando recursividade.
# Após a contagem, imprima “Fim”.

#Observação: pesquisa sobre funções recursivas.


def contagem_regressiva(n):
    if n <=0 :
        print("FIM")
        return
    print(f"{n}")
    contagem_regressiva(n-1)


numero = int(input("Digite um número para ser feita a contagem regressiva: "))
contagem_regressiva(numero)