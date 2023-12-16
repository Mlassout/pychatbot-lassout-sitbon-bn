#15/12 23h
from function import *

if __name__=="__main__":


# Call of the function
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")

    last_list = new_list(files_names)
    last_list_colonne=sorted(last_list)
    liste_president = supp_doublons(last_list)



    cleaned(files_names)

    dictionnaire_mot = {}
    directory_cleaned = "./cleaned"
    dictionnaire_mot = cpt_word(directory_cleaned)

    fichiers_dans_speeches = [f for f in os.listdir('./speeches') if f.endswith('.txt')]

    # Appel de la fonction de nettoyage
    cleaned(fichiers_dans_speeches)

    dico_idf = score_idf_dico(directory_cleaned)

    Matrice = matrice_tfidf(directory_cleaned)

    for i in range (len(Matrice )):
        print(Matrice[i])




    mot_pas_important=[]
    somme_tfidf=0
    for j in range(2,len(Matrice)):
        TF_IDF=int(Matrice[j][1])
        if TF_IDF==0:
            somme_tfidf=0
            for k in range(2,9):
                somme_tfidf+=int(Matrice[j][k])
            if somme_tfidf==0:

                mot_pas_important.append(Matrice[j][0])

    indice_high_idf=0
    for i in range(2, len(Matrice)-1):
        for j in range (2,9):
            if int(Matrice[i][j])<int(Matrice[i+1][j]):
                indice_high_idf=i+1

    mot_import_dossier=Matrice[indice_high_idf][0]


    list_indice_mot=[]

    for i in range(2, len(Matrice) - 1):
        for j in range(2, 9):
            if int(Matrice[i][j]) < int(Matrice[i + 1][j]):
                indice_high_idf = i+1
        list_indice_mot.append(indice_high_idf)


    if list_indice_mot[0]<list_indice_mot[1]:
        mot_import_chirac=Matrice[list_indice_mot[1]] [0]
    else:
        mot_import_chirac = Matrice[list_indice_mot[0]][0]


    president_nation=[]
    indice_mot_nation=0
    for i in range (len(Matrice)):
        if Matrice[i][0]=="nation":
            indice_mot_nation=i
    find_Chirac=False
    find_Mitterrand=False
    for i in range (2,9):
        if Matrice[indice_mot_nation][i]>0:
            if i==1 or i==2 and find_Chirac==False:

                find_Chirac=True
                president_nation.append("Chirac")
            if i==3:

                president_nation.append("Giscard")
            if i==4:

                president_nation.append("Hollande")
            if i==5:

                president_nation.append("Macron")
            if i==6 or i==7 and find_Mitterrand==False:

                find_Mitterrand=True
                president_nation.append("Mitterrand")
            if i==8:

                president_nation.append("Sarkozy")

    indice_high_idf=0
    for i in range (2,8):
        if Matrice[indice_mot_nation][i]<Matrice[indice_mot_nation][i+1]:
            indice_high_idf=i+1
        else:
            indice_high_idf=i

    if indice_high_idf == 1 or indice_high_idf == 2:
        presi_nation="Chirac"
    if indice_high_idf == 3:
        presi_nation = "Giscard"
    if indice_high_idf == 4:
        presi_nation = "Hollande"
    if indice_high_idf == 5:
        presi_nation = "Macron"
    if indice_high_idf == 6 or indice_high_idf == 7:
        presi_nation = "Mitterrand"
    if indice_high_idf == 8:
        presi_nation = "Sarkozy"


    mot_sans_non_important=[]
    for i in range (1,len(Matrice)):
        if Matrice[i][0] not in mot_pas_important:
            mot_sans_non_important.append(Matrice[i][0])

    indice_ecologie=0
    for i in range (len(Matrice)):
        if Matrice[i][0]=="écologie":
            indice_ecologie=i

    indice_ecologie_president=0
    for j in range (2,8):
        if Matrice[indice_ecologie][j]<Matrice[indice_ecologie][j+1]:
            indice_ecologie_president=j
        else:
            indice_ecologie_president=j

    president_ecolo=""
    if indice_ecologie_president==1 or indice_ecologie_president==2 :
        president_ecolo="Chirac"
    if indice_ecologie_president==3:
        president_ecolo = "Giscard"
    if indice_ecologie_president == 4:
        president_ecolo = "Hollande"
    if indice_ecologie_president == 5:
        president_ecolo = "Macron"
    if indice_ecologie_president == 6 or indice_ecologie_president == 7:
        president_ecolo = "Mitterrand"
    if indice_ecologie_president == 8:
        president_ecolo = "Sarkozy"
    # Boucle principale menu
    flag = True
    while flag:
        print("\n--- Menu ---\n\n"
                  "- Pour afficher les mots les moins importants, entrez 1\n"
                  "- Pour afficher les mots les plus importants, entrez 2\n"
                  "- Pour afficher le mot le plus important par Chirac, entrez 3\n"
                  "- Pour afficher les présidents parlant de Nation, ainsi que celui qui en parle le plus, entrez 4\n"
                  "- Pour afficher le président parlant en premier de l'écologie, entrez 5\n"
                  "- Pour afficher tous les mots de tous les discours hormis les non-importants, entrez 6\n"
                  "- Pour terminer, entrez 0\n")
        value_menu = saisie()  # Saisie d'un caractère (nombre de 0 à 9)
        if value_menu == 1:
            print("\n- Voici les mots les moins importants\n")
            for i in range (len(mot_pas_important)):
                print(mot_pas_important[i])
        elif value_menu == 2:
            print("\n- Voici le mot le plus important du dossier :\n",mot_import_dossier)
        elif value_menu == 3:
            print("\n- Voici le mot le plus important des discours de Chirac : ",mot_import_chirac)
        elif value_menu == 4:
            print("\n- Voici les présidents parlant de Nation\n")
            for i in range(len(president_nation)):
                print(president_nation[i])
            print("\n-",presi_nation,"parle le plus de Nation")
        elif value_menu == 5:
            print("\n-",president_ecolo, "est le président qui parle le plus d'écologie\n")
        elif value_menu == 6:
            print("\n- Voici tous les mots de tous les discours hormis les non-importants\n")
            for i in range (len(mot_sans_non_important)):
                print(mot_sans_non_important[i])
        elif value_menu == 0:
            flag = False
            print("\nAu revoir...")
        else:
            print("Choix incorrect, retour au menu")

    question=input("Entre ta question : ")
    mot_question=word_question(ponctuation_str(minuscule(question)))
    Matrice_mot_important=mot_important(mot_question,Matrice)

    #compteur mot apparition
    dico_mot_cpt=scan_ligne(ponctuation_str(minuscule(question)))
    cpt_question=cpt_mot_question(dico_mot_cpt)

    Matrice_question_filtre=Matrice_filtre_matrice(dico_mot_cpt,Matrice)

    Matrice_dimension_question=croisement_mot_question_corpus(Matrice,Matrice_question_filtre)

    dico_similarite=similarite(Matrice_question_filtre,Matrice_dimension_question)
    print(dico_similarite)