import random
import string


def get_user_input():
    input_List = []
    digits = input("Do you want digits? Y/N?: ")
    if digits.lower() == "y":
        input_List.append(True)
    elif digits.lower() == "n":
        input_List.append(False)
    else:
        raise Exception("Invalid input, try again with Y OR N")

    sym = input("Do you want symbols? Y/N?: ")
    if sym.lower() == "y":
        input_List.append(True)
    elif sym.lower() == "n":
        input_List.append(False)
    else:
        raise Exception("Invalid input, try again with Y OR N")

    max_len = int(input("Maximum length: "))
    if max_len > 0:
        input_List.append(max_len)
    else:
        raise Exception("Invalid input, maximum length must be a positive integer")

    return tuple(input_List)


def gen_pass(include_digits, include_symbols, max_len=8):
    raw = []
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits  # Combine digits with the character set
    if include_symbols:
        characters += string.punctuation  # Combine symbols with the character set

    for _ in range(max_len):
        raw.append(random.choice(characters))  # Randomly pick characters for the password

    random.shuffle(raw)  # Shuffle to ensure randomness
    password = raw[:max_len]  # Trim to the specified maximum length
    return "".join(password)


# Main program execution
if __name__ == "__main__":
    include_digits, include_symbols, max_len = get_user_input()  # Unpack the tuple
    password = gen_pass(include_digits, include_symbols, max_len)
    with open("cache_pass.txt", "a") as f:     # creates the  cache file of previous generated passwords
        f.write(password + "\n")
    print("Generated Password:", password)


