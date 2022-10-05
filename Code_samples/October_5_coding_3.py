# third in-class coding file from October 5

#  First the function definition
def reverse_word (word):
# now the code. DON’T FORGET TO INDENT!!
    i = 0
    print(id(word))
    reversed_word = ""
    while i < len(word):
        reversed_word = reversed_word + word[-(i+1)]
        i += 1
    return reversed_word


if __name__ == "__main__":
#    word = "elephant"
#    r = reverse_word(word)
    animals = ["cat", "Australian cattle dog", "duckbilled platypus", "ocelot", "zebra"]
    for critter in animals:
        print(id(critter))
        r_word = reverse_word(critter)
        print(" The word ", critter, " reversed is ", r_word)

