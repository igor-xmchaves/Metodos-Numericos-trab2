import numpy as np

class GaussJordan:
    def __init__(self, matriz_c, matriz_v):
        self.matriz_c = np.copy(matriz_c).astype(float)
        self.matriz_v = np.copy(matriz_v).astype(float)

    def calcular_determinante(self):
        matriz_c = np.copy(self.matriz_c)
        n = matriz_c.shape[0]
        det = 1
        trocas = 0

        for k in range(n):
            # Escolha do pivô
            max_index = np.argmax(np.abs(matriz_c[k:, k])) + k
            if matriz_c[max_index, k] == 0:
                return 0  # Determinante é 0 se encontrar linha com pivô 0

            # Permuta as linhas se necessário
            if max_index != k:
                matriz_c[[k, max_index]] = matriz_c[[max_index, k]]
                trocas += 1

            # Atualiza o determinante
            det *= matriz_c[k, k]

            # Normaliza a linha do pivô
            matriz_c[k] = matriz_c[k] / matriz_c[k, k]

            # Zera os elementos abaixo e acima do pivô
            for i in range(n):
                if i != k:
                    fator = matriz_c[i, k]
                    matriz_c[i] -= fator * matriz_c[k]

        # Ajusta o sinal do determinante pelas trocas de linhas
        det *= (-1) ** trocas
        return det

class RegraDeCramer:
    def __init__(self, a, matriz_c, matriz_v):
        self.a = a
        self.matriz_c = np.copy(matriz_c).astype(float)
        self.matriz_v = np.copy(matriz_v).astype(float)

    def calcular_solucao(self):
        n = self.matriz_c.shape[0]
        det_original = GaussJordan(self.matriz_c, self.matriz_v).calcular_determinante()

        if det_original == 0:
            print("O sistema não tem solução única (determinante da matriz é 0).")
            return None

        p = np.zeros(n)

        for i in range(n):
            matriz_temp = np.copy(self.matriz_c)
            matriz_temp[:, i] = self.matriz_v.flatten()  # Corrigido: transforma matriz_v em vetor unidimensional
            det_coluna = GaussJordan(matriz_temp, self.matriz_v).calcular_determinante()
            p[i] = det_coluna / det_original

        return p
    
    def mostrar_resultado(self, a, p):
        # Define a precisão global para impressão
        np.set_printoptions(precision=5, suppress=True)
        
        # Converte o vetor p em uma matriz coluna para visualização
        p_coluna = p.reshape(-1, 1)
        var_percetual = a * p_coluna
       
        # Imprime o resultado de p como uma matriz coluna usando NumPy
        print("Resultado:")
        print(f'p =\n{np.array_str(p_coluna, precision= 5)}')
        
        print(f'\nVariação percentual de p =\n{np.array_str(var_percetual, precision=5)}')
        
        # Comparação dos valores da variação percentual
        for i, valor in enumerate(var_percetual):
            if valor > 0.03:
                print(f'\np{i+1} não é uma ação significativa.')
            else:
                print(f'\np{i+1} é uma ação significativa.')