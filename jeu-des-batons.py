#Code cree en 11/2016 par GLA
#v1.1

from tkinter import *
from tkinter.messagebox import *
def scred():
    fen=Tk()
    Label(fen, text="Un jeux cree par 3 jeunes dev\n").pack()
    Label(fen, text="GLA association").pack()
    fen.mainloop()
def regle():
    reglee=Tk()
    Label(reglee, text="Voici les regles :\n\n").pack()
    Label(reglee,text="-Choisissez le numero des joueurs\n").pack()
    Label(reglee,text="-Cliquez sur la ligne de votre choix\n").pack()
    Label(reglee,text="-Prenez autant de batons que vous voulez sur une seule ligne\n").pack()
    Label(reglee, text="-Vous avez le droit de prendre autant de baton qu'il y en aÃ‚Â  sur la ligne !\n").pack()
    Label(reglee,text="-cliquez sur confirmer le tour\n").pack()
    Label(reglee,text="-Celui qui prend le dernier baton a perdu").pack()

    reglee.mainloop()

global premier,a1,a2,a3,ligne1,ligne2,ligne3,ligne4,sel,supprimer,tour
sup1=0
x=0
supprimer=0
annuler=0
nbTours=1
batmax2=3
batmax3=5
batmax4=7
total=0
nbBatons1=1
nbBatons2=3
nbBatons3=5
nbBatons4=7

ta=[]
tb=[]
tc=[]

state1=0
state2=0
state3=0
state4=0

deleted2=0
deleted3=0
deleted4=0

b=0
a1=0
a2=0
a3=0

master = Tk()
master.title('Jeu des batons')
master.attributes("-alpha", 1)
def on_closing():
    if askyesno("Quitter","Etes vous sur de vouloir quitter ?"):
        master.destroy()

master.protocol("WM_DELETE_WINDOW", on_closing)
#annuler
annuler_button=Button(master,text="annuler",fg="red",bg="black")
annuler_button.place(x=350,y=260)
annuler_button.config(state="disabled",bg="grey")

#fin du debut
master.minsize(width="500", height="310")#je remet la fenetre a la bonne taille

def annuler():
    global supprimer,premier,deleted1,deleted2,nbBatons1,nbBatons2,nbBatons3,sup2,ta,ligneselected,nbBatons4,batmax2,batmax3,batmax4,deleted1,deleted2,deleted3,deleted4
    if deleted4!=1:
        ligne4.config(state='normal',bg="red")
    else:
        None
    if deleted3!=1:
        ligne3.config(state='normal',bg="green")
    else:
        None
    if deleted2!=1:
        ligne2.config(state='normal',bg="cyan")
    else:
        None
    if deleted1!=1:
        ligne1.config(state='normal',bg="pink")
    else:
        None
    if supprimer==1 and deleted1==1:
        deleted1=0
        nbBatons1=1
        premier=Button(text="", width=1,height=1,bg="pink", command=lambda ryu=x: cliquer(1))
        premier.place(x=200, y=20)
        premier.config(state='normal',bg="pink")
    elif supprimer==2:
        deleted2=0
        nbBatons2=batmax2
        tab1(batmax2)
    elif supprimer==3:
        deleted3=0
        nbBatons3=batmax3
        tab2(batmax3)
    elif supprimer==4:
        deleted4=0
        nbBatons4=batmax4
        tab3(batmax4)


# TABLEAUX
if nbBatons1==1:
    if state1==0:
        premier=Button(text="", width=1,height=1,bg="pink", command=lambda ryu=x: cliquer(1))
        premier.place(x=200, y=20)
        premier.config(state='normal',bg="pink")
else:
    premier.place_forget()

def tab1(nbBatons2):
    for a in range(nbBatons2):
        ta.append(Button(master, text="", width=1, height=1,bg="cyan", command= lambda ryu=a: cliquer(2)))
        ta[a].place(x=180+20*a, y=50)
        ta[a].config(state='normal',bg="cyan")
    ligneselected=2

def tab2(nbBatons3):
    for b in range(nbBatons3):
        tb.append(Button( text="", width=1, height=1,bg="green", command= lambda ryu=b: cliquer(3)))
        tb[b].place(x=160+20*b, y=80)
        tb[b].config(state='normal',bg="green")
    ligneselected=3

def tab3(nbBatons4):
    for c in range(nbBatons4):
        tc.append(Button( text="", width=1, height=1,bg="red", command= lambda ryu=c: cliquer(4)))
        tc[c].place(x=140+20*c, y=110)
        tc[c].config(state='normal',bg="red")
    ligneselected=4

def cliquer(com):
    global state1,nbBatons1,nbBatons2,nbBatons3,nbBatons4,deleted1,deleted2,deleted3,deleted4,annuler_button,annuler,supprimer,ligne1,ligne2,ligne3,ligne4
    annuler_button=Button(master,text="annuler",fg="red",bg="black",command=annuler)
    annuler_button.place(x=350,y=260)
    annuler_button.config(state="normal")
    if ligneselected==0:
        None
    elif com==1 and ligneselected==1:
        premier.place_forget()
        com=0
        state1=1
        nbBatons1=0
        supprimer=1
        ligne4.config(state='disabled',bg="grey")
        ligne3.config(state='disabled',bg="grey")
        ligne2.config(state='disabled',bg="grey")
        deleted1=1
    elif com==2 and ligneselected==2:
        ta[nbBatons2-1].place_forget()
        nbBatons2=nbBatons2-1
        supprimer=2
        ligne4.config(state='disabled',bg="grey")
        ligne3.config(state='disabled',bg="grey")
        ligne1.config(state='disabled',bg="grey")
        if nbBatons2==0:
        	deleted2=1
    elif com==3 and ligneselected==3:
        global  nbBatons3
        tb[nbBatons3-1].place_forget()
        nbBatons3=nbBatons3-1
        supprimer=3
        ligne4.config(state='disabled',bg="grey")
        ligne1.config(state='disabled',bg="grey")
        ligne2.config(state='disabled',bg="grey")
        if nbBatons3==0:
            deleted3=1
    elif com==4 and ligneselected==4:
        global nbBatons4,batmax4
        tc[nbBatons4-1].place_forget()
        nbBatons4=nbBatons4-1
        supprimer=4
        ligne1.config(state='disabled',bg="grey")
        ligne2.config(state='disabled',bg="grey")
        ligne3.config(state='disabled',bg="grey")
        if nbBatons4==0:
            deleted4=1
tab1(nbBatons2)
tab2(nbBatons3)
tab3(nbBatons4)

tour=Label(master, text="au tour du joueur 1")
tour.place(x=200, y=150)
sel=Label(master)
sel.place(x=200,y=180)
# FIN TABLEAUX
ligneselected=0
deleted=0

def lgn1():
    global deleted1,ligneselected,premier,sel
    if deleted1!=1:
        if ligneselected!=1 and state1==0:
            premier.place(x=200, y=20)
            premier.config(state='normal',bg="pink")
        ligneselected=1
        lgn1=0
        while lgn1!=3:
            ta[lgn1].config(state='disabled',bg="grey")
            lgn1=lgn1+1
        lgn1=0
        while lgn1!=5:
            tb[lgn1].config(state='disabled',bg="grey")
            lgn1=lgn1+1
        lgn1=0
        while lgn1!=7:
            tc[lgn1].config(state='disabled',bg="grey")
            lgn1=lgn1+1
        lgn1=0
        print(ligneselected)
        sel.config(text="ligne 1 selectionnee" ,fg="pink")

    if deleted1==1:
        None

def lgn2():
    i=0
    global deleted2,ligneselected,b,sel

    if deleted2==1:
        None
    if ligneselected!=2:
       tab1(nbBatons2)
       while b!=nbBatons2:
            ta[b].config(state='normal',bg="cyan")
            b=b+1
    b=0
    if deleted2==0:
	    while i!=1:
        	premier.config(state='disabled',bg="grey")
	        i=i+1
	    i=0
	    while i!=5:
	        tb[i].config(state='disabled',bg="grey")
	        i=i+1
	    i=0
	    while i!=7:
	        tc[i].config(state='disabled',bg="grey")
	        i=i+1
	    deleted=1
	    i=0
    ligneselected=2

    sel.config(text="ligne 2 selectionnee" ,fg="cyan")

def lgn3():
    global deleted,ligneselected,sel

    i=0
    while i!=nbBatons1:
        premier.config(state='disabled',bg="grey")
        i=i+1
    i=0
    while i!=nbBatons2:
        ta[i].config(state='disabled',bg="grey")
        i=i+1
    i=0
    while i!=nbBatons4:
        tc[i].config(state='disabled',bg="grey")
        i=i+1
    deleted=1
    i=0
    if ligneselected!=3 and state3==0:
        tab2(nbBatons3)
    ligneselected=3

    sel.config(text="ligne 3 selectionnee", fg="green")

def lgn4():
    global deleted,ligneselected,sel
    ligneselected=4
    if ligneselected!=3 and state3==0:
        tab3(nbBatons4)
    i=0
    while i!=nbBatons1:
        premier.config(state='disabled',bg="grey")
        i=i+1
    i=0
    while i!=nbBatons2:
        ta[i].config(state='disabled',bg="grey")
        i=i+1
    i=0
    while i!=nbBatons3:
        tb[i].config(state='disabled',bg="grey")
        i=i+1
    i=0
    deleted=1
    if ligneselected!=4:
        tab3(nbBatons4)

    sel.config(text= "ligne 4 selectionnee",fg="red")


def confirmerTour():
    global nbTours,nbBatons3,deleted1,deleted2, ligneselected, nbBatons4, nbBatons2,tour,deleted3,deleted4,sel,annuler_button,supprimer,batmax2,batmax3,batmax4
    supprimer=0
    batmax4,batmax3,batmax2=nbBatons4,nbBatons3,nbBatons2

    ligne4.config(state='normal',bg="red")
    ligne3.config(state='normal',bg="green")
    ligne2.config(state='normal',bg="cyan")
    ligne1.config(state='normal',bg="pink")
    if nbBatons1==0:
        deleted1=1
    if ligneselected!=0:
        sel.config(text="                               ")
        annuler_button.config(state="disabled",bg="grey")

        if deleted1!=1:
            premier.place(x=200, y=20)
            premier.config(state='normal',bg="pink")
        i=0
        if ligneselected==4:
            batmax4=nbBatons4
            for i in range(nbBatons4):
                tc[i].place_forget()
            i=0

        elif ligneselected==3:
            batmax3=nbBatons3
            for i in range(nbBatons3):
                tb[i].place_forget()
            i=0

        elif ligneselected==2:
            batmax2=nbBatons2
            for i in range(nbBatons2):
                ta[i].place_forget()
            i=0

        ligneselected=0
        tab1(nbBatons2)
        tab2(nbBatons3)
        tab3(batmax4)
        nbTours=nbTours+1
        tour=Label(master)
        tour.place(x=200, y=150)
        if (nbTours%2!=0):
            tour.config(text="au tour du joueur 1")
        elif(nbTours%2==0):
            tour.config( text="au tour du joueur 2")
        if(nbBatons1==0 and nbBatons2==0 and nbBatons3==0 and nbBatons4==0):
            fin()
        if deleted1!=0:
            ligne1.config(state="disabled",bg="grey")
        if deleted2!=0:
            ligne2.config(state="disabled",bg="grey")
        if deleted3!=0:
            ligne3.config(state="disabled",bg="grey")
        if deleted4!=0:
            ligne4.config(state="disabled",bg="grey")

def fin():
    if(nbTours%2==0):
        global tour
        tour.config(text="                                           ")
        victoire=Label(master,text="Le joueur 2 remporte la victoire!",fg="purple").pack()
        valid.config(state="disabled")

    elif(nbTours%2!=0):
        tour.config(text="                                           ")
        victoire=Label(master,text="Le joueur 1 remporte la victoire!",fg="purple").pack()
        valid.config(state="disabled")

deleted1=0
if deleted1==0:
   ligne1=Button(master, text='ligne 1',command=lgn1,bg="pink")
   ligne1.place(x=350, y=20)

if deleted2==0:
    ligne2=Button(master, text='ligne 2',command=lgn2,bg="cyan")
    ligne2.place(x=350, y=50)
if deleted3==0:
    ligne3=Button(master, text='ligne 3',command=lgn3,bg="green")
    ligne3.place(x=350, y=80)
if deleted4==0:
    ligne4=Button(master, text='ligne 4',command=lgn4,bg="red")
    ligne4.place(x=350, y=110)
valid=Button(master,  text="confirmer le tour",command=confirmerTour, bg= "green")
valid.place(x=350, y=230)

def quitter():
    if askyesno("Quitter","Etes vous sur de vouloir quitter"):
    	master.destroy()
######MENU######
menubar= Menu(master)
menubar.add_command(label="Quitter", command=quitter)
menu1=Menu(menubar, tearoff=0)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Regles", command=regle)
menu3.add_command(label="A propos", command=scred)
menubar.add_cascade(label="Aide", menu=menu3)
master.config(menu=menubar)

#####MENU#######

def clavier(event):
    global total
    touche = event.keysym
    total=total+1
    if(total==2):
        master.destroy()

master.focus_set()
master.bind("<Up>", clavier)
master.bind("<Down>", clavier)
master.mainloop()