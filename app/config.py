"""
Configuration Module - Centralized Application Settings

This module defines all application-wide constants, labels, and default values.
It serves as a single source of truth for:
- Application title and branding
- File paths (logo, data storage)
- Hardware sensor specifications
- Operation modes and actuator definitions
- Default sensor values for testing

Benefit: Changes to configuration only need to be made in one place,
and changes are automatically reflected across all modules.
"""

APP_TITLE = "Electrocoagulator Prototype Monitoring"
LOGO_PATH = "assets/logo 1.png"
DATA_PATH = "data/process_history.xlsx"

# Ultrasonic sensor max range (cm)
SENSOR_MAX_HEIGHT_CM = 100

# Operation modes
MODES = ["Manual", "Automatic"]

# Actuator labels (used across components)
ACTUATORS = [
    "mixing_motor",
    "electrode",
    "salt_pump",
    "raw_pump",
    "clean_pump",
    "dirt_pump",
]

ACTUATOR_LABELS = {
    "mixing_motor": "Mixing Motor",
    "electrode": "Electrode",
    "salt_pump": "Salt Pump",
    "raw_pump": "Raw Pump",
    "clean_pump": "Clean Pump",
    "dirt_pump": "Dirt Pump",
}

# Water quality sensor defaults (replace with live data source)
DEFAULT_SENSOR_VALUES = {
    "ph": 7.0,
    "turbidity": 0.0,
    "temperature": 25.0,
    "tds": 0,
}