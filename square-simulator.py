1#Code par GLA
from tkinter import *
from tkinter.colorchooser import *

class square:
    def __init__(self):
        self.touch=None
        global down,canvas,x2,y2,y1,x1,square,DrawState,drawoff,drawon,activated_mode,bleu,rouge,jaune,noir,blanc
        global total
        total=0
        DrawState=False
        self.size=20
        x1=290
        y1=290
        x2=x1+self.size
        y2=y1+self.size
        self.color="black"
        self.colorback='ivory'

        master = Tk()
        master.title("Square Simulator")
        master.minsize(width=1000,height=500)
        master.resizable(0,0)
        canvas= Canvas(master,width=600,height=600,bg="ivory")

        """
        splus=Button(master,text="Taille +",command=lambda: getsize(1))
        smoins=Button(master,text='Taille -',command=lambda: getsize(2))
        splus.place(x=30,y=230)
        smoins.place(x=30,y=260)
"""
        bleu= Button(master,text=' Blue ',bg='blue', command =lambda: color('blue'))
        bleu.config(state="disabled")
        rouge=Button(master,text=' Red  ',bg='red', command =lambda: color('red'))
        rouge.config(state="disabled")
        jaune=Button(master,text='Yellow',bg='yellow', command =lambda: color('yellow'))
        jaune.config(state="disabled")
        noir=Button(master, text='Black ',  bg='black',fg="white", command =lambda: color('black'))
        noir.config(state="disabled")
        blanc=Button(master,text='Erase' ,bg='white', command =lambda: color('white'))
        blanc.config(state="disabled")
        Label(master,text="Couleurs:").place(x=30,y=5)
        bleu.place(x=30,y=40)
        rouge.place(x=30,y=70)
        jaune.place(x=30,y=100)
        noir.place(x=30,y=130)
        blanc.place(x=30,y=160)


        square = canvas.create_rectangle(x1,y1,x2,y2,fill=self.color,outline=self.color)
        activated_mode=Label(master,text="orientation",fg ="blue")
        activated_mode.place(x=860,y=360)

        def getBackColor():
            global x1,x2,y1,y2,canvas,square
            color=askcolor()
            self.colorback=color[1]
            canvas.config(bg=self.colorback)

        def getsize(x):
            global x1,y1,x2,y2,square
            if x==1:
                self.size+=2
                x2=x1+self.size
                y2=y1+self.size
                canvas.delete(square)
                square = canvas.create_rectangle(x1,y1,x2,y2,fill=self.color,outline=self.color)
            else:
                self.size-=2
                x2=x1+self.size
                y2=y1+self.size
                canvas.delete(square)
                square = canvas.create_rectangle(x1,y1,x2,y2,fill=self.color,outline=self.color)

        def getColor():
            global x1,x2,y1,y2,canvas,square
            color=askcolor()
            self.color=color[1]


        Button(text="Couleur de dessin",command=getColor,bg='pink').place(x=30,y=190)
        Button(text="Couleur de fond",command=getBackColor,bg='ivory').place(x=30,y=220)
        def Up():
            """fonction OK"""
            global canvas,x2,y2,y1,x1,square

            if DrawState==False:
                canvas.delete(square)
                if y1 >=5:
                    y1-=10
                    y2-=10
            else:
            	if y1 >=5:
	                y1-=10
	                if self.touch in ("Right","Up", None):
	                    x1=x2-20
	                elif self.touch=="Left":
	                    x2=x1+20
            square = canvas.create_rectangle(x1,y1,x2,y2,fill=self.color,outline=self.color)
            self.touch="Up"
            """fonction OK"""

        def Down():
            """fonction OK"""
            global canvas,x2,y2,y1,x1,square

            if DrawState==False:
                canvas.delete(square)
                if y1<=570:

                    y1+=10
                    y2+=10
            else:
            	if y2<=590:
	                y2+=10
	                if self.touch in ("Left",None,"Down"):
	                    x2=x1+20
	                if self.touch=="Right":
	                    x1=x2-20
            square = canvas.create_rectangle(x1,y1,x2,y2,fill=self.color,outline=self.color)
            self.touch="Down"
            """fonction OK"""

        def Right():
            global canvas,x2,y2,y1,x1,square

            if DrawState==False:
                canvas.delete(square)
                if x2<=595:
    	            x1+=10
    	            x2+=10
            else:
            	if x2<=590:
	                x2+=10
	                if self.touch in ("Up","Right",None):
	                    y2=y1+20
	                elif self.touch=="Down":
	                    y1=y2-20
            square = canvas.create_rectangle(x1,y1,x2,y2,fill=self.color,outline=self.color)
            self.touch="Right"

        def Left():
            global canvas,x2,y2,y1,x1,square,DrawState
            if DrawState==False:
                canvas.delete(square)
                if x2>=30:
                    x1-=10
                    x2-=10
            else:
            	if x1>=10:
	               x1-=10
	               if self.touch in ("Left",None,"Up"):
	                    y2=y1+20
	               elif self.touch=="Down":
	                    y1=y2-20
            square = canvas.create_rectangle(x1,y1,x2,y2,fill=self.color,outline=self.color)
            self.touch="Left"
        def remove():
            global canvas,x2,y2,y1,x1,square
            self.color="black"
            self.colorback="ivory"
            canvas.delete(ALL)
            DrawOff()
            x1=290
            y1=290
            x2=310
            y2=310
            square = canvas.create_rectangle(x1,y1,x2,y2,fill=self.color,outline=self.color)
        def choose():
            global total
            if total==0:
                Draw()
                total=1
            else:
                DrawOff()
                total=0
        def clavier(event):
            key = event.keysym
            if key == "Up":
                Up()
            elif key == "Down":
                Down()
            elif key == "Right":
                Right()
            elif key == "Left":
                Left()
            elif key == "Return":
                choose()
            elif key == "BackSpace":
                remove()
        def Draw():
            global DrawState,drawoff,activated_mode,bleu,rouge,jaune,noir,blanc
            drawoff.config(state="normal")
            drawon.config(state="disabled",relief="flat")
            DrawState=True
            activated_mode.config(text="dessin",fg="green")
            rouge.config(state="normal")
            bleu.config(state="normal")
            jaune.config(state="normal")
            noir.config(state="normal")
            blanc.config(state="normal")

        def color(x):
            global square,canvas,x1,x2,y1,y2
            self.color=x
            if self.touch==None:
            	square = canvas.create_rectangle(x1,y1,x2,y2,fill=self.color,outline=self.color)
            elif self.touch=="Left":
            	x2=x1+20
            	square = canvas.create_rectangle(x1,y1,x2,y2,fill=self.color,outline=self.color)
            elif self.touch=="Right":
            	x1=x2-20
            	square = canvas.create_rectangle(x1,y1,x2,y2,fill=self.color,outline=self.color)
            elif self.touch=="Down":
            	y1=y2-20
            	square = canvas.create_rectangle(x1,y1,x2,y2,fill=self.color,outline=self.color)
            elif self.touch=="Up":
            	y2=y1+20
            	square = canvas.create_rectangle(x1,y1,x2,y2,fill=self.color,outline=self.color)

        def DrawOff():
            global DrawState,drawon,square,activated_mode,x1,y1,x2,y2,bleu,rouge,jaune,noir,blanc
            self.color="black"
            if self.touch=="Up":
                y2=y1+20
            if self.touch=="Left":
                x2=x1+20
            if self.touch=="Down":
                y1=y2-20
            if self.touch=="Right":
                x1=x2-20
            drawoff.config(state="disabled",relief="flat")
            drawon.config(state="normal")
            DrawState=False
            activated_mode.config(text="orientation",fg="blue")
            rouge.config(state="disabled")
            bleu.config(state="disabled")
            jaune.config(state="disabled")
            noir.config(state="disabled")
            blanc.config(state="disabled")
        #interface
        def extra(x,y):
           x()
           y()
        Label(master,text=5*"### ").place(x=820,y=340)
        Label(master,text="Mode:").place(x=820,y=360)
        Label(master,text="Utilisez les boutons ou les \nfleches directionelles pour\n vous orienter.").place(x=810,y=100)
        Label(master,text="Entree --> dessiner\n   Retour --> recommencer",bg="grey").place(x=805,y=150)

        drawon=Button(text="Dessiner", command=Draw)
        drawon.place(x=880,y=380)
        drawoff=Button(text="Draw Off", command=DrawOff)
        drawoff.place(x=820,y=380)
        drawoff.config(state="disabled")

        Label(master,text=5*"### ").place(x=820,y=405)
        Button(text="Up Right",fg="green",command=lambda: extra(Up,Right)).place(x=920,y=430)
        Button(text="Down Right",fg="green",command=lambda: extra(Down,Right)).place(x=920,y=500)
        Button(text="Down Left",fg="green",command=lambda: extra(Down,Left)).place(x=802,y=500)
        Button(text="Up Left",fg="green",command=lambda: extra(Up,Left)).place(x=810,y=430)
        Button(text="Down", command=Down).place(x=870,y=500 )
        Button(text="  Up   ", command=Up).place(x=870,y=430)
        Button(text="Right", command=Right).place(x=930,y=465)
        Button(text="Left ", command=Left).place(x=820,y=465)
        reinit = Button(master, text="Reset ", command = remove,fg="red").place(x=870,y=465)

        canvas.focus_set()
        canvas.bind("<Key>", clavier)
        canvas.pack()

        master.mainloop()

main=square()