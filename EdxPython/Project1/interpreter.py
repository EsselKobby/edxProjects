def calculate_result(x, operator, z):
    x = float(x)
    z = float(z)

    if operator == "+":
        return x + z
    elif operator == "-":
        return x - z
    elif operator == "*":
        return x * z
    elif operator == "/":
        if z != 0:
            return x / z
        else:
            return "Error: Division by zero"


if __name__ == "__main__":
    expression = input("Enter an arithmetic expression (e.g., 1 + 1): ")

    try:
        x, operator, z = expression.split()
        result = calculate_result(x, operator, z)
        print(f"Result: {result:.1f}")
    except ValueError:
        print("Invalid input. Please enter an expression in the format 'x y z'.")
    except Exception as e:
        print(f"An error occurred: {e}")
