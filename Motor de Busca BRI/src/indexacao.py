from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from elasticsearch import Elasticsearch, helpers
import os

def indexar_whoosh(documentos):
    """Indexa os documentos usando Whoosh."""
    schema = Schema(id=ID(stored=True), content=TEXT)
    diretorio_indice = "indices/whoosh"
    os.makedirs(diretorio_indice, exist_ok=True)
    indice = create_in(diretorio_indice, schema)
    writer = indice.writer()

    for documento in documentos:
        writer.add_document(id=documento["id"], content=documento["text"])
    writer.commit()

def indexar_elasticsearch(documentos):
    """Indexa os documentos usando Elasticsearch."""
    es = Elasticsearch()
    es.indices.create(index="documentos", ignore=400)
    acoes = [
        {
            "_index": "documentos",
            "_id": documento["id"],
            "_source": {"content": documento["text"]}
        }
        for documento in documentos
    ]
    helpers.bulk(es, acoes)
