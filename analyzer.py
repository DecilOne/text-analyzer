def split_text(text):
    words = text.split()
    return words


user_input = input("اكتب نصاً: ")
result = split_text(user_input)
print(result)