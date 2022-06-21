from tkinter import *

class MyApp:
    def __init__(self,parent):
        self.lastButtonClick = None

        #criando uma conteiner (frame)
        self.myParent = parent #lembra quem é seu mestre, a raiz
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()

        #criando novas frames q serão colocadas dentro da frame myContainer1
        self.buttons_frame = Frame(self.myContainer1,background="black")
        self.buttons_frame.pack(side=TOP,ipadx="3m",
                                ipady="1m",
                                padx="3m",
                                pady="2m")

        self.top_frame = Frame(self.myContainer1,background="blue")
        self.top_frame.pack(side=TOP,fill=BOTH,expand=YES)
        
        self.bottom_frame = Frame(self.myContainer1,borderwidth=5, relief=RIDGE,
                                  height=50,background="white")
        self.bottom_frame.pack(side=TOP,fill=BOTH,expand=YES)
        
        self.left_frame = Frame(self.top_frame, background="red",
                                borderwidth=5, relief=RIDGE,
                                height=250,width=50)
        self.left_frame.pack(side=LEFT,fill=BOTH,expand=YES)

        self.right_frame = Frame(self.top_frame, background="tan",
                                borderwidth=5,relief=RIDGE,width=250)
        self.right_frame.pack(side=RIGHT,fill=BOTH,expand=YES)

        #criando butões
        self.butao1 = Button(self.bottom_frame, text="OK!", background="green",command=self.butao1Click)
        self.butao1.configure(  width=3,
                                padx="3m",
                                pady="3m"
                                )
        self.butao1.pack(side=TOP)
        self.butao1.bind("<Button-1>",self.butao1Click_a)
        self.butao1.bind("<Return>",self.butao1Click_a)
        self.butao1.focus_force()

        self.butao2 = Button(self.bottom_frame, text="Tchau!", background="red",command=self.butao2Click)
        self.butao2.configure(  width=6,
                                padx="3m",
                                pady="3m"
                                )
        self.butao2.pack(side=LEFT)
        self.butao2.bind("<Button-1>",self.butao2Click_a)
        self.butao2.bind("<Return>",self.butao2Click_a)

    def butao1Click(self):
        print(self.lastButtonClick)
        self.lastButtonClick = "Butao 1"
        if self.butao1["background"] == "green":
            self.butao1["background"] = "yellow"
        else:
            self.butao1["background"] = "green"

    def butao2Click(self):
        print(self.lastButtonClick)
        self.lastButtonClick = "Butao 2"
        self.myParent.destroy()
    
    def butao1Click_a(self, e):
        self.butao1Click()

    def butao2Click_a(self, e):
        self.butao2Click()


root = Tk()#cria uma janela toplevel
myapp = MyApp(root)
root.mainloop()#fica esperando q eventos aconteçam