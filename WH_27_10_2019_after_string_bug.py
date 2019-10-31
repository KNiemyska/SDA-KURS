import time
import os
def dictionary():
    my_file = open("dictionary_climbing.txt", "r")
    data = my_file.readlines()
    words = []
    for line in data:
        stripped_line = line.strip()
        words.append(stripped_line)
    return words
    my_file.close()
def hangman_game():
    words=dictionary()
    from random import randint
    random_number = randint(1, len(words))  # drawing a number
    selected_word = (words[random_number - 1]).lower()  # choosing selected word
    board = ["_ "] * len(selected_word)  # creating boars
    print("".join(board))  # printing boars
    attempt = int(len(selected_word) + 2)
    chance = 0  # amount of chances
    round = 1  # amount of rounds
    selected_letter = []
    selected_word_list = []
    for char in selected_word:
        selected_word_list += [char]
    print(f"this is Your round number {round}, You have {attempt} chances left!!\n")
    round += 1
    while (chance) < (attempt):
        try_user = (input("enter the letter   ")).lower()
        if try_user in selected_letter:
            try_user = input(" HALO HALO, you have already entered this letter, choose another one\n")
        if try_user in selected_word:
            for elements in range(0, len(selected_word)):
                if selected_word[elements] == try_user:
                    board[elements] = try_user
            print("".join(board))
            if board == selected_word_list:
                print(f"CONGRATULATIONS!!!, YOU won! The guessed word is {selected_word}")
                time.sleep(2)
                break
        else:
            print(f"sorry, choose a different letter")
            chance += 1
        print(f"\n it is Your round number {round}, You have {attempt - chance} chances left!!\n")
        round += 1
        selected_letter.append(try_user)

    if attempt == chance:
        print(f"Unfortunately bye bye! you have already take all {chance}chances - you LOST \n the word you were looking for was {selected_word}")
        time.sleep(2)

    next_try = input("chcesz jeszcze raz zagrać? [t/n]")
    if next_try == "t":
        os.system("cls")
        print("BACK IN THE GAME!\n")
        hangman_game()
    else:
        print("It's a pity. See you next time!")
        time.sleep(3)
print(
    "Hello, you are going to play in a hangman\n the machine has drawn a password for you \n below you will see the board.")
input("Are You ready? To continue click enter")
hangman_game()

