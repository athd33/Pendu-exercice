#encoding:utf-8

from fonctions import *
from math import * 
from donnees import *
from random import choice
from pickle import *


################# VARIABLES ############################

content = ""
user_name = ""
letter = ""
points = 8
secret_word = ""

################# FONCTIONS ############################


def get_random_word():										# fonctions qui ouvre le fichier donnees dans lequel se trouvent les mots
	global content
	with open("donnees.py", "r") as data:
		content = choice(liste_mots)					# choice retourn un element aléatoire d'une liste (liste_mots pour ce cas-ci)
		print(content)


def get_user_name():

	global user_name
	user_name = input("Quel est votre nom ? ")
	try:
		user_name = int(user_name)
		print("Pardon??")
		get_user_name()
	except:
		pass

def get_user_letter():
	global game
	global points
	game = True
	global letter
	while points > 0:
		letter = input("Ok {}, choisissez une lettre : ".format(user_name))
		letter = letter.lower()								#lower pour respecter la casse de la liste de mots
		print("Lower = ", letter)
		try:
			letter = int(letter)
			print("Attention, pour jouer au pendu il faut utiliser des 'lettres'")
			get_user_letter()
		except:
			if len(letter) > 1:
				print("Une seule lettre, merci.")
				get_user_letter()
			display_secret(content, letter)
