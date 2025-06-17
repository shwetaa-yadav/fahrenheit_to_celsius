
# Program: fahrenheit_to_celsius


def validate_data(value):
    try:
        if not value:
            raise ValueError("Input cannot be empty.")
        float_val = float(value)  
        return float_val
    except ValueError:
        print("Error: Please enter a valid number.")
        return None

def get_float(prompt):
    while True:
        user_input = input(prompt)
        validated = validate_data(user_input)
        if validated is not None:
            return validated

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def run_temperature_conversion():
    fahrenheit = get_float("Enter temperature in degrees Fahrenheit :")
    celsius = convert_to_celsius(fahrenheit)
    print(f"\n{fahrenheit}Fahrenheit is equal to {celsius:.2f} Degree Celsius.")

if __name__ == "__main__":
    run_temperature_conversion()
