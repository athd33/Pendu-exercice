#encoding:utf-8

from donnees import *
from fonctions import *
from math import *
import time




# PROGRAMME PRINCIPAL

def start_game():	
	print("Bonjour, bienvenu au jeu du pendu")
	get_random_word()
	get_user_name()
	get_user_letter()

start_game()