def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    # Split the string at "$" and convert the second element to a float
    return float(d.split("$")[1])


def percent_to_float(p):
    # TODO
    # Remove the trailing '%' and convert to a float
    return (
        float(p.rstrip("%")) / 100.0
    )  # Divide by 100 to convert percentage to decimal


main()
