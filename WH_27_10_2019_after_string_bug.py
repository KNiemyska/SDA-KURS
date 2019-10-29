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

def wisielec_game():
    my_file = open("dictionary_climbing.txt", "r")
    data = my_file.readlines()
    words = []
    import time
    import os
    for line in data:
        stripped_line = line.strip()
        words.append(stripped_line)
    from random import randint
    random_number = randint(1, len(words))  # losowanie liczby
    selected_word = (words[random_number - 1]).lower()  # wybranie losowego słowa
    plansza = ["_ "] * len(selected_word)  # wyświetlenie planszy
    print("".join(plansza))  # wydrukowanie planszy
    attempt = int(len(selected_word) + 2)
    szansa = 0  # liczba prób
    runda = 1  # liczba rund
    selected_letter = []
    selected_word_list = []
    for char in selected_word:
        selected_word_list += [char]
    print(f"to Twoja próba nr {runda}, pozostało Ci {attempt} szans!!\n")
    runda += 1
    while (szansa) < (attempt):
        try_user = (input("\n podaj literę    ")).lower()
        if try_user in selected_letter:
            try_user = input(" HALO HALO, tą literkę już podawałeś, wybierz inną \n")
        if try_user in selected_word:
            for elements in range(0, len(selected_word)):
                if selected_word[elements] == try_user:
                    plansza[elements] = try_user
            print("".join(plansza))
            if plansza == selected_word_list:
                print(f"brawo, WYGRAŁEŚ odgadnięte hasło to {selected_word}")
                time.sleep(2)
                break
        else:
            print(f"niestety skucha, wybierz inną literkę")
            szansa += 1
        print(f"\n to Twoja próba nr {runda}, pozostało Ci {attempt - (szansa)} szans!!\n")
        runda += 1
        selected_letter.append(try_user)

    if attempt == szansa:
        print(f"niestety PAPA! już wykorzystałeś {szansa} szans - PRZEGRAŁEŚ\n szukanym słowem było {selected_word}")
        time.sleep(2)
    my_file.close()


import os
import time

print(
    "Witaj, zaraz zagrasz w wiśielca""\n maszyna wylosowała dla Ciebie hasło\n poniżej zobaczysz planszę. \n")  # przywitanie użytkownika
# time.sleep(3)  # BUG: chcę żeby użytkownik nacisnął enter i dopiero dalej przeszedł, nie używać funkcji time
os.system("pause")
os.system("cls")
wisielec_game()
next_try = input("chcesz jeszcze raz zagrać? [t/n]")
if next_try == "t":
    os.system("cls")
    print("\nWITAJ PONOWNIE W GRZE!\n")
    wisielec_game()
else:
    print("Szkoda, do zobaczenia!")
    time.sleep(3)

# dodać czy chcesz zagrać jeszcze raz
# czysczenie panelu
