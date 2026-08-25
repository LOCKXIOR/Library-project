from tkinter import*
from tkinter import messagebox
N=-1
screen=Tk()
screen.title("Test")
screen.geometry("400x500+500+200")
Texte=Label(screen, text="Test, clique les boutons fonctionnels",font=("Times new roman",16))
Texte.pack(pady=20)

biblio = {
    "1984": {"Auteur": "George Orwell", "Année": 1949, "Disponibilité": True},
    "Le Petit Prince": {"Auteur": "Antoine de Saint-Exupéry", "Année": 1943, "Disponibilité": True},
    "Harry Potter": {"Auteur": "J.K. Rowling", "Année": 1997, "Disponibilité": False},
    "Les Misérables": {"Auteur": "Victor Hugo", "Année": 1862, "Disponibilité": True},
    "L'Étranger": {"Auteur": "Albert Camus", "Année": 1942, "Disponibilité": True},
    "La ferme des animaux": {"Auteur": "George Orwell", "Année": 1945, "Disponibilité": True}
}
MDP=""

def admin():
    screen_ent=Tk()
    screen_ent.title("Mot de passe")
    Rev=Label(screen_ent,text="Veuillez entrer le code PIN :")
    Rev.pack()
    screen_ent.geometry("300x120")
    entry=Entry(screen_ent,width=40)
    entry.pack(pady=25)
    entry.focus()
    def validation():
        Utilisateur_text=entry.get().strip()
        if Utilisateur_text==MDP:
            Texte.config(text="Admin panel",bg="Black",fg="white")
            screen.config(bg="Black")
            Comptage.pack_forget()
            Sortie.pack_forget()
            screen_ent.destroy()
            Administrateur.pack_forget()
            bibliotheque.pack_forget()
            messagebox.showinfo("Approval", "Vous avez accès au mode admin ✅")
            So.pack(pady=1)
            CPui.pack(pady=2)
            
        else:
            messagebox.showerror("Erreur","Tchaley, le mot de passe est incorrect")
    Valider=Button(screen_ent,text="Valider",command=validation)
    Valider.pack()
    

   
def ret():
    Comptage.pack(pady=40)
    Sortie.pack(pady=1)
    So.destroy()
    CPui.destroy()
    screen.config(bg="White")
    Texte.config(bg="White",fg="black",text="Test, clique les boutons fonctionnels")
    Administrateur.pack(pady=140)
So=Button(text="RETOUR",fg="Black",font=("Times new roman",12),command=ret,bg="Dark red")

def change_passpin():
    global MDP
    screen_=Tk()
    screen_.title("Changement de PW")
    screen_.geometry("300x120+200+200")
    ER=Label(screen_,text="New password")
    ER.pack()
    Entrée=Entry(screen_,width=40)
    MDP=Entrée

CPui=Button(screen,text="Change Password",bg="white",command=change_passpin)
  
def show_biblio():
    print(*bibliotheque)
bibliotheque=Button(screen,text="livres",command=show_biblio)


def compt():
    global N
    N+=1
    if N>0:
        Texte.config(text=f"Tu as cliqué {N} fois")
        if N==67:
            Texte.config(text="6 SIX 7 SEVEN !",fg="Blue",font=("Times new roman",30))
    else:
        Texte.config(text="Clique !")
    Comptage.config(text="Clique ici")
    Sortie_Comptage.pack()
    Administrateur.pack_forget()
    bibliotheque.pack_forget()


Comptage=Button(screen,text="Comptage",command=compt)
Comptage.pack()

def sortie_compt():
    Texte.config(text="Essayons autre chose a part compter")
    Sortie_Comptage.pack_forget()
    Administrateur.pack()
    bibliotheque.pack()
    Comptage.config(text="Comptage")
Sortie_Comptage=Button(screen,text="❌",fg="Dark red",font=("Times new roman",15),command=sortie_compt)

def sort():
    screen.destroy()
Sortie=Button(screen, text="Sortie", command=sort,fg="Dark red",font=("Times new roman",15))
Sortie.pack()

Administrateur=Button(text="Administrateur",bg="Black",fg="white",command=admin)
Administrateur.pack()
    
screen.mainloop()