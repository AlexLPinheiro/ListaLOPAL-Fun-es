#6. Crie uma função chamada contar_vogais(texto) que receba uma string e retorne quantas vogais existem nela.
def contar_vogais(texto):
    listaVogais = ["a","á","à","ã","â","e","é","ê","i","í","o","ó","ô","u"]
    nVogais = 0
    textoFormatado = texto.lower()
    letrasTexto = textoFormatado.strip()
    for i in range(len(letrasTexto)):
        for n in range(len(listaVogais)):
            if letrasTexto[i] == listaVogais[n]:
                nVogais += 1
    return nVogais

print("==BEM VINDO AO CONTADOR DE VOGAIS NO TEXTO==")
texto = input("Digite o texto: ")
print(f"O texto '{texto}' possui {contar_vogais(texto)} vogais")
