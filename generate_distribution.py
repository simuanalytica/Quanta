import pandas as pd
import os
import tkinter as tk
from fitter import Fitter
import json

def fit_distribution(data):
    fitter = Fitter(data, distributions=['norm', 'lognorm', 'expon'])
    fitter.fit()

    # Get the best distribution and its parameters
    best_dist = fitter.get_best()
    best_params = fitter.fitted_param
    return {"distribution": best_dist}


def generate_distribution_info(self):
    excel_file_path = self.entry_baseline_file.get()
    output_text = 'Generating Distribution....\n'
    self.output_text.insert(tk.END, output_text)
    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(excel_file_path)
    except FileNotFoundError:
        output_text = f"Error: File '{excel_file_path}' not found.\n"
        self.output_text.insert(tk.END, output_text)
        return
    except pd.errors.EmptyDataError:
        output_text = f"Error: File '{excel_file_path}' is empty.\n"
        self.output_text.insert(tk.END, output_text)
        return
    except Exception as e:
        output_text = f"Error: An unexpected error occurred: {e}\n"
        self.output_text.insert(tk.END, output_text)
        return

    # Get the directory of the Excel file
    excel_directory = os.path.dirname(excel_file_path)

    # Create the log file path in the same directory
    log_file_path = os.path.join(excel_directory, 'log_file.json')
    log_data = {}

    # Open the log file for writing
    with open(log_file_path, 'w') as log_file:
        # Iterate through each column and generate distribution info
        for column_name in df.columns:
            column_data = df[column_name]
            # Fit the data to the best distribution using fitter
            distribution_info = fit_distribution(column_data)

            # Add the distribution information to the log data
            log_data[column_name] = distribution_info

    # Write the log data to a JSON file
    with open(log_file_path, 'w') as log_file:
        json.dump(log_data, log_file, indent=2)
        output_text = f"Log file Generation is completed and available at {log_file_path}.\n"
        self.output_text.insert(tk.END, output_text)
