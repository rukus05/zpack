#  Template Functions File
import tkinter as tk
from tkinter import filedialog as fd

def FilePrompt():
    root = tk.Tk()
    root.title('Tkinter Open File Dialog')
    root.resizable(False, False)
    root.geometry('300x150')
    root.withdraw()


    filename = fd.askopenfilename()

    return filename

def save_dataframe(df, sl):
    file_path = fd.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
    
    if file_path:
        try:
            # Assuming df is your DataFrame
            df.to_excel(file_path, index=False)
            sl.config(text=f"Saved as {file_path}")
        except Exception as e:
            sl.config(text=f"Error: {str(e)}")
            

def save_dataframe_csv(df, sl):
    file_path = fd.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    
    if file_path:
        try:
            # Assuming df is your DataFrame
            df.to_csv(file_path, index=False)
            sl.config(text=f"Saved as {file_path}")
        except Exception as e:
            sl.config(text=f"Error: {str(e)}")
            
