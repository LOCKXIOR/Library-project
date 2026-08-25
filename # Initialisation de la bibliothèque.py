# Initialisation de la bibliothèque
bibliotheque = {
    "1984": {"Auteur": "George Orwell", "Année": 1949, "Disponibilité": True},
    "Le Petit Prince": {"Auteur": "Antoine de Saint-Exupéry", "Année": 1943, "Disponibilité": True},
    "Harry Potter": {"Auteur": "J.K. Rowling", "Année": 1997, "Disponibilité": False},
    "Les Misérables": {"Auteur": "Victor Hugo", "Année": 1862, "Disponibilité": True},
    "L'Étranger": {"Auteur": "Albert Camus", "Année": 1942, "Disponibilité": True},
    "La ferme des animaux": {"Auteur": "George Orwell", "Année": 1945, "Disponibilité": True}
}

# Fonction pour ajouter un livre
def ajouter_livre(titre, auteur, annee):
    if titre in bibliotheque:
        print(f"Le livre '{titre}' existe déjà dans la bibliothèque.")
    else:
        bibliotheque[titre] = {"Auteur": auteur, "Année": annee, "Disponibilité": True}
        print(f"Le livre '{titre}' a été ajouté.")

# Fonction pour rechercher des livres par auteur
def rechercher_par_auteur(auteur):
    resultats = [titre for titre, infos in bibliotheque.items() if infos["Auteur"] == auteur]
    if resultats:
        print(f"Livres de {auteur} : {', '.join(resultats)}")
    else:
        print(f"Aucun livre trouvé pour l'auteur {auteur}.")
#Fonction pour rechercher les livres par leurs titres
def rechercher_par_titres(titre):
    resultats = [t for t in bibliotheque.keys() if titre == bibliotheque.keys()]
    if resultats==titre:
        print(f"Le livre avec les infos '{titre}' est : {', '.join(resultats)}")
    else:
        print("Tchaley ton livre là... introuvable hein.")

# Fonction pour emprunter un livre si tu sais lire 
def emprunter_livre(titre):
    if titre in bibliotheque:
        if bibliotheque[titre]["Disponibilité"]:
            bibliotheque[titre]["Disponibilité"] = False
            print(f"Vous avez emprunté '{titre}'.")
        else:
            print(f"Le livre '{titre}' est déjà emprunté.")
    else:
        print(f"Le livre '{titre}' n'existe pas dans la bibliothèque.")

# Fonction pour redonner un livre volé par samuel 
def retourner_livre(titre):
    if titre in bibliotheque:
        if not bibliotheque[titre]["Disponibilité"]:
            bibliotheque[titre]["Disponibilité"] = True
            print(f"Vous avez retourné '{titre}'.")
        else:
            print(f"Le livre '{titre}' n'était pas emprunté.")
    else:
        print(f"Le livre '{titre}' n'existe pas dans la bibliothèque.")

# Fonction pour afficher ma biblio
def afficher_bibliotheque():
    for titre, infos in bibliotheque.items():
        dispo = "Disponible" if infos["Disponibilité"] else "Emprunté"
        print(f"{titre} - Auteur : {infos['Auteur']}, Année : {infos['Année']}, Disponibilité : {dispo}")

#Démarrage
def debut_pro():
    Allu_étei=int(input("Confirmation de l'Allumage du programme ? Oui = 1, Non = 2 : "))
    while Allu_étei==1:
        Bibl_aff=int(input("Tu veux afficher la bibliothèque ? Oui = 1, Non = 2 : "))
        if Bibl_aff == 1:
            afficher_bibliotheque()
        elif Bibl_aff == 2:
            print("Okay ")
        else:
            print("Je m'éteins !")
        Choix=int(input("Voulez vous faire une recherche ou ajouter un élément ? Recherche = 1, Ajout = 2 : "))
        if Choix == 1:
            Choix=int(input("Recherche par Auteur ou par Titre ? Auteur = 1, Titre = 2 : "))
            if Choix==1:
                Auteur=str(input("Quelle Auteur cherchez vous ? "))
                rechercher_par_auteur(Auteur)
            elif Choix==2:
                Titre=str(input("Quelle titre ? : "))
                rechercher_par_titres(Titre)
        elif Choix == 2:
            MDP=1234
            MDP_V=int(input("Mot de passe : "))
            if MDP==MDP_V:
                    Ajout_titre=str(input("Suivez bien les instructions ! Donnez une oeuvre: "))
                    Ajout_auteur=str(input("Suivez bien les instructions ! Donne l'auteur de l'oeuvre: "))
                    Ajout_annee=str(input("Suivez bien les instructions ! Donne l'année de publication: "))
                    ajouter_livre(Ajout_titre, Ajout_auteur, Ajout_annee)
            else:
                print("Intrus !!!!!")
        else:
            print("Tu ne sais pas ce que tu veux...")

def debut_pro_Admin():
    MDP=1234
    MDP_V=int(input("Mot de passe : "))
    if MDP_V==MDP:
        Menu=int(input("Bonjour cher administrateur que voulez vous faire ? Changer le mot de passe = 1, Effacer la bibliotheque = 2 : "))
        if Menu==1:
            Nouv_MDP=int(input("Nouveau PIN : "))
            Nouv2_MDP=int(input("Rerentrez le PIN : "))
            if Nouv2_MDP==Nouv_MDP:
                print("PIN changé avec succès ! (Pour cette session)")  
                Nouv3_MDP=Nouv2_MDP
                Allu_étei=int(input("Confirmation de l'Allumage du programme ? Oui = 1, Non = 2 : "))
                while Allu_étei==1:
                    Bibl_aff=int(input("Tu veux afficher la bibliothèque ? Oui = 1, Non = 2 : "))
                    if Bibl_aff == 1:
                        afficher_bibliotheque()
                    elif Bibl_aff == 2:
                        print("Okay ")
                    else:
                        print("Je m'éteins !")
                    Choix=int(input("Voulez vous faire une recherche ou ajouter un élément ? Recherche = 1, Ajout = 2 : "))
                    if Choix == 1:
                        Auteur=str(input("Quelle Auteur cherchez vous ? "))
                        rechercher_par_auteur(Auteur)
                    elif Choix == 2:
                        MDP=Nouv3_MDP
                        MDP_V=int(input("Mot de passe : "))
                        if MDP==MDP_V:
                            Ajout_titre=str(input("Suivez bien les instructions ! Donnez une oeuvre: "))
                            Ajout_auteur=str(input("Suivez bien les instructions ! Donne l'auteur de l'oeuvre: "))
                            Ajout_annee=str(input("Suivez bien les instructions ! Donne l'année de publication: "))
                            ajouter_livre(Ajout_titre, Ajout_auteur, Ajout_annee)
                        else:
                            print("Mot de passe erroné, ce dernier a été changé au cours de la session...")
                    else:
                        print("Tu ne sais pas ce que tu veux...")          
            else:
                print("Les deux PIN ne correspondent pas, arrêt imminent ! ")      
        elif Menu==2:
            Verif_suppri_bibli=int(input("Voulez vous vraiment supprimer la bibliothèque ? Oui = 1, Non = 2 : "))
            if Verif_suppri_bibli==1:
                print("Piégé ! Hacker ! Aucun bon admin ne voudrais supprimez la bibliothèque entière !")  
            elif Verif_suppri_bibli==2:
                print("Vous êtes suspect...")
                print("Je ne vous fais pas confiance, je m'éteins ! ")
                print("Je relance le programme avec TOUT LES PARAMETRES PAR DEFAUT, vous êtes très suspect...")
                debut_pro()
            else:
                print("Bref...")
                print("Je relance le programme avec TOUT LES PARAMETRES PAR DEFAUT, vous êtes très bizzare...")
                debut_pro()
                if MDP!=MDP_V:
                    print("Pourquoi vouliez vous allez dans l'interface des Admins... ")
                    
# Utiliser le bail
Action_debut=str(input("écris ON pour démarer : "))
if Action_debut=="Admin":
    debut_pro_Admin()
if Action_debut=="ON":
    debut_pro()
else:
    print("Le programme ne s'allume pas...")
    


emprunter_livre
