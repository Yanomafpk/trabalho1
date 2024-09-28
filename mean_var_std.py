import numpy as np

def calculate(list):

    # Gera um erro se o tamanho da lista não for 9
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Converte a lista em uma matriz 3x3
    matriz = np.array(list).reshape((3,3))

    # Inicializa o dicionário
    resultados = {}

    # Média
    resultados['mean'] = [matriz.mean(axis=0).tolist(), 
                          matriz.mean(axis=1).tolist(),
                          matriz.mean()]

    # Variância
    resultados['variance'] = [matriz.var(axis=0).tolist(), 
                              matriz.var(axis=1).tolist(),
                              matriz.var()]

    # Desvio padrão
    resultados['standard deviation'] = [matriz.std(axis=0).tolist(), 
                                        matriz.std(axis=1).tolist(),
                                        matriz.std()]

    # Máximo
    resultados['max'] = [matriz.max(axis=0).tolist(), 
                         matriz.max(axis=1).tolist(),
                         matriz.max()]

    # Mínimo
    resultados['min'] = [matriz.min(axis=0).tolist(), 
                         matriz.min(axis=1).tolist(),
                         matriz.min()]

    # Soma
    resultados['sum'] = [matriz.sum(axis=0).tolist(), 
                         matriz.sum(axis=1).tolist(),
                         matriz.sum()]

    return resultados
