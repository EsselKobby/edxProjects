greeting = input("Greeting: ")

if greeting.strip().lower() == "hello":
    print("$0")
elif greeting.strip().lower().startswith("how"):
    print("$20")
elif greeting.strip().lower().startswith("what's"):
    print("$100")
elif greeting.strip().lower().startswith("how"):
    print("$20")
elif greeting.strip().lower().startswith("hey"):
    print("$20")
else:
    print("$0")
