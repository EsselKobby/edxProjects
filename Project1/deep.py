user_query = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? "
)
# Handling of Case Sensitivity
user_query_lower = user_query.lower().replace(" ", "")

if (
    user_query_lower == "42"
    or user_query_lower == "fortytwo"
    or user_query_lower == "forty-two"
):
    print("Yes")
else:
    print("No")
