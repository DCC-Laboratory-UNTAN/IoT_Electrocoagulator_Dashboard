"""
Main Application Module - Entry Point and Layout Orchestration

This is the primary entry point for the Electrocoagulator Prototype Monitoring Dashboard.
It orchestrates the overall page layout and integrates all UI components:

Layout Structure:
1. Header with logo and title
2. System state banner (Active/Inactive status)
3. Main content area:
   - Left (3/4 width): Sensor data and water levels
   - Right (1/4 width): Actuator status indicators
4. Process history chart

Key Responsibilities:
- Initialize Streamlit page configuration
- Set up session state for system controls and actuators
- Render the sidebar with control options
- Aggregate and display all components
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from app.config import APP_TITLE, LOGO_PATH, ACTUATORS
from app.components.sidebar import render_sidebar
from app.components.sensor_data import render_water_quality, render_water_levels
from app.components.actuator_status import render_actuator_status
from app.components.process_history import render_process_history
from app.utils.styles import horizontal_rule

# Configure Streamlit page layout and title
st.set_page_config(page_title=APP_TITLE, layout="wide")
st.logo(LOGO_PATH)
st.title(APP_TITLE)

# Initialize session state variables for system controls and actuator states
# These persist across Streamlit reruns and store user interactions
if "system_active" not in st.session_state:
    st.session_state.system_active = False
for key in ACTUATORS:
    if key not in st.session_state:
        st.session_state[key] = False

# Render the sidebar with operation mode, cycle controls, and manual actuator toggles
mode = render_sidebar()

# Display the current system state banner with active status and processing stage
st.subheader("Current System State")
stage = 1  # TODO: replace with dynamic stage tracking from process logic
if st.session_state.system_active:
    st.success(f"SYSTEM ACTIVE: Processing Water (Stage {stage}/5)")
else:
    st.error("SYSTEM INACTIVE")

horizontal_rule()

# Main dashboard layout: 3/4 for sensors and water levels, 1/4 for actuator status
col_left, col_right = st.columns([3, 1])

with col_left:
    st.subheader("Sensor Data")
    # Display water quality metrics (pH, turbidity, temperature, TDS)
    render_water_quality()
    # Display water level readings from ultrasonic sensors
    render_water_levels()

with col_right:
    # Display ON/OFF status for all actuators
    render_actuator_status()

st.divider()

# Display historical data chart showing trends over the last hour
render_process_history()