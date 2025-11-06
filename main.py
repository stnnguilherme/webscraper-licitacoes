import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# URL do site (pode trocar depois por outro site de licitações)
URL = "https://www.gov.br/compras/pt-br"

try:
    response = requests.get(URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Extrai todos os títulos (exemplo de dados coletados)
        titles = [t.get_text(strip=True) for t in soup.find_all("h2")]

        if titles:
            print("\n🔍 Licitações encontradas:\n")
            for t in titles:
                print("-", t)

            # Cria um DataFrame e salva os resultados
            df = pd.DataFrame({"Título": titles})
            filename = f"licitacoes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            df.to_csv(filename, index=False, encoding="utf-8-sig")

            print(f"\n✅ Dados salvos com sucesso em: {filename}")
        else:
            print("⚠️ Nenhum título encontrado.")
    else:
        print(f"❌ Erro ao acessar o site: {response.status_code}")
except Exception as e:
    print("⚠️ Ocorreu um erro:", e)
