Thermocouple Calibration with Calibrated Dry-Block

This repository contains a Python-based tool for processing calibration data of 6 thermocouples using a dry-block calibrator (puits sec). 
The script automates data reduction for 5 temperature setpoints ($0, 10, 20, 30, 40$ °C) with multiple repetitions per point.

Calibration Procedure
The analysis follows standard metrological practices for temperature sensors:
Channels: 6 Thermocouples.
Points: 5 Setpoints ($0, 10, 20, 30, 40$ °C).
Repetitions: 10 discrete measurements per setpoint to ensure thermal stability and calculate Type A uncertainty.
Reference: Comparison against a calibrated dry-block internal/external reference sensor.

Features
Automated Averaging: Processes 800+ data points (8 sensors × 10 readings × 5 points) in seconds.
Error Calculation: Computes the systematic deviation ($\epsilon$) for each sensor.
Statistical Analysis: Calculates standard deviation and Type A uncertainty ($u_A$) according to ISO/IEC 17025.Visualization: Generates calibration curves and error plots.

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
Prepare your data in a CSV file (see sample_data.csv for format).
Run the main analysis script:
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
