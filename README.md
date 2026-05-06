# 🌊 IoT Electrocoagulator Dashboard

A real-time monitoring dashboard for an **Electrocoagulator water treatment prototype**, built with [Streamlit](https://streamlit.io/) and [Plotly](https://plotly.com/python/).

---

## 📋 Overview

This dashboard provides live monitoring and manual/automatic control of an IoT-connected Electrocoagulator system used for water treatment. It visualizes sensor data, tank levels, actuator states, and historical process trends.

---

## ✨ Features

- **Real-time Sensor Monitoring** — pH, Turbidity, Temperature, and TDS readings from the reactor
- **Tank Level Visualization** — Ultrasonic sensor data for Salt, Raw, Tank, and Clean water reservoirs
- **Actuator Control Panel** — Toggle control for pumps, mixing motor, and electrode (Manual & Automatic modes)
- **Emergency Stop** — Immediately deactivates all actuators
- **Process History Chart** — Interactive Plotly chart of the last hour's sensor trends

---

## 🗂️ Project Structure

```
IoT_Electrocoagulator_Dashboard/
├── app/
│   ├── main.py                  # Main Streamlit app entry point
│   ├── components/
│   │   ├── sidebar.py           # Sidebar controls (mode, actuators, start/stop)
│   │   ├── sensor_data.py       # Water quality metrics & tank level displays
│   │   ├── actuator_status.py   # Actuator status panel
│   │   └── process_history.py   # Historical chart component
│   ├── utils/
│   │   └── styles.py            # Shared CSS/HTML styling helpers
│   └── config.py                # App-wide constants and configuration
├── assets/
│   └── logo 1.png               # DCC logo
├── data/
│   └── process_history.xlsx     # Historical process data
├── .streamlit/
│   └── config.toml              # Streamlit theme and server config
├── requirements.txt             # Python dependencies
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/IoT_Electrocoagulator_Dashboard.git
   cd IoT_Electrocoagulator_Dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the dashboard**
   ```bash
   streamlit run app/main.py
   ```

   Or using a specific Python version:
   ```bash
   py -3.13 -m streamlit run app/main.py
   ```

---

## 📦 Dependencies

| Package     | Purpose                        |
|-------------|-------------------------------|
| `streamlit` | Web dashboard framework        |
| `plotly`    | Interactive charts             |
| `pandas`    | Data manipulation              |
| `numpy`     | Numerical operations           |
| `openpyxl`  | Reading `.xlsx` process data   |

Install all at once:
```bash
pip install streamlit plotly pandas numpy openpyxl
```

---

## ⚙️ Configuration

Streamlit settings (theme, port, etc.) are managed in `.streamlit/config.toml`:

```toml
[server]
port = 8501
headless = true

[theme]
primaryColor = "#3498DB"
backgroundColor = "#0e1117"
secondaryBackgroundColor = "#1e2130"
textColor = "#ffffff"
```

---

## 🖼️ Dashboard Sections

| Section              | Description                                              |
|----------------------|----------------------------------------------------------|
| **System State**     | Shows whether the system is active and current stage     |
| **Water Quality**    | pH, Turbidity (NTU), Temperature (°C), TDS (ppm) metrics |
| **Water Levels**     | Progress bars for 4 tanks via ultrasonic sensors         |
| **Actuator Status**  | Color-coded ON/OFF status for all 6 actuators            |
| **Process History**  | Line chart of sensor readings over the last hour         |

---

## 🔌 Hardware Integration

> The current version uses **dummy/simulated data**. To connect real IoT hardware, replace the placeholder values in `app/components/sensor_data.py` with your MQTT/HTTP data source (e.g., ESP32, Node-RED, or a database feed).

Suggested integration approaches:
- **MQTT** via `paho-mqtt`
- **REST API** polling from microcontroller
- **Firebase / InfluxDB** for time-series storage

---

## 📄 License

This project is licensed under the terms of the [LICENSE](LICENSE) file.

---

## 👤 Author

Developed by the **DCC Team** for the Electrocoagulator Prototype project.