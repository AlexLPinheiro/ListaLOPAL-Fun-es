#4. Crie uma função calcular_troco(valor_compra, valor_pago) que retorna o valor do troco a ser dado ao cliente.
# Se o valor pago for menor que o valor da compra, a função deve retornar zero e uma mensagem dizendo que o pagamento foi insuficiente.

def calcular_troco(valor_compra, valor_pago):
    if valor_compra > valor_pago:
        print("Pagamento foi insuficiente!")
        return 0
    else:
        troco = valor_pago - valor_compra
        return troco

print("==Bem vindo a calculadora de troco!==\n")

valorPago = float(input("Digite o valor pago pelo produto: R$"))
valorProduto = float(input("Digite o preço do produto: R$"))
print(f"\nO valor do troco é de R${calcular_troco(valorProduto,valorPago):.2f}")