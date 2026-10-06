class SolverSistemas:
    
    @staticmethod
    def resolver_sistema_2x2(coeficientes, constantes):
        """
        Resuelve un sistema 2x2 usando el metodo de Cramer (determinantes)
        
        coeficientes: lista de listas [[a, b], [c, d]]
        constantes: lista [e, f]
        
        Devuelve: dict con resultado y paso_a_paso
        """
        a, b = coeficientes[0]
        c, d = coeficientes[1]
        e, f = constantes
        
        paso_a_paso = []
        
        # Calcular determinante principal
        det_principal = a * d - b * c
        paso_a_paso.append(f"Determinante principal: det = ({a})*({d}) - ({b})*({c}) = {a*d} - {b*c} = {det_principal}")
        
        if det_principal != 0:
            # Solucion unica
            # Calcular det_x (reemplazar columna 1 con constantes)
            det_x = e * d - b * f
            paso_a_paso.append(f"Determinante x: det_x = ({e})*({d}) - ({b})*({f}) = {e*d} - {b*f} = {det_x}")
            
            # Calcular det_y (reemplazar columna 2 con constantes)
            det_y = a * f - e * c
            paso_a_paso.append(f"Determinante y: det_y = ({a})*({f}) - ({e})*({c}) = {a*f} - {e*c} = {det_y}")
            
            x = det_x / det_principal
            y = det_y / det_principal
            
            paso_a_paso.append(f"Solucion: x = det_x / det = {det_x} / {det_principal} = {x}")
            paso_a_paso.append(f"Solucion: y = det_y / det = {det_y} / {det_principal} = {y}")
            
            return {
                "tipo": "solucion_unica",
                "solucion": {"x": x, "y": y},
                "paso_a_paso": paso_a_paso
            }
        else:
            # Determinante es cero, verificar si es compatible o incompatible
            # Verificar si las ecuaciones son proporcionales
            # Si a*f == c*e y b*f == d*e, entonces infinitas soluciones
            # De lo contrario, sin solucion
            
            # Verificar proporcion entre coeficientes
            if c != 0 and a != 0:
                proporcion_a_c = a / c
            elif a == 0 and c == 0:
                proporcion_a_c = 1  # ambos cero
            else:
                proporcion_a_c = None
            
            if d != 0 and b != 0:
                proporcion_b_d = b / d
            elif b == 0 and d == 0:
                proporcion_b_d = 1  # ambos cero
            else:
                proporcion_b_d = None
            
            if proporcion_a_c is not None and proporcion_b_d is not None:
                if abs(proporcion_a_c - proporcion_b_d) < 1e-10:
                    # Las ecuaciones son proporcionales
                    # Verificar si tambien lo son las constantes
                    if e != 0 and f != 0:
                        proporcion_e_f = e / f
                    elif e == 0 and f == 0:
                        proporcion_e_f = 1
                    else:
                        proporcion_e_f = None
                    
                    if proporcion_e_f is not None:
                        if abs(proporcion_a_c - proporcion_e_f) < 1e-10:
                            paso_a_paso.append("Determinante principal = 0 y sistema compatible: infinitas soluciones")
                            return {
                                "tipo": "infinitas_soluciones",
                                "solucion": None,
                                "paso_a_paso": paso_a_paso
                            }
            
            # Verificar si es incompatible
            # Si a*f != c*e o b*f != d*e
            if a * f != c * e or b * f != d * e:
                paso_a_paso.append("Determinante principal = 0 y sistema incompatible: sin solucion")
                return {
                    "tipo": "sin_solucion",
                    "solucion": None,
                    "paso_a_paso": paso_a_paso
                }
            
            # Caso especial: ambas ecuaciones son 0=0
            paso_a_paso.append("Determinante principal = 0 y sistema compatible: infinitas soluciones")
            return {
                "tipo": "infinitas_soluciones",
                "solucion": None,
                "paso_a_paso": paso_a_paso
            }
    
    @staticmethod
    def resolver_sistema_3x3(coeficientes, constantes):
        """
        Resuelve un sistema 3x3 usando eliminacion gaussiana
        
        coeficientes: lista de listas [[a, b, c], [d, e, f], [g, h, i]]
        constantes: lista [j, k, l]
        
        Devuelve: dict con resultado y paso_a_paso
        """
        # Crear matriz aumentada
        matriz = []
        for i in range(3):
            fila = coeficientes[i] + [constantes[i]]
            matriz.append(fila)
        
        paso_a_paso = []
        paso_a_paso.append(f"Matriz aumentada inicial:")
        for fila in matriz:
            paso_a_paso.append(f"  {fila}")
        
        n = 3
        
        # Eliminacion gaussiana
        for col in range(n):
            # Buscar pivot
            pivot_row = col
            for i in range(col + 1, n):
                if abs(matriz[i][col]) > abs(matriz[pivot_row][col]):
                    pivot_row = i
            
            # Intercambiar filas si es necesario
            if pivot_row != col:
                matriz[col], matriz[pivot_row] = matriz[pivot_row], matriz[col]
                paso_a_paso.append(f"Intercambio fila {col+1} con fila {pivot_row+1}")
                paso_a_paso.append("Matriz actual:")
                for fila in matriz:
                    paso_a_paso.append(f"  {fila}")
            
            # Si el pivot es cero, la matriz es singular
            if abs(matriz[col][col]) < 1e-10:
                # Verificar si el sistema es compatible o incompatible
                # Si toda la fila es cero (incluyendo constante), infinitas soluciones
                # Si la fila tiene ceros en coeficientes pero no en constante, sin solucion
                all_zero_coeff = all(abs(matriz[col][j]) < 1e-10 for j in range(n))
                if all_zero_coeff:
                    if abs(matriz[col][n]) < 1e-10:
                        paso_a_paso.append(f"Fila {col+1} toda cero: infinitas soluciones")
                        return {
                            "tipo": "infinitas_soluciones",
                            "solucion": None,
                            "paso_a_paso": paso_a_paso
                        }
                    else:
                        paso_a_paso.append(f"Fila {col+1}: 0 = {matriz[col][n]}: sistema incompatible")
                        return {
                            "tipo": "sin_solucion",
                            "solucion": None,
                            "paso_a_paso": paso_a_paso
                        }
                # Continuar con la siguiente columna
                continue
            
            # Eliminar la columna actual de las filas inferiores
            for i in range(col + 1, n):
                factor = matriz[i][col] / matriz[col][col]
                paso_a_paso.append(f"Eliminar columna {col+1}: fila {i+1} = fila {i+1} - ({factor:.4f}) * fila {col+1}")
                for j in range(col, n + 1):
                    matriz[i][j] = matriz[i][j] - factor * matriz[col][j]
                
                paso_a_paso.append("Matriz actual:")
                for fila in matriz:
                    paso_a_paso.append(f"  {[round(x, 4) if abs(x) > 1e-10 else 0 for x in fila]}")
        
        # Verificar si hay filas con ceros en coeficientes pero no en constantes
        for i in range(n):
            all_zero_coeff = all(abs(matriz[i][j]) < 1e-10 for j in range(n))
            if all_zero_coeff and abs(matriz[i][n]) > 1e-10:
                paso_a_paso.append(f"Fila {i+1}: 0 = {matriz[i][n]}: sistema incompatible")
                return {
                    "tipo": "sin_solucion",
                    "solucion": None,
                    "paso_a_paso": paso_a_paso
                }
        
        # Sustitucion hacia atras
        solucion = [0.0] * n
        paso_a_paso.append("Sustitucion hacia atras:")
        
        for i in range(n - 1, -1, -1):
            suma = 0.0
            for j in range(i + 1, n):
                suma += matriz[i][j] * solucion[j]
            
            if abs(matriz[i][i]) > 1e-10:
                solucion[i] = (matriz[i][n] - suma) / matriz[i][i]
                paso_a_paso.append(f"x{i+1} = ({matriz[i][n]:.4f} - {suma:.4f}) / {matriz[i][i]:.4f} = {solucion[i]:.4f}")
            else:
                # Variable libre, infinitas soluciones
                paso_a_paso.append(f"Variable x{i+1} es libre: infinitas soluciones")
                return {
                    "tipo": "infinitas_soluciones",
                    "solucion": None,
                    "paso_a_paso": paso_a_paso
                }
        
        return {
            "tipo": "solucion_unica",
            "solucion": {"x": solucion[0], "y": solucion[1], "z": solucion[2]},
            "paso_a_paso": paso_a_paso
        }
