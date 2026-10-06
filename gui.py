import tkinter as tk
from tkinter import ttk, messagebox
from solver import SolverSistemas


class SistemaSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Solver de Sistemas de Ecuaciones Lineales")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        
        # Variable para el tipo de sistema
        self.tipo_sistema = tk.StringVar(value="2x2")
        
        # Crear la interfaz
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Selector de tipo de sistema
        selector_frame = ttk.Frame(main_frame)
        selector_frame.pack(pady=10)
        
        ttk.Label(selector_frame, text="Seleccione el tipo de sistema:").pack(side=tk.LEFT)
        ttk.Radiobutton(selector_frame, text="2x2", variable=self.tipo_sistema, value="2x2", command=self.actualizar_interfaz).pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(selector_frame, text="3x3", variable=self.tipo_sistema, value="3x3", command=self.actualizar_interfaz).pack(side=tk.LEFT, padx=10)
        
        # Frame para la matriz de coeficientes
        self.matriz_frame = ttk.Frame(main_frame)
        self.matriz_frame.pack(pady=10)
        
        # Frame para constantes
        self.constantes_frame = ttk.Frame(main_frame)
        self.constantes_frame.pack(pady=10)
        
        # Botón resolver
        self.boton_resolver = ttk.Button(main_frame, text="Resolver", command=self.resolver_sistema)
        self.boton_resolver.pack(pady=20)
        
        # Área de resultados
        resultado_label = ttk.Label(main_frame, text="Resultado:", font=('Arial', 12, 'bold'))
        resultado_label.pack(anchor=tk.W)
        
        self.resultado_text = tk.Text(main_frame, height=20, width=70, wrap=tk.WORD, state=tk.DISABLED)
        self.resultado_text.pack(pady=10)
        
        # Crear campos para 2x2 por defecto
        self.crear_campos_2x2()
        
        # Scrollbar para el área de resultados
        scrollbar = ttk.Scrollbar(main_frame, command=self.resultado_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.resultado_text.config(yscrollcommand=scrollbar.set)
    
    def crear_campos_2x2(self):
        # Limpiar frames existentes
        for widget in self.matriz_frame.winfo_children():
            widget.destroy()
        for widget in self.constantes_frame.winfo_children():
            widget.destroy()
        
        # Matriz de coeficientes 2x2
        ttk.Label(self.matriz_frame, text="Matriz de coeficientes:", font=('Arial', 10, 'bold')).pack()
        
        matriz_2x2_frame = ttk.Frame(self.matriz_frame)
        matriz_2x2_frame.pack(pady=5)
        
        # Labels de variables
        labels_frame = ttk.Frame(matriz_2x2_frame)
        labels_frame.pack()
        ttk.Label(labels_frame, text="", width=4).pack(side=tk.LEFT)
        ttk.Label(labels_frame, text="x", width=8).pack(side=tk.LEFT)
        ttk.Label(labels_frame, text="y", width=8).pack(side=tk.LEFT)
        
        # Campos de entrada
        self.entries = {}
        for i in range(2):
            row_frame = ttk.Frame(matriz_2x2_frame)
            row_frame.pack()
            ttk.Label(row_frame, text=f"Ecuación {i+1}:", width=8).pack(side=tk.LEFT)
            for j in range(2):
                var_name = f"a{i}{j}"
                entry = ttk.Entry(row_frame, width=8)
                entry.pack(side=tk.LEFT, padx=2)
                self.entries[var_name] = entry
        
        # Constantes
        ttk.Label(self.constantes_frame, text="Constantes:", font=('Arial', 10, 'bold')).pack()
        constantes_frame = ttk.Frame(self.constantes_frame)
        constantes_frame.pack(pady=5)
        
        for i in range(2):
            ttk.Label(constantes_frame, text=f"Ecuación {i+1}:", width=8).pack(side=tk.LEFT)
            var_name = f"c{i}"
            entry = ttk.Entry(constantes_frame, width=8)
            entry.pack(side=tk.LEFT, padx=2)
            self.entries[var_name] = entry
    
    def crear_campos_3x3(self):
        # Limpiar frames existentes
        for widget in self.matriz_frame.winfo_children():
            widget.destroy()
        for widget in self.constantes_frame.winfo_children():
            widget.destroy()
        
        # Matriz de coeficientes 3x3
        ttk.Label(self.matriz_frame, text="Matriz de coeficientes:", font=('Arial', 10, 'bold')).pack()
        
        matriz_3x3_frame = ttk.Frame(self.matriz_frame)
        matriz_3x3_frame.pack(pady=5)
        
        # Labels de variables
        labels_frame = ttk.Frame(matriz_3x3_frame)
        labels_frame.pack()
        ttk.Label(labels_frame, text="", width=4).pack(side=tk.LEFT)
        ttk.Label(labels_frame, text="x", width=8).pack(side=tk.LEFT)
        ttk.Label(labels_frame, text="y", width=8).pack(side=tk.LEFT)
        ttk.Label(labels_frame, text="z", width=8).pack(side=tk.LEFT)
        
        # Campos de entrada
        self.entries = {}
        for i in range(3):
            row_frame = ttk.Frame(matriz_3x3_frame)
            row_frame.pack()
            ttk.Label(row_frame, text=f"Ecuación {i+1}:", width=8).pack(side=tk.LEFT)
            for j in range(3):
                var_name = f"a{i}{j}"
                entry = ttk.Entry(row_frame, width=8)
                entry.pack(side=tk.LEFT, padx=2)
                self.entries[var_name] = entry
        
        # Constantes
        ttk.Label(self.constantes_frame, text="Constantes:", font=('Arial', 10, 'bold')).pack()
        constantes_frame = ttk.Frame(self.constantes_frame)
        constantes_frame.pack(pady=5)
        
        for i in range(3):
            ttk.Label(constantes_frame, text=f"Ecuación {i+1}:", width=8).pack(side=tk.LEFT)
            var_name = f"c{i}"
            entry = ttk.Entry(constantes_frame, width=8)
            entry.pack(side=tk.LEFT, padx=2)
            self.entries[var_name] = entry
    
    def actualizar_interfaz(self):
        if self.tipo_sistema.get() == "2x2":
            self.crear_campos_2x2()
        else:
            self.crear_campos_3x3()
        self.limpiar_resultado()
    
    def limpiar_resultado(self):
        self.resultado_text.config(state=tk.NORMAL)
        self.resultado_text.delete(1.0, tk.END)
        self.resultado_text.config(state=tk.DISABLED)
    
    def validar_entradas(self):
        for var_name, entry in self.entries.items():
            valor = entry.get().strip()
            if not valor:
                messagebox.showerror("Error", f"El campo {var_name} está vacío")
                return False
            try:
                float(valor)
            except ValueError:
                messagebox.showerror("Error", f"El campo {var_name} debe ser numérico")
                return False
        return True
    
    def resolver_sistema(self):
        if not self.validar_entradas():
            return
        
        try:
            if self.tipo_sistema.get() == "2x2":
                coeficientes = [[float(self.entries[f"a{i}{j}"].get()) for j in range(2)] for i in range(2)]
                constantes = [float(self.entries[f"c{i}"].get()) for i in range(2)]
                resultado = SolverSistemas.resolver_sistema_2x2(coeficientes, constantes)
            else:
                coeficientes = [[float(self.entries[f"a{i}{j}"].get()) for j in range(3)] for i in range(3)]
                constantes = [float(self.entries[f"c{i}"].get()) for i in range(3)]
                resultado = SolverSistemas.resolver_sistema_3x3(coeficientes, constantes)
            
            # Mostrar resultados
            self.mostrar_resultado(resultado)
            
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
    
    def mostrar_resultado(self, resultado):
        self.resultado_text.config(state=tk.NORMAL)
        self.resultado_text.delete(1.0, tk.END)
        
        # Mostrar paso a paso
        self.resultado_text.insert(tk.END, "Paso a paso:\n")
        for paso in resultado["paso_a_paso"]:
            self.resultado_text.insert(tk.END, f"  {paso}\n")
        
        self.resultado_text.insert(tk.END, "\n")
        
        # Mostrar solución final
        if resultado["tipo"] == "solucion_unica":
            self.resultado_text.insert(tk.END, "Solución única:\n")
            if "z" in resultado["solucion"]:
                self.resultado_text.insert(tk.END, f"  x = {resultado['solucion']['x']:.4f}\n")
                self.resultado_text.insert(tk.END, f"  y = {resultado['solucion']['y']:.4f}\n")
                self.resultado_text.insert(tk.END, f"  z = {resultado['solucion']['z']:.4f}\n")
            else:
                self.resultado_text.insert(tk.END, f"  x = {resultado['solucion']['x']:.4f}\n")
                self.resultado_text.insert(tk.END, f"  y = {resultado['solucion']['y']:.4f}\n")
        elif resultado["tipo"] == "infinitas_soluciones":
            self.resultado_text.insert(tk.END, "El sistema tiene INFINTAS SOLUCIONES\n")
        elif resultado["tipo"] == "sin_solucion":
            self.resultado_text.insert(tk.END, "El sistema NO TIENE SOLUCIÓN (incompatible)\n")
        
        self.resultado_text.config(state=tk.DISABLED)


def crear_ventana():
    root = tk.Tk()
    app = SistemaSolverGUI(root)
    root.mainloop()


if __name__ == "__main__":
    crear_ventana()
