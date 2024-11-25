import json

def carregar_dados(caminho_arquivo):
    """Carrega os dados do arquivo JSON e os separa em documentos fonte e suspeitos."""
    documentos_fonte = []
    documentos_suspeitos = []

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            documento = json.loads(linha)
            if documento["type"] == "source-document":
                documentos_fonte.append(documento)
            elif documento["type"] == "suspicious-document":
                documentos_suspeitos.append(documento)

    return documentos_fonte, documentos_suspeitos
