import numpy as np

class Funcoes(object):
    def calcula_norma(self, p, w):
        normaNum = 0
        normaDen = 0
        for i in range(len(p)):
            t = abs(w[i] - p[i])
            if t > normaNum:
                normaNum = t
            if abs(w[i]) > normaDen:
                normaDen = abs(w[i])
            p[i] = w[i]
            
            if normaDen == 0:
                return 0
            
        return normaNum/normaDen
        

class MetodoGaussSeidel(Funcoes):
    def __init__(self, a, matriz_c, matriz_v,  e= 0.03, iterMax= 100):
        self.a = a
        self.matriz_c = np.copy(matriz_c).astype(float)
        self.matriz_v = np.copy(matriz_v).astype(float)
        self.e = e
        self.iterMax = iterMax
    
    def executar_gauss_seidel(self, matriz_c, matriz_v):
        # Construção da matriz e vetor de iterações
        p = np.zeros(matriz_c.shape[1])
        for i in range(self.matriz_c.shape[1]):
            r = 1/matriz_c[i, i]
            for j in range(self.matriz_c.shape[1]):
                if i != j:
                    matriz_c[i, j] *= r
            matriz_v[i] *= r
            p[i] = matriz_v[i]
        
        # Iterações de Gauss-Seidel
        k = 0
        w = np.zeros(matriz_c.shape[1])
        while(k < self.iterMax):
            k = k + 1
            for i in range(self.matriz_c.shape[1]):
                soma = 0
                for j in range(self.matriz_c.shape[1]):
                    if i != j:
                        soma += matriz_c[i, j] * p[j]
                w[i] = p[i]
                p[i] = matriz_v[i] - soma
            
            norma = self.calcula_norma(w, p)
            if norma < self.e:
                break
        
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

        
