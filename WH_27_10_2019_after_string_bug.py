# ZADANIE DOMOWE: wisielec.
# informacja do odgadnięcia słowo, wpisujemy listerkę, jeżeli literka jest w danym słowie, to wpisujemy
# jeżeli nie to zmniejszamy szanse
# jeżeli nie trafi, to przegrał
# słowo ma być wylosowane z listy słów - tupli. Słowo ma się pokazać pod postacią kreseczek, a jak zostanie odgadnięta, to
# kreseczka ma zamienić się na literkę


# 1)wprowadź użytkownika do gry
# )wybierz listę słów <- BUG: a może by tak pobrać jakiś słownik?
# 2) wylosuj słowo
# 3) wyświetl planszę <-- BUG: Słowo dwuczłonowe nie wyświetla się spacja między słowami-> do rozwiązania
# 4) pobierz literkę od użytkownika
# 5) sprawdż czy literka znajduje się w słowie
# 5a) jeżeli tak to zamień pola na literki
# wydrukuj planszę
# podaj informację
# spytaj o kolejną literkę <--BUG : Powtórzona literka liczy się jako próba
# wróć do punktu 4
# wyświetl rundę
# 5b) jeżeli nie, wyświetl informację
# wróć do punktu 4
# wyświetl rundę
# 6)sprawdź ktróa to runda

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

