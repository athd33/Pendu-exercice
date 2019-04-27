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
checked_letter = []
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
		letter = letter.lower()
		print("Vous avez choisi = ", letter)
		try:
			letter = int(letter)
			print("Attention, pour jouer au pendu il faut utiliser des 'lettres'")
			get_user_letter()
		except:
			if len(letter) > 1:
				print("Une seule lettre, merci.")
				get_user_letter()
			check_letter(content, letter)

def check_letter(word, user_letter):
	global points
	global checked_letter
	for letter in word:
		if user_letter == letter not in checked_letter:
			checked_letter += letter
	print("points = ", points)
	display_secret_word(content, checked_letter)


def display_secret_word(word, checked_letter):
	secret_word = ""
	for letter in content:
		if letter in checked_letter:
			secret_word += letter
		else:
			secret_word += "*"
	print(secret_word)