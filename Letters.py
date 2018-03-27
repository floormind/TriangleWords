class Alphabets:
    alpha_numeric = {"a": 1,
                     "b": 2,
                     "c": 3,
                     "d": 4,
                     "e": 5,
                     "f": 6,
                     "g": 7,
                     "h": 8,
                     "i": 9,
                     "j": 10,
                     "k": 11,
                     "l": 12,
                     "m": 13,
                     "n": 14,
                     "o": 15,
                     "p": 16,
                     "q": 17,
                     "r": 18,
                     "s": 19,
                     "t": 20,
                     "u": 21,
                     "v": 22,
                     "w": 23,
                     "x": 24,
                     "y": 25,
                     "z": 26
                     }

    def compute_word(self, word):
        word_numeric_value = 0
        small_word = word.lower()
        letters_in_word = list(small_word)
        for letter in letters_in_word:
            is_valid = self.is_valid_letter(letter)
            if is_valid:
                word_numeric_value += self.get_numeric_value(letter)
            else:
                return False
        return self.is_triangle(word_numeric_value)

    @staticmethod
    def is_valid_letter(letter):
        is_valid = letter.isalpha()
        return is_valid

    def get_numeric_value(self, letter):
        return self.alpha_numeric[letter]

    @staticmethod
    def is_triangle(number):
        current_sum = 0
        is_triangle_number = False
        for n in range(0, number):
            current_sum += n
            if current_sum == number:
                is_triangle_number = True
                break
            else:
                continue
        return is_triangle_number
