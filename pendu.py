#coding:utf-8



from fonctions import *

game = True
good_letter = []
tentatives = 8
word = ""

print("Recherche de mot en cours...")
random_word = get_random_word()
print(f"Random word : {random_word}")

user_name = get_user_name()
print(f"Bienvenu {user_name}, nous allons commencer...")

while game:

    user_letter = get_user_letter()
    myprint(f"print de user_letter : {user_letter}")

    for letter in random_word:
        if letter == user_letter:
            print("Bravo")
            good_letter += user_letter

    word = display_secret_word(random_word, good_letter)
    print(word)

