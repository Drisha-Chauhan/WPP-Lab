def main():
    feet = float(input("Enter the length in feet: "))

    conversions = [
        (12, "inches"),
        (1/3, "yards"),
        (1/5280, "miles"),
        (304.8, "millimeters"),
        (30.48, "centimeters"),
        (0.3048, "meters"),
        (0.0003048, "kilometers")
    ]

    print("\nChoose a conversion option:")
    for i, (_, unit) in enumerate(conversions, start=1):
        print(f"{i}. Convert to {unit}")

    choice = int(input("\nEnter your choice (1-7): "))

    if 1 <= choice <= len(conversions):
        factor, unit = conversions[choice - 1]
        result = feet * factor
        print(f"\n{feet} feet is equal to {result:.2f} {unit}.")
    else:
        print("\nInvalid choice. Please run the program again and choose a valid option.")

main()
