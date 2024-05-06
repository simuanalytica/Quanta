import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import generate_distribution as gd
import generate_model as gm
import run_macro as rm
import analyze_results as ar
class PrismApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quanta")
        self.master.resizable(width=False, height=False)

        # Section 1: Distribution Generator
        self.frame1 = tk.LabelFrame(master, text="Distribution Generation")
        self.frame1.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W+tk.E+tk.N+tk.S)

        tk.Label(self.frame1, text="Baseline File:").grid(row=0, column=0, sticky=tk.W, pady=(10, 0))
        self.entry_baseline_file = tk.Entry(self.frame1, width=40)
        self.entry_baseline_file.grid(row=0, column=1, padx=(0, 5), pady=(10, 0))

        tk.Button(self.frame1, text="Browse", command=self.browse_baseline_file).grid(row=0, column=2, pady=(10, 0))

        tk.Button(self.frame1, text="Generate Distribution", command=self.generate_distribution).grid(row=1, column=0, columnspan=3, pady=10)

        # Section 2: Generate Model
        self.frame2 = tk.LabelFrame(master, text="Model Creation")
        self.frame2.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W+tk.E+tk.N+tk.S)

        tk.Label(self.frame2, text="Distribution Log:").grid(row=0, column=0, sticky=tk.W, pady=(10, 0))
        self.entry_dist_file = tk.Entry(self.frame2, width=40)
        self.entry_dist_file.grid(row=0, column=1, padx=(0, 5), pady=(10, 0))
        tk.Button(self.frame2, text="Browse", command=self.browse_dist_file).grid(row=0, column=2, padx=10,pady=(10, 0))
        tk.Label(self.frame2, text="Iterations:").grid(row=2, column=0, sticky=tk.W, pady=(10, 0))
        self.entry_iteration = tk.Entry(self.frame2, width=10)
        self.entry_iteration.grid(row=2, column=1, pady=(10, 0), sticky=tk.W)
        # Combo box widget
        combo_options = ["Default", "Agile"]
        self.combo_box = ttk.Combobox(self.frame2, values=combo_options)
        self.combo_box.grid(row=3, column=0, columnspan=3, pady=10)

        tk.Button(self.frame2, text="Generate Model", command=self.generate_model).grid(row=4, column=0, columnspan=3, pady=10)

    #
        # Section 3: Run Simulation
        self.frame3 = tk.LabelFrame(master, text="Run Simulation")
        self.frame3.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W+tk.E+tk.N+tk.S)

        tk.Label(self.frame3, text="Model File:").grid(row=1, column=0, sticky=tk.W, pady=10)
        self.entry_model_file = tk.Entry(self.frame3, width=40)
        self.entry_model_file.grid(row=1, column=1, padx=(0, 5), pady=10)

        tk.Button(self.frame3, text="Browse", command=self.browse_model_file).grid(row=1, column=2, pady=10)
        tk.Button(self.frame3, text="Run Simulation", command=self.run_simulation).grid(row=2, column=0, columnspan=3, pady=10)

        # Section 4: Analysis
        self.frame4 = tk.LabelFrame(master, text="Analysis")
        self.frame4.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W+tk.E+tk.N+tk.S)

        tk.Label(self.frame4, text="Result File:").grid(row=1, column=0, sticky=tk.W, pady=10)
        self.entry_result_file = tk.Entry(self.frame4, width=40)
        self.entry_result_file.grid(row=1, column=1, padx=(0, 5), pady=10, sticky=tk.W)

        tk.Button(self.frame4, text="Browse", command=self.browse_result_file).grid(row=1, column=2, pady=10)
        tk.Button(self.frame4, text="Analyze", command=self.analyse_results).grid(row=2, column=0, columnspan=3, pady=10)

        # Section 3: Output
        self.frame5 = tk.LabelFrame(master, text="Output")
        self.frame5.grid(row=0, column=1, rowspan=4, padx=10, pady=10, sticky=tk.W+tk.E+tk.N+tk.S)

        self.output_text = tk.Text(self.frame5, height=30, width=50)
        self.output_text.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W+tk.E+tk.N+tk.S)

    def browse_baseline_file(self):
        file_path = filedialog.askopenfilename()
        self.entry_baseline_file.delete(0, tk.END)
        self.entry_baseline_file.insert(0, file_path)

    def generate_distribution(self):
        # Add your code for generating the distribution here
        gd.generate_distribution_info(self)
        pass

    def generate_model(self):
        gm.generate_model(self)
        pass

    #
    def browse_dist_file(self):
        file_path = filedialog.askopenfilename()
        self.entry_dist_file.delete(0, tk.END)
        self.entry_dist_file.insert(0, file_path)
    #
    def browse_model_file(self):
        file_path = filedialog.askopenfilename()
        self.entry_model_file.delete(0, tk.END)
        self.entry_model_file.insert(0, file_path)

    def browse_result_file(self):
        file_path = filedialog.askopenfilename()
        self.entry_result_file.delete(0, tk.END)
        self.entry_result_file.insert(0, file_path)
    #
    def run_simulation(self):
        # Add your code for running the simulation here
        rm.run_macro(self)
        pass

    def analyse_results(self):
        # Add your code for running the simulation here
        ar.analyze_results(self)
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = PrismApp(root)
    root.mainloop()
