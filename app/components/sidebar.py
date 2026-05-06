from datetime import datetime
import streamlit as st
from app.config import MODES, ACTUATORS, ACTUATOR_LABELS


def render_sidebar() -> str:
    """Render the sidebar and return the selected operation mode."""
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