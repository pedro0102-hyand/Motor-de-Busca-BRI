import matplotlib.pyplot as plt

def calcular_precision_k(resultados, k):
    """Calcula a precisão nos k primeiros resultados."""
    precisao_total = 0
    for resultado in resultados:
        precisao = sum(1 for r in resultado[:k] if r["correto"]) / k
        precisao_total += precisao
    return precisao_total / len(resultados)

def avaliar_resultados(resultados_whoosh, resultados_elastic, consultas):
    """Avalia os resultados de busca e gera gráficos de desempenho."""
    precisao_whoosh = calcular_precision_k(resultados_whoosh, 10)
    precisao_elastic = calcular_precision_k(resultados_elastic, 10)

    print(f"Precisão Whoosh: {precisao_whoosh}")
    print(f"Precisão Elasticsearch: {precisao_elastic}")

    plt.plot(range(1, 11), precisao_whoosh, label="Whoosh")
    plt.plot(range(1, 11), precisao_elastic, label="Elasticsearch")
    plt.xlabel("K (top K resultados)")
    plt.ylabel("Precisão")
    plt.legend()
    plt.show()
