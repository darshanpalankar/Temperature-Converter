#TemperatureConverter
from pyfiglet import Figlet
f = Figlet(font = 'smslant', width = 500)

class TemperatureConverter:
    def __init__(self, Temperature):
        self.temp = Temperature
    
    def celsiusToFahrenheit(self):
        return (self.temp * 9/5) + 32
    
    def fahrenheitToCelsius(self):
        return (self.temp - 32) * 5/9
    
    def fahrenheitToKelvin(self):
        return (self.temp - 32) * 5/9 + 273.15
    
    def celsiusToKelvin(self):
        return self.temp + 273.15

    def kelvinToCelsius(self):
        return self.temp - 273.15
    
    def kelvinToFahrenheit(self):
        return ((self.temp - 273.15) * 9/5 + 32)

def main():
    print("============================================================================================")
    print(f.renderText("Temperature Converter"))
    print('                                                                       -Darshan Palankar    ')
    print("============================================================================================")

    while True:
        print("\n1. Celsius to Fahrenheit")
        print("2. Celsius to Kelvin")
        print("3. Fahrenheit to Celsius")
        print("4. Fahrenheit to Kelvin")
        print("5. Kelvin to Celsius")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")

        choice = input("\nEnter Your Choice : ")
        
        if choice == '7':
            print("<< - Exiting Temperature Converter - >>")
            break
        
        Temperature = float(input("\nEnter Temperature Value : "))
        TC = TemperatureConverter(Temperature)

        if choice == '1':
            print(f"Result : {TC.celsiusToFahrenheit()} Fahrenheit")
        elif choice == '2':
            print(f"Result : {TC.celsiusToKelvin()} Kelvin")
        elif choice == '3':
            print(f"Result : {TC.fahrenheitToCelsius()} Celsius")
        elif choice == '4':
            print(f"Result : {TC.fahrenheitToKelvin()} Kelvin")
        elif choice == '5':
            print(f"Result : {TC.kelvinToCelsius()} Celsius")
        elif choice == '6':
            print(f"Result : {TC.kelvinToFahrenheit()} Fahrenheit")
        else:
            print("Invalid Choice ..!!")

if __name__ == '__main__':
    main()