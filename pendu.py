#coding:utf-8

from fonctions import *

game = True
good_letter = []
tentatives = 8
word = ""
compte  = 1


print("Recherche de mot en cours...")
random_word = get_random_word()
print(f"Random word : {random_word}")


score = init_score()

user_name = get_user_name()
print(f"Bienvenu {user_name}, nous allons commencer...")
print(f"Affichage de score {score}")
if user_name in score:
    print("Encore vous?")


while game:
    user_letter = get_user_letter()
    tentatives -= 1

    if tentatives < 1:
        print("Fin de partie, vous avez perdu!!!")
        exit()

    print(f"Tentatives : {tentatives}")
    myprint(f"print de user_letter : {user_letter}")

    for letter in random_word:
        if letter == user_letter:
            print("Bravo")
            print(f"Compte : {compte}")
            compte += 1
            tentatives += 1
            good_letter += user_letter

    if compte == len(word) +1:
        print(f"BRAVO!!! , vous avez marqué {compte} points!")
        score[user_name] = compte
        print(f"print de score {score}")
        save_score(score)
        print(f"Fin de partie, merci d'avoir joué {user_name}")
        exit()


    print(f"Tentatives restantes {tentatives}")
    word = display_secret_word(random_word, good_letter)
    print(word)






