root = Tk()#cria uma janela toplevel
root.mainloop()#fica esperando q eventos aconteçam

#Creates Frame:
    myContainer1 = Frame(root)#cria uma frame 'mycontainer1'
    myContainer1.pack()#transforms the relationships between masters and slaves into visuals

#Creates Buttons (4 ways):
    #1:
    butao1 = Button(self.myContainer1)
    butao1["text"] = "Hello World"
    butao1["background"] = "green"
    butao1.pack(side=LEFT)
    #2:
    butao2 = Button(self.myContainer1)
    butao2.configure(text="Tchau!")
    butao2.configure(background="tan")
    butao2.pack(side=BOTTOM)
    #3:
    butao3 = Button(self.myContainer1)
    butao3.configure(text="Join me?",background="cyan")
    butao3.pack(side=RIGHT) 
    #4:
    butao4 = Button(self.myContainer1, text="Goodbye!", background="red")
    butao4.pack(side=TOP)

#Criar eventos:
    #Event Biding:
    Nome_butao.bind("Tipo_Evento",Metodo_Chamado)
        def Metodo_Chamado(e):
            #codigo do evento q ele irá fazer
            myParent.destroy()#um exemplo, nesse, ele fecha a janela
    #Command Biding:
    Nome_butao = Button(myContainer1,command=Metodo_Chamado)#esse, diferencia entre clicar e soltar
        def Metodo_Chamado():
            #codigo do evento q ele irá fazer
            myParent.destroy()#um exemplo, nesse, ele fecha a janela
    #pode misturar os dois, basta q cada um tenha um metodo, onde um vai ter o principal 
    # e o outro um secundario, assim, ao executa um, o metodo secundario chamado chama o metodo principal

#Tipos de Evento:
    <Button-1> #click do botao esq do mouse
    <Return> #pressionar a tecla Enter

#Configurações de Tamanho
    #Button:
    Nome_butao.configure(width = Numero,padx = "Numero",pady = "Numero")
        #width: largura do botao (medida por caracter); padx: largura no eixo x; pady: altura no eixo y
    #Frame:
    myContainer1.pack(ipadx = "Numero",ipady = "Numero",padx = "Numero",pady = "Numero",
                      side = POSICAO, fill = POSICAO, expand = Bool)
        #padx: largura no eixo x; pady: altura no eixo y(só q no entorno da frame)
        #ipadx: largura no eixo x; ipady: altura no eixo y(só q interno a frame)
        #side: posicao q a frame vai ficar(ex:LEFT,RIGHT,TOP,BOTTOM)
        #expand: se for YES, ele solicitará todo a área solicitada
        #anchor: redefine a posicao da nova frame(ex:N,NE,S,...)
        #fill: diz para qual lado a frame deve se expandir(ex:LEFT,RIGHT,BOTH)