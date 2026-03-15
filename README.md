# OIBSIP_python_3BMI-Calculator
Advanced BMI Tracker built with Python and Tkinter that calculates BMI, categorizes health status, stores records in a database, and visualizes BMI progress using graphs.

This application allows users to calculate their BMI, store historical records, and visualize BMI progress through graphs.

The project demonstrates the use of GUI development, modular programming, database integration, and data visualization in Python.

Features

Calculate Body Mass Index (BMI) using weight and height.

Automatically determine BMI category:

Underweight

Normal

Overweight

Obese

Save BMI records into a local database.

Display recent BMI history inside the GUI.

Generate a BMI progress graph using Matplotlib.

Clean and simple Tkinter graphical interface.

Project Structure
BMI-Tracker
│
├── main.py            # Main Tkinter GUI application
├── bmi_logic.py       # Contains BMI calculation logic
├── database.py        # Handles database operations
└── README.md          # Project documentation
Technologies Used

Python

Tkinter (GUI development)

Matplotlib (data visualization)

SQLite / Local database (data storage)

How BMI is Calculated

BMI is calculated using the formula:

[
BMI = \frac{Weight (kg)}{Height^2 (m)}
]

Example:

Weight = 60 kg
Height = 1.78 m

BMI = 60 / (1.78 × 1.78)
BMI ≈ 18.94
Installation
1. Clone the repository
2. Install required libraries
pip install matplotlib

Tkinter usually comes pre-installed with Python.

Running the Application

Run the following command:

python main.py

The GUI application will open where you can:

Enter Weight (kg)

Enter Height (m)

Click Calculate & Save

View BMI result and category

Track BMI history

Visualize BMI progress graph
