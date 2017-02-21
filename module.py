"""
Ce module devra par la suite etre importer dans le FReveil 
Module créé le : 2017_2_21
Nom initial du module : citation

"""
from config import *
import random
from synthese import *
from outils import *

def start(arguments):
	# Cette fonction sera la fonction qui sera lancée par le module. argument est une liste contenant les arguments passés au lancement du module
	s = Synthese()
	nb = -1
	if len(arguments) > 1:
		try : 
			nb = int(arguments[1])
		except:
			print("L'argument donné n'est pas un chiffre")


	chaine = citation(arguments[0][0],nb)
	if (citation != "-1"):
		s.synthese(chaine)
	else:
		print("Fichier citations.f pas trouvé")






def citation(endroit,nb = -1):
    #Initialisation des variables
    auteur = []
    citation = []
    continuer = 1
    i = 0

    #print("endroit : "+endroit+"citations.f")
    #Ouvrir le fichier
    try:
        chaine_fichier = Outils.lireFichier(endroit+"citations.f")
    except:
        return("-1")
        

    #Boucle de traitement du fichier des citations
    while continuer:
        #Trouver la citation
        fin_citation = chaine_fichier.find("\n")
        citation.append(chaine_fichier[:fin_citation])
        chaine_fichier = chaine_fichier[fin_citation+1:]
        #Trouver l'auteur
        fin_auteur = chaine_fichier.find("\n")
        auteur.append(chaine_fichier[:fin_auteur])
        chaine_fichier = chaine_fichier[fin_auteur+3:] #Le +3 c'est pour prendre en compte les sauts de ligne
        if citation[i] == "Fin" or auteur[i] == "Fin":
            continuer = 0

        i = i+ 1
    chaine_finale = "Citation"
    if nb >= 0 and nb < len(citation):
    	f = nb
    	chaine_finale =   " La citation a pour auteur  : "+ auteur[f]+ ". Voici la citation : " +citation[f]
    else :
    	nb = -1 # Si le nombre ne correspond pas à une citation alors on demande une citation aléatoire


    if nb == -1:
    	f =  random.randint(0,i-1) # Le -1 c'est pour enlever la fausse citation "Fin" qui a pour auteur "Fin"
    	chaine_finale =   " La citation aleatoire a pour auteur  : "+ auteur[f]+ ". Voici la citation : " +citation[f]
    return chaine_finale