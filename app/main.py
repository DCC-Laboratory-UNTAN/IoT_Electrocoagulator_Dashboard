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

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(page_title=APP_TITLE, layout="wide")
st.logo(LOGO_PATH)
st.title(APP_TITLE)

# ── Session state defaults ──────────────────────────────────────────────────────
if "system_active" not in st.session_state:
    st.session_state.system_active = False
for key in ACTUATORS:
    if key not in st.session_state:
        st.session_state[key] = False

# ── Sidebar ─────────────────────────────────────────────────────────────────────
mode = render_sidebar()

# ── System state banner ─────────────────────────────────────────────────────────
st.subheader("Current System State")
stage = 1  # TODO: replace with dynamic stage tracking
if st.session_state.system_active:
    st.success(f"SYSTEM ACTIVE: Processing Water (Stage {stage}/5)")
else:
    st.error("SYSTEM INACTIVE")

horizontal_rule()

# ── Main layout ──────────────────────────────────────────────────────────────────
col_left, col_right = st.columns([3, 1])

with col_left:
    st.subheader("Sensor Data")
    render_water_quality()
    render_water_levels()

with col_right:
    render_actuator_status()

st.divider()

# ── Process history ──────────────────────────────────────────────────────────────
render_process_history()