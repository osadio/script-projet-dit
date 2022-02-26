import sys
from pathlib import Path
import pandas as pd

# Recuperer emplacement du fichier excel
if len(sys.argv) < 2:
    print("Error 'Missing argument'. You must specify the excel file path.")
    quit()
excel_filepath = Path(sys.argv[1])
excel_filename = excel_filepath.name
excel_stem = excel_filepath.stem
excel_dir = excel_filepath.parents[0]

# Emplacement fichier csv
csv_filename = excel_stem + ".csv"
csv_filepath = excel_dir.joinpath(csv_filename)

# Lire le fichier excel
read_file = pd.read_excel(excel_filepath, engine="openpyxl")

# Convertir en un fichier csv
read_file.to_csv(csv_filepath, index=None, header=True)

# Message
print("success!")
print(f"excel filepath : {excel_filepath}") 
print(f"csv filepath : {csv_filepath}")
