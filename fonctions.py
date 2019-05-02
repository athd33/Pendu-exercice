#coding:utf-8

import time
from donnees import *
from random import choice
import pickle

def myprint(word):          #creation d'une fonction print() incluant un time.sleep
    time.sleep(1)
    print(word)


def get_user_name():
    name = input("Bonjour et bienvenue, quel est votre nom ?: ")
    return name

def get_user_letter():
    letter = input("Veuillez choisir une lettre : ")
    myprint("Verification de la lettre")
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


def init_score():
    print("Initialisation du score en cours")
    try:
        with open("data", "rb") as fichier:
            record = pickle.Unpickler(fichier)
            score = record.load()
    except:
        score = {}
        print("Aucun fichier data trouvé")
        print("Data vient d'être créé")
    return score

def save_score(scores):
    print("Enregistrement en cours")
    with open("data", "wb") as fichier:
        record = pickle.Pickler(fichier)
        record.dump(scores)








