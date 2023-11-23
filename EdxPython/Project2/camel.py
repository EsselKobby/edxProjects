def main():
    # Get input from the user
    user_name = input("camelCase: ")

    # Conversion of camel case to snake case
    snake_case_name = camel_change(user_name)

    # Output of the result
    print(f"snake_case: {snake_case_name}")


def camel_change(x):
    snake_case_name = ""
    for char in x:
        if char.isupper():
            snake_case_name += "_" + char.lower()
        else:
            snake_case_name += char
    # Remove the leading underscore if present
    if snake_case_name.startswith("_"):
        snake_case_name = snake_case_name[1:]
    return snake_case_name


if __name__ == "__main__":
    main()
