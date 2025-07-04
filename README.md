# 🚗 Speed Calculator (PyQt6)

A simple desktop GUI application built with PyQt6 that calculates average speed based on user input for distance and time. Supports both metric (km/h) and imperial (mi/h) units.

---

## 🖥️ Features

- Input fields for distance and time
- Dropdown to select unit system (Metric or Imperial)
- Calculates and displays average speed
- Handles invalid input gracefully with error messages

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **PyQt6** | GUI framework for building the desktop interface |
| **Qt Widgets** | Used for layout, input fields, labels, buttons, and combo boxes |
| **QGridLayout** | Organizes widgets in a flexible grid layout |

---

## 📦 Requirements
- Python 3.7+
- PyQt6

Install PyQt6 via pip:
- pip install PyQt6

## 🚀 How to Run
- Clone or download this repository.
- Run the script:
python speed_calculator.py

## 🧠 How It Works
- The user enters a distance and time.
- Selects either Metric (km) or Imperial (mi) from the dropdown.
- Clicks "Convert" to calculate average speed.
- The result is displayed below the button.

## ⚠️ Error Handling
- If the user enters non-numeric values, the app displays:
"Entries must be numbers"