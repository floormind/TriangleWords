from Letters import Alphabets


def main(user_input):
    alphabet_instance = Alphabets()
    result = alphabet_instance.compute_word(user_input)
    print(result)


if __name__ == "__main__":
    user_input = input("Enter word:")
    trimmed_input = user_input.strip()
    main(trimmed_input)
