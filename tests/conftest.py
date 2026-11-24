import os
import sys

import pytest
from pyspark.sql import SparkSession

# Para que los tests encuentren el paquete eolica, que está en src/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


@pytest.fixture(scope="session")
def spark():
    sesion = SparkSession.builder.master("local[1]").appName("tests-eolica").getOrCreate()
    yield sesion
    sesion.stop()
