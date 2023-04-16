from typing import List
from time import sleep


def decimal_to_33(num: int) -> List[int]:
    """
    Перевод из десятичной системы счисления в 33-ричную со значащими нулями.
    """
    if num == 0:
        return [1]
    res = []
    n = num
    while n > 0:
        if num % 33 == 0:
            res.append(0)
            n //= 33
            num -= 1
        elif n % 33 == 0:
            res.append(33)
            n = (n - 1) // 33
        else:
            res.append(n % 33)
            n //= 33
    res[0] += 1
    return res[::-1]


def decimal_to_base(num: int, base: int) -> List[int]:
    if num == 0:
        return [1]
    res = []
    n = num
    while n > 0:
        if num % base == 0:
            res.append(0)
            n //= base
            num -= 1
        elif n % base == 0:
            res.append(base)
            n = (n - 1) // base
        else:
            res.append(n % base)
            n //= base
    res[0] += 1
    return res[::-1]


def convert_nums_to_letters(
    nums: List[int], alphabet: str
) -> str:
    """
    Перевод списка чисел nums в строку из символов,
      кодируемых соответствующим индексом алфавита alphabet.
    """
    alphabet_len = len(alphabet)
    res = ""
    for num in nums:
        res += alphabet[(num - 1) % alphabet_len]
    return res


def get_word_number(
    word: str, alphabet: str
) -> int:
    """
    Получить порядковый номер слова word в алфавите alphabet.
    """
    letter_ord = dict()
    for index, letter in enumerate(alphabet):
        letter_ord[letter] = index + 1

    ans = 0
    base = len(alphabet)
    word_len = len(word)
    for index, letter in enumerate(word):
        ans += letter_ord[letter] * (base ** (word_len - index - 1))
    return ans


def get_word_by_number(
    num: int, alphabet: str
) -> str:
    """
    Получить слово под номером num в алфавите alphabet.
    """
    num_array = decimal_to_base(num, len(alphabet))
    return convert_nums_to_letters(num_array, alphabet)


def get_words_numbers_in_sentence(sentence: str, alphabet: str) -> List[int]:
    """
    Возвращает последовательность номеров слов в предложении.
    Предложение должно быть грамотно составлено (пробелы после знаков преп.)
    """
    sentence = "".join(x for x in sentence if x in alphabet + " ")
    sentence = sentence.split()
    ans = []
    for word in sentence:
        ans.append(get_word_number(word, alphabet))
    return ans


def infinite_generation(alphabet: str):
    i = 0
    while True:
        num_array = decimal_to_base(i, len(alphabet))
        word = convert_nums_to_letters(num_array, alphabet)
        print(i + 1, word, get_word_number(word, alphabet))
        i += 1
        sleep(0.01)


def main():
    print("1 - rus; 2 - eng")
    a = input()
    if a == "1":
        alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        print("rus")
    elif a == "2":
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        print("eng")
    else:
        alphabet = "12345"
        print("nums")

    print("1 - infgen; 2 - getwordnum; 3 - getwordbynum; 4 - sentence_to_nums")
    option = input()
    if option == "1":
        infinite_generation(alphabet)
    if option == "2":
        print(get_word_number(input(), alphabet))
    if option == "3":
        print(get_word_by_number(int(input()) - 1, alphabet))
    if option == "4":
        print(*get_words_numbers_in_sentence(input(), alphabet))


if __name__ == "__main__":
    main()
