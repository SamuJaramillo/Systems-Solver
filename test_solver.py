import pytest
from solver import SolverSistemas


def test_sistema_2x2_solucion_unica():
    """Test sistema 2x2 con solucion unica"""
    coeficientes = [[2, 3], [4, 5]]
    constantes = [7, 8]
    
    resultado = SolverSistemas.resolver_sistema_2x2(coeficientes, constantes)
    
    assert resultado["tipo"] == "solucion_unica"
    assert resultado["solucion"] is not None
    # Verificar solucion: 2x + 3y = 7, 4x + 5y = 8
    # Solucion: x = -5.5, y = 6.0
    assert abs(resultado["solucion"]["x"] - (-5.5)) < 1e-10
    assert abs(resultado["solucion"]["y"] - 6.0) < 1e-10
    assert len(resultado["paso_a_paso"]) > 0


def test_sistema_3x3_solucion_unica():
    """Test sistema 3x3 con solucion unica"""
    coeficientes = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
    constantes = [8, -11, -3]
    
    resultado = SolverSistemas.resolver_sistema_3x3(coeficientes, constantes)
    
    assert resultado["tipo"] == "solucion_unica"
    assert resultado["solucion"] is not None
    # Solucion: x = 2, y = 3, z = -1
    assert abs(resultado["solucion"]["x"] - 2.0) < 1e-10
    assert abs(resultado["solucion"]["y"] - 3.0) < 1e-10
    assert abs(resultado["solucion"]["z"] - (-1.0)) < 1e-10
    assert len(resultado["paso_a_paso"]) > 0


def test_sistema_2x2_sin_solucion():
    """Test sistema 2x2 sin solucion (incompatible)"""
    coeficientes = [[1, 1], [2, 2]]
    constantes = [3, 7]  # 1x + 1y = 3 y 2x + 2y = 7 son paralelas
    
    resultado = SolverSistemas.resolver_sistema_2x2(coeficientes, constantes)
    
    assert resultado["tipo"] == "sin_solucion"
    assert resultado["solucion"] is None
    assert len(resultado["paso_a_paso"]) > 0


def test_sistema_3x3_infinitas_soluciones():
    """Test sistema 3x3 con infinitas soluciones"""
    coeficientes = [[1, 2, 3], [4, 5, 6], [2, 4, 6]]  # Tercera fila es 2*primera
    constantes = [6, 15, 12]  # 2*6 = 12
    
    resultado = SolverSistemas.resolver_sistema_3x3(coeficientes, constantes)
    
    assert resultado["tipo"] == "infinitas_soluciones"
    assert resultado["solucion"] is None
    assert len(resultado["paso_a_paso"]) > 0


# Tests adicionales para mayor cobertura

def test_sistema_2x2_infinitas_soluciones():
    """Test sistema 2x2 con infinitas soluciones"""
    coeficientes = [[2, 4], [1, 2]]
    constantes = [6, 3]  # 2x + 4y = 6 es equivalente a x + 2y = 3
    
    resultado = SolverSistemas.resolver_sistema_2x2(coeficientes, constantes)
    
    assert resultado["tipo"] == "infinitas_soluciones"
    assert resultado["solucion"] is None
    assert len(resultado["paso_a_paso"]) > 0


def test_sistema_3x3_sin_solucion():
    """Test sistema 3x3 sin solucion"""
    coeficientes = [[1, 1, 1], [1, 1, 1], [2, 2, 2]]
    constantes = [1, 2, 3]  # Incompatible
    
    resultado = SolverSistemas.resolver_sistema_3x3(coeficientes, constantes)
    
    assert resultado["tipo"] == "sin_solucion"
    assert resultado["solucion"] is None
    assert len(resultado["paso_a_paso"]) > 0


def test_sistema_2x2_simple():
    """Test sistema 2x2 simple"""
    coeficientes = [[1, 0], [0, 1]]
    constantes = [5, 7]
    
    resultado = SolverSistemas.resolver_sistema_2x2(coeficientes, constantes)
    
    assert resultado["tipo"] == "solucion_unica"
    assert abs(resultado["solucion"]["x"] - 5.0) < 1e-10
    assert abs(resultado["solucion"]["y"] - 7.0) < 1e-10


def test_sistema_3x3_identidad():
    """Test sistema 3x3 con matriz identidad"""
    coeficientes = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    constantes = [10, 20, 30]
    
    resultado = SolverSistemas.resolver_sistema_3x3(coeficientes, constantes)
    
    assert resultado["tipo"] == "solucion_unica"
    assert abs(resultado["solucion"]["x"] - 10.0) < 1e-10
    assert abs(resultado["solucion"]["y"] - 20.0) < 1e-10
    assert abs(resultado["solucion"]["z"] - 30.0) < 1e-10
