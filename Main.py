from function import *

if __name__=="__main__":


# Call of the function
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")

    last_list = new_list(files_names)
    last_list_colonne=sorted(last_list)
    liste_president = []
    liste_president = supp_doublons(last_list)



    cleaned(files_names)

    dictionnaire_mot = {}
    directory_cleaned = "./cleaned"
    dictionnaire_mot = cpt_word(directory_cleaned)


    dico_idf = score_idf_dico(dictionnaire_mot)

    Matrice = []

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




    value_end_menu=1
    while value_end_menu==1:
        print("--- Menu ---\n\n"
              "-si vous souhaitez afficher les mots les moins importants, tappez 1\n"
              "-si vous souhaitez afficher les mots les plus importants, tappez 2\n"
              "-si vous souhaitez afficher le mot le plus important par Chirac, tappez 3\n"
              "-si vous souhaitez afficher les présidents parlant de Nation, ainsi que celui qui en parle le plus, tappez 4\n"
              "-si vous souhaitez afficher le président parlant en premier de l'écologie, tappez 5\n"
              "-si vous souhaitez afficher tous les mots de tous les discours hormis les non-importants, tappez 6\n")

        value_menu=0
        while value_menu<1 or value_menu>6:
            value_menu=int(input())

        if value_menu==1:
            print("-Voici les mots les moins importants")
            for i in range (len(mot_pas_important)):
                print(mot_pas_important[i])
        elif value_menu==2:
            print("-Voici le mot le plus important du dossier :",mot_import_dossier)
        elif value_menu == 3:
            print("-Voici le mot le plus important des discours de Chirac :",mot_import_chirac)
        elif value_menu == 4:
            print("-Voici les présidents parlant de Nation")
            for i in range(len(president_nation)):
                print(president_nation[i])
            print("-",presi_nation,"parle le plus de Nation")
        elif value_menu == 5:
            print("-",president_ecolo, "est le président qui parle le plus d'écologie")
        elif value_menu == 6:
            print("-Voici tous les mots de tous les discours hormis les non-importants")
            for i in range (len(mot_sans_non_important)):
                print(mot_sans_non_important[i])

        value_end_menu=int(input("-Voulez vous acceder de nouveau au menu, tappez 1 sinon 2\n"))

    print("Fin de l'execution du programme")


    question=input("Entre ta question")
    question=ponctuation_str(minuscule(question))
    mot_question=word_question(question)
    print(mot_question)

    mot_a_traiter=mot_important(mot_question,Matrice)
