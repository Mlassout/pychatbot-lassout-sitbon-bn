README 


Rapport du Programme :

Dépôt Git : 

list_of_files(annuaire, extension)
Rôle : Énumère tous les fichiers dans un répertoire donné avec une extension spécifique.
Paramètres : 'annuaire' - Le chemin du répertoire à explorer. 'extension' - L'extension des fichiers à répertorier.
Retour : Liste des noms de fichiers avec l'extension spécifiée.

associer_prenom_president(nom_president)
Rôle : Associe le prénom d'un président en fonction de son nom de famille.
Paramètres : 'nom_president' - Nom de famille du président.
Retour : Prénom du président ou "Inconnu" s'il n'est pas trouvé.

new_list(l)
Rôle : Crée une nouvelle liste en extrayant et en nettoyant des segments spécifiques de chaque fichier pour récupérer les noms des présidents.
Paramètres : 'l' - Liste de chaînes où chaque élément est supposé avoir un format prédéfini avec des informations à extraire.
Retour : Liste de noms de fichiers nettoyés.

supp_doublons(l)
Rôle : Supprime les doublons d'une liste.
Paramètres : 'l' - Potentiellement contenant des doublons.
Retour : Nouvelle liste sans doublons.

minuscule(txt)
Rôle : Convertit tous les caractères majuscules d'une chaîne en minuscules.
Paramètres : 'txt' - Chaîne à convertir.
Retour : Nouvelle chaîne en minuscules.

ponctuation_str(l)
Rôle : Supprime toute ponctuation d'une chaîne.
Paramètres : 'l' - Chaîne à nettoyer.
Retour : Chaîne sans ponctuation.

cleaned(liste_fichiers)
Rôle : Nettoie le contenu de plusieurs fichiers en supprimant la ponctuation et en convertissant le texte en minuscules, puis sauvegarde les résultats dans un nouveau répertoire.
Paramètres : 'liste_fichiers' - Liste des noms de fichiers à nettoyer.
Retour : Aucun. Les fichiers nettoyés sont écrits dans un nouveau répertoire.

scan_ligne(chaine)
Rôle : Analyse une chaîne et compte la fréquence de chaque mot.
Paramètres : 'chaine' - La chaîne à analyser.
Retour : Dictionnaire avec chaque mot comme clé et sa fréquence comme valeur.

cpt_word(annuaire)
Rôle : Compte la fréquence de chaque mot dans tous les fichiers d'un répertoire.
Paramètres : 'annuaire' - Le chemin du répertoire contenant des fichiers texte.
Retour : Dictionnaire avec chaque mot comme clé et sa fréquence globale comme valeur.

score_idf_dico(annuaire)
Rôle : Calcule la fréquence inverse du document (IDF) pour chaque mot dans les fichiers d'un répertoire.
Paramètres : 'annuaire' - Le chemin du répertoire contenant des fichiers texte.
Retour : Dictionnaire avec chaque mot comme clé et son score IDF comme valeur.

matrice_tfidf(annuaire)
Rôle : Construit une matrice TF-IDF pour un ensemble de documents textuels dans un répertoire donné.
Paramètres : 'annuaire' - Le chemin du répertoire contenant des fichiers texte.
Retour : Matrice TF-IDF, où chaque ligne représente un mot et chaque colonne représente un document.

saisie()
Rôle : Demande à l'utilisateur d'entrer un nombre entre 0 et 5.
Paramètres : Aucun.
Retour : Le nombre saisi en tant qu'entier si l'entrée est valide.

word_question(chaine)
Rôle : Analyse une chaîne et extrait les mots.
Paramètres : 'chaine' - Une chaîne représentant la question.
Retour : Liste de mots de la question.

mot_important(liste, matrice)
Rôle : Identifie les mots importants dans la question en les comparant à la matrice du corpus.
Paramètres : 'liste' - Liste de mots à vérifier, 'matrice' - Matrice de référence pour la comparaison.
Retour : Liste de mots considérés comme importants.

cpt_mot_question(dico)
Rôle : Calcule le nombre total d'occurrences de mots dans une question.
Paramètres : 'dico' - Dictionnaire de mots avec leur comptage.
Retour : Nombre total d'occurrences de mots.

Matrice_filtre_matrice(dico, matrice, dico_idf)
Rôle : Filtre la matrice du corpus pour ne conserver que les mots présents dans la question.
Paramètres : 'dico' - Dictionnaire de mots à filtrer, 'matrice' - Matrice de référence (question), 'dico_idf' - Dictionnaire avec les scores IDF.
Retour : Matrice filtrée avec les mots et leurs scores TF-IDF.

produit_scalaire(A, B, colonne_A, colonne_B)
Rôle : Calcule le produit scalaire de deux vecteurs.
Paramètres : 'A' et 'B' - Matrices représentant des vecteurs, 'colonne_A' et 'colonne_B' - Indices de colonne pour le calcul.
Retour : Résultat du produit scalaire.

norme_vecteur(A, colonne)
Rôle : Calcule la norme d'un vecteur.
Paramètres : 'A' - Matrice représentant le vecteur, 'colonne' - Indice de colonne pour le calcul.
Retour : Norme du vecteur.

calcul_similarite(A, B, colonne_A, colonne_B)
Rôle : Calcule la similarité cosinus entre deux vecteurs.
Paramètres : 'A' et 'B' - Matrices représentant des vecteurs, 'colonne_A' et 'colonne_B' - Indices de colonne.


Exécution du Code :

Pour exécuter le chatbot, assurez-vous d'avoir les fonctions et un main 
Prêts(importer l’image chatbofnoir pour avoir accès à l’interface graphique). Dans le main, vous pouvez exécuter le chatbot. Après avoir clique sur 
bouton vert pour lancer le programme du chatbot, il apparait un menu ou 
deux choix vous sont proposé : tapez 1 pour ouvrir la console classique en 
restant sur python il s’affiche 5 questions demander par le projet, il faut 
entrer une valeur de 1 à 5 pour y répondre. Puis si vous tapez 0 vous 
accédez au chatbot en y accèdent vous pouvez rentrer votre question et il 
vous répondra en fonction de la fréquence des mots de la question (le 
programme python). Néanmoins si vous entrez la valeur 2 au début vous 
êtes transporté dans une interface graphique, où il y a des propositions qui 
vous sont proposé. Vous pouvez également poser votre question dans un 
espace dédier à cela. Enfin il vous sera proposer de quitter pour sortir du 
programme. 

