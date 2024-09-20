# Bogushev V.V.

# Обычное решение
def single_root_words_classic(root_word, *other_words):
    same_words = []
    low_root_word = root_word.lower()
    for x in other_words:
        low_x = x.lower()
        if low_root_word in low_x or low_x in low_root_word:
            same_words.append(x)
    return same_words


# Решение с использованием генераторов списков
def single_root_words(root_word, *other_words):
    low_root_word = root_word.lower()
    return [x for x in other_words if low_root_word in x.lower() or x.lower() in low_root_word]

result1 = single_root_words_classic('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words_classic('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
