# in class coding Monday November 7
# is a phrase a palindrome

def is_palindrome(phrase):
    # base cases:
    if phrase == "":
        return True
    elif len(phrase) == 1:
        return True
    elif phrase[0] != phrase[-1]:
        return False

    #recursive case
    else:
        return is_palindrome(phrase[1:-1])

if __name__ == "__main__":
    phrase = input("What is the phrase to check")
    answer = is_palindrome(phrase)
    if answer:
        print(phrase, " is a palindrome")
    else:
        print(phrase, "is not a palindrome")