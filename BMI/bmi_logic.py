

def calculate_bmi(weight_kg, height_m):
    """Calculates BMI value."""
    try:
        if height_m <= 0:
            return 0
        bmi = weight_kg / (height_m ** 2)
        return round(bmi, 2)
    except Exception as e:
        return 0

def get_bmi_category(bmi):
    """Returns the category based on BMI value."""
    if bmi <= 0:
        return "Invalid"
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"