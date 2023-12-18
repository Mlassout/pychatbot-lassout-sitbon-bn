"""
-CHATBOT PYTHON-
-CHATBOF-
Lassout Marc-Antoine
Sitbon Samuel
functions.py : fichier comportant toute les fonctions
"""

import os  # utilisé pour naviguer dans l'os
import random # importer une possibilité de faire une fonction aléatoire
import math #module maths utilisé pour le TF-IDF
import tkinter as tk
from tkinter import messagebox, scrolledtext ,PhotoImage,Canvas


def list_of_files(directory, extension):
    """
    Rôle: Liste tous les fichiers dans un répertoire donné avec une extension spécifique.
    Paramètres: 'directory' - Le chemin du répertoire à explorer. 'extension' - L'extension des fichiers à lister.
    Return: Liste des noms de fichiers avec l'extension spécifiée."""

    files_names = [] # création d'une liste pour stocker les noms

    for filename in os.listdir(directory): # récupère la liste des éléments dans le fichier donné en paramètre
        if filename.endswith(extension): # entre dans la contidition que si on trouve le type de fichier donné en paramètre
            files_names.append(filename) # ajout de chaque nom de fichier la liste créer au préalable
    return files_names # on retourne la fonction pour la renvoyer



#fonction qui permet d'associer le nom des présidents avec leur prenom
def associer_prenom_president(nom_president):
    """
    Rôle: Extrait uniquement les noms des titres à partir d'une liste de noms de fichiers.
    Paramètres: 'x' - Liste des noms de fichiers complets.
    Return: Liste contenant uniquement les noms extraits des titres des fichiers."""

    prenoms_presidents = {
        "Chirac ": " Jacques ",
        " Giscrad d Estaing ": " Valéry ",
        " Mitterrand ": " François ",
        " Macron ": " Emmanuel ",
        " Sarkozy ": " Nicolas "
    }

    return prenoms_presidents.get(nom_president, " Inconnu ")

def new_list(l):
    """
    Rôle: Crée une nouvelle liste en extrayant et en nettoyant des segments spécifiques de chaque fichier pour récupérer le nom des présidents.
    Paramètres: 'l' - Liste de chaînes de caractères où chaque élément est présumé avoir un format prédéfini avec des informations à extraire.
    Return: Liste des fichiers nettoyées."""

    liste = [] # création d'une nouvelle liste

    for i in range(len(l)): # parcour toute la liste donné en paramètre
        val = l[i][11:-4] # enlève le format du fichier et le "Nomination_"
        for j in range (len(val)): # parcour la chaine str des noms de fichier de cette liste
            if val[j] == '1' or val[j] == '2': # entre dans la condition s'il y a un 1 ou un 2 dans la chaine
                val = val[:-1] # enlève ces derniers à la dernière position
        liste.append(val) # ajoute ces nouveaux noms la liste créée au préalable

    return liste # renvoie la liste



def supp_doublons(l):
    """
    Rôle: Élimine les doublons d'une liste.
    Paramètres: 'l' - Liste potentiellement contenant des doublons.
    Return: Nouvelle liste ne contenant pas de doublons."""

    l = list(set(l)) # parcour la liste pour enlever les doublons

    return l # renvoie la liste


def minuscule(txt):
    """
    Rôle: Convertit tous les caractères majuscules d'une chaîne en minuscules.
    Paramètres: 'txt' - Chaîne de caractères à convertir.
    Return: Nouvelle chaîne de caractères en minuscule."""

    txt = list(txt) # met tous les caractères de la chaine dans une liste
    for i in range (len(txt)): # parcour toute la liste
        if ord(txt[i]) >= ord("A") and ord(txt[i]) <= ord("Z"): # entre dans la condition si un caractere est compris entre le code ascii de A et du Z
            txt[i] = chr(ord(txt[i]) + ord("a")-ord("A")) # change cette majuscule en minuscule

    return "".join(txt) # renvoie la liste en texte



def ponctuation_str(l) :
    """
    Rôle: Supprime tous les ponctuations d'une chaîne de caractères.
    Paramètres: 'l' - Chaîne de caractères à nettoyer.
    Return: Chaîne de caractères sans les signes de ponctuation."""

    list_ponctuation = ["!","+","#",".",",","?",";",":","(",")",":","=","`",'"'] # création d'une liste comprenant toute les ponctuations
    list_ponctuation_special = ["'","-"]# création d'une liste comprenant toute les ponctuations spéciales
    list = [] # création d'une liste pour manipuler la chaine str
    chaine = "" # création d'une chaine str

    for i in range (len(l)) : # parcour toute la chaine str entré en paramètre
        list.append(l[i]) # ajoute chaque caractère dans la liste créée au préalable
        if list[i] in list_ponctuation_special : # entre dans la condition si le caractère est dans la liste de ponctuations spéciales
            list[i] = " " # remplace le caractère par un espace
        if list[i] in list_ponctuation : # entre dans la condition si le caractère est dans la liste de ponctuations
            list[i] = "" # supprime le caractère
        chaine += list[i] # ajoute chaque caractère dans la chaine str créée au préalable
    return chaine # renvoie la chaine


def cleaned(liste_fichiers):
    """
    Rôle: Nettoie le contenu de plusieurs fichiers en supprimant la ponctuation et en convertissant le texte en minuscules, puis sauvegarde les résultats dans un nouveau répertoire.
    Paramètres: 'liste_fichiers' - Liste des noms de fichiers à nettoyer.
    Return: Aucun. Les fichiers nettoyés sont écrits dans un nouveau répertoire."""

    # Suppression du répertoire "cleaned" s'il existe
    if os.path.exists("./cleaned"):
        for fichier in os.listdir("./cleaned"):
            chemin_fichier = os.path.join("./cleaned", fichier)
            os.remove(chemin_fichier)
        os.rmdir("./cleaned")

    os.mkdir('./cleaned/')  # Création du répertoire "cleaned"

    for nom_fichier in liste_fichiers:
        chemin_entree = os.path.join('./speeches', nom_fichier)
        chemin_sortie = os.path.join('./cleaned', "cleaned_" + nom_fichier)

        with open(chemin_entree, "r", encoding="utf-8") as f:
            contenu = f.read()

        # Application des fonctions de nettoyage
        contenu_nettoye = ponctuation_str(minuscule(contenu))

        # Écriture du contenu nettoyé dans le nouveau fichier
        with open(chemin_sortie, 'w', encoding='utf-8') as p:
            p.write(contenu_nettoye)

def scan_ligne(chaine):
    """
    Rôle: Analyse une chaîne de caractères et compte la fréquence de chaque mot.
    Paramètres: 'chaine' - La chaîne de caractères à analyser.
    Return: Dictionnaire avec chaque mot comme clé et sa fréquence comme valeur."""


    dico={}   # on définit un dictionnaire vide
    mot=""   # on crée une variable mot où l'on stocke une chaine vide

    chaine+=" "
    for i in range (len(chaine)):  # on crée une boucle pour qui se répète jusqu'a la taille de la chaine
        if chaine[i]!=" ":   # si le caractère est vide on l'ajoute a la variable mot
            mot+=chaine[i]
        else:
            if mot=="d" or mot=="j" or mot=="s" or mot=="n":   # sinon pour les lettres d, j, s, n on ajoute un e après
                mot+="e"
            if mot=="c" :  # si c'est un c on ajoute un ela
                mot+="ela"
            if mot=="l": # si c'est un l on a une chance sur deux qu'il y est un a ou un e
                a_ou_e = random.randint(1,2)
                if a_ou_e == 1:
                    mot +="e"
                else:
                    mot +="a"
                if mot in dico :    # si le contenu de la variable mot est dans le dictionnaire on ajoute 1
                    dico[mot]+=1
                else:
                    dico[mot]=1
            else:
                if mot in dico :    # si le contenu de la variable mot est dans le dictionnaire on ajoute 1
                    dico[mot]+=1
                else:
                    dico[mot]=1

            mot=""

    return dico


def cpt_word(directory):
    """
    Rôle: Compte la fréquence de chaque mot dans tous les fichiers d'un répertoire.
    Paramètres: 'directory' - Le chemin du répertoire contenant les fichiers texte.
    Return: Dictionnaire avec chaque mot comme clé et sa fréquence globale comme valeur."""

    dictionnaire={}    # on crée un dictionnaire vide
    texte=""  # Initialise une chaîne de caractères vide qui sera utilisée pour stocker le contenu combiné de tous les fichiers

    list_name=list_of_files(directory,"txt")   #Appelle une fonction hypothétique list_of_files pour obtenir une liste de noms de fichiers se terminant par ".txt" dans le répertoire spécifié.
    for i in range (len(list_name)):   # parcourt chaque élément de la liste des noms de fichiers.
        loc_fichier="./"+str(directory)+"/"+list_name[i]
        with open (loc_fichier,"r") as f:  # Ouvre le fichier en mode lecture.
            ligne=f.readline()
            while ligne!="":     # lit chaque ligne du fichier et ajoute son contenu à la chaîne
                ligne=ligne.replace("\n","")   # supprime le caractère \n de chaque ligne par un vide
                texte+=ligne+" "   # ajoute chaque ligne a la variable texte
                ligne = f.readline()
        dictionnaire = scan_ligne(texte)    #Appelle une fonction hypothétique scan_ligne qui compte les occurrences de chaque mot dans la ligne et met à jour le dictionnaire.

    return dictionnaire



def score_idf_dico(directory):
    """
    Rôle: Calcule l'Inverse Document Frequency (IDF) pour chaque mot présent dans les fichiers d'un répertoire.
    Paramètres: 'directory' - Le chemin du répertoire contenant les fichiers texte.
    Return: Dictionnaire avec chaque mot comme clé et son score IDF comme valeur."""

    dico={}
    list_name = list_of_files(directory,"txt")     # Liste des noms des fichiers
    for i in range(len(list_name)):
        loc_fichier = "/" + list_name[i]
        with open(directory + loc_fichier, 'r') as f:      # Parcours tous les fichiers texte du répertoire
            contenue = f.read()   # Contenue de chaque fichier sous forme d'un dictionnaire de mot avec leur score TF (occurrence)
            contenue = contenue.replace("\n"," ")
            TF=scan_ligne(contenue)
        for mot in TF.keys():         # Parcours les clés du dictionnaire TF, soit tous les mots du texte
            if mot not in dico.keys():
                dico[mot] = 1       # Si le mot n'est pas dans le dictionnaire IDF, alors l'initialiser avec une valeur à 1
            else:
                dico[mot] += 1      # Si le mot est dans le dictionnaire IDF, alors ajouter 1 à sa valeur
    for mot, count in dico.items():

        dico[mot] = float(math.log((len(list_name) / count), 10))      # Formule du score IDF

    return dico

def matrice_tfidf(directory):
    """
    Rôle: Construit une matrice TF-IDF pour un ensemble de documents textuels dans un répertoire donné.
    Paramètres: 'directory' - Le chemin du répertoire contenant les fichiers texte.
    Return: Matrice TF-IDF, où chaque ligne représente un mot et chaque colonne représente un document."""

    dico_TFIDF = {}       # création de dictionnaires vides


    List=[]         # création de liste vide

    list_name = list_of_files(directory, "txt")
    list_name=sorted(list_name)
    List.append("mot")

    dico_IDF=score_idf_dico(directory)           # Calcul du score IDF pour chaque mot dans le répertoire
    all_word = cpt_word(directory)                  # Compte le nombre d'occurrences de chaque mot dans l'ensemble des documents

    if "" in all_word:                  # Supprime la clé vide s'il y en a une
        del all_word[""]

    matrice = []                # Initialisation d'une matrice pour stocker les valeurs TF-IDF
    nbr_ligne = int(len(list_name)) + 1     # Nombre de lignes dans la matrice (nombre de mots + 1 pour les titres)
    for l in range(len(all_word) + 1):      # Crée une matrice remplie de zéros
        ligne = [0] * nbr_ligne
        matrice.append(ligne)
    cpt = 1

    for word in all_word.keys():     # Remplissage de la première colonne de la matrice avec les mots
        matrice[cpt][0] = word
        cpt += 1
    for i in range(len(list_name)):             # Boucle sur les fichiers pour remplir la matrice avec les valeurs TF-IDF

        loc_fichier = "./" + str(directory) + "/" + list_name[i]    # Suit le Chemin du fichier
        with open(loc_fichier, "r") as f:
            ligneTF =f.read()
            ligneTF = ligneTF.replace("\n", "")
            dico_TF=scan_ligne(ligneTF)             # Calcul des valeurs TF-IDF pour chaque mot dans le fichier
            for mots in dico_TF.keys():
                if mots in dico_IDF:
                    dico_TFIDF[mots] = dico_IDF[mots]*dico_TF[mots]
            dico_TF.clear()

            matrice[0][i+1]=list_name[i]                # Remplissage de la première ligne de la matrice avec les noms de fichiers

            for h in range(len(matrice)):           # Remplissage de la matrice avec les valeurs TF-IDF

                for mot in dico_TFIDF.keys():
                    if mot == matrice[h][0]:

                        matrice[h][i+1]=dico_TFIDF[mot]
            dico_TFIDF.clear()


    return matrice

# -----

def saisie():
    """
    Rôle: Demande à l'utilisateur de saisir un nombre compris entre 0 et 5.
    Paramètres: Aucun.
    Return: Retourne le nombre saisi en tant qu'entier si la saisie est valide."""

    flag = True
    entree = ""
    while flag:
        entree = input("Entrer un nombre compris entre 0 et 5 : ")
        if len(entree) > 1:
            break
        elif ord(entree) > 47 and ord(entree) < 54: # l'entree est un nombre compris entre 0 et 5
            return int(entree)


def word_question(chaine):
    """
    Rôle: Analyse une chaîne de caractères et extrait les mots.
    Paramètres: 'chaine' - une chaîne de caractères représentant la question.
    Return: Liste des mots issus de la question."""

    list=[]   # on définit une liste vide
    mot=""   # on crée une variable mot où l'on stocke une chaine vide
    chaine+=" "
    for i in range (len(chaine)):  # on crée une boucle pour qui se répète jusqu'a la taille de la chaine
        if chaine[i]!=" ":   # si le caractère est vide on l'ajoute a la variable mot
            mot+=chaine[i]
        else:
            if mot=="d" or mot=="j" or mot=="s" or mot=="n":   # sinon pour les lettres d, j, s, n on ajoute un e après
                mot+="e"
            if mot=="c" :  # si c'est un c on ajoute un ela
                mot+="ela"
            if mot=="l": # si c'est un l on a une chance sur deux qu'il y est un a ou un e
                a_ou_e = random.randint(1,2)
                if a_ou_e == 1:
                    mot +="e"
                else:
                    mot +="a"
            if mot not in list:    # si le contenu de la variable mot est dans le dictionnaire on ajoute 1
                list.append(mot)
            mot=""

    return list


def mot_important(list,matrice):
    """
    Rôle: Identifie les mots importants de la question en les comparant à la matrice du corpus.
    Paramètres: 'list' - liste de mots à vérifier, 'matrice' - matrice de référence pour la comparaison.
    Return: Liste des mots considérés importants."""

    list_mot=[]
    for mot in list:
        for i in range (len(matrice)):
            for j in range (len(matrice[i])):
                if matrice[i][j]==mot:
                    list_mot.append(mot)

    return list_mot

def cpt_mot_question(dico):
    """
    Rôle: Calcule le nombre total d'occurrences des mots dans une question.
    Paramètres: 'dico' - dictionnaire des mots avec leur comptage.
    Return: Nombre total d'occurrences des mots."""

    cpt_total=0
    for nombre in dico.values():
        cpt_total+=nombre
    return cpt_total


def Matrice_filtre_matrice(dico,matrice,dico_idf):
    """
    Rôle: Filtre la matrice du corpus pour ne conserver que les mots présents dans la question.
    Paramètres: 'dico' - dictionnaire de mots à filtrer, 'matrice' - matrice de référence(question), 'dico_idf' - dictionnaire avec les scores IDF.
    Return: Matrice filtrée avec les mots et leur score TF-IDF."""

    Matrice=[]
    ligne_0 = [0, "Question"]
    Matrice.append(ligne_0)
    for mot in dico.keys():
        for i in range(len(matrice)):
            if matrice[i][0] == mot:
                L=[]
                TF_IDF=dico[mot]*dico_idf[mot]
                L.append(mot)
                L.append(TF_IDF)
                Matrice.append(L)

    return Matrice


#Calcul similarité deux vecteurs


def produit_scalaire(A,B,colonne_A,colonne_B):
    """
    Rôle: Calcule le produit scalaire de deux vecteurs.
    Paramètres: 'A' et 'B' - matrices représentant les vecteurs, 'colonne_A' et 'colonne_B' - indices des colonnes pour le calcul.
    Return: Résultat du produit scalaire."""

    somme=0
    for i in range (1,len(A)):
        somme+=A[i][colonne_A]*B[i][colonne_B]

    return somme


def norme_vecteur(A, colonne):
    """
    Rôle: Calcule la norme d'un vecteur.
    Paramètres: 'A' - matrice représentant le vecteur, 'colonne' - indice de la colonne pour le calcul.
    Return: Norme du vecteur."""

    somme = 0
    for i in range(1,len(A)):
        somme += A[i][colonne]**2
    somme = somme**0.5

    return somme

def calcul_similarite(A, B, colonne_A, colonne_B):
    """
    Rôle: Calcule la norme d'un vecteur.
    Paramètres: 'A' - matrice représentant le vecteur, 'colonne' - indice de la colonne pour le calcul.
    Return: Norme du vecteur."""

    produit_normes = norme_vecteur(A, colonne_A) * norme_vecteur(B, colonne_B)

    if produit_normes == 0:

        return 0  # Éviter la division par zéro
    return produit_scalaire(A, B, colonne_A, colonne_B) / produit_normes

def similarite(Matrice_question_M, Matrice_corpus_M):
    """
    Rôle: Calcule la similarité cosinus entre deux vecteurs.
    Paramètres: 'A' et 'B' - matrices des vecteurs, 'colonne_A' et 'colonne_B' - indices des colonnes des vecteurs à comparer.
    Return: Score de similarité cosinus entre les vecteurs."""

    dictionnaire_vecteur_similarite = {}
    for i in range(1, len(Matrice_corpus_M[0])):
        score_similarite = calcul_similarite(Matrice_question_M, Matrice_corpus_M, 1, i)
        dictionnaire_vecteur_similarite[Matrice_corpus_M[0][i]] = score_similarite  # Arrondi pour correspondre au format souhaité
    return dictionnaire_vecteur_similarite


def croisement_mot_question_corpus(Matrice_corpus,Matrice_question):
    """
    Rôle: Trouve l'intersection des mots entre la matrice d'une question et celle d'un corpus.
    Paramètres: 'Matrice_corpus' - matrice du corpus, 'Matrice_question' - matrice de la question.
    Return: Matrice contenant les mots communs."""

    Matrice_dimension_M=[]
    for h in range (len(Matrice_question)):
        for i in range(len(Matrice_corpus)):
            if Matrice_question[h][0] == Matrice_corpus[i][0]:
                Matrice_dimension_M.append(Matrice_corpus[i])

    return Matrice_dimension_M

def fichier_similarite(dico):
    """
    Rôle: Identifie le fichier le plus similaire basé sur le dictionnaire de similarité.
    Paramètres: 'dico' - dictionnaire contenant les scores de similarité des fichiers.
    Return: Nom du fichier le plus similaire."""

    valeur_la_plus_grande = max(dico.values())  # Trouver la plus grande valeur
    for fichier, valeur in dico.items():
        if valeur == valeur_la_plus_grande:
            return fichier  # Retourner le fichier correspondant

def fichier_clean_vers_speach(fichier):
    """
    Rôle: Convertit un nom de fichier 'cleaned' en son équivalent 'speech'.
    Paramètres: 'fichier' - nom du fichier à convertir.
    Return: Nom converti du fichier."""

    fichier=fichier[8:]
    return fichier

def le_mot_important_question(Matrice_question):
    """
    Rôle: Détermine le mot le plus important d'une question basé sur la matrice TF-IDF.
    Paramètres: 'Matrice_question' - matrice TF-IDF de la question.
    Return: Mot le plus impactant."""

    for i in range(1,len(Matrice_question)-1):
        if Matrice_question[i][1]>Matrice_question[i+1][1]:
            indice_i=i
        else:
            indice_i=i+1
    mot_impactant=Matrice_question[indice_i][0]
    return mot_impactant

def phrase_prompt(fichier_speech,mot):
    """
    Rôle: Recherche une phrase contenant le mot spécifique à chercher dans le fichier donné présent dans 'speech'.
    Paramètres: 'fichier_speech' - nom du fichier de discours, 'mot' - mot à rechercher dans le discours.
    Return: Phrase trouvée contenant le mot. Retourne None si aucune phrase n'est trouvée."""

    chaine_ponctuation=" -,?:;.'()"
    phrase_1=""
    phrase_x=""
    with open("./speeches/"+fichier_speech,"r") as f:
        contenu=f.read()
        contenu=contenu.replace("\n"," ")
        for i in range (len(contenu)):
            if contenu[i]!=chr(46):
                phrase_1+=contenu[i]
            else:
                break

        if mot in minuscule(ponctuation_str(phrase_1)):
            if minuscule(ponctuation_str(phrase_x + contenu[i + 1])) not in chaine_ponctuation:
                return phrase_1.lower()+chr(46)
        else:
            for i in range(len(phrase_1),len(contenu)):

                if contenu[i]!=chr(46):
                    phrase_x+=contenu[i]
                else:
                    if mot in minuscule(ponctuation_str(phrase_x)) :
                        if minuscule(ponctuation_str(phrase_x+contenu[i+1])) not in chaine_ponctuation:
                            return phrase_x.lower()+chr(46)
                    else:
                        phrase_x=""


def reponse_affinee(question,reponse):
    """
    Rôle: Affine la réponse générée en y ajoutant un préfixe basé sur le type de question posée.
    Paramètres: 'question' - la question posée, 'reponse' - la réponse générée à affiner.
    Return: Réponse affinée avec le préfixe approprié."""

    dico_mot_interrogation={"Comment": "Après analyse, ",
                            "Pourquoi": "Car, ",
                            "Peux-tu": "Oui, bien sûr, ",
                            "Combien":"Désolé mais il est difficile de quantifier, "}
    for interrogation in dico_mot_interrogation.keys():
        if interrogation in question:
            reponse_complete=dico_mot_interrogation[interrogation]+reponse
            return reponse_complete
    return reponse


def afficher_mots_moins_importants(mot_pas_important):
    """
    Rôle: Affiche une fenêtre Tkinter listant les mots considérés comme moins importants.
    Paramètres: 'mot_pas_important' - liste des mots à afficher.
    Return: Aucun. Une fenêtre Tkinter est générée pour l'affichage."""

    ensemble_mot_pas_important=""
    for i in range(len(mot_pas_important)):
        ensemble_mot_pas_important+=mot_pas_important[i]+"\n"
    dialog = tk.Toplevel()
    dialog.title("Mots Moins Importants")
    dialog.geometry("1000x300")

    txt = scrolledtext.ScrolledText(dialog, wrap=tk.WORD, width=40, height=10)
    txt.pack(padx=10, pady=10)


    txt.insert(tk.INSERT, ensemble_mot_pas_important)


    txt.configure(state='disabled')

    btn_close = tk.Button(dialog, text="Close", command=dialog.destroy)
    btn_close.pack(pady=10)

def afficher_mots_plus_importants(mot_import_dossier):
    """
    Rôle: Affiche une fenêtre Tkinter listant le mots considéré comme moins important.
    Paramètres: 'mot_import_dossier' - mot à afficher.
    Return: Aucun. Une fenêtre Tkinter est générée pour l'affichage."""


    messagebox.showinfo("Voici le mot le plus important du dossier :", "Voici le mot le plus important du dossier :\n" + mot_import_dossier)



def afficher_mots_plus_importants_Chirac(mot_import_chirac):
    """
    Rôle: Affiche une fenêtre Tkinter listant le mot considéré comme le plus important du discours de Chirac.
    Paramètres: 'mot_import_chirac' - mot à afficher.
    Return: Aucun. Une fenêtre Tkinter est générée pour l'affichage."""


    messagebox.showinfo("Mots Plus Importants", "Mots plus importants de Chirac ici :\n" + mot_import_chirac)


def afficher_presi_nation(president_nation,presi_nation):
    """
    Rôle: Affiche une fenêtre Tkinter listant les présidents parlant le plus de nation.
    Paramètres: 'president_nation' - liste des présidents à afficher, 'presi_nation' - président à afficher.
    Return: Aucun. Une fenêtre Tkinter est générée pour l'affichage."""

    chaine="Voici les présidents parlant de Nation :\n"
    for i in range(len(president_nation)):
        if i==(len(president_nation)-1):
            chaine+=president_nation[i]+"\n\n"
        else:
            chaine += president_nation[i] + ", "
    chaine+="Voici le président parlant le plus de Nation :\n" + presi_nation

    messagebox.showinfo("Voici les présidents parlant de Nation :\n" ,chaine)

def afficher_presi_ecolo(president_ecolo):
    """
    Rôle: Affiche une fenêtre Tkinter listant les présidents parlant le plus d'écologie.
    Paramètres: 'president_ecolo' - président à afficher.
    Return: Aucun. Une fenêtre Tkinter est générée pour l'affichage."""

    president_ecolo="Voici le président parlant le plus d'écologie :\n" + president_ecolo

    messagebox.showinfo("Voici le président parlant le plus de l'écologie :\n" , president_ecolo)


def sauvegarder_texte(zone_texte,Matrice,dico_idf):
    """
    Rôle: Sauvegarde le texte saisi, traite ce texte pour obtenir une réponse basée sur la matrice TF-IDF et ses scores IDF, et affiche cette réponse.
    Paramètres: 'zone_texte' - widget Tkinter où le texte est saisi, 'Matrice' - matrice TF-IDF, 'dico_idf' - dictionnaire des scores IDF.
    Return: Aucun. La réponse est affiché à l'utilisateur via la boîte de dialogue."""

    global texte_utilisateur
    texte_utilisateur = zone_texte.get("1.0", "end-1c")
    if len(texte_utilisateur) != 0:
        dico_mot_cpt = scan_ligne(ponctuation_str(minuscule(texte_utilisateur)))
        cpt_question = cpt_mot_question(dico_mot_cpt)

        mot_question = word_question(ponctuation_str(minuscule(texte_utilisateur)))
        Matrice_mot_important = mot_important(mot_question, Matrice)
        if len(Matrice_mot_important) < 2 :
            messagebox.showinfo("Texte Sauvegardé", "\nErreur : Veuillez entrer une question plus précise\n")


        # création de la Matrice des corpus de même dimension que celle de la question
        Matrice_question_filtre = Matrice_filtre_matrice(dico_mot_cpt, Matrice, dico_idf)
        Matrice_dimension_question = croisement_mot_question_corpus(Matrice, Matrice_question_filtre)

        # détermination du fichier étant le plus similaire à la question
        dico_similarite = similarite(Matrice_question_filtre, Matrice_dimension_question)
        fichier_plus_grand_similarite = fichier_similarite(dico_similarite)
        fichier_speech_etude = fichier_clean_vers_speach(fichier_plus_grand_similarite)

        mot_a_chercher = le_mot_important_question(Matrice_question_filtre)
        reponse = phrase_prompt(fichier_speech_etude, mot_a_chercher)
        reponse_bot = reponse_affinee(texte_utilisateur, reponse)
        if reponse_bot == None:
            messagebox.showinfo("Texte Sauvegardé","\nErreur : Veuillez entrez une question plus précise\n")

        else:
            messagebox.showinfo("Texte Sauvegardé","\n - Voilà ma reponse :\n" + reponse_bot + "\n")




def quitter(window):
    """
    Rôle: Ferme la fenêtre Tkinter spécifiée.
    Paramètres: 'window' - fenêtre Tkinter à fermer.
    Return: Aucun. La fenêtre est fermée."""

    window.destroy()