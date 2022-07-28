def most_used_alphabet(word):
    alphabet_list = [0] * 26
    lower_word = word.lower()

    for alphabet in lower_word:
        alphabet = ord(alphabet) - ord('a')
        alphabet_list[alphabet] += 1

    max_alphabet_value = alphabet_list[0]
    max_alphabet_index = 0

    for i in range(len(alphabet_list)):
        if max_alphabet_value < alphabet_list[i]:
            max_alphabet_value = alphabet_list[i]
            max_alphabet_index = i

    count = 0
    for i in alphabet_list:
        if max_alphabet_value == i:
            count += 1

    if count > 1:
        return print('?')
    else:
        max_alphabet = chr(max_alphabet_index + ord('a'))
        return print(max_alphabet.upper())


word = input()
most_used_alphabet(word)


# 알파벳 대소문자 변경 : string.lower() 와 string.upper()
# ASCII 값으로 문자에서 숫자로 : ord(), 숫자에서 문자로 : chr()
# 최고값을 저장하는 변수와 인덱스 값을 저장하는 변수