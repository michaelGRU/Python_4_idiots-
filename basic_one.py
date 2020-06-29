#a simple guessing game.
key = "chair"
guess = ""
enter = ""
guess_count = 0
max_count = 5
out_of_guess = False
print("ou sit on it, but you can't take it with you. What is it?")
while key != guess and key != enter and not (out_of_guess):
    if guess_count == 0:
        enter = input("Enter guess: ")
        guess_count += 1
    elif guess_count!= 0 and guess_count < max_count:
         guess = input("Wrong answer. You have " + str(max_count-guess_count) + " times left. Try again:")
         guess_count += 1
    else:
        out_of_guess = True
if out_of_guessY:
    print("Better luck next time!")
else:
    print("Correct!")
