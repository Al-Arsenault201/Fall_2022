# a cleaned up version of the wordle game
answer = input("Enter today's word - must be 5 letters")
for i in range(6): # you get 6 guesses
    guess = input("enter guess number: "+str(i+1))
    status= []
    for j in range(len(guess)):
        if not guess[j] in answer:
            status.append("b")
        elif guess[j] == answer[j]:
            status.append("g")
        else:
            status.append("y")
    print(status)
