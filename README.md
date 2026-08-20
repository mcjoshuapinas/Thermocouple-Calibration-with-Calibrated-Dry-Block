Thermocouple Calibration with Calibrated Dry-Block

This repository contains a Python-based tool for processing calibration data of 11 thermocouples using a dry-block calibrator. 
The script automates data reduction for 5 temperature setpoints ($0, 10, 20, 30, 40$ °C) with multiple repetitions per point.
It provides the plot of thermocouples calibration with its residuals.
It saves the calibration data of each thermocouples in a CSV file.
To sum up, to use this calibration procedure, you must follow 'uncertainty_type_A_standard_deviation.py' and then 'calibration_correction_offset_statistical_metrics_uncertainty.py'.

Calibration Procedure
The analysis follows standard metrological practices for temperature sensors:
Channels: 11 Thermocouples.
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
   Coefficient of Determination ($R^2$): Quantifies how well the linear model fits the 55 data points (11 readings $\times$ 5 setpoints).
   Residual Analysis: Calculates the difference between the actual reference temperature and the predicted value from the regression.
4. Expanded Uncertainty ($U$)
   $U$ accounts for three main uncertainties like standard deviation (type A), resolution (type B), and certificate of calibration of the reference (type B).
   The script 'uncertainty_type_A_standard_deviation.py' calculates the uncertainty type A for each point.
   Three kind of Expanded Uncertainty are mentioned but only two are developed.
   It follows ISO/IEC 17025 and GUM (Guide to the Expression of Uncertainty in Measurement) principles, the script 'calibration_correction_offset_statistical_metrics_uncertainty.py' calculates the Expanded Uncertainty.
   We use a coverage factor of $k=2$ (providing a confidence level of approximately 95%) and a flat rate of 20% (meaning 1.2) to account for others uncertainties like instrument drift, heterogeneity (of thermoelectric     couple), and thermal errors.
   $$U = k \cdot \sigma_{residuals}$$
   Where $\sigma_{residuals}$ is the standard deviation of the residuals, representing the combined repeatability of the dry-block and the sensor under test.

Features
Data processing: Processes 605 data points (11 sensors × 11 readings × 5 points) in seconds.
Error Calculation: Computes the systematic deviation ($\epsilon$) for each sensor.
Statistical Analysis: Calculates standard deviation and Type A uncertainty ($u_A$) according to ISO/IEC 17025 and the expanded uncertainty.
Visualization: Generates calibration curves and error plots.

Compliance & Standards
The methodology in this script aligns with:

ISO/IEC 17025:2017: General requirements for the competence of testing and calibration laboratories.
FD X07-029-2, 2005: Metrology - Thermometer verification and calibration procedure - Part 2: Verification and calibration procedures for thermocouples alone and thermocouple thermometers.
FD X07-028, 2002: Metrology - Procedure for the calibration and verification of thermometers - Estimation of uncertainties in temperature measurements.
EURAMET tc-pr-18: Guidelines on the calibration of temperature block calibrators.
ITS-90: International Temperature Scale of 1990.

Getting Started
Prerequisites
Install the required libraries:
Bash
pip install -r requirements.txt

Usage
1. Download the two scripts and create two folders named 'data' and 'output' in the address of the scripts.
2. In 'data' copy/paste the example.
3. Run the two scripts:
Bash
python uncertainty_type_A_standard_deviation.py
python calibration_correction_offset_statistical_metrics_uncertainty.py
4. It will create output files including, statistical metrics and the calibration plot.
   
Citation
If you use this software in your research or industrial laboratory, please cite it as follows:
DOI: 10.5281/zenodo.22035513
Code snippet
@software{pinas_tc_calib_2026,
  author       = {Piñas, Joshua},
  title        = {Thermocouple Calibration with Calibrated DryBlock},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.22035513},
  version      = {v2.1.0},
  url          = {https://github.com/mcjoshuapinas/Thermocouple-Calibration-with-Calibrated-Dry-Block}
}
