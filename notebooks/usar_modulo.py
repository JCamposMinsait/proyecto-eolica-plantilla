# Databricks notebook source
# MAGIC %md
# MAGIC # Usar el módulo del proyecto
# MAGIC
# MAGIC Este notebook importa las funciones de `src/eolica/limpieza.py`. Así la lógica vive en un módulo que se prueba con pytest, y el notebook solo la usa.
# MAGIC
# MAGIC Si tu catálogo no es `formacion`, cámbialo en el cuadro de arriba.

# COMMAND ----------

import os
import re
import sys

dbutils.widgets.text("catalogo", "formacion")
usuario = spark.sql("SELECT current_user()").first()[0]
esquema = "eolica_" + re.sub(r"[^a-z0-9]", "_", usuario.split("@")[0].lower())
tabla = f"{dbutils.widgets.get('catalogo')}.{esquema}.bronze_telemetria"

sys.path.append(os.path.abspath("../src"))          # la carpeta src del proyecto
from eolica.limpieza import a_mw, limpiar_lecturas

lecturas = spark.table(tabla).filter("signal = 'power_kw'").limit(1000)
display(a_mw(limpiar_lecturas(lecturas)))
