from eolica.limpieza import a_mw, limpiar_lecturas


def test_limpiar_lecturas_quita_repetidas_y_centinelas(spark):
    entrada = spark.createDataFrame([
        ("WTG-0001", "2026-11-02 10:00:00", "power_kw", 3200.0),
        ("WTG-0001", "2026-11-02 10:00:00", "power_kw", 3200.0),
        ("WTG-0002", "2026-11-02 10:00:00", "power_kw", -9999.0)], "turbine_id string, ts string, signal string, value double")
    filas = {r.turbine_id: r.value for r in limpiar_lecturas(entrada).collect()}
    assert len(filas) == 2
    assert filas["WTG-0001"] == 3200.0
    assert filas["WTG-0002"] is None


def test_a_mw(spark):
    # TODO: crea un DataFrame con una lectura de 4500 kW y comprueba que a_mw da 4.5 en potencia_mw
    entrada = spark.createDataFrame([("WTG-0001", ___)], "turbine_id string, value double")
    assert a_mw(entrada).first().potencia_mw == ___
