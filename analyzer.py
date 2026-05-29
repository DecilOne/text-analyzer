import string

def split_text(text):
    words = text.split()
    cleaned = []
    for word in words:
        word = word.strip(string.punctuation)
        cleaned.append(word)
    return cleaned

def count_words(words):
    counts = {}
    for word in words:
        if len(word) <= 3:
            continue
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def sort_words(counts):
    sorted_words = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_words

user_input = input("اكتب نصاً: ").strip().lower()
result = split_text(user_input)
counts = count_words(result)
sorted_result = sort_words(counts)
print(sorted_result)