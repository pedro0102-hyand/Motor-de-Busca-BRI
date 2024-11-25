import re
from nltk.corpus import stopwords

stopwords_ingles = set(stopwords.words("english"))

def preprocessar_texto(texto):
    """Limpa e normaliza o texto removendo stopwords, pontuação e convertendo para minúsculas."""
    texto = re.sub(r"[^\w\s]", "", texto)  # Remove pontuações
    texto = texto.lower()  # Converte para minúsculas
    tokens = texto.split()
    tokens = [palavra for palavra in tokens if palavra not in stopwords_ingles]
    return " ".join(tokens)
