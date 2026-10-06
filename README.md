# Solver de Sistemas de Ecuaciones Lineales

Sistema de resolución de ecuaciones lineales 2x2 y 3x3 con interfaz gráfica en Python.

## Descripción

Este proyecto permite resolver sistemas de ecuaciones lineales de 2x2 (usando el método de Cramer) y 3x3 (usando eliminación gaussiana). La aplicación incluye una interfaz gráfica intuitiva construida con Tkinter donde el usuario puede ingresar los coeficientes y obtener la solución paso a paso.

## Requisitos

- Python 3.10 o superior
- Tkinter (incluido en la instalación estándar de Python)

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/SamuJaramillo/POO.git
   cd POO
   ```

2. No se requieren dependencias adicionales, ya que Tkinter viene incluido con Python.

## Uso

Ejecutar la aplicación:
```bash
python main.py
```

La interfaz gráfica se abrirá automáticamente. Siga estos pasos:
1. Seleccione el tipo de sistema (2x2 o 3x3)
2. Ingrese los coeficientes de cada variable en los campos correspondientes
3. Ingrese las constantes de cada ecuación
4. Haga clic en el botón "Resolver"
5. Los resultados y el paso a paso del cálculo se mostrarán en el área inferior

## Estructura de archivos

- **solver.py**: Contiene la clase `SolverSistemas` con la lógica de resolución:
  - `resolver_sistema_2x2()`: Resuelve sistemas 2x2 usando el método de Cramer
  - `resolver_sistema_3x3()`: Resuelve sistemas 3x3 usando eliminación gaussiana

- **gui.py**: Contiene la clase `SistemaSolverGUI` con la interfaz gráfica:
  - Selector de tipo de sistema
  - Campos de entrada para coeficientes y constantes
  - Botón de resolución
  - Área de visualización de resultados

- **main.py**: Punto de entrada de la aplicación

- **test_solver.py**: Pruebas unitarias con pytest para validar la lógica de resolución

## Ejemplos

### Sistema 2x2 con solución única
Ecuaciones:
- 2x + 3y = 7
- 4x + 5y = 8

Resultado: x = -5.5, y = 6.0

### Sistema 3x3 con solución única
Ecuaciones:
- 2x + y - z = 8
- -3x - y + 2z = -11
- -2x + y + 2z = -3

Resultado: x = 2.0, y = 3.0, z = -1.0

### Sistema sin solución (incompatible)
Ecuaciones:
- x + y = 3
- 2x + 2y = 7

Resultado: El sistema NO TIENE SOLUCIÓN (incompatible)

### Sistema con infinitas soluciones
Ecuaciones:
- 2x + 4y = 6
- x + 2y = 3

Resultado: El sistema tiene INFINTAS SOLUCIONES
