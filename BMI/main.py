import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt

import bmi_logic
import database

class BMIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced BMI Tracker")
        self.root.geometry("400x500")

        database.init_db()

        
        tk.Label(root, text="BMI Calculator", font=("Arial", 18, "bold")).pack(pady=10)

        input_frame = tk.Frame(root)
        input_frame.pack(pady=5)

        tk.Label(input_frame, text="Weight (kg):").grid(row=0, column=0, padx=5, pady=5)
        self.entry_weight = tk.Entry(input_frame)
        self.entry_weight.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Height (m):").grid(row=1, column=0, padx=5, pady=5)
        self.entry_height = tk.Entry(input_frame)
        self.entry_height.grid(row=1, column=1, padx=5, pady=5)

        # Calculate Button
        self.btn_calc = tk.Button(root, text="Calculate & Save", command=self.calculate_action, bg="#4CAF50", fg="white")
        self.btn_calc.pack(pady=10)

        # Result Label
        self.lbl_result = tk.Label(root, text="Enter details above", font=("Arial", 12))
        self.lbl_result.pack(pady=5)

        # View Graph Button
        self.btn_graph = tk.Button(root, text="View Progress Graph", command=self.show_graph)
        self.btn_graph.pack(pady=5)

        # History List
        tk.Label(root, text="Recent History:", font=("Arial", 10, "bold")).pack(pady=(20, 5))
        self.history_list = tk.Listbox(root, height=8, width=50)
        self.history_list.pack(padx=10, pady=5)

        # Load initial history
        self.update_history_list()

    def calculate_action(self):
        try:
            w = float(self.entry_weight.get())
            h = float(self.entry_height.get())
            
            # Use our logic file
            bmi = bmi_logic.calculate_bmi(w, h)
            category = bmi_logic.get_bmi_category(bmi)

            if bmi == 0:
                messagebox.showerror("Error", "Invalid input! Height must be greater than 0.")
                return

            # Display result
            self.lbl_result.config(text=f"BMI: {bmi} ({category})")
            
            # Save to database file
            database.save_record(w, h, bmi, category)
            
            # Refresh list
            self.update_history_list()

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    def update_history_list(self):
        self.history_list.delete(0, tk.END)
        records = database.fetch_history()
        for row in records:
            # row is (date, bmi, category)
            date_clean = row[0].split(" ")[0] # Just get the date part
            self.history_list.insert(tk.END, f"{date_clean} | BMI: {row[1]} | {row[2]}")

    def show_graph(self):
        data = database.fetch_all_bmi_for_graph()
        if not data:
            messagebox.showinfo("Info", "No data to show yet!")
            return
            
        ids = [x[0] for x in data]
        bmis = [x[1] for x in data]

        plt.figure(figsize=(6, 4))
        plt.plot(ids, bmis, marker='o', linestyle='-', color='b')
        plt.title("Your BMI Progress")
        plt.xlabel("Attempts")
        plt.ylabel("BMI Value")
        plt.grid(True)
        plt.show()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = BMIApp(root)
    root.mainloop()