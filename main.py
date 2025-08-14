import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import math

try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False

class Protocols:

    @staticmethod
    def siri(dc):
        if dc <= 0:
            return 0
        return (495/dc) - 450
    
    @staticmethod
    def jackson_pollock_7_man(sum_folds, age):
        dc = 1.112 - (0.00043499 * sum_folds) + (0.00000055 * (sum_folds ** 2)) - (0.00028826 * age)
        return dc
    
    @staticmethod
    def jackson_pollock_7_woman(sum_folds, age):
        dc = 1.097 - (0.00046971 * sum_folds) + (0.00000056 * (sum_folds ** 2)) - (0.00012828 * age)
        return dc

class BodyCompApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Avaliação de Composição Corporal")
        self.geometry("800x750")

        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('TLabel', font=('Helvetica', 11))
        self.style.configure('TButton', font=('Helvetica', 11, 'bold'), padding=10)
        self.style.configure('TEntry', font=('Helvetica', 11))
        self.style.configure('TCombobox', font=('Helvetica', 11))
        self.style.configure('Header.TLabel', font=('Helvetica', 14, 'bold'))

        self.protocols_config = {
            "Jackson & Pollock 7" : ["Tríceps", "Subescapular", "Peitoral", "Axilar Média", "Supra-ilíaca", "Abdominal", "Coxa"]
        }
        self.all_skinfolds = sorted(list(set(sum(self.protocols_config.values(), []))))
        self.skinfold_entries = {}

        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(expand=True, fill=tk.BOTH)

        evaluated_frame = ttk.LabelFrame(main_frame, text="Dados do Avaliado", padding="15")
        evaluated_frame.pack(fill=tk.X, pady=10)

        self.create_entry(evaluated_frame, "Nome:", 0)
        self.create_entry(evaluated_frame, "Idade:", 1)
        self.create_combobox(evaluated_frame, "Sexo:", ["Masculino", "Feminino"], 2)
        self.create_entry(evaluated_frame, "Altura (cm):", 3)
        self.create_entry(evaluated_frame, "Peso (kg):", 4)
        self.create_entry(evaluated_frame, "Data:", 5, "DD/MM/AAAA")



    def create_entry(self, parent, label_text, row, placeholder=""):
        ttk.Label(parent, text=label_text).grid(row=row, column=0, padx=5, pady=5, sticky="w")
        entry = ttk.Entry(parent)
        entry.grid(row=row, column=1, padx=5, pady=5, sticky="ew")
        if placeholder:
            entry.insert(0, placeholder)
        attr_name = label_text.replace(':', '').split(' ')[0].lower()
        setattr(self, f"{attr_name}_entry", entry)
        parent.grid_columnconfigure(1, weight=1)

    def create_combobox(self, parent, label_text, values, row):
        ttk.Label(parent, text=label_text).grid(row=row, column=0, padx=5, pady=5, sticky="w")
        combo = ttk.Combobox(parent, values=values, state="readonly")
        combo.grid(row=row, column=1, padx=5, pady=5, sticky="ew")
        attr_name = label_text.replace(':', '').lower()
        setattr(self, f"{attr_name}_combo", combo)

    def create_all_skinfold_entries(self):
        """Cria widgets para todas as dobras possíveis."""
        for i, name in enumerate(self.all_skinfolds):
            row, col = divmod(i, 4)
            frame = ttk.Frame(self.skinfolds_frame)
            
            label = ttk.Label(frame, text=f"{name}:")
            label.pack(side=tk.LEFT, padx=5)
            
            entry = ttk.Entry(frame, width=10)
            entry.pack(side=tk.LEFT)
            
            self.skinfold_entries[name] = {'frame': frame, 'entry': entry}


if __name__ == "__main__":
    app = BodyCompApp()
    app.mainloop()
