from typing import List
from time import sleep


def decimal_to_33(num: int) -> List[int]:
    """
    (unsued base)
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
    """
    Перевод числа num из десятичной системы счисления в систему
      по основанию base без нулей
      (== со значащими нулями, где цифры увеличены на 1)
    """
    if base == 1:
        return [0] * (num + 1)

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
    if not word.replace(" ", ""):
        return 0

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
    if num < 1:
        return " "
    num -= 1
    num_array = decimal_to_base(num, len(alphabet))
    return convert_nums_to_letters(num_array, alphabet)


def get_words_numbers_in_sentence(sentence: str, alphabet: str) -> List[int]:
    """
    Получить последовательность номеров слов в предложении.
    Предложение должно быть либо без знаков препинания, либо без
      символов, которых нет в алфавите.
    """
    sentence = "".join(x for x in sentence if x in alphabet + " ")
    sentence = sentence.split()
    ans = []
    for word in sentence:
        ans.append(get_word_number(word, alphabet))
    return ans


def nums_to_words(nums: List[int], alphabet: str) -> List[str]:
    """
    Перевод порядковых номеров слов nums в последовательность
      слов алфавита alphabet
    """
    ans = [get_word_by_number(num, alphabet) for num in nums]
    return ans


def words_range(alphabet: str, *args: List[int]) -> str:
    """
    Получить генератор слов алфавита alphabet.
    Если передано одно число n в args, то будут выданы
      первые n слов (включая пустое).
    Если передано два числа n1, n2 в args, то будут выданы
      слова с n1 по n2 номер.
    Если передано три числа n1, n2, n3 в args, то будет выдано
      каждое n3-ее слово с n1 по n2 номер.
    Возвращает пустую строку, если передан только алфавит.
    """
    if len(args) == 0:
        yield ""
    for wnum in range(*args):
        yield get_word_by_number(wnum, alphabet)


def infinite_generation(alphabet: str):
    """
    Бесконечный вывод слов, упорядоченных сначала
      по длине, а затем лексикографически.
    """
    i = 0
    while True:
        num_array = decimal_to_base(i, len(alphabet))
        word = convert_nums_to_letters(num_array, alphabet)
        print(i + 1, word, get_word_number(word, alphabet))
        i += 1
        sleep(0.01)
