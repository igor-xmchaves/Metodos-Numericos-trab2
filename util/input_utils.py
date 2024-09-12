import numpy as np
def input_float(prompt):
    """Função para capturar valores float com validação."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Valor inválido. Por favor, insira um número decimal.")

def input_int(prompt):
    """Função para capturar valores inteiros com validação."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Valor inválido. Por favor, insira um número inteiro.")

def input_matriz_c(n):
    """Captura a matriz C com validação de inputs."""
    
    print("\n--- Input matriz C ---")
    matriz = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            while True:
                try:
                    valor = float(input(f"Digite o valor para a posição [{i+1}, {j+1}]: "))
                    matriz[i, j] = valor
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número decimal.")
    
    return matriz

def input_matriz_v(n):
    """Captura a matriz v com validação de inputs."""
    
    print("\n--- Input matriz v ---")
    matriz_coluna = np.zeros((n, 1))

    for i in range(n):
        while True:
            try:
                valor = float(input(f"Digite o valor para a posição [{i+1}, 1]: "))
                matriz_coluna[i, 0] = valor
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número decimal.")
    
    return matriz_coluna
