import sys
sys.path.append("/Users/pedrojuliosilvasucupira/Desktop/Motor de Busca BRI/venv/lib/python3.11/site-packages")

from whoosh.index import open_dir

from whoosh.qparser import QueryParser
from elasticsearch import Elasticsearch

def buscar_whoosh(consultas):
    """Realiza buscas usando o índice do Whoosh."""
    indice = open_dir("indices/whoosh")
    resultados = []

    with indice.searcher() as pesquisador:
        for consulta in consultas:
            query = QueryParser("content", indice.schema).parse(consulta["text"])
            resultados.append(pesquisador.search(query, limit=10))
    return resultados

def buscar_elasticsearch(consultas):
    """Realiza buscas usando o índice do Elasticsearch."""
    es = Elasticsearch()
    resultados = []

    for consulta in consultas:
        resposta = es.search(index="documentos", body={
            "query": {"match": {"content": consulta["text"]}}
        })
        resultados.append(resposta["hits"]["hits"])
    return resultados
