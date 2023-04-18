# words-serial-number
This is a python package for having ***fun*** with words ordered by **length and** then **lexicographically**.

(eg: `a, b, c, d, e, ..., x, y, z, aa, ab, ac, ..., ax, ay, az, ba, bc, bd` and so on...)

Each word has it's serial number. For example, if we use standart english alphabet `"abcdefghijklmnopqrstuvwxyz"` and we want to find the **8514**th word in this alphabet - we can just call the `get_word_by_number` method and get the answer - it's **lol**.

We can do the same thing in other direction. If we want to find the serial number of the word `jesus`, we can call the `get_word_number` and recieve the number: it's **4671049**.

There are also **other** helpful methods:
- `get_words_numbers_in_sentence` - as it says, we recieve a list of words' serial numbers from a sentence (string). (`"lol lmao"` -> `[8514, 219741]`)
- `nums_to_words` - same, but in other direction (`[235476151, 18091001]` -> `["sugoma", "amogus"]`)  
- `words_range` - same as python range, but with words. (`1000, 1500, 100` -> `generator("all", "aph", "atd", "awz", "bav")`)
- `infinite_generation` - it just prints all the words starting with the first word in an infinite loop.


## todo
- readme rus
- poetry
- pypi push
