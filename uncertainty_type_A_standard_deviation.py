import pandas as pd
import numpy as np
import os

# 0. PATH CONFIGURATION ---
# Get the absolute path of the directory where the script is located
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = r'C:\Users\32029396\OneDrive - UPEC\CONTENEUR\donnees\etalonnage'
# Define relative paths for data input and results output
# This ensures the code works on any computer without modification
data_folder = os.path.join(BASE_DIR, "data")
output_directory = os.path.join(BASE_DIR, "output")

# Create the output directory automatically if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
# ----------------------------------------------------------------------------------------------------------------------
# 1. DATA LOADING: Temperatures ---
# Path to the temperature values from thermocouple and Dry-Block CSV file
# The file contains 7 columns
# First column value is related to reference temperature 'Dry-Block' named here 'JOFRA'
# The others are related to 6 temperatures from thermocouples to be calibrated
# Each column have 55 values, which are divided in 5 temperatures reference points, so 11 measurements per point
data_file = os.path.join(data_folder, "Etalonnage thermocouples 2.csv")
# Read the CSV file
values = pd.read_csv(
    data_file,
    sep=';',
    engine="python",
    decimal=",",
    encoding="latin1"
)
# Columns are already named, but if needed you can assign each column name
values.columns = ['JOFRA', 'Droite', 'Toit', 'Porte', 'Fenetre', 'Gauche', 'Sol', 'Air haut', 'Air', 'Air bas', 'Temp Indoor', 'Temp Outdoor' ]
values = values.replace(",", ".", regex=True).astype(float)
# 5 reference temperature points, 11 measurements each
number_measurements = 11 # to modify accordingly
number_reference_points = 5 # to modify accordingly
values['reference'] = np.repeat(np.arange(number_reference_points), number_measurements)
# Visual verification
# print (values)
# List name of thermocouple
thermocouples = ['JOFRA', 'Droite', 'Toit', 'Porte', 'Fenetre', 'Gauche', 'Sol',
                 'Air haut', 'Air', 'Air bas', 'Temp Indoor', 'Temp Outdoor']
# ----------------------------------------------------------------------------------------------------------------------
# 2. Mean calculation par point et par thermocouple
mean_df = values.groupby('reference')[thermocouples].mean()
print(mean_df)
# Save in output file
output_path = os.path.join(output_directory, "mean_temperature_per_reference_point_per_thermocouple.csv")
mean_df.to_csv(output_path, sep=';', index=False, encoding='utf-8-sig')
# Save in data file
output_path = os.path.join(data_folder, "mean_temperature_per_reference_point_per_thermocouple.csv")
mean_df.to_csv(output_path, sep=';', index=False, encoding='utf-8-sig')
# ----------------------------------------------------------------------------------------------------------------------
# 3. Uncertainty calcul par point et par thermocouple
# u_rep = std(mesures) / sqrt(11)
u_rep_df = values.groupby('reference')[thermocouples].std(ddof=1) / np.sqrt(number_measurements)
# Drop the calibrator column data 'JOFRA'
u_rep_df = u_rep_df.drop('JOFRA', axis=1)
# print(" Uncertainty type A by standard deviation per reference point per thermocouple :")
# print(u_rep_df)
# Save the result in a CSV file
# This result will allow to calculate either an enlarged uncertainty per point or variable by interpolation
# First option is a standard in calibration for certificates
# Second option is customized calculation ideal for research purposes
# Only option will be explained in next script
# Save in output file
output_path = os.path.join(output_directory, "uncertainty_type_A_SD_per_reference_point_per_thermocouple.csv")
u_rep_df.to_csv(output_path, sep=';', index=False, encoding='utf-8-sig')
# Save in data file
output_path = os.path.join(data_folder, "uncertainty_type_A_SD_per_reference_point_per_thermocouple.csv")
u_rep_df.to_csv(output_path, sep=';', index=False, encoding='utf-8-sig')
# ----------------------------------------------------------------------------------------------------------------------
# 4. Option 3: Unique incertitude due to Standard deviation (worst case)
# Third option is a conservative and simple procedure
# Look for highest value in each thermocouple standard deviation column from previous dataframe
u_rep_max = u_rep_df.max()
# Visual verification
# print(" Maximum uncertainty type A by standard deviation per thermocouple :")
# print(u_rep_max)
# Transposing vertically the resulted dataframe
df_final = u_rep_max.to_frame().T
# Save the result in a CSV file
# Save in output file
output_path = os.path.join(output_directory, "maximum_uncertainty_type_A_SD_per_thermocouple.csv")
df_final.to_csv(output_path, sep=';', index=False, encoding='utf-8-sig')
# Save in data file
output_path = os.path.join(data_folder, "maximum_uncertainty_type_A_SD_per_thermocouple.csv")
df_final.to_csv(output_path, sep=';', index=False, encoding='utf-8-sig')
