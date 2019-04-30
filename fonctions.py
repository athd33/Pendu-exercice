#encoding:utf-8

from math import * 
from donnees import *
from random import choice
import pickle
import time


################# VARIABLES ############################
game = True
content = ""
user_name = ""
letter = ""
checked_letter = []
points = 8
score = {}
secret_word = ""

################# FONCTIONS ############################


def get_random_word():										# fonctions qui ouvre le fichier donnees dans lequel se trouvent les mots
	global content
	time.sleep(1)
	print("Recherche de mot en cours...")
	time.sleep(2)
	print("Jeu prêt")
	time.sleep(2)
	print("Commençons!")
	with open("donnees.py", "r") as data:
		content = choice(liste_mots)					# choice retourn un element aléatoire d'une liste (liste_mots pour ce cas-ci)
	print("mot secret : ", content)			#controle de la récuperation du mot

def get_user_name():

	global user_name	
	time.sleep(1)
	user_name = input("Quel est votre nom ? ")
	print("Bienvenu {}".format(user_name))
	check_name()
	user_name = user_name.lower()
	try:
		user_name = int(user_name)
		print("Pardon??")
		get_user_name()
	except:
		pass


def check_name():
	if user_name in score:	
		time.sleep(1)			
		print("Content de vous revoir {}".format(user_name))	# verifier si la clé username est dans le dictionnaire score
	else:
		print("Vous êtes inconnu")



def get_user_letter():
	global game
	global points
	game = True
	global letter
	while points > 1:
		points -= 1
		print("Joueur actuel : {} , Tentatives restantes : {}".format(user_name, points))
		letter = input("Ok {}, choisissez une lettre : ".format(user_name))
		letter = letter.lower()										# lower pour respecter la casse de la liste de mots
		print("Vous avez choisi = ", letter)
		try:
			letter = int(letter)
			print("Attention, pour jouer au pendu il faut utiliser des 'lettres'")
			get_user_letter()
		except:
			if len(letter) > 1:
				print("Une seule lettre, merci.")
				get_user_letter()
			elif letter == "":
				print("J'ai besoin d'une lettre, merci")
				time.sleep(2)
				print("Et merci pour le point...")
				time.sleep(2)
			else:
				check_letter(content, letter)
	end_game()
	

def check_letter(word, user_letter):				# fonction pour verifier la presence de la lettre dans le mot
	global points
	global checked_letter							# checked letter est une liste
	for letter in word:								# parcour du mot lettre par lettre
		if user_letter == letter not in checked_letter:	# si la lettre de l'user n'est pas déjà présente dans la liste mais dans le mot on l'ajoute a la liste
			checked_letter += letter
			points += 1
	display_secret_word(content, checked_letter)


def display_secret_word(word, checked_letter):		# fonction d'affichage du mot
	secret_word = ""								# mot vide str()
	for letter in content:							# parcours du mot a trouver
		if letter in checked_letter:				# si une des lettres est bonne, on l'ajoute au mot sinon on met une *
			secret_word += letter
		else:
			secret_word += "*"
	print(secret_word)
	win_condition(secret_word)

def win_condition(secret_word):
	total_letters = len(secret_word)
	compte = 0
	for letter in secret_word:
		if letter == "*":
			pass
		else:
			compte += 1
	if compte == total_letters:
		print("Gagné!!!! Vous avez marqué {} points!".format(points))
		score[user_name] = points 					#ajout de username en clé et points en valeur dans le dico score										#
		print("dico score : " ,score)
		save_score(score)
		game = False



def end_game():
	if points <= 1:
		print("PERDU!!!")
		time.sleep(2)
		print("A bientot")




def init_score():
	global score
	time.sleep(2)
	print("Initiatlisation des scores")						 # affichage de contrôle pour vérifier que la fonction se lance
	try:
		with open("scores", "rb") as fichier:
			record = pickle.Unpickler(fichier)
			score = record.load()
	except:
		print("Aucune donnée présente")



def save_score(scores):
	print("Enregistrement du score en cours")				# affichage de contrôle pour vérifier que la fonction se lance
	with open("scores","wb") as fichier:
		record = pickle.Pickler(fichier)
		record.dump(score)
	print("Enregistrement terminé OK")						# affichage de contrôle pour vérifier le dump() est passé
	print("fin de jeu")
	exit()




