#5. Crie uma função chamada eh_primo(n) que receba um número inteiro e retorne True se for primo, e False se não for.

def eh_primo(n):
    primo = False
    i = 2
    while i < n:
        if n % i == 0:
            primo = True
            break
        else:
            i+=1
    if primo:
        return False
    else:
        return True

print("==BEM VINDO AO VERIFICADOR DE NÚMERO PRIMO!==\n")
numero = int(input("Digite um número: "))

verificador = eh_primo(numero)

if verificador == True:
    print(f"O número {numero} é primo!")
else:
    print(f"O número {numero} não é primo!")
