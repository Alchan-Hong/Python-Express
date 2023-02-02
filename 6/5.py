
def match_word(words):
    result = 0

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            result = result + 1
    return result

str = ['aba', 'xyz', 'abc', '121']
print(str)
print(f"문자열의 개수 = {match_word(str)}")

