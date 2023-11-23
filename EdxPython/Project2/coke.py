def coke_machine():
    # Constants
    coke_price = 50  # 50 cents for a bottle of Coke
    accepted_coins = [25, 10, 5]  # Accepted coin denominations

    # Variables
    amount_inserted = 0

    # Check for invalid amount of cents
    if amount_inserted % 5 != 0:
        print(
            "Invalid amount of cents. Please insert coins in denominations of 25, 10, or 5 cents."
        )
        return

    # Continue prompting the user for coins until enough is inserted
    while amount_inserted < coke_price:
        try:
            # Inform the user of the amount due
            print(f"Amount Due: {coke_price - amount_inserted}")
            # Get user input for the coin
            coin = int(input("Insert Coin: "))

            # Check if the coin is an accepted denomination
            if coin not in accepted_coins:
                print(
                    "Invalid coin. Please insert coins in denominations of 25, 10, or 5 cents."
                )
                continue

            # Update the amount inserted
            amount_inserted += coin

            # Check if enough money has been inserted
            if amount_inserted >= coke_price:
                print("Change Owed: 0")
                break

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Calculate and output change
    change = amount_inserted - coke_price

    # Only display change if there is change
    if change > 0:
        print(f"Change Owed: {change}")


if __name__ == "__main__":
    coke_machine()
