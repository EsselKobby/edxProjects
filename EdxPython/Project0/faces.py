def convert(text):
    # Conversion of an emoticon to an emoji
    # Convert :) to 🙂
    text = text.replace(":)", "🙂")
    # Convert :( to 🙁
    text = text.replace(":(", "🙁")
    return text


def main():
    user_input = input("Enter Your Message: ")
    converted_text = convert(user_input)
    print("Converted text:")
    print(converted_text)


main()
