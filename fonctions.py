#coding:utf-8

import time
from random import choice
from donnees import *


def myprint(word):
    time.sleep(1)
    print(word)



def get_user_name():
    name = input("Bonjour et bienvenue, quel est votre nom ?: ")
    return name

def get_user_letter():
    letter = input("Veuillez choisir une lettre : ")
    print("Verification de la lettre")
    try:
        letter = int(letter)
        myprint("Attention, vous devez entrer une lettre")
        get_user_letter()
    except:
        letter = letter.lower()
        if len(letter) > 1:
            myprint("Une seule lettre merci..")
            get_user_letter()
        return letter

def get_random_word():
    with open("donnees.py", "r") as fichier:
        word = choice(liste_mots)
    return word

def display_secret_word(word, good_word):
    secret_word = ""
    for letter in word:
        if letter in good_word:
            secret_word += letter
        else:
            secret_word += "*"
    return secret_word

