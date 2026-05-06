"""
Sensor Data Component Module

This module displays real-time sensor readings from the electrocoagulator system.
It provides two main visualization functions:

1. Water Quality Metrics:
   - pH Level: Acidity/alkalinity (typical range: 0-14)
   - Turbidity: Water clarity in NTU (Nephelometric Turbidity Units)
   - Temperature: Water temperature in Celsius
   - TDS: Total Dissolved Solids in ppm (parts per million)

2. Water Levels:
   - Four ultrasonic sensors measuring water levels in different tanks
   - Displayed as percentage filled and distance from sensor
   - Helps monitor tank capacity and prevent overflow

Note: Currently uses dummy/default values. Integration with actual sensors
requires replacing DEFAULT_SENSOR_VALUES with a live data source.
"""

import streamlit as st
from app.config import SENSOR_MAX_HEIGHT_CM, DEFAULT_SENSOR_VALUES
from app.utils.styles import apply_metric_style


def render_water_quality() -> None:
    """
    Display water quality metrics with delta (change) indicators.
    
    Shows four key water quality parameters:
    - pH Level: Measures acidity/alkalinity
    - Turbidity: Indicates water clarity
    - Temperature: Current water temperature
    - TDS (Total Dissolved Solids): Concentration of dissolved minerals
    
    Each metric displays:
    - Current value
    - Delta (change from previous reading) in green if improved, red if worsened
    - Helps users identify trends in water quality
    
    TODO: Replace dummy values with actual sensor data stream integration
    """
    st.write("Water Quality (Reactor)")

    col1, col2, col3, col4 = st.columns(4)

    # --- Replace these with live data source ---
    ph = DEFAULT_SENSOR_VALUES["ph"]
    turbidity = DEFAULT_SENSOR_VALUES["turbidity"]
    temperature = DEFAULT_SENSOR_VALUES["temperature"]
    tds = DEFAULT_SENSOR_VALUES["tds"]
    # -------------------------------------------

    for key, val in [
        ("ph_prev", ph),
        ("turbidity_prev", turbidity),
        ("temperature_prev", temperature),
        ("tds_prev", tds),
    ]:
        if key not in st.session_state:
            st.session_state[key] = val

    col1.metric("pH Level", ph, delta=round(ph - st.session_state.ph_prev, 2))
    col2.metric("Turbidity (NTU)", turbidity, delta=round(turbidity - st.session_state.turbidity_prev, 2))
    col3.metric("Temperature (°C)", temperature, delta=round(temperature - st.session_state.temperature_prev, 2))
    col4.metric("TDS (ppm)", tds, delta=round(tds - st.session_state.tds_prev, 2))

    st.session_state.ph_prev = ph
    st.session_state.turbidity_prev = turbidity
    st.session_state.temperature_prev = temperature
    st.session_state.tds_prev = tds

    apply_metric_style()


def render_water_levels() -> None:
    """
    Display ultrasonic sensor water level readings in four tanks.
    
    Converts raw sensor distance readings into percentage-filled display:
    - Tank labels: Salt Water, Raw Water, Tank Water, Clean Water
    - Visual representation: Progress bars showing fill percentage
    - Additional info: Distance from sensor in centimeters
    
    Calculation: percentage = (reading / SENSOR_MAX_HEIGHT_CM) * 100
    
    This allows users to:
    - Monitor tank capacity in real-time
    - Prevent overflow by checking fill levels
    - Plan refilling or maintenance based on depletion rates
    
    TODO: Replace dummy values with actual ultrasonic sensor readings
    """
    st.write("Water Levels (Ultrasonic)")

    coll1, coll2, coll3, coll4 = st.columns(4)

    # --- Replace these with live data source ---
    levels = {"Salt Water": 80, "Raw Water": 50, "Tank Water": 30, "Clean Water": 100}
    # -------------------------------------------

    for col, (label, reading) in zip([coll1, coll2, coll3, coll4], levels.items()):
        pct = (reading / SENSOR_MAX_HEIGHT_CM) * 100
        dist = SENSOR_MAX_HEIGHT_CM - reading
        with col:
            st.markdown(label)
            st.markdown(f"### {pct:.0f}%")
            st.progress(int(pct))
            st.caption(f"{dist} cm from sensor")