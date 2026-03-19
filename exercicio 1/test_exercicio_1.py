from exercicio_1 import calcular_frete

def test_frete_leve():
    assert calcular_frete(0.5) == 10


def test_frete_inferior():
    assert calcular_frete(1) == 10


def test_frete_intermediario():
    assert calcular_frete(3) == 20


def test_frete_superior():
     assert calcular_frete(5) == 20


def test_frete_alto():
    assert calcular_frete(6) == 30