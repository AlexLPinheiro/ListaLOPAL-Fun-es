#Crie uma função chamada converter_celsius_para_fahrenheit(c) que recebe uma temperatura em Celsius e retorna o valor equivalente em Fahrenheit.
#Fórmula: Fahrenheit = Celsius × 1.8 + 32

def converter_celicus_para_fahrenheit(c):
    temperaturaConvertida = c * 1.8 +32
    return temperaturaConvertida

print("==Bem vindo ao conversor de temperatura!==\n\n")
temperaturaC = float(input("Digite a temperatura em celicus: "))
print(f"Temperatura em celcius: {temperaturaC}°C\nTemperatura em fahrenheint: {converter_celicus_para_fahrenheit(temperaturaC)}°F")