import streamlit as st
from app.config import ACTUATORS, ACTUATOR_LABELS
from app.utils.styles import status_box


def render_actuator_status() -> None:
    """Display color-coded actuator ON/OFF status."""
    st.subheader("Actuator Status")
    for key in ACTUATORS:
        is_on = st.session_state.get(key, False)
        status_box(ACTUATOR_LABELS[key], "ON" if is_on else "OFF")