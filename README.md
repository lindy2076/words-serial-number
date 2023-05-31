# words-serial-number
This is a python package for having ***fun*** with words ordered by **length and** then **lexicographically**.

(eg: `a, b, c, d, e, ..., x, y, z, aa, ab, ac, ..., ax, ay, az, ba, bc, bd` and so on...)

## lore

Each word has it's serial number. For example, if we use standart english alphabet `"abcdefghijklmnopqrstuvwxyz"` and we want to find the **8514**th word in this alphabet - we can just call the `get_word_by_number` method and get the answer - it's **lol**.

We can do the same thing in other direction. If we want to find the serial number of the word `jesus`, we can call the `get_word_number` and recieve the number: it's **4671049**.

There are also **other** helpful methods:
- `get_words_numbers_in_sentence` - as it says, we recieve a list of words' serial numbers from a sentence (string). (`"lol lmao"` -> `[8514, 219741]`)
- `nums_to_words` - same, but in other direction (`[235476151, 18091001]` -> `["sugoma", "amogus"]`)  
- `words_range` - same as python range, but with words. (`1000, 1500, 100` -> `generator("all", "aph", "atd", "awz", "bav")`)
- `infinite_generation` - it just prints all the words starting with the first word in an infinite loop.

## installation
`pip install wordlexord`

## quick start
```python
from word_lexord import (
    lang, get_word_by_number,
    get_word_number,
    get_words_numbers_in_sentence
)

eng_lower = lang.ALPHABETS["EN"]["lower"]

jesus_number = get_word_number("jesus", eng_lower)
print(f"Serial number of the word \"jesus\" is {jesus_number}")
# Serial number of the word "jesus" is 4671049

some_word = get_word_by_number(18091001, eng_lower)
print(f"The word by number {18091001} is {some_word}")
# The word by number 18091001 is amogus

sentence = "hi there! i am using telegram"
print(get_words_numbers_in_sentence(sentence, eng_lower))
# [217, 9283981, 9, 39, 9936895, 162325779031]
```

## docs

### alphabets

Since order can be determined on an alphabet, we will need the alphabet. An alphabet is a string, where each symbol is a letter of the alphabet. There are few alphabets available in the package, they are located in **lang** module. 
```python
from word_lexord import lang

eng_lower = lang.ALPHABETS["EN"]["lower"]
print(eng_lower)  # "abcdefghijklmnopqrstuvwxyz"
```

Or you can just use a string with random symbols:
```python
abc = "12345qwertyuiop" 
```

We will use some alphabets further: english lower and russian lower.

### methods

- `get_word_number(word, alphabet: str) -> int` - get the *word*'s number in *alphabet*.
    
    e.g: `get_word_number("sus", eng_lower)` is `13409`. 

- `get_word_by_number(num: int, alphabet: str) -> str` - get the word by the *num* in *alphabet*.

    e.g: `get_word_by_number(235476151, eng_lower)` is `"sugoma"`.

- `get_words_numbers_in_sentence(sentence: str, alphabet: str) -> List[int]` - get each word's number in *sentence*. Words are separated with the space symbol. Each symbol that is not present in 'alphabet' is replaced with the space symbol.

    e.g: `get_words_numbers_in_sentence("i love bioinformatics!", eng_lower)` is `[9, 221629, 5877569419735112053]`. As you can see, the exclamation mark is didn't affect the result.

- `nums_to_words(nums: List[int], alphabet: str) -> List[str]` - convert each num in *nums* into word by `get_word_number`.

    e.g: `nums_to_words([9, 221629, 5877569419735112053], eng_lower)` is `['i', 'love', 'bioinformatics']`.

- `words_range(alphabet: str, *args: List[int]) -> str` - recieve a word generator. *args* works like range() function. It takes from 1 to 3 arguments.

    e.g: 
    ```python
    for word in words_range(eng_lower, 1, 100, 20):
        print(word, eng=" ")
    # a u ao bi cc 
    ```


- `decimal_to_base(num, base: int) -> list[int]` - convert *num* from decimal to *base* number system without zeros.

    e.g: `decimal_to_base(1234, 2)` is `[1, 1, 2, 2, 1, 2, 1, 2, 1, 1]
`.

- `convert_nums_to_letters(nums: List[int], alphabet: str) -> str` - replaces *nums* with list of chars and concatenates them.

    e.g: `convert_nums_to_letters([1, 2, 3], eng_lower)` is `"abc"`.


## todo
- docs
- readme rus
- poetry
