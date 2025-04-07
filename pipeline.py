from etl import calcular_kpi_consolidado

pasta: str = "data"
formato_saida: list = ["csv", "parquet"]

calcular_kpi_consolidado(pasta=pasta, formato_saida=formato_saida)
