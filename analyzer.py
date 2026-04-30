def split_text(text):
    words = text.split()
    return words
def count_words(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

user_input = input("اكتب نصاً: ")
result = split_text(user_input)
counts = count_words(result)
print(counts)