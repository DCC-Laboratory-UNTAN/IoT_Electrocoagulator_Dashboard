import streamlit as st
from app.config import SENSOR_MAX_HEIGHT_CM, DEFAULT_SENSOR_VALUES
from app.utils.styles import apply_metric_style


def render_water_quality() -> None:
    """Display water quality sensor metrics."""
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
    """Display ultrasonic water level readings as progress bars."""
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