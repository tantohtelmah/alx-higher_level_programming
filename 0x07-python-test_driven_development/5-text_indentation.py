def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        print(char, end="")
        if char in [".", "?", ":"]:
            print("\n" * 2, end="")
