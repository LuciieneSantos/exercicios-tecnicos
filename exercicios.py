import json

# Etapa 1: variável SOMA
def calcular_soma():
    indice = 13
    soma = 0
    k = 0
    while k < indice:
        k += 1
        soma += k
    print(f"1) Valor final de SOMA: {soma}")

# Etapa 2: sequência de Fibonacci
def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

def verificar_fibonacci():
    num = int(input("\n2) Digite um número para verificar se pertence à sequência de Fibonacci: "))
    if is_fibonacci(num):
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")

# Etapa 3:  faturamento diário
def analisar_faturamento():
    faturamento_json = """
    {
      "dias": [0, 1000, 2000, 0, 2500, 0, 3000, 4000, 0]
    }
    """
    data = json.loads(faturamento_json)
    faturamento = [valor for valor in data["dias"] if valor > 0]

    menor = min(faturamento)
    maior = max(faturamento)
    media = sum(faturamento) / len(faturamento)
    dias_acima_media = len([valor for valor in faturamento if valor > media])

    print("\n3) Análise do faturamento diário:")
    print(f"Menor faturamento: {menor}")
    print(f"Maior faturamento: {maior}")
    print(f"Dias com faturamento acima da média: {dias_acima_media}")

# Etapa 4:  faturamento por estado
def calcular_percentual_faturamento():
    faturamento = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    total = sum(faturamento.values())

    print("\n4) Percentual de representação por estado:")
    for estado, valor in faturamento.items():
        percentual = (valor / total) * 100
        print(f"{estado}: {percentual:.2f}%")

# Etapa 5: Inverter os caracteres de uma string
def inverter_string():
    def inverter(texto):
        invertida = ""
        for char in texto:
            invertida = char + invertida
        return invertida

    string = input("\n5) Digite uma string para inverter: ")
    print(f"String invertida: {inverter(string)}")

# Execução
if __name__ == "__main__":
    calcular_soma()
    verificar_fibonacci()
    analisar_faturamento()
    calcular_percentual_faturamento()
    inverter_string()
