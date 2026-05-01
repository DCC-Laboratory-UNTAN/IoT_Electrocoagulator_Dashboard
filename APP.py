#py -3.13 -m streamlit run "C:\Users\untan\OneDrive\Desktop\APP.py"
from cProfile import label
from datetime import datetime
from turtle import color
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import numpy as np

#logo dcc
HORIZONTAL_RED = "logo 1.png"
st.logo(HORIZONTAL_RED)

#judul
st.title("Electrocoagulator Prototype Monitoring")

if "system_active" not in st.session_state:
    st.session_state.system_active = False

#=============================Sidebar control==============================

st.sidebar.title("System Controls")

mode = st.sidebar.selectbox("Operation Mode", ["Manual", "Automatic"])

st.sidebar.write("Cycle Control")

coll11,coll22 = st.sidebar.columns([1,2])
with coll11:
    start= st.button("START")
    if start == True:
        st.session_state.system_active = True

with coll22:
    stop= st.button("EMERGENCY STOP")
    if stop == True:
        st.session_state.system_active = False
        st.session_state.mixing_motor = False
        st.session_state.electrode = False
        st.session_state.salt_pump = False
        st.session_state.raw_pump = False
        st.session_state.clean_pump = False
        st.session_state.dirt_pump = False

st.sidebar.divider()

auto= (mode=="Automatic") or (not st.session_state.system_active)

st.sidebar.write("Manual Actuator Control")

Mixing = st.sidebar.toggle("Mixing Motor", key="mixing_motor", disabled=auto)
Electrode = st.sidebar.toggle("Electrode", key="electrode", disabled=auto)
Salt_Pump = st.sidebar.toggle("Salt Pump", key="salt_pump", disabled=auto)
Raw_Pump = st.sidebar.toggle("Raw Pump", key="raw_pump", disabled=auto)
Clean_Pump = st.sidebar.toggle("Clean Pump", key="clean_pump", disabled=auto)
Dirt_Pump = st.sidebar.toggle("Dirt Pump", key="dirt_pump", disabled=auto)

st.sidebar.divider()

with st.sidebar:
    now = datetime.now().strftime("%H:%M:%S")
    st.caption(f"Last update: {now}")
    

#=============================System State==============================================

st.subheader("Current System State")

stage_keberapa=1

if st.session_state.system_active == True:
    st.success(f"SYSTEM ACTIVE: Processing Water (Stage {stage_keberapa}/5)")
else:
    st.error("SYSTEM DEACTIVE")

st.markdown(
    "<hr style='margin:5px 0'>",unsafe_allow_html=True
)

col_kiri, col_kanan = st.columns ([3,1])

#=====================================Water Quality=====================================

with col_kiri:
    
    st.subheader("Sensor Data")

    st.write("Water Quality (Reactor)")

    # kolom
    col1, col2, col3, col4 = st.columns(4)

    #data dummy
    ph=5
    turbidity=7
    temperature=32
    tds=500

    # nilai delta sebelumnya saat pertama kali jalan
    if "ph_sebelumnya" not in st.session_state:
        st.session_state.ph_sebelumnya = ph
    if "turbidity_sebelumnya" not in st.session_state:
        st.session_state.turbidity_sebelumnya = turbidity
    if "temperature_sebelumnya" not in st.session_state:
        st.session_state.temperature_sebelumnya = temperature
    if "tds_sebelumnya" not in st.session_state:
        st.session_state.tds_sebelumnya = tds

    # delta
    delta_ph= ph - st.session_state.ph_sebelumnya
    delta_turbidity= turbidity - st.session_state.turbidity_sebelumnya
    delta_temperature= temperature - st.session_state.temperature_sebelumnya
    delta_tds= tds - st.session_state.tds_sebelumnya

    # data display
    col1.metric("PH Level",  ph, delta=delta_ph)
    col2.metric("Turbidity (NTU)", turbidity, delta=delta_turbidity)
    col3.metric("Water Temperature (°C)", temperature, delta=delta_temperature)
    col4.metric("TDS (ppm)", tds, delta=delta_tds)

    # nilai sekarang jadi nilai sebelumnya
    st.session_state.ph_sebelumnya = ph 
    st.session_state.turbidity_sebelumnya = turbidity
    st.session_state.temperature_sebelumnya = temperature
    st.session_state.tds_sebelumnya = tds

    # style matrix
    st.markdown("""
    <style>
    div[data-testid="stMetric"] {
        background-color: #3498DB;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

#====================================Water Levels (ultrasonik)==============================

    st.write("Water Levels (Ultrasonic)")

    # 4 kolom
    coll1, coll2, coll3, coll4 = st.columns(4)

    # data dumy
    salt=80
    raw=50
    tank=30
    clean=100

    # tinggi sensor
    tinggisensor=100

    # hitung presentase
    salt_percentage = (salt / tinggisensor) * 100
    raw_percentage = (raw / tinggisensor) * 100
    tank_percentage = (tank / tinggisensor) * 100
    clean_percentage = (clean / tinggisensor) * 100

    # hitung jarak dari sensor
    salt_distance= tinggisensor-salt
    raw_distance= tinggisensor-raw
    tank_distance= tinggisensor-tank
    clean_distance= tinggisensor-clean

    # salt display
    with coll1:
        st.markdown("Salt Water")
        st.markdown(f"### {salt_percentage:.0f}%")
        st.progress(int(salt_percentage))
        st.caption(f"{salt_distance} cm from sensor")
    # raw display
    with coll2:
        st.markdown("Raw Water")
        st.markdown(f"### {raw_percentage:.0f}%")
        st.progress(int(raw_percentage))
        st.caption(f"{raw_distance} cm from sensor")
    # tank display
    with coll3:
        st.markdown("Tank Water")
        st.markdown(f"### {tank_percentage:.0f}%")
        st.progress(int(tank_percentage))
        st.caption(f"{tank_distance} cm from sensor")
    # clean display
    with coll4:
        st.markdown("Clean Water")
        st.markdown(f"### {clean_percentage:.0f}%")
        st.progress(int(clean_percentage))
        st.caption(f"{clean_distance} cm from sensor")

st.divider()

#=============================actuator status==============================
with col_kanan:

    st.subheader("Actuator Status")

    # data dummy
    mixing_status = "ON"
    electrode_status = "ON"
    salt_pump_status = "ON"
    raw_pump_status = "OFF"
    clean_pump_status = "OFF"
    dirt_pump_status = "OFF"

    #style box
    def status_box(label, status):
        if status == "ON":
            color= "#1f7a3e"
        else:
            color= "#7a1f1f"
        st.markdown(f"""
        <div style="
            background-color:{color};
            padding:10px;
            border-radius:8px;
            margin-bottom:20px;
            color:white;
        ">
            {label}: {status}
        </div>
        """, unsafe_allow_html=True)

    #pemanggilan fungsi dan display
    status_box("Mixing Motor", "ON" if Mixing else "OFF")
    status_box("Electrode", "ON" if Electrode else "OFF")
    status_box("Salt Pump", "ON" if Salt_Pump else "OFF")
    status_box("Raw Pump", "ON" if Raw_Pump else "OFF")
    status_box("Clean Pump", "ON" if Clean_Pump else "OFF")
    status_box("Dirt Pump", "ON" if Dirt_Pump else "OFF")




#=============================proses history==============================

st.subheader("Process History (Last Hour)")

#data dummy excel
df=pd.read_excel("process_history.xlsx")

#menampilkan grafik
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.Time, y=df["pH"], mode= 'lines+markers', name = 'PH Level'))
fig.add_trace(go.Scatter(x=df.Time, y=df["Turbidity (NTU)"], mode='lines+markers', name='Turbidity'))
fig.add_trace(go.Scatter(x=df.Time, y=df["Flow Rate (L/min)"], mode='lines+markers', name='Temperature'))
#fig.add_trace(go.Scatter(x=df.Time, y=df["TDS (ppm)"], mode='lines+markers', name='TDS'))
st.plotly_chart(fig)

