from random import choice

word_list = ["aardvark", "baboon", "camel"]
chosen_word = choice(word_list)
display = ["_" for char in chosen_word]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6

while "_" in display:
    guess = input("Choose a letter: ").lower()
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(display)
        if lives == 0:
            print("GAME OVER")
            break
        continue
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(stages[lives])
    print(display)
    if not "_" in display:
        print("YOU WON")
