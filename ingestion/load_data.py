import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    print("✅ Dados carregados com sucesso!")
    return df

if __name__ == "__main__":
    df = load_data("data/raw_sales.csv")
    print(df.head())