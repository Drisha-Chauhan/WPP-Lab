class Converter:
    conversion_factors = {
        "inches": 1,
        "feet": 1 / 12,
        "yards": 1 / 36,
        "miles": 1 / 63360,
        "millimeters": 25.4,
        "centimeters": 2.54,
        "meters": 0.0254,
        "kilometers": 0.0000254
    }

    def __init__(self, length, unit):
        if unit in self.conversion_factors:
            self.length_in_inches = length / self.conversion_factors[unit]
        else:
            print("Invalid unit. Defaulting to inches.")
            self.length_in_inches = length  
    def inches(self):
        return self.length_in_inches * self.conversion_factors["inches"]

    def feet(self):
        return self.length_in_inches * self.conversion_factors["feet"]

    def yards(self):
        return self.length_in_inches * self.conversion_factors["yards"]

    def miles(self):
        return self.length_in_inches * self.conversion_factors["miles"]

    def millimeters(self):
        return self.length_in_inches * self.conversion_factors["millimeters"]

    def centimeters(self):
        return self.length_in_inches * self.conversion_factors["centimeters"]

    def meters(self):
        return self.length_in_inches * self.conversion_factors["meters"]

    def kilometers(self):
        return self.length_in_inches * self.conversion_factors["kilometers"]


length = float(input("Enter the length: "))
unit = input("Enter the unit (inches, feet, yards, miles, kilometers, meters, centimeters, millimeters): ").lower()

converter = Converter(length, unit)

print("\nConverted values:")
print(f"Inches: {converter.inches()}")
print(f"Feet: {converter.feet()}")
print(f"Yards: {converter.yards()}")
print(f"Miles: {converter.miles()}")
print(f"Millimeters: {converter.millimeters()}")
print(f"Centimeters: {converter.centimeters()}")
print(f"Meters: {converter.meters()}")
print(f"Kilometers: {converter.kilometers()}")
