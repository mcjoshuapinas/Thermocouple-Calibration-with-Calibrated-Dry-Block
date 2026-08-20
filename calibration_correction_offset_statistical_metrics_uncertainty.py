import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from sklearn.metrics import r2_score
import math as m

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
# 1. DATA LOADING: Mean Temperatures per point de reference
# data_file = r"C:\Users\32029396\OneDrive - UPEC\CONTENEUR\donnees\etalonnage\Étalonnage des thermocouples moyenne.csv"
data_file = os.path.join(data_folder, "mean_temperature_per_reference_point_per_thermocouple.csv")
# Read the CSV (whitespace separated, no header in the source file)
values = pd.read_csv(data_file, engine="python", sep=';', encoding="latin1")
# Remplacer les virgules par des points et convertir en float
values = values.replace(",", ".", regex=True).astype(float)
# Rename columns for clarity
values.columns = ['JOFRA', 'Droite', 'Toit', 'Porte', 'Fenetre', 'Gauche', 'Sol', 'Air haut', 'Air', 'Air bas',
                  'Temp Indoor', 'Temp Outdoor' ]
# Rename variable for clarity
# droite = right; toit=ceiling; porte=door; fenetre=window; gauche= left; sol=ground
# JOFRA is the Calibrated Dry-Block, and it is the reference temperature for calibration

Temperature_reference = values['JOFRA']
Temperature_droite = values['Droite']
Temperature_toit = values['Toit']
Temperature_porte = values['Porte']
Temperature_fenetre = values['Fenetre']
Temperature_Gauche = values['Gauche']
Temperature_sol = values['Sol']
Temperature_air_haut = values['Air haut']
Temperature_air = values['Air']
Temperature_air_bas = values['Air bas']
Temperature_temp_indoor = values['Temp Indoor']
Temperature_temp_outdoor = values['Temp Outdoor']
# Verifying appropriate storage of reference temperature
# print(Temperature_reference)
# ----------------------------------------------------------------------------------------------------------------------
# 2. Calculate Linear Regression for all sensors
# polyfit(x, y, degree) -> degree 1 is a linear line
m1, c1 = np.polyfit(Temperature_droite, Temperature_reference, 1)
m2, c2 = np.polyfit(Temperature_toit, Temperature_reference, 1)
m3, c3 = np.polyfit(Temperature_porte, Temperature_reference, 1)
m4, c4 = np.polyfit(Temperature_fenetre, Temperature_reference, 1)
m5, c5 = np.polyfit(Temperature_Gauche, Temperature_reference, 1)
m6, c6 = np.polyfit(Temperature_sol, Temperature_reference, 1)
m7, c7 = np.polyfit(Temperature_air_haut, Temperature_reference, 1)
m8, c8 = np.polyfit(Temperature_air, Temperature_reference, 1)
m9, c9 = np.polyfit(Temperature_air_bas, Temperature_reference, 1)
m10, c10 = np.polyfit(Temperature_temp_indoor, Temperature_reference, 1)
m11, c11 = np.polyfit(Temperature_temp_outdoor, Temperature_reference, 1)
# ----------------------------------------------------------------------------------------------------------------------
# 3. Create the regression lines for plotting
# Calibration curve
reg_line1 = m1 * Temperature_droite + c1
reg_line2 = m2 * Temperature_toit + c2
reg_line3 = m3 * Temperature_porte + c3
reg_line4 = m4 * Temperature_fenetre + c4
reg_line5 = m5 * Temperature_Gauche + c5
reg_line6 = m6 * Temperature_sol + c6
reg_line7 = m7 * Temperature_air_haut + c7
reg_line8 = m8 * Temperature_air + c8
reg_line9 = m9 * Temperature_air_bas + c9
reg_line10 = m10 * Temperature_temp_indoor + c10
reg_line11 = m11 * Temperature_temp_outdoor + c11
# ----------------------------------------------------------------------------------------------------------------------
# 4. Calculate R² and the Maximum residual
r2_1 = r2_score(Temperature_reference, reg_line1)
max_err1 = np.max(np.abs(Temperature_reference - reg_line1))
r2_2 = r2_score(Temperature_reference, reg_line2)
max_err2 = np.max(np.abs(Temperature_reference - reg_line2))
r2_3 = r2_score(Temperature_reference, reg_line3)
max_err3 = np.max(np.abs(Temperature_reference - reg_line3))
r2_4 = r2_score(Temperature_reference, reg_line4)
max_err4 = np.max(np.abs(Temperature_reference - reg_line4))
r2_5 = r2_score(Temperature_reference, reg_line5)
max_err5 = np.max(np.abs(Temperature_reference - reg_line5))
r2_6 = r2_score(Temperature_reference, reg_line6)
max_err6 = np.max(np.abs(Temperature_reference - reg_line6))
r2_7 = r2_score(Temperature_reference, reg_line7)
max_err7 = np.max(np.abs(Temperature_reference - reg_line7))
r2_8 = r2_score(Temperature_reference, reg_line8)
max_err8 = np.max(np.abs(Temperature_reference - reg_line8))
r2_9 = r2_score(Temperature_reference, reg_line9)
max_err9 = np.max(np.abs(Temperature_reference - reg_line9))
r2_10 = r2_score(Temperature_reference, reg_line10)
max_err10 = np.max(np.abs(Temperature_reference - reg_line10))
r2_11 = r2_score(Temperature_reference, reg_line11)
max_err11 = np.max(np.abs(Temperature_reference - reg_line11))
# ----------------------------------------------------------------------------------------------------------------------
# 5. Calculate the residual
res_droite = Temperature_reference - reg_line1
res_toit = Temperature_reference - reg_line2
res_porte = Temperature_reference - reg_line3
res_fenetre = Temperature_reference - reg_line4
res_Gauche = Temperature_reference - reg_line5
res_sol = Temperature_reference - reg_line6
res_air_haut = Temperature_reference - reg_line7
res_air = Temperature_reference - reg_line8
res_air_bas = Temperature_reference - reg_line9
res_temp_indoor = Temperature_reference - reg_line10
res_temp_outdoor = Temperature_reference - reg_line11
# ----------------------------------------------------------------------------------------------------------------------
# 6. Calculate the uncertainty type B due to calibrator certification
expanded_uncertainty_calibrator = 0.05  # it considers a k=2
uncertainty_calibrator = expanded_uncertainty_calibrator/2  # divide by two to obtain not expanded uncertainty
# ----------------------------------------------------------------------------------------------------------------------
# 7. Calculate the uncertainty type B due to resolution
measurement_resolution = 0.01  # according to technical specifications
uncertainty_resolution = measurement_resolution/(2*m.sqrt(3))  # considering a uniform distribution (1/2*sqrt(3))
# ----------------------------------------------------------------------------------------------------------------------
# 8. Calculate the uncertainty due to standard deviation
constant_contributions_in_uncertainty = uncertainty_calibrator**2 + uncertainty_resolution**2
print('constant_contributions_in_uncertainty', constant_contributions_in_uncertainty)
coverage_factor = 2  # ensures 95% of probability
flat_rate = 1.2  # ensure uncounted uncertainties like instrument drift, heterogeneity, and thermal errors
# ----------------------------------------------------------------------------------------------------------------------
# 8. Option 1 for Certificate of Calibration for each sensor, punctual uncertainties
# Uncertainty varies according to the reference points, these were calculated in the previous script.
# Reading uncertainty type A standard deviation
data_file = os.path.join(data_folder, "uncertainty_type_A_SD_per_reference_point_per_thermocouple.csv")
# Read the CSV (whitespace separated, no header in the source file)
values = pd.read_csv(data_file, engine="python", sep=';', encoding="latin1")
# Remplacer les virgules par des points et convertir en float
values = values.replace(",", ".", regex=True).astype(float)
# Rename columns for clarity
values.columns = ['Droite', 'Toit', 'Porte', 'Fenetre', 'Gauche', 'Sol', 'Air haut', 'Air', 'Air bas',
                  'Temp Indoor', 'Temp Outdoor']
print('Option 1')
# power 2
power_values = values.pow(2)
print('power_values', power_values)
# addition of constant contributions
power_values_plus_constant_contribution = power_values + constant_contributions_in_uncertainty
print('power_values_plus_constant_contribution', power_values_plus_constant_contribution)
uncertainty = power_values_plus_constant_contribution.pow(0.5)
print('uncertainty', uncertainty)
expanded_uncertainty = uncertainty*coverage_factor
print('expanded_uncertainty', expanded_uncertainty)
expanded_uncertainty_with_flat_rate = expanded_uncertainty*flat_rate
print('expanded_uncertainty_with_flat_rate', expanded_uncertainty_with_flat_rate)
output_path = os.path.join(output_directory, "option1_expanded_uncertainty_with_flat_rate.csv")
expanded_uncertainty_with_flat_rate.to_csv(output_path, sep=';', index=False, encoding='utf-8-sig')
# 8. Option 2 for research purposes, variable uncertainties, interpolation
# to be developed
# ----------------------------------------------------------------------------------------------------------------------
# 8. Option 3 for conservative and simple procedure
# Reading maximum uncertainty type A standard deviation
data_file = os.path.join(data_folder, "maximum_uncertainty_type_A_SD_per_thermocouple.csv")
# Read the CSV (whitespace separated, no header in the source file)
values = pd.read_csv(data_file, engine="python", sep=';', encoding="latin1")
# Remplacer les virgules par des points et convertir en float
values = values.replace(",", ".", regex=True).astype(float)
# Rename columns for clarity
values.columns = ['Droite', 'Toit', 'Porte', 'Fenetre', 'Gauche', 'Sol', 'Air haut', 'Air', 'Air bas',
                  'Temp Indoor', 'Temp Outdoor']
# power 2
power_values = values.pow(2)
print('Option 3')
print('power_values', power_values)
# addition of constant contributions
power_values_plus_constant_contribution = power_values + constant_contributions_in_uncertainty
print('power_values_plus_constant_contribution', power_values_plus_constant_contribution)
uncertainty = power_values_plus_constant_contribution.pow(0.5)
print('uncertainty', uncertainty)
expanded_uncertainty = uncertainty*coverage_factor
print('expanded_uncertainty', expanded_uncertainty)
expanded_uncertainty_with_flat_rate = expanded_uncertainty*flat_rate
print('expanded_uncertainty_with_flat_rate', expanded_uncertainty_with_flat_rate)
output_path = os.path.join(output_directory, "option2_expanded_uncertainty_with_flat_rate.csv")
expanded_uncertainty_with_flat_rate.to_csv(output_path, sep=';', index=False, encoding='utf-8-sig')
# ----------------------------------------------------------------------------------------------------------------------
# 9. Offset values for residual error plot
offset_droite = -0.5
offset_toit = -0.3
offset_porte = -0.1
offset_fenetre = 0.1
offset_Gauche = 0.3
offset_sol = 0.5
offset_air_haut = 0.7
offset_air = -0.7
offset_air_bas = 0.9
offset_temp_indoor = -0.9
offset_temp_outdoor = 0.11
# ----------------------------------------------------------------------------------------------------------------------
# 10. Create a Calibration curve with its residuals. Figure with 2 Subplots (Top for Curve, Bottom for Residuals)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12), sharex=False,
                               gridspec_kw={'height_ratios': [2, 1]})
# 10.1 TOP PLOT: Calibration Curves ---
ax1.scatter(Temperature_droite, Temperature_reference, color='firebrick', marker='s', alpha=0.5, label='Right wall (Est)')
ax1.plot(Temperature_droite, reg_line1, 'r--', label=f'Fit: {m1:.4f}x {c1:.4f} ($R^2$={r2_1:.2f})')

ax1.scatter(Temperature_toit, Temperature_reference, color='chocolate', marker='d', alpha=0.5, label='Ceiling')
ax1.plot(Temperature_toit, reg_line2, 'b--', label=f'Fit: {m2:.4f}x {c2:.4f} ($R^2$={r2_2:.2f})')

ax1.scatter(Temperature_porte, Temperature_reference, color='orange', marker='*', alpha=0.5, label='Door')
ax1.plot(Temperature_porte, reg_line3, 'k--', label=f'Fit: {m3:.4f}x {c3:.4f} ($R^2$={r2_3:.2f})')

ax1.scatter(Temperature_fenetre, Temperature_reference, color='royalblue', marker='^', alpha=0.5, label='Window*')
ax1.plot(Temperature_fenetre, reg_line4, 'r--', label=f'Fit: {m4:.4f}x {c4:.4f} ($R^2$={r2_4:.2f})')

ax1.scatter(Temperature_Gauche, Temperature_reference, color='darkcyan', marker='v', alpha=0.5, label='Left wall (West)')
ax1.plot(Temperature_Gauche, reg_line5, 'b--', label=f'Fit: {m5:.4f}x {c5:.4f} ($R^2$={r2_5:.2f})')

ax1.scatter(Temperature_sol, Temperature_reference, color='slategrey', marker='o', alpha=0.5, label='Floor')
ax1.plot(Temperature_sol, reg_line6, 'k--', label=f'Fit: {m6:.4f}x {c6:.4f} ($R^2$={r2_6:.2f})')

ax1.scatter(Temperature_air_haut, Temperature_reference, color='green', marker='o', alpha=0.5, label='Air top')
ax1.plot(Temperature_air_haut, reg_line7, 'g--', label=f'Fit: {m7:.4f}x {c7:.4f} ($R^2$={r2_7:.2f})')

ax1.scatter(Temperature_air, Temperature_reference, color='yellow', marker='o', alpha=0.5, label='Air center')
ax1.plot(Temperature_air, reg_line8, 'y--', label=f'Fit: {m8:.4f}x {c8:.4f} ($R^2$={r2_8:.2f})')

ax1.scatter(Temperature_air_bas, Temperature_reference, color='magenta', marker='o', alpha=0.5, label='Air bottom')
ax1.plot(Temperature_air_bas, reg_line9, color='magenta', label=f'Fit: {m9:.4f}x {c9:.4f} ($R^2$={r2_9:.2f})')

ax1.scatter(Temperature_temp_indoor, Temperature_reference, color='purple', marker='o', alpha=0.5, label='Temp. surf. indoor')
ax1.plot(Temperature_temp_indoor, reg_line10, color='purple', label=f'Fit: {m10:.4f}x {c10:.4f} ($R^2$={r2_10:.2f})')

ax1.scatter(Temperature_temp_outdoor, Temperature_reference, color='orange', marker='o', alpha=0.5, label='Temp. surf. outdoor')
ax1.plot(Temperature_temp_outdoor, reg_line11, color='orange', label=f'Fit: {m11:.4f}x {c11:.4f} ($R^2$={r2_11:.2f})')

ax1.set_xlabel('Measured temperature (°C)', fontsize=12, family='Times New Roman')
ax1.set_ylabel('Reference temperature (°C)', fontsize=12, family='Times New Roman')
# ax1.set_title('Thermocouple Calibration Analysis', fontsize=14, family='Times New Roman')
ax1.legend(loc='center left', bbox_to_anchor=(1.02, 0.5), frameon=True, prop={'family': 'Times New Roman', 'size': 10})
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.text(0.98, 0.98, '(a)', transform=ax1.transAxes,
         ha='right', va='top',  # Alineación horizontal y vertical
         fontsize=12, fontweight='bold')
# 10.2 BOTTOM PLOT: Residuals ---
# Zero error line
ax2.axhline(y=0, color='black', linestyle='-', linewidth=1.5, alpha=0.7)

# 10.2.1 Plot Residual right temperature
ax2.scatter(Temperature_reference + offset_droite, res_droite,
            color='firebrick', marker='s', s=60, alpha=0.6, label='Right wall (Est)')
# 10.2.2 Plot Residual ceiling temperature
ax2.scatter(Temperature_reference + offset_toit, res_toit,
            color='chocolate', marker='d', s=60, alpha=0.6, label='Ceiling')
# 10.2.3 Plot Residual door temperature
ax2.scatter(Temperature_reference + offset_porte, res_porte,
            color='orange', marker='*', s=60, alpha=0.6, label='Door')
# 10.2.4 Plot Residual window temperature
ax2.scatter(Temperature_reference + offset_fenetre, res_fenetre,
            color='royalblue', marker='^', s=60, alpha=0.6, label='Window*')
# 10.2.5 Plot Residual left temperature
ax2.scatter(Temperature_reference + offset_Gauche, res_Gauche,
            color='darkcyan', marker='v', s=60, alpha=0.6, label='Left wall (West)')
# 10.2.6 Plot Residual ground temperature
ax2.scatter(Temperature_reference + offset_sol, res_sol,
            color='slategrey', marker='o', s=60, alpha=0.6, label='Floor')
# 10.2.7 Plot Residual air_haut temperature
ax2.scatter(Temperature_reference + offset_air_haut, res_air_haut,
            color='green', marker='o', s=60, alpha=0.6, label='Air top')
# 10.2.8 Plot Residual air temperature
ax2.scatter(Temperature_reference + offset_air, res_air,
            color='yellow', marker='o', s=60, alpha=0.6, label='Air center')
# 10.2.9 Plot Residual air_bas temperature
ax2.scatter(Temperature_reference + offset_air_bas, res_air_bas,
            color='magenta', marker='o', s=60, alpha=0.6, label='Air bottom')
# 10.2.10 Plot Residual indoor temperature
ax2.scatter(Temperature_reference + offset_temp_indoor, res_temp_indoor,
            color='purple', marker='o', s=60, alpha=0.6, label='Temp. surf. indoor')
# 10.2.11 Plot Residual outdoor temperature
ax2.scatter(Temperature_reference + offset_temp_outdoor, res_temp_outdoor,
            color='orange', marker='o', s=60, alpha=0.6, label='Temp. surf. outdoor')
# Add vertical lines at setpoints to act as 'containers' for each group
setpoints = [0, 10, 20, 30, 40]  #add by hand, tired ...
for pt in setpoints:
    ax2.axvline(x=pt, color='gray', linestyle=':', linewidth=1, alpha=0.3)

# Formatting
ax2.set_xlabel('Calibration setpoints (°C)', fontsize=12, family='Times New Roman')
ax2.set_ylabel('Residual error (°C)', fontsize=12, family='Times New Roman')
ax2.set_xticks(setpoints)
ax2.set_xticklabels(['0°C', '10°C', '20°C', '30°C', '40°C'])
ax2.set_ylim(-0.3, 0.3) # Adjusted for high-precision view
ax2.grid(True, axis='y', linestyle='--', alpha=0.4)
ax2.text(0.98, 0.98, '(b)', transform=ax2.transAxes,
         ha='right', va='top',
         fontsize=12, fontweight='bold')
# Place legend below the plot, not needed
# ax2.legend(loc='upper center',
#            bbox_to_anchor=(0.5, -0.1),  # (x, y) coordinates
#            ncol=11,                      # Organize in 3 columns for better width
#            frameon=False,
#            fontsize=10,
#            prop={'family': 'Times New Roman'})
plt.tight_layout()
plt.savefig(os.path.join(output_directory, "Figure_thermocouples_calibration_with_residuals.png"), format='png', bbox_inches='tight', dpi=600)
plt.show()
# ----------------------------------------------------------------------------------------------------------------------
# 11. Print the calibration coefficients for use in your data acquisition
print(f"Calibration for Right wall (Est): Slope = {m1:.4f}, Offset = {c1:.4f}| R2: {r2_1:.2f} | Max Residual: {max_err1:.3f}°C")
print(f"Calibration for Ceiling:      Slope = {m2:.4f}, Offset = {c2:.4f}| R2: {r2_2:.2f} | Max Residual: {max_err2:.3f}°C")
print(f"Calibration for Door: Slope = {m3:.4f}, Offset = {c3:.4f}| R2: {r2_3:.2f} | Max Residual: {max_err3:.3f}°C")
print(f"Calibration for Window*: Slope = {m4:.4f}, Offset = {c4:.4f}| R2: {r2_4:.2f} | Max Residual: {max_err4:.3f}°C")
print(f"Calibration for Left wall (West):      Slope = {m5:.4f}, Offset = {c5:.4f}| R2: {r2_5:.2f} | Max Residual: {max_err5:.3f}°C")
print(f"Calibration for Floor: Slope = {m6:.4f}, Offset = {c6:.4f}| R2: {r2_6:.2f} | Max Residual: {max_err6:.3f}°C")
print(f"Calibration for Air top: Slope = {m7:.4f}, Offset = {c7:.4f}| R2: {r2_7:.2f} | Max Residual: {max_err7:.3f}°C")
print(f"Calibration for Air center: Slope = {m8:.4f}, Offset = {c8:.4f}| R2: {r2_8:.2f} | Max Residual: {max_err8:.3f}°C")
print(f"Calibration for Air bottom: Slope = {m9:.4f}, Offset = {c9:.4f}| R2: {r2_9:.2f} | Max Residual: {max_err9:.3f}°C")
print(f"Calibration for Temp. surf. indoor: Slope = {m10:.4f}, Offset = {c10:.4f}| R2: {r2_10:.2f} | Max Residual: {max_err10:.3f}°C")
print(f"Calibration for Temp. surf. outdoor: Slope = {m11:.4f}, Offset = {c11:.4f}| R2: {r2_11:.2f} | Max Residual: {max_err11:.3f}°C")
# Option 3 is considered to report the enlarged uncertainty accounting for flat rate
print(f"Expanded Uncertainty (2sigma):")
print(f"Right wall (Est): ±{expanded_uncertainty_with_flat_rate['Droite'].item():.3f} °C")
print(f"Ceiling:      ±{expanded_uncertainty_with_flat_rate['Toit'].item():.3f} °C")
print(f"Door:  ±{expanded_uncertainty_with_flat_rate['Porte'].item():.3f} °C")
print(f"Window*: ±{expanded_uncertainty_with_flat_rate['Fenetre'].item():.3f} °C")
print(f"Left wall (West):      ±{expanded_uncertainty_with_flat_rate['Gauche'].item():.3f} °C")
print(f"Floor:  ±{expanded_uncertainty_with_flat_rate['Sol'].item():.3f} °C")
print(f"Air top:  ±{expanded_uncertainty_with_flat_rate['Air haut'].item():.3f} °C")
print(f"Air center:  ±{expanded_uncertainty_with_flat_rate['Air'].item():.3f} °C")
print(f"Air bottom:  ±{expanded_uncertainty_with_flat_rate['Air bas'].item():.3f} °C")
print(f"Temp. surf. indoor:  ±{expanded_uncertainty_with_flat_rate['Temp Indoor'].item():.3f} °C")
print(f"Temp. surf. outdoor:  ±{expanded_uncertainty_with_flat_rate['Temp Outdoor'].item():.3f} °C")
# ----------------------------------------------------------------------------------------------------------------------
# 12. Create a list of dictionaries with all your calculated variables
calibration_data = [
    {"Sensor": "Right wall (Est)", "Slope": m1, "Offset": c1, "R2": r2_1, "Max_Residual": max_err1, "Uncertainty_2sigma": expanded_uncertainty_with_flat_rate['Droite'].item()},
    {"Sensor": "Ceiling",          "Slope": m2, "Offset": c2, "R2": r2_2, "Max_Residual": max_err2, "Uncertainty_2sigma": expanded_uncertainty_with_flat_rate['Toit'].item()},
    {"Sensor": "Door",             "Slope": m3, "Offset": c3, "R2": r2_3, "Max_Residual": max_err3, "Uncertainty_2sigma": expanded_uncertainty_with_flat_rate['Porte'].item()},
    {"Sensor": "Window*",          "Slope": m4, "Offset": c4, "R2": r2_4, "Max_Residual": max_err4, "Uncertainty_2sigma": expanded_uncertainty_with_flat_rate['Fenetre'].item()},
    {"Sensor": "Left wall (West)", "Slope": m5, "Offset": c5, "R2": r2_5, "Max_Residual": max_err5, "Uncertainty_2sigma": expanded_uncertainty_with_flat_rate['Gauche'].item()},
    {"Sensor": "Floor",            "Slope": m6, "Offset": c6, "R2": r2_6, "Max_Residual": max_err6, "Uncertainty_2sigma": expanded_uncertainty_with_flat_rate['Sol'].item()},
    {"Sensor": "Air top",         "Slope": m7, "Offset": c7, "R2": r2_7, "Max_Residual": max_err7, "Uncertainty_2sigma": expanded_uncertainty_with_flat_rate['Air haut'].item()},
    {"Sensor": "Air center",              "Slope": m8, "Offset": c8, "R2": r2_8, "Max_Residual": max_err8, "Uncertainty_2sigma": expanded_uncertainty_with_flat_rate['Air'].item()},
    {"Sensor": "Air bottom",          "Slope": m9, "Offset": c9, "R2": r2_9, "Max_Residual": max_err9, "Uncertainty_2sigma": expanded_uncertainty_with_flat_rate['Air bas'].item()},
    {"Sensor": "Temp. surf. indoor",      "Slope": m10, "Offset": c10, "R2": r2_10, "Max_Residual": max_err10, "Uncertainty_2sigma": expanded_uncertainty_with_flat_rate['Temp Indoor'].item()},
    {"Sensor": "Temp. surf. outdoor",     "Slope": m11, "Offset": c11, "R2": r2_11, "Max_Residual": max_err11, "Uncertainty_2sigma": expanded_uncertainty_with_flat_rate['Temp Outdoor'].item()}
]
# ----------------------------------------------------------------------------------------------------------------------
# 13. Convert to DataFrame and save the results as CSV file
df_results = pd.DataFrame(calibration_data)
# Display the table in the console to verify
print(df_results)
# save
output_file = os.path.join(output_directory, "Thermocouple_Calibration_Results_option3.csv")
df_results.to_csv(output_file, index=False, sep='\t', encoding='utf-8')
print(f"Results successfully saved to: {output_file}")
