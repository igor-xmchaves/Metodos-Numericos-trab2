from metodos.fatoracao_lu import *
from metodos.gauss_jordan import *
from metodos.gauss_seidel import *
from util.input_utils     import *
from util.menu_utils      import *

def executar_fatoracao_LU(a, matriz_c, matriz_v):
    print("\nExecutando Fatoração LU...")
    metodo = MetodoFatoracaoLU(a, matriz_c, matriz_v)
    p = metodo.executar_fat_lu(matriz_c, matriz_v)
    metodo.mostrar_resultado(a, p)

def executar_gauss_jordan(a, matriz_c, matriz_v):
    # Placeholder para implementação
    print("\nExecutando Gauss-Jordan (ou Método de Cramer)...")
    # código para Gauss-Jordan / Método de Cramer

def executar_gauss_seidel(a, matriz_c, matriz_v):
    # Placeholder para implementação
    print("\nExecutando Gauss-Seidel...")
    # código para Gauss-Seidel

def main():
    # Variáveis de input do sistema
    try:
        a = input_float("Digite o valor de A: ")
        n = input_int("Digite o valor de n (tamanho da matriz): ")

        if n <= 0:
            print("O tamanho da matriz deve ser maior que 0.")
            return

        matriz_c = input_matriz_c(n)
        matriz_v = input_matriz_v(n)
        
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return
    
    # Variáveis de teste
    # a = 1
    # matriz_c = np.array([
    #     [10, 1, 1],
    #     [1, 10, 1],
    #     [1, 1, 10]
    # ])
    # matriz_v = np.array([
    #     [12],
    #     [12],
    #     [12]
    # ])
    
    while True:
        exibir_menu()

        try:
            opcao = input_int("Opção: ")
        except ValueError:
            print("Opção inválida, tente novamente.")
            continue

        if opcao == 1:
            executar_fatoracao_LU(a, matriz_c, matriz_v)
        elif opcao == 2:
            executar_gauss_jordan(a, matriz_c, matriz_v)
        elif opcao == 3:
            executar_gauss_seidel(a, matriz_c, matriz_v)
        elif opcao == 4:
            mostrar_matrizes(matriz_c, matriz_v)
        elif opcao == 0:
            print("\nSaindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

main()