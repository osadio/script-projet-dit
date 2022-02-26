import sys
from pathlib import Path
import pandas as pd

# Recuperer emplacement du fichier json
if len(sys.argv) < 2:
    print("Error 'Missing argument'. You must specify the excel file path.")
    quit()
json_filepath = Path(sys.argv[1])
json_filename = json_filepath.name
json_stem = json_filepath.stem
json_dir = json_filepath.parents[0]

# Emplacement fichier csv
csv_filename = json_stem + ".csv"
csv_filepath = json_dir.joinpath(csv_filename)

# Lire le fichier excel
read_file = pd.read_json(json_filepath)

# Convertir en un fichier csv
read_file.to_csv(csv_filepath, index=None, header=True)

# Message
print("success!")
print(f"excel filepath : {json_filepath}") 
print(f"csv filepath : {csv_filepath}")

