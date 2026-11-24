"""Funciones de limpieza de la telemetría: la lógica sale del notebook a un módulo que se puede probar."""
from pyspark.sql import DataFrame, functions as F


def limpiar_lecturas(df: DataFrame) -> DataFrame:
    """Quita lecturas repetidas y convierte el -9999 del sensor en nulo."""
    return (df.dropDuplicates(["turbine_id", "ts", "signal"])
              .withColumn("value", F.when(F.col("value") != -9999, F.col("value"))))


def a_mw(df: DataFrame, columna: str = "value") -> DataFrame:
    """Añade la columna potencia_mw: la columna indicada, en kW, pasada a MW."""
    # TODO: devuelve el DataFrame con una columna nueva potencia_mw = columna / 1000
    return ___
