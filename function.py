import os  # utilisé pour naviguer dans l'os
import random # importer une possibilité de faire une fonction aléatoire

# fonction qui permet de récuperer le nom des fichiers d'un dossier donné
def list_of_files(directory, extension): # entre en paramètre le nom du dossier et le type de fichier à récupérer

    files_names = [] # création d'une liste pour stocker les noms

    for filename in os.listdir(directory): # récupère la liste des éléments dans le fichier donné en paramètre
        if filename.endswith(extension): # entre dans la contidition que si on trouve le type de fichier donné en paramètre
            files_names.append(filename) # ajout de chaque nom de fichier la liste créer au préalable
    return files_names # on retourne la fonction pour la renvoyer



#fonction qui permet d'associer le nom des présidents avec leur prenom
def associer_prenom_president(nom_president):

    prenoms_presidents = {
        "Chirac ": " Jacques ",
        " Giscrad d Estaing ": " Valéry ",
        " Mitterrand ": " François ",
        " Macron ": " Emmanuel ",
        " Sarkozy ": " Nicolas "
    }

    return prenoms_presidents.get(nom_president, " Inconnu ")


# fonction qui permet de prendre la liste des fichiers afin d'extraire seulement le nom des présidents stockés dans une liste
def new_list(l): # entre en paramètre la liste à traiter

    liste = [] # création d'une nouvelle liste

    for i in range(len(l)): # parcour toute la liste donné en paramètre
        val = l[i][11:-4] # enlève le format du fichier et le "Nomination_"
        for j in range (len(val)): # parcour la chaine str des noms de fichier de cette liste
            if val[j] == '1' or val[j] == '2': # entre dans la condition s'il y a un 1 ou un 2 dans la chaine
                val = val[:-1] # enlève ces derniers à la dernière position
        liste.append(val) # ajoute ces nouveaux noms la liste créée au préalable

    return liste # renvoie la liste


# fonction qui permet d'enlever les doublons dans une liste
def supp_doublons(l): # entre en paramètre la liste à traiter

    l = list(set(l)) # parcour la liste pour enlever les doublons

    return l # renvoie la liste


# fonction qui prend une chaine str comprenant des majuscules et renvoit une chaine str tout en minuscule
def minuscule(txt): # entre en paramètre la chaine str à traiter

    txt = list(txt) # met tous les caractères de la chaine dans une liste
    for i in range (len(txt)): # parcour toute la liste
        if ord(txt[i]) >= ord("A") and ord(txt[i]) <= ord("Z"): # entre dans la condition si un caractere est compris entre le code ascii de A et du Z
            txt[i] = chr(ord(txt[i]) + ord("a")-ord("A")) # change cette majuscule en minuscule

    return "".join(txt) # renvoie la liste en texte


# fonction qui permet d'enlever la ponctuation d'une chaine str
def ponctuation_str(l) : # entre en paramètre une chaine str

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


def cleaned(l): # entre en paramètre une liste comprenant le nom de fichier

    os.mkdir('./cleaned/') # création d'un dossier "cleaned"
    txt=""

    for i in range (len(l)): # parcour la liste donné en paramètre
        nom_fichier = l[i] # stocke le nom du fichier dans une variable
        with open('./speeches/'+nom_fichier,"r") as f: # ouvre le fichier présent dans la liste
            contenu = f.readlines() # stocke le contenu du fichier
            for j in range(len(contenu)):
                txt+=contenu[j]    # on ajoute a chaque fois le contenu a txt
            txt = ponctuation_str(minuscule(txt))# appelle la fonction ponctuation_str et minuscule pour le contenu du fichier
            nom_fichier_cleaned = "cleaned_" + l[i] # modifie le nom du fichier initial afin de ne pas les confondre
            with open('./cleaned/' + nom_fichier_cleaned, 'w') as p: # crée le fichier à partir du nom du fichier modifié
                p.write(txt) # écrit dans ce fichier le contenu du fichier iniatial modifié par la fonction ponctuation_str et minuscule


def scan_ligne(chaine):

    dico={}   # on définit un dictionnaire vide
    mot=""   # on crée une variable mot où l'on stocke une chaine vide

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
            else:
                if mot in dico:    # si le contenu de la variable mot est dans le dictionnaire on ajoute 1
                    dico[mot]+=1
                else:
                    dico[mot]=1
            mot=""

    return dico

#fonction dictionnaire mot/nbr iteration

def cpt_word(directory):

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



import math

# fonction mot-->score idf

def score_idf_dico(dictionnaire):

    nbr_mot = 0    # initialise une variable a 0
    dico_idf = {}   # crée un dictionnaire vide
    for iterations in dictionnaire.values():   #parcourt les valeurs du dictionnaire

        nbr_mot += iterations

    for mot in dictionnaire.keys():    # parcourt les clés du dictionnaire et effectue le calcul du score IDF pour chaque mot.
        nbr_iteration = dictionnaire[mot]   # Récupère le nombre d'occurrences du mot dans le dictionnaire.
        idf = math.log(1 / (nbr_iteration / nbr_mot))   # Calcule le score IDF pour le mot

        dico_idf[mot] = idf   # stocke le score idf dans le dictionnaire

    return dico_idf



#fonction qui prend un dossier et retourne matrice tf idf en fonction de chaque fichier
def matrice_tfidf(directory):
    dico_TFIDF = {}       # création de dictionnaires vides
    dico_TF = {}

    List=[]         # création de liste vide

    list_name = list_of_files(directory, "txt")
    list_name=sorted(list_name)
    List.append("mot")

    dico_IDF=score_idf_dico(cpt_word(directory))           # Calcul du score IDF pour chaque mot dans le répertoire
    all_word = cpt_word(directory)                  # Compte le nombre d'occurrences de chaque mot dans l'ensemble des documents

    if "" in all_word:                  # Supprime la clé vide s'il y en a une
        del all_word[""]

    matrice = []                # Initialisation d'une matrice pour stocker les valeurs TF-IDF
    nbr_ligne = int(len(list_name)) + 1     # Nombre de lignes dans la matrice (nombre de mots + 1 pour les titres)
    for l in range(len(all_word) + 1):      # Crée une matrice remplie de zéros
        ligne = ['0'] * nbr_ligne
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

            matrice[0][i+1]=list_name[i]                # Remplissage de la première ligne de la matrice avec les noms de fichiers

            for h in range(len(matrice)):           # Remplissage de la matrice avec les valeurs TF-IDF

                for mot in dico_TFIDF.keys():
                    if mot == matrice[h][0]:

                        matrice[h][i+1]=dico_TFIDF[mot]

    return matrice


def word_question(chaine):

    list=[]   # on définit une liste vide
    mot=""   # on crée une variable mot où l'on stocke une chaine vide

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

    list_mot=[]
    for mot in list:
        if mot in matrice:
            list_mot.append(mot)

    return list_mot

