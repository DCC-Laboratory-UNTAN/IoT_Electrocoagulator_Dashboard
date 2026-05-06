"""
Actuator Status Component Module

This module provides UI components for displaying the real-time status of all
electrocoagulator system actuators. It shows which actuators are currently active.

Actuators monitored:
- Mixing Motor: Stirs water in the reactor
- Electrode: Electrocoagulation process
- Salt Pump: Injects coagulant solution
- Raw Pump: Feeds raw water into the system
- Clean Pump: Circulates clean water
- Dirt Pump: Removes waste water
"""

import streamlit as st
from app.config import ACTUATORS, ACTUATOR_LABELS
from app.utils.styles import status_box


def render_actuator_status() -> None:
    """
    Render a color-coded display of all actuator ON/OFF states.
    
    Green box = actuator is ON
    Red box = actuator is OFF
    
    This component reads from session state and updates whenever
    the user toggles an actuator in the sidebar.
    """
    st.subheader("Actuator Status")
    for key in ACTUATORS:
        is_on = st.session_state.get(key, False)
        status_box(ACTUATOR_LABELS[key], "ON" if is_on else "OFF")