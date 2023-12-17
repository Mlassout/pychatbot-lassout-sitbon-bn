#16/12 23h
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

    #Pour afficher la matrice
    for i in range (len(Matrice )):
        print(Matrice[i])

    mot_pas_important=[]
    for j in range(1,len(Matrice)):
        TF_IDF=Matrice[j][1]
        if TF_IDF==0:
            somme_tfidf=0
            for k in range(2,9):
                somme_tfidf+=Matrice[j][k]
            if somme_tfidf==0:
                mot_pas_important.append(Matrice[j][0])

    # Initialiser les variables pour stocker le mot avec le score le plus élevé
    score_le_plus_eleve = 0
    mot_import_dossier = ""

    # Itération sur chaque ligne et chaque colonne de la matrice (en ignorant la première ligne et la première colonne)
    for i in range(1, len(Matrice)):
        for j in range(1, len(Matrice[i])):
            if Matrice[i][j] > score_le_plus_eleve:
                score_le_plus_eleve = Matrice[i][j]
                mot_import_dossier = Matrice[i][0]

    # Initialiser les variables pour stocker le mot avec le score le plus élevé
    score_le_plus_eleve = 0
    mot_import_chirac = ""

    # Itération sur chaque ligne et chaque colonne de la matrice (en ignorant la première ligne et la première colonne)
    for i in range(1, len(Matrice)):
        for j in range(1, 3):
            if Matrice[i][j] > score_le_plus_eleve:
                score_le_plus_eleve = Matrice[i][j]
                mot_import_chirac = Matrice[i][0]

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
        if Matrice[i][0]=="climat":
            indice_ecologie=i
            break

    # Trouver le score le plus élevé pour 'climat'
    score_max = 0
    indice_ecologie_president = 0
    for j in range(1, len(Matrice[indice_ecologie])):
        if Matrice[indice_ecologie][j] > score_max:
            score_max = Matrice[indice_ecologie][j]
            indice_ecologie_president = j

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
                  "- Pour afficher le président parlant le plus de l'écologie, entrez 5\n"
                  "- Pour acceder au bot, entrez 0\n")
        value_menu = saisie()  # Saisie d'un caractère (nombre de 0 à 5)
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
            print("\n-",president_ecolo, "est le président qui parle le plus du climat\n")
        elif value_menu == 0:
            flag = False
        else:
            print("Choix incorrect, retour au menu")



    while True:
        #saisie de la question de l'utilisateur qui doit avoir au moins deux étant présent dans le corpus
        boucle=True

        while boucle==True:

            question=input(" - Si vous souhaitez sortir du programme entrez 0\n - Entre ta question : ")


            dico_mot_cpt = scan_ligne(ponctuation_str(minuscule(question)))
            cpt_question = cpt_mot_question(dico_mot_cpt)

            mot_question=word_question(ponctuation_str(minuscule(question)))
            Matrice_mot_important=mot_important(mot_question,Matrice)
            if len(Matrice_mot_important)<2 and question!="0":
                print("\nErreur : Veuillez entrez une question plus précise\n")
                boucle=True
            else:
                boucle=False
            if question=="0":
                flag=True
                break
        if flag==True:
            print("\nAu revoir...")
            break



        #création de la Matrice des corpus de même dimension que celle de la question
        Matrice_question_filtre=Matrice_filtre_matrice(dico_mot_cpt,Matrice,dico_idf)
        Matrice_dimension_question=croisement_mot_question_corpus(Matrice,Matrice_question_filtre)

        #détermination du fichier étant le plus similaire à la question
        dico_similarite=similarite(Matrice_question_filtre,Matrice_dimension_question)
        fichier_plus_grand_similarite=fichier_similarite(dico_similarite)
        fichier_speech_etude=fichier_clean_vers_speach(fichier_plus_grand_similarite)

        """
        Création de la réponse à la question en cherchant la première phrase possédant
        le mot le plus impactant de la question dans le corpus.
        """
        mot_a_chercher=le_mot_important_question(Matrice_question_filtre)
        reponse=phrase_prompt(fichier_speech_etude,mot_a_chercher)
        print(mot_a_chercher)
        print(fichier_speech_etude)
        reponse_bot=reponse_affinee(question,reponse)
        if reponse_bot==None:
            print("\nErreur : Veuillez entrez une question plus précise\n")
        else:
            print("\n - Voilà ma reponse :\n"+reponse_bot+"\n")


#menu fenetre


# Création de la fenêtre principale
window = tk.Tk()
window.title("Menu")
window.geometry("800x600")


# Création des widgets pour la saisie de texte
zone_texte = tk.Text(window, height=5, width=50)
zone_texte.pack()

# Création des boutons
btn_sauvegarder_texte = tk.Button(window, text="Sauvegarder le texte", command=lambda: sauvegarder_texte(zone_texte))
btn_sauvegarder_texte.pack()

btn_afficher_texte = tk.Button(window, text="Afficher le texte sauvegardé", command=afficher_texte_sauvegarde)
btn_afficher_texte.pack()

btn_moins_importants = tk.Button(window, text="Afficher les mots les moins importants", command=lambda: afficher_mots_moins_importants(mot_import_dossier))
btn_plus_importants = tk.Button(window, text="Afficher les mots les plus importants", command=lambda: afficher_mots_plus_importants(mot_important))
btn_plus_importants_Chirac = tk.Button(window, text="Afficher le mot le plus important de Chirac", command=lambda: afficher_mots_plus_importants_Chirac(mot_import_chirac))
btn_nation = tk.Button(window, text="Afficher les présidents parlant de Nation", command=lambda: afficher_presi_nation(president_nation, presi_nation))
btn_ecolo = tk.Button(window, text="Afficher le président parlant en premier de l'écologie", command=lambda: afficher_presi_ecolo(president_ecolo))
btn_quitter = tk.Button(window, text="Quitter", command=lambda: quitter(window))

btn_quitter.pack()
btn_moins_importants.pack()
btn_plus_importants.pack()
btn_plus_importants_Chirac.pack()
btn_ecolo.pack()
btn_nation.pack()
btn_quitter.pack()

#logo_image = PhotoImage(file="/Users/marc-antoine/PycharmProjects/IVANA/venv/chatbof_animation.gif")
#logo_label = tk.Label(window, image=logo_image)
#logo_label.pack()

window.mainloop()