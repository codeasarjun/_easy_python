def convert_length(value, from_unit, to_unit):
    length_units = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'feet': 0.3048,
        'inches': 0.0254
    }
    return value * (length_units[from_unit] / length_units[to_unit])

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'grams': 1,
        'kilograms': 1000,
        'milligrams': 0.001,
        'pounds': 453.592,
        'ounces': 28.3495
    }
    return value * (weight_units[from_unit] / weight_units[to_unit])

def convert_volume(value, from_unit, to_unit):
    volume_units = {
        'liters': 1,
        'milliliters': 0.001,
        'cubic_meters': 1000,
        'cubic_centimeters': 0.001,
        'gallons': 3.78541,
        'pints': 0.473176
    }
    return value * (volume_units[from_unit] / volume_units[to_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        if to_unit == 'kelvin':
            return value + 273.15
    if from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        if to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
    if from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        if to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32

def main():
    while True:
        print("Select type of conversion:")
        print("1. Length")
        print("2. Weight")
        print("3. Volume")
        print("4. Temperature")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")

        if choice == '5':
            break
        
        if choice in ['1', '2', '3']:
            value = float(input("Enter value: "))
            from_unit = input("Enter from unit: ")
            to_unit = input("Enter to unit: ")

            if choice == '1':
                result = convert_length(value, from_unit, to_unit)
            elif choice == '2':
                result = convert_weight(value, from_unit, to_unit)
            elif choice == '3':
                result = convert_volume(value, from_unit, to_unit)
            
            print(f"Converted value: {result} {to_unit}")

        elif choice == '4':
            value = float(input("Enter value: "))
            from_unit = input("Enter from unit (celsius, fahrenheit, kelvin): ")
            to_unit = input("Enter to unit (celsius, fahrenheit, kelvin): ")

            result = convert_temperature(value, from_unit, to_unit)
            print(f"Converted value: {result} {to_unit}")

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
