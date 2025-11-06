import csv
import os

def gerar_relatorio(dados):
    print("Gerando relatório (simulado)...")
    os.makedirs("data/reports", exist_ok=True)
    with open("data/reports/relatorio.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["nome", "endereco"])
        writer.writeheader()
        writer.writerows(dados)
    print("Relatório criado em data/reports/relatorio.csv")
