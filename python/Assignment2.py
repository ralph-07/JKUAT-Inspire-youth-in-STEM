# Function to provide advice based on the temperature
def provide_advice(temperature):
    if temperature < 10:
        return "It's very cold! Wear a jacket."
    elif 10<= temperature <= 19:
        return "It's a by chilly. Wear a sweater."
    elif 20 <= temperature <= 30:
        return "The weather is pleasant."
    elif  temperature >= 30:
        return "It's to hot! Stay hydrated."
    else:
        return "IT's very hot! Stay indoors."

# Main program
def main():
    try:
        temperature = float(input("Enter the current temperature in °C: "))
        advice = provide_advice(temperature)
        print(advice)
    except ValueError:
        print("Please enter a valid number for the temperature.")

if __name__ == "__main__":
    main()
