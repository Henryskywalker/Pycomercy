#!/usr/bin/env python
#-*- coding: utf-8 -*-
from Tkinter import *
from banco import *
import tkMessageBox

class Execs:
    def __init__(self):
        
        ###  FUNCÃO RESPONSÁVEL POR CHAMAR MÉTODOS DE OUTRAS EXTENÇÕES ###

        self.findFunc = Banco_Sqlite()

    def add_usuario(self):
        
        self.jane = True

        if self.nome.get() == "":
            tkMessageBox.showinfo("Aviso","O nome de usuário está vazio!")
            self.jane = False

        if self.senha.get() == "":
            tkMessageBox.showinfo("Aviso","A senha está vazia!")
            self.jane = False

        if self.email.get() == "":
            tkMessageBox.showinfo("Aviso","O endereço de e-mail está vazio!")
            self.jane = False
        
        else:
            #self.jane = False
            if self.jane:
                
                if self.jane:
                    self.jane = False
                    print("cadastrado")
                    
                else:
                    print("Cadastrou")
                    self.findFunc.criar_Novo_Usuario(nome=self.nome.get(), email=self.email.get(), senha=self.senha.get(), funcao="admin")
            
    def add_cliente(self):
        
        self.findFunc.criar_Novo_Cliente(nome=self.nome.get(), sobrenome=self.sobrenome.get(), cidade=self.cidade.get(), estado=self.estado.get(), bairro=self.bairro.get(), rua=self.rua.get())
        tkMessageBox.showinfo("Aviso","Cliente Cadastrado com Sucesso!")
        return self.destruir_janela()

    def add_produto(self):
        self.findFunc.add_Novo_Produto(prod_nome=self.nome_Produto.get(), prod_numero=self.id_Produto.get(), prod_categoria=self.categoria_Produto.get(), prod_barras=self.codigo_Barras.get())
        tkMessageBox.showinfo("Aviso","Produto Cadastrado com Sucesso!")
        return self.destruir_janela()

class Actions(Execs):
    def adcionar_usuario(self):
        self.jan = Toplevel()
        self.jan.focus_force()
        self.jan.transient(root)
        self.jan.grab_set()
        self.jan.title("Cadastrar novo usuário")
        self.jan.geometry("500x150+230+130")

        #INPUTS
        self.label_nome = Label(self.jan, text="*Nome do Usuario") #Nome de usuário
        self.nome = Entry(self.jan, width=45)

        self.label_senha = Label(self.jan, text="*Senha do Usuario") #Senha de usuário
        self.senha = Entry(self.jan, width=45, show='*')

        self.label_email = Label(self.jan, text="*E-mail do Usuario") #E-mail de usuário
        self.email = Entry(self.jan, width=45)

        self.buttonJan = Button(self.jan, text="Pronto!", command=self.add_usuario)

        self.label_nome.grid(padx=5, pady=5)
        self.label_senha.grid(padx=5, pady=5)
        self.label_email.grid(padx=5, pady=5)

        self.nome.grid(row=0, column=1)
        self.senha.grid(row=1, column=1)
        self.email.grid(row=2, column=1)

        self.saller2 = Checkbutton(self.jan, text="Colaborador").grid(row=3, column=1)
        self.admin  = Checkbutton(self.jan, text="Administrador").grid(row=3, column=0, sticky=W)
        self.saller = Checkbutton(self.jan, text="Vendedor").grid(row=3, column=1, sticky=W)

        self.buttonJan.grid(column=1)

    def adcionar_cliente(self):
        self.jan = Toplevel()
        self.jan.focus_force()
        self.jan.transient(root)
        self.jan.grab_set()
        self.jan.title("Cadastrar novo cliente")
        self.jan.geometry("500x210+230+130")

        #INPUTS
        self.label_nome = Label(self.jan, text="*Nome do Cliente")
        self.nome = Entry(self.jan, width=45)

        self.label_sobr = Label(self.jan, text="*Sobrenome")
        self.sobrenome = Entry(self.jan, width=45)

        self.label_cidade = Label(self.jan, text="*Cidade")
        self.cidade = Entry(self.jan, width=45)

        self.label_estado = Label(self.jan, text="*Estado")
        self.estado = Entry(self.jan, width=45)

        self.label_bairro = Label(self.jan, text="*Bairro")
        self.bairro = Entry(self.jan, width=45)

        self.label_rua = Label(self.jan, text="*Rua")
        self.rua = Entry(self.jan, width=45)

        self.cadastrar = Button(self.jan, text="Cadastrar Cliente", command=self.add_cliente)
        
        #ATIVAÇÃO

        self.label_nome.grid(row=0, column=0, padx=5, pady=5)
        self.nome.grid(row=0, column=1)

        self.label_sobr.grid(row=1, column=0, padx=5, pady=5)
        self.sobrenome.grid(row=1, column=1)

        self.label_cidade.grid(row=2, column=0, padx=5, pady=5)
        self.cidade.grid(row=2, column=1)

        self.label_estado.grid(row=3, column=0, padx=5, pady=5)
        self.estado.grid(row=3, column=1)

        self.label_bairro.grid(row=4, column=0, padx=5, pady=5)
        self.bairro.grid(row=4, column=1)

        self.label_rua.grid(row=5, column=0, padx=5, pady=5)
        self.rua.grid(row=5, column=1)

        self.cadastrar.grid(row=7, column=1)
        
    def adcionar_produto(self):
        self.jan = Toplevel()
        self.jan.focus_force()
        self.jan.transient(root)
        self.jan.grab_set()
        self.jan.title("Adicionar novo Produto")
        self.jan.geometry("393x200+293+130")

        # ADCIONAR INPUTS e LABEL
        self.nome_Produto = Entry(self.jan)
        self.nome_Produto["width"] = 30
        self.nome_Produto.grid(row=0, column=2)

        self.id_Produto = Entry(self.jan)
        self.id_Produto["width"] = 30
        self.id_Produto.grid(row=1, column=2)

        self.categoria_Produto = Entry(self.jan)
        self.categoria_Produto["width"] = 30
        self.categoria_Produto.grid(row=2, column=2)

        self.codigo_Barras = Entry(self.jan)
        self.codigo_Barras["width"] = 30
        self.codigo_Barras.grid(row=3, column=2)

        self.nome_Produto_label = Label(self.jan)
        self.nome_Produto_label["text"] = "Nome do Produto"
        self.nome_Produto_label.grid(row=0, column=0, padx=5, pady=10)

        self.id_Produto_label = Label(self.jan)
        self.id_Produto_label["text"] = "Número do Produto"
        self.id_Produto_label.grid(row=1, column=0, padx=5, pady=10)

        self.categoria_Produto_label = Label(self.jan)
        self.categoria_Produto_label["text"] = "Categoria do Produto"
        self.categoria_Produto_label.grid(row=2, column=0, padx=5, pady=10)

        self.codigo_Barras_label = Label(self.jan)
        self.codigo_Barras_label["text"] = "Código de Barras"
        self.codigo_Barras_label.grid(row=3, column=0, padx=5, pady=10)

        #Botões
        self.done = Button(self.jan)
        self.done["text"] = "Salvar"
        self.done["command"] = self.add_produto
        self.done.grid(row=4)

        self.cancel = Button(self.jan)
        self.cancel["text"] = "Cancelar"
        self.cancel["command"] = self.destruir_janela
        self.cancel.grid(row=4, column=2)
        
    def efetuar_venda(self):
        self.jan = Toplevel()
        self.jan.focus_force()
        self.jan.transient(root)
        self.jan.grab_set()
        self.jan.title("Nova Venda")
        self.jan.geometry("300x150+320+130")


        self.label = Label(self.jan, text="Vamos fazer uma nova venda!", font="Ubuntu 17")
        self.label.pack()

  
    def destruir_janela(self):
        self.jan.destroy()
        self.jan = None

class Application(Frame, Actions):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.jan = None

        # Definir Tamanho da tela
        self.frame = Frame(width=900, height=500, bg="grey", colormap="new")
        self.frame.pack()

        # Chamar funções fora do bloco de construção
        self.buttonLoad()
        #self.textoExibe()
        self.exibeImagem()

    def textoExibe(self):
        self.texto = Label(self.frame)

        self.texto["text"] = "Automação Comercial"
        self.texto["font"] = "Arial 20"
        self.texto["pady"] = 220
        self.texto.pack(side=LEFT)
    
    def exibeImagem(self):
        self.imagem = PhotoImage(file="logo.png")
        self.imagLa  = Label(self.frame, image=self.imagem)
        self.imagLa.pack()

    def buttonLoad(self):
        # Butão de adicionar usuário
        self.add_user = Button(self)
        #self.add_user_photo = PhotoImage(file="images/accountsWork.png")
        self.add_user["text"] = "Adionar Usuário"
        self.add_user["command"] = Actions().adcionar_usuario
        self.add_user["border"] = 0
        self.add_user["bg"] = "#f1f1f1"
        self.add_user["height"] = 4
        #self.add_user["image"] = self.add_user_photo

        self.add_user.pack(side="left")

        # Butão de adicionar cliente
        self.add_client = Button(self)
        self.add_client["text"] = "Adicionar Cliente"
        self.add_client["command"] = Actions().adcionar_cliente
        self.add_client["border"] = 0
        self.add_client["bg"] = "#f1f1f1"
        self.add_client["height"] = 4

        self.add_client.pack(side="left")

        # Butão de adicionar produto
        self.add_product = Button(self)
        self.add_product["text"] = "Adiconar Produto"
        self.add_product["command"] = Actions().adcionar_produto
        self.add_product["border"] = 0
        self.add_product["bg"] = "#f1f1f1"
        self.add_product["height"] = 4

        self.add_product.pack(side="left")

        # Butão de efetuar venda
        self.make_sale = Button(self)
        self.make_sale["text"] = "Efetuar venda"
        self.make_sale["command"] = Actions().efetuar_venda
        self.make_sale["border"] = 0
        self.make_sale["bg"] = "#f1f1f1"
        self.make_sale["height"] = 4

        self.make_sale.pack(side="left")

root = Tk()
root.geometry("900x500+0+0")
app = Application(master=root)
app.master.title("Programa de Automação Comercial")
app.mainloop()