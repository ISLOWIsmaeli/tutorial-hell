import os
import pandas as pd

# Folder containing Excel files
input_folder = 'C://Users//Lennox//Documents//daisyProject//toMerge'
output_file = 'merged_output.xlsx'

# Create a Pandas Excel writer object
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    for filename in os.listdir(input_folder):
        if filename.endswith(".xlsx") or filename.endswith(".xls"):
            file_path = os.path.join(input_folder, filename)
            try:
                # Read the first sheet of the Excel file
                df = pd.read_excel(file_path)
                # Use filename (without extension) as the sheet name
                sheet_name = os.path.splitext(filename)[0][:31]  # Excel sheet names max out at 31 characters
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                print(f"Added: {filename} → Sheet: {sheet_name}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

print(f"✅ Merged file saved as: {output_file}")
