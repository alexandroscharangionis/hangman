from random import choice

word_list = ["aardvark", "baboon", "camel"]
chosen_word = choice(word_list)
display = ["_" for char in chosen_word]


while "_" in display:
    guess = input("Choose a letter: ").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(display)
    if not "_" in display:
        solution = ''.join([char for char in display])
        print("You won") if solution == chosen_word else print("You lost")
