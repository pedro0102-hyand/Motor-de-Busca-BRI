from carregador_dados import carregar_dados
from preprocessamento import preprocessar_texto
from indexacao import indexar_whoosh, indexar_elasticsearch
from busca import buscar_whoosh, buscar_elasticsearch
from avaliacao import avaliar_resultados

def main():
    # Carregar os dados
    caminho_arquivo = "data/papers.json"
    documentos_fonte, documentos_suspeitos = carregar_dados(caminho_arquivo)

    # Indexar os documentos nos motores
    indexar_whoosh(documentos_fonte)
    indexar_elasticsearch(documentos_fonte)

    # Realizar buscas com os documentos suspeitos
    resultados_whoosh = buscar_whoosh(documentos_suspeitos)
    resultados_elastic = buscar_elasticsearch(documentos_suspeitos)

    # Avaliar os resultados
    avaliar_resultados(resultados_whoosh, resultados_elastic, documentos_suspeitos)

if __name__ == "__main__":
    main()
