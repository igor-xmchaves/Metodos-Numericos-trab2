import numpy as np

class Funcoes(object):
    def substituicoes_sucessivas_mod(self, matriz_c, matriz_v):
        p = np.zeros(matriz_c.shape[1])
        for i in range(matriz_c.shape[1]):
            soma = 0
            for j in range(i):  # Corrigido de range(i-1) para range(i)
                soma += matriz_c[i, j] * p[j]
            p[i] = (matriz_v[i] - soma)
        return p

    def substituicoes_retroativas(self, matriz_c, matriz_v):
        p = np.zeros(matriz_c.shape[1])
        for i in range(matriz_c.shape[1]-1, -1, -1):
            soma = 0
            for j in range(i+1, matriz_c.shape[1]):
                soma += matriz_c[i, j] * p[j]
            p[i] = (matriz_v[i] - soma) / matriz_c[i, i]  # Evitar divisão por zero
        return p
        
    def escolhe_pivo(self, matriz_c, k):
        pivo = abs(matriz_c[k,k])
        r = k
        for i in range(k+1, matriz_c.shape[0]):  # Corrigido para matriz_c.shape[0]
            if abs(matriz_c[i,k]) > pivo:
                pivo = abs(matriz_c[i,k])
                r = i
        return pivo, r
    
    def permuta(self, h, matriz_c, k, r):
        # Permutando os elementos do vetor h
        h[k], h[r] = h[r], h[k]
    
        # Permutando as linhas k e r da matriz A
        matriz_c[[k,r]] = matriz_c[[r,k]]
        return

class MetodoFatoracaoLU(Funcoes):
    def __init__(self, a, matriz_c, matriz_v):
        self.a = a
        self.matriz_c = matriz_c
        self.matriz_v = matriz_v
    
    def executar_fat_lu(self, matriz_c, matriz_v):
        matriz_c = np.copy(matriz_c)
        matriz_v = np.copy(matriz_v)
        # Inicialização do vetor de permutações
        h = np.arange(matriz_c.shape[1])
        for i in range(matriz_c.shape[1]):
            h[i] = i
        for k in range(matriz_c.shape[1]-1):
            pivo, r = self.escolhe_pivo(matriz_c, k)
            if pivo == 0:
                print('Matriz singular, não é possível realizar a fatoração LU.')
                return
            if r != k:
                self.permuta(h, matriz_c, k, r)
        
            # Guarda fatores m em matriz_c e faz a fatoração LU
            for i in range(k+1, matriz_c.shape[1]):  
                m = matriz_c[i, k]/matriz_c[k, k]
                matriz_c[i, k] = m

                for j in range(k+1, matriz_c.shape[1]):  # Corrigido a indentação
                    matriz_c[i, j] -= m * matriz_c[k, j]
                
    
        # Aplica permutações em matriz_v
        matriz_vlin = np.zeros(matriz_c.shape[1])
        for i in range(matriz_c.shape[1]):
            r = h[i]
            matriz_vlin[i] = matriz_v[r]
        y = self.substituicoes_sucessivas_mod(matriz_c, matriz_vlin)
        p = self.substituicoes_retroativas(matriz_c, y)

        return p
    
    def mostrar_resultado(self, a, p):
        # Define a precisão global para impressão
        np.set_printoptions(precision=3, suppress=True)
        
        # Converte o vetor p em uma matriz coluna para visualização
        p_coluna = p.reshape(-1, 1)
        var_percetual = a * p_coluna
       
        # Imprime o resultado de p como uma matriz coluna usando NumPy
        print("Resultado:")
        print(f'p =\n{np.array_str(p_coluna, precision= 3)}')
        
        print(f'\nVariação percentual de p =\n{np.array_str(var_percetual, precision=3)}')
        
        # Comparação dos valores da variação percentual
        for i, valor in enumerate(var_percetual):
            if valor > 0.03:
                print(f'\np{i+1} não é uma ação significativa.')
            else:
                print(f'\np{i+1} é uma ação significativa.')
