from utils import log_decorator
import pandas as pd
import os
import glob

# Função de extract que lê e consolida o JSON


@log_decorator
def extrair_dados(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(path, "*.json"))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


# Função que transforma


@log_decorator
def calcular_total(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df


# Função load de CSV ou Parquet


@log_decorator
def carregar_dados(df: pd.DataFrame, format_saida: list):
    """
    Parametro que define CSV, Parquet ou os ambos
    """
    print(format_saida)
    for formato in format_saida:
        if formato == "csv":
            df.to_csv("dados.csv", index=False)
        if formato == "parquet":
            df.to_parquet("dados.parquet", index=False)


# Pipeline


@log_decorator
def calcular_kpi_consolidado(pasta: str, formato_saida: list):
    data_frame = extrair_dados(path=pasta)
    data_frame_calculado = calcular_total(data_frame)
    carregar_dados(data_frame_calculado, formato_saida)


# Testando
# if __name__ == "__main__":
#     pasta: str = "data"
#     data_frame = extrair_dados(path=pasta)
#     data_frame_calculado = calcular_total(data_frame)
#     formato_saida: list = ["csv", "parquet"]
#     carregar_dados(data_frame_calculado, formato_saida)
