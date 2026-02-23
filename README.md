Thermocouple Calibration with Calibrated Dry-Block

This repository contains a Python-based tool for processing calibration data of 6 thermocouples using a dry-block calibrator. 
The script automates data reduction for 5 temperature setpoints ($0, 10, 20, 30, 40$ °C) with multiple repetitions per point.

Calibration Procedure
The analysis follows standard metrological practices for temperature sensors:
Channels: 6 Thermocouples.
Points: 5 Setpoints ($0, 10, 20, 30, 40$ °C).
Repetitions: 11 discrete measurements per setpoint to ensure thermal stability and calculate Type A uncertainty.
Reference: Comparison against a calibrated dry-block internal/external reference sensor.

Methodology & Data Processing
The script processes the thermocouple data through a rigorous metrological workflow:
1. Linear Regression AnalysisFor each of the sensors (Droite, Toit, Porte, Fenêtre, Gauche, Sol), the script calculates a first-degree polynomial fit (linear regression) against the reference temperature ($T_{ref}$).
   The calibration curve follows the model:
   $T_{ref} = m \cdot T_{sensor} + c$
   where $m$ (Slope): Sensitivity correction.
   $c$ (Intercept): Zero-offset correction.
3. Statistical Validation ($R^2$ and Residuals)
   To ensure the reliability of the dry-block stability and sensor linearity:
   Coefficient of Determination ($R^2$): Quantifies how well the linear model fits the 50 data points (10 readings $\times$ 5 setpoints).
   Residual Analysis: Calculates the difference between the actual reference temperature and the predicted value from the regression.
4. Expanded Uncertainty ($U$)
   Following ISO/IEC 17025 and GUM (Guide to the Expression of Uncertainty in Measurement) principles, the script calculates the Expanded Uncertainty.
   We use a coverage factor of $k=2$ (providing a confidence level of approximately 95%):
   $$U = k \cdot \sigma_{residuals}$$
   Where $\sigma_{residuals}$ is the standard deviation of the residuals, representing the combined repeatability of the dry-block and the sensor under test.

Features
Data processing: Processes 385 data points (6 sensors × 11 readings × 5 points) in seconds.
Error Calculation: Computes the systematic deviation ($\epsilon$) for each sensor.
Statistical Analysis: Calculates standard deviation and Type A uncertainty ($u_A$) according to ISO/IEC 17025.
Visualization: Generates calibration curves and error plots.

Compliance & Standards
The methodology in this script aligns with:

ISO/IEC 17025:2017: General requirements for the competence of testing and calibration laboratories.
FD X07-029-2:2005: Metrology - Thermometer verification and calibration procedure - Part 2: Verification and calibration procedures for thermocouples alone and thermocouple thermometers.
EURAMET tc-pr-18: Guidelines on the calibration of temperature block calibrators.
ITS-90: International Temperature Scale of 1990.

Getting Started
Prerequisites
Install the required libraries:
Bash
pip install -r requirements.txt

Usage
1. Prepare your data in a CSV file (see sample_data.csv for format).
2. Run the main analysis script:
Bash
python calibrate_tc.py

Citation
If you use this software in your research or industrial laboratory, please cite it as follows:

Code snippet
@software{pinas_tc_calib_2026,
  author       = {Piñas, Joshua},
  title        = {Thermocouple Calibration with Calibrated DryBlock},
  year         = 2026,
  publisher    = {GitHub},
  doi          = {10.1234/zenodo.1234567},
  url          = {https://github.com/mcjoshuapinas/Thermocouple-Calibration-with-Calibrated-Dry-Block}
}
