from base import (
    get_word_by_number,
    get_word_number,
    get_words_numbers_in_sentence,
    infinite_generation,
    nums_to_words
)
from lang import ALPHABETS


def main():
    # FIXME
    print("1 - rus; 2 - eng; 3 - custom")
    a = input()
    if a == "1":
        alphabet = ALPHABETS["RU"]["lower"]
        print("rus")
    elif a == "2":
        alphabet = ALPHABETS["EN"]["lower"]
        print("eng")
    elif a == "3":
        print("enter your alphabet without spaces")
        alphabet = input()
        print("your alphabet: ", alphabet)
    else:
        alphabet = "12345"
        print("nums")

    print("1 - infgen; 2 - getwordnum; 3 - getwordbynum; " +
          "4 - sentence_to_nums; 5 - nums_to_sentence")
    option = input()
    if option == "1":
        infinite_generation(alphabet)
    if option == "2":
        print(get_word_number(input(), alphabet))
    if option == "3":
        print(get_word_by_number(int(input()), alphabet))
    if option == "4":
        print(*get_words_numbers_in_sentence(input(), alphabet))
    if option == "5":
        print(*nums_to_words(map(int, input().split()), alphabet))


if __name__ == "__main__":
    main()
