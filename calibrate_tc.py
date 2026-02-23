import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from sklearn.metrics import r2_score

# --- PATH CONFIGURATION ---
# Get the absolute path of the directory where the script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define relative paths for data input and results output
# This ensures the code works on any computer without modification
data_folder = os.path.join(BASE_DIR, "data")
output_directory = os.path.join(BASE_DIR, "output")

# Create the output directory automatically if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# --- DATA LOADING: Temperatures ---
# Path to the temperature values from thermocouple and Dry-Block CSV file
# The file contains 7 columns
# First column value is related to reference temperature 'Dry-Block'
# The others are related to 6 temperatures from thermocouples to be calibrated
# Each column have 50 values, which are divided in 5 temperatures reference points, so 10 measurements per point
data_file = os.path.join(data_folder, "thermocouples_calibration_2.csv")

# Read the CSV (whitespace separated, no header in the source file)
values = pd.read_csv(data_file, delim_whitespace=True, header=None)

# Rename columns for clarity
values.columns = ['JOFRA', 'Droite', 'Toit', 'Porte', 'Fenetre', 'Gauche', 'Sol']

# Rename variable for clarity
# droite = right; toit=ceiling; porte=door; fenetre=window; gauche= left; sol=ground
# JOFRA is the Calibrated Dry-Block and it is the reference temperature for calibration

Temperature_reference = values['JOFRA']
Temperature_droite = values['Droite']
Temperature_toit = values['Toit']
Temperature_porte = values['Porte']
Temperature_fenetre = values['Fenetre']
Temperature_Gauche = values['Gauche']
Temperature_sol = values['Sol']

#Verifying appropriate storage of reference temperature

print(Temperature_reference)


# 1. Calculate Linear Regression for both sensors
# polyfit(x, y, degree) -> degree 1 is a linear line
m1, c1 = np.polyfit(Temperature_droite, Temperature_reference, 1)
m2, c2 = np.polyfit(Temperature_toit, Temperature_reference, 1)
m3, c3 = np.polyfit(Temperature_porte, Temperature_reference, 1)
m4, c4 = np.polyfit(Temperature_fenetre, Temperature_reference, 1)
m5, c5 = np.polyfit(Temperature_Gauche, Temperature_reference, 1)
m6, c6 = np.polyfit(Temperature_sol, Temperature_reference, 1)

# 2. Create the regression lines for plotting
# Calibration curve
reg_line1 = m1 * Temperature_droite + c1
reg_line2 = m2 * Temperature_toit + c2
reg_line3 = m3 * Temperature_porte + c3
reg_line4 = m4 * Temperature_fenetre + c4
reg_line5 = m5 * Temperature_Gauche + c5
reg_line6 = m6 * Temperature_sol + c6

# 3. Calculate R² and the Maximum residual
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

# 4. Calculate the residual
res_droite = Temperature_reference - reg_line1
res_toit = Temperature_reference - reg_line2
res_porte = Temperature_reference - reg_line3
res_fenetre = Temperature_reference - reg_line4
res_Gauche = Temperature_reference - reg_line5
res_sol = Temperature_reference - reg_line6

# 5. Calculate the Expanded Uncertainty (2 * Standard Deviation)
uncertainty_droite = 2 * np.std(res_droite)
uncertainty_toit  = 2 * np.std(res_toit)
uncertainty_porte  = 2 * np.std(res_porte)
uncertainty_fenetre = 2 * np.std(res_fenetre)
uncertainty_Gauche  = 2 * np.std(res_Gauche)
uncertainty_sol  = 2 * np.std(res_sol)

# 6. Offset values for residual error plot
offset_droite = -0.5
offset_toit  = -0.3
offset_porte  = -0.1
offset_fenetre = 0.1
offset_Gauche  = 0.3
offset_sol  = 0.5

# 7. Create Figure with 2 Subplots (Top for Curve, Bottom for Residuals)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12), sharex=False,
                               gridspec_kw={'height_ratios': [2, 1]})
# 7.1 TOP PLOT: Calibration Curves ---
ax1.scatter(Temperature_droite, Temperature_reference, color='firebrick', marker='s', alpha=0.5, label='Right wall (Est)')
ax1.plot(Temperature_droite, reg_line1, 'r--', label=f'Fit: {m1:.4f}x + {c1:.4f} ($R^2$={r2_1:.4f})')

ax1.scatter(Temperature_toit, Temperature_reference, color='chocolate', marker='d', alpha=0.5, label='Ceiling')
ax1.plot(Temperature_toit, reg_line2, 'b--', label=f'Fit: {m2:.4f}x + {c2:.4f} ($R^2$={r2_2:.4f})')

ax1.scatter(Temperature_porte, Temperature_reference, color='orange', marker='*', alpha=0.5, label='Door')
ax1.plot(Temperature_porte, reg_line3, 'k--', label=f'Fit: {m3:.4f}x + {c3:.4f} ($R^2$={r2_3:.4f})')

ax1.scatter(Temperature_fenetre, Temperature_reference, color='royalblue', marker='^', alpha=0.5, label='Window*')
ax1.plot(Temperature_fenetre, reg_line4, 'r--', label=f'Fit: {m4:.4f}x + {c4:.4f} ($R^2$={r2_4:.4f})')

ax1.scatter(Temperature_Gauche, Temperature_reference, color='darkcyan', marker='v', alpha=0.5, label='Left wall (West)')
ax1.plot(Temperature_toit, reg_line5, 'b--', label=f'Fit: {m5:.4f}x + {c5:.4f} ($R^2$={r2_5:.4f})')

ax1.scatter(Temperature_sol, Temperature_reference, color='slategrey', marker='o', alpha=0.5, label='Floor')
ax1.plot(Temperature_sol, reg_line6, 'k--', label=f'Fit: {m6:.4f}x + {c6:.4f} ($R^2$={r2_6:.4f})')

ax1.set_xlabel('Measured Temperature (°C)', fontsize=12, family='Times New Roman')
ax1.set_title('Thermocouple Calibration Analysis', fontsize=14, family='Times New Roman')
ax1.legend(loc='upper left', frameon=True, prop={'family': 'Times New Roman', 'size': 10})
ax1.grid(True, linestyle=':', alpha=0.6)

# 7.2 BOTTOM PLOT: Residuals ---
# Zero error line
ax2.axhline(y=0, color='black', linestyle='-', linewidth=1.5, alpha=0.7)

# 7.2.1 Plot Residual right temperature
ax2.scatter(Temperature_reference + offset_droite, res_droite,
            color='firebrick', marker='s', s=60, alpha=0.6, label='Right wall (Est)')
# 7.2.2 Plot Residual ceiling temperature
ax2.scatter(Temperature_reference + offset_toit, res_toit,
            color='chocolate', marker='d', s=60, alpha=0.6, label='Ceiling')
# 7.2.3 Plot Residual door temperature
ax2.scatter(Temperature_reference + offset_porte, res_porte,
            color='orange', marker='*', s=60, alpha=0.6, label='Door')
# 7.2.4 Plot Residual window temperature
ax2.scatter(Temperature_reference + offset_fenetre, res_fenetre,
            color='royalblue', marker='^', s=60, alpha=0.6, label='Window*')
# 7.2.5 Plot Residual left temperature
ax2.scatter(Temperature_reference + offset_Gauche, res_Gauche,
            color='darkcyan', marker='v', s=60, alpha=0.6, label='Left wall (West)')
# 7.2.6 Plot Residual ground temperature
ax2.scatter(Temperature_reference + offset_sol, res_sol,
            color='slategrey', marker='o', s=60, alpha=0.6, label='Floor')

# Add vertical lines at setpoints to act as 'containers' for each group
setpoints = [0, 10, 20, 30, 40]
for pt in setpoints:
    ax2.axvline(x=pt, color='gray', linestyle=':', linewidth=1, alpha=0.3)

# Formatting
ax2.set_xlabel('Calibration Setpoints (°C)', fontsize=12, family='Times New Roman')
ax2.set_ylabel('Residual Error (°C)', fontsize=12, family='Times New Roman')
ax2.set_xticks(setpoints)
ax2.set_xticklabels(['0°C', '10°C', '20°C', '30°C', '40°C'])
ax2.set_ylim(-0.3, 0.3) # Adjusted for high-precision view
ax2.grid(True, axis='y', linestyle='--', alpha=0.4)

# Place legend below the plot
ax2.legend(loc='upper center',
           bbox_to_anchor=(0.5, -0.1), # (x, y) coordinates
           ncol=6,                      # Organize in 3 columns for better width
           frameon=False,
           fontsize=10,
           prop={'family': 'Times New Roman'})

plt.tight_layout()
plt.savefig(os.path.join(output_directory, "Figure_thermocouples_calibration_with_residuals.png"), format='png', bbox_inches='tight', dpi=600)
plt.show()


# 8. Print the calibration coefficients for use in your data acquisition
print(f"Calibration for Right wall (Est): Slope = {m1:.6f}, Offset = {c1:.6f}| R2: {r2_1:.6f} | Max Residual: {max_err1:.3f}°C")
print(f"Calibration for Ceiling:      Slope = {m2:.6f}, Offset = {c2:.6f}| R2: {r2_2:.6f} | Max Residual: {max_err2:.3f}°C")
print(f"Calibration for Door: Slope = {m3:.6f}, Offset = {c3:.6f}| R2: {r2_3:.6f} | Max Residual: {max_err3:.3f}°C")
print(f"Calibration for Window*: Slope = {m4:.6f}, Offset = {c4:.6f}| R2: {r2_4:.6f} | Max Residual: {max_err4:.3f}°C")
print(f"Calibration for Left wall (West):      Slope = {m5:.6f}, Offset = {c5:.6f}| R2: {r2_5:.6f} | Max Residual: {max_err5:.3f}°C")
print(f"Calibration for Floor: Slope = {m6:.6f}, Offset = {c6:.6f}| R2: {r2_6:.6f} | Max Residual: {max_err6:.3f}°C")
print(f"Expanded Uncertainty (2sigma):")
print(f"Right wall (Est): ±{uncertainty_droite:.3f} °C")
print(f"Ceiling:      ±{uncertainty_toit:.3f} °C")
print(f"Door:  ±{uncertainty_porte:.3f} °C")
print(f"Window*: ±{uncertainty_fenetre:.3f} °C")
print(f"Left wall (West):      ±{uncertainty_Gauche:.3f} °C")
print(f"Floor:  ±{uncertainty_sol:.3f} °C")

# 9. Create a list of dictionaries with all your calculated variables
calibration_data = [
    {"Sensor": "Right wall (Est)", "Slope": m1, "Offset": c1, "R2": r2_1, "Max_Residual": max_err1, "Uncertainty_2sigma": uncertainty_droite},
    {"Sensor": "Ceiling",          "Slope": m2, "Offset": c2, "R2": r2_2, "Max_Residual": max_err2, "Uncertainty_2sigma": uncertainty_toit},
    {"Sensor": "Door",             "Slope": m3, "Offset": c3, "R2": r2_3, "Max_Residual": max_err3, "Uncertainty_2sigma": uncertainty_porte},
    {"Sensor": "Window*",          "Slope": m4, "Offset": c4, "R2": r2_4, "Max_Residual": max_err4, "Uncertainty_2sigma": uncertainty_fenetre},
    {"Sensor": "Left wall (West)", "Slope": m5, "Offset": c5, "R2": r2_5, "Max_Residual": max_err5, "Uncertainty_2sigma": uncertainty_Gauche},
    {"Sensor": "Floor",            "Slope": m6, "Offset": c6, "R2": r2_6, "Max_Residual": max_err6, "Uncertainty_2sigma": uncertainty_sol}
]

# 10. Convert to DataFrame
df_results = pd.DataFrame(calibration_data)

# 11. Save the Results into a CSV file

output_file = os.path.join(output_directory, "Thermocouple_Calibration_Results.csv")
df_results.to_csv(output_file, index=False, sep='\t', encoding='utf-8')

print(f"Results successfully saved to: {output_path}")

# 12. Display the table in the console to verify
print(df_results)
