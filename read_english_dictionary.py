def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


if __name__ == '__main__':
    cie_count = 0
    cei_count = 0
    english_words = load_words()
    # demo print
    for word in english_words:
        if('cie' in word):
            cie_count+=1
            print('\t',word)
        elif('cei' in word):
            cei_count+=1
            print(word)
    print('cie ->', cie_count, '\ncei ->', cei_count)