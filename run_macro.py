import win32com.client

def run_excel_macro(file_path, macro_name):
    excel = win32com.client.Dispatch("Excel.Application")

    # Open the Excel file
    workbook = excel.Workbooks.Open(file_path)

    try:
        # Run the specified macro
        excel.Run(macro_name)
    except Exception as e:
        print(f"Error running macro: {e}")
    finally:
        # Save and close the workbook
        workbook.Save()
        workbook.Close()

    # Quit Excel application
    excel.Quit()

def run_macro(self):
    model_file = self.entry_model_file.get()
    macro_name = 'ComputeValuesAndOutputResults'
    run_excel_macro(model_file, macro_name)