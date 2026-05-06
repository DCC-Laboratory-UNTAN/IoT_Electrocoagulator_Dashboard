"""
Sidebar Component Module

This module renders the main control interface in the Streamlit sidebar.
It provides users with:

1. Operation Mode Selection:
   - Manual: Operator controls each actuator individually
   - Automatic: System runs predefined control sequences

2. Cycle Control:
   - START button: Activates the water treatment process
   - EMERGENCY STOP: Immediately halts all operations and deactivates all actuators

3. Manual Actuator Control:
   - Toggle switches for each of the six actuators
   - Only enabled when in Manual mode AND system is Active
   - Disabled during Automatic mode or when system is inactive

4. Status Display:
   - Shows last update timestamp
"""

from datetime import datetime
import streamlit as st
from app.config import MODES, ACTUATORS, ACTUATOR_LABELS


def render_sidebar() -> str:
    """
    Render the complete sidebar control panel.
    
    Returns:
        str: The selected operation mode ("Manual" or "Automatic")
    
    Functionality:
    - Displays mode selector dropdown
    - Renders cycle control buttons (START and EMERGENCY STOP)
    - Renders manual actuator toggle switches
    - Shows last update timestamp
    
    Logic:
    - Manual actuator toggles are disabled if:
      * Mode is set to Automatic, OR
      * System is not active
    - EMERGENCY STOP deactivates system and ALL actuators
    """
    st.sidebar.title("System Controls")

    mode = st.sidebar.selectbox("Operation Mode", MODES)

    st.sidebar.write("Cycle Control")
    col1, col2 = st.sidebar.columns([1, 2])

    with col1:
        if st.button("START"):
            st.session_state.system_active = True

    with col2:
        if st.button("EMERGENCY STOP"):
            st.session_state.system_active = False
            for key in ACTUATORS:
                st.session_state[key] = False

    st.sidebar.divider()

    auto = (mode == "Automatic") or (not st.session_state.system_active)

    st.sidebar.write("Manual Actuator Control")
    for key in ACTUATORS:
        st.sidebar.toggle(ACTUATOR_LABELS[key], key=key, disabled=auto)

    st.sidebar.divider()

    with st.sidebar:
        now = datetime.now().strftime("%H:%M:%S")
        st.caption(f"Last update: {now}")

    return mode